from pathlib import Path
import json, traceback
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
URL = (ROOT / 'prototipo' / 'clinagenda.html').as_uri()
KEY = 'clinagenda-aula-v1'
results = []
errors = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={'width': 1440, 'height': 1000}, accept_downloads=True)
    page = context.new_page()
    page.on('pageerror', lambda e: errors.append(str(e)))
    def state(): return page.evaluate('(k) => JSON.parse(localStorage.getItem(k))', KEY)
    def fresh():
        page.goto(URL)
        page.evaluate('(k)=>localStorage.removeItem(k)', KEY)
        page.reload()
        page.wait_for_load_state('networkidle')
    def tab(name): page.get_by_role('tab', name=name, exact=True).click()
    def action(name, scope=None): (scope or page).locator(f'[data-action="{name}"]:visible').first.click()
    def slot(date, time): page.locator(f'[data-slot="{date}|{time}"]').click()
    def quick(value): page.locator(f'[data-reply="{value}"]').click()
    def send(text):
        page.locator('#chat-input').fill(text)
        page.locator('#chat-form button').click()
    def modal_save(): page.locator('#modal button[type=submit]').click()
    def assert_status(text): assert text in page.locator('#status').inner_text(), page.locator('#status').inner_text()
    def close_modal(): action('close-modal')
    def book(date='2026-09-14', time='09:40', pid='p1'):
        tab('Agenda'); slot(date,time); action('book')
        page.locator('#booking-patient').select_option(pid)
        modal_save()
        expect(page.locator('#modal')).not_to_be_visible()
        return state()['appointments'][-1]
    def chat(cid='c1'):
        tab('Canal WhatsApp'); page.locator('#chat-filter').select_option('all')
        page.locator(f'[data-conversation="{cid}"]').click()
    def test(name, fn):
        try:
            fresh(); fn()
            results.append({'test':name,'result':'PASS'})
            print('PASS',name,flush=True)
        except Exception as e:
            results.append({'test':name,'result':'FAIL','error':str(e),'trace':traceback.format_exc()})
            print('FAIL',name,str(e),flush=True)
            page.screenshot(path=str(ROOT/'qa'/f'failure-{len(results)}.png'),full_page=True)

    def lifecycle():
        a=book()
        assert a['status']=='booked'
        assert any(str(a['protocol']) in m['text'] for m in state()['conversations'][0]['messages'])
        action('confirm'); assert_status('Presença confirmada')
        assert state()['appointments'][-1]['presence']=='confirmed'
        action('reschedule'); page.locator('#booking-time').fill('10:00'); modal_save()
        saved=state()['appointments'][-1]
        assert saved['id']==a['id'] and saved['time']=='10:00' and saved['presence']=='pending'
        assert 'Livre' in page.locator('[data-slot="2026-09-14|09:40"]').inner_text()
        action('cancel'); modal_save()
        assert state()['appointments'][-1]['status']=='cancelled'
        assert 'Livre' in page.locator('[data-slot="2026-09-14|10:00"]').inner_text()
        tab('Pacientes'); assert 'Cancelada' in page.locator('#history-table').inner_text()
        tab('Gestão'); assert 'Consulta cancelada' in page.locator('#audit-table').inner_text()
        page.reload(); assert state()['appointments'][-1]['status']=='cancelled'
    test('Agendar, confirmar, remarcar, cancelar, histórico, auditoria e persistência', lifecycle)

    def conflicts():
        slot('2026-09-14','08:20'); action('book'); assert_status('Horário já ocupado')
        assert len(state()['appointments'])==8
        action('reschedule'); page.locator('#booking-time').fill('09:00'); modal_save()
        expect(page.locator('#modal-error')).to_contain_text('Horário já ocupado')
        assert next(a for a in state()['appointments'] if a['id']=='a2')['time']=='08:20'
        page.locator('#booking-date').fill('2026-09-16'); page.locator('#booking-time').fill('13:20'); modal_save()
        expect(page.locator('#modal-error')).to_contain_text('Dia bloqueado')
        page.locator('#booking-date').fill('2026-09-19'); modal_save()
        expect(page.locator('#modal-error')).to_contain_text('Fora do horário')
        page.locator('#booking-date').fill('2026-12-01'); modal_save()
        expect(page.locator('#modal-error')).to_contain_text('Fora da vigência')
        close_modal()
        page.locator('#specialty').select_option('Pediatria'); slot('2026-09-14','08:20'); action('book'); modal_save()
        expect(page.locator('#modal-error')).to_contain_text('paciente já possui consulta')
    test('Conflitos de médico, paciente, bloqueio, fim de semana e vigência', conflicts)

    def filters():
        original=page.locator('#agenda-table').inner_text()
        page.locator('#unit').select_option('u2')
        expect(page.locator('#doctor')).to_have_value('d6')
        assert 'Carla Tavares' in page.locator('#agenda-table').inner_text()
        assert page.locator('#agenda-table').inner_text()!=original
        action('next-week'); assert page.locator('#date').input_value()=='2026-09-21'
        action('prev-week'); assert page.locator('#date').input_value()=='2026-09-14'
        page.locator('#period').select_option('afternoon'); assert '13:00' in page.locator('#agenda-table').inner_text()
        action('demo-date'); expect(page.locator('#period')).to_have_value('morning')
        tab('Gestão'); page.locator('[data-unit="u3"]').click()
        expect(page.locator('#unit')).to_have_value('u3')
    test('Filtros de unidade, especialidade, médico, período e semanas', filters)

    def whatsapp():
        chat('c1'); first=page.locator('#chat-log').inner_text()
        page.locator('[data-conversation="c6"]').click()
        assert 'Rita' in page.locator('#chat-name').inner_text()
        assert page.locator('#chat-log').inner_text()!=first
        page.locator('#chat-filter').select_option('waiting')
        assert page.locator('#conversation-table [data-conversation]').count()==1
        action('take-chat'); send('Olá Rita, vou ajudar.'); assert 'Olá Rita' in page.locator('#chat-log').inner_text()
        action('release-chat'); expect(page.locator('#chat-mode')).to_have_text('Assistente')
        chat('c1'); quick('1'); quick('1'); quick('1'); quick('1'); quick('1')
        expect(page.locator('#chat-log')).to_contain_text('Agendar para')
        quick('1'); a=state()['appointments'][-1]
        assert a['origin']=='WhatsApp' and a['patient']=='p1'
        quick('5'); quick('2')
        assert state()['appointments'][-1]['presence']=='confirmed'
        quick('3'); quick('2'); quick('1'); quick('1')
        assert state()['appointments'][-1]['id']==a['id'] and state()['appointments'][-1]['revision']==1
        quick('4'); quick('2'); quick('2')
        assert state()['appointments'][-1]['status']=='booked'
        quick('4'); quick('2'); quick('1')
        assert state()['appointments'][-1]['status']=='cancelled'
        action('view-chat-appointment'); expect(page.locator('#modal')).to_be_visible(); close_modal()
        action('chat-patient'); expect(page.locator('#patient-name')).to_have_value('Maria das Graças Silva')
    test('WhatsApp: troca de cliente e fila, humano, agendamento, confirmação, remarcação e cancelamento', whatsapp)

    def stale_bot():
        chat(); quick('1'); quick('1'); quick('1'); quick('1'); quick('1')
        c=state()['conversations'][0]; date=c['draft']['date']; time=c['draft']['time']
        book(date,time,'p8')
        chat(); quick('1')
        assert 'Horário já ocupado' in page.locator('#chat-log').inner_text()
        matches=[a for a in state()['appointments'] if a['date']==date and a['time']==time and a['doctor']=='d1' and a['status']!='cancelled']
        assert len(matches)==1 and matches[0]['patient']=='p8'
        assert state()['conversations'][0]['step']=='slot'
    test('Vaga oferecida pelo bot ocupada pela recepção antes da confirmação', stale_bot)

    def onboard():
        chat(); action('new-conversation'); page.locator('#new-phone').fill('83900000123'); modal_save()
        quick('2'); assert len(state()['patients'])==8
        quick('MENU'); quick('1'); send('Paciente Teste Aula'); send('31/02/1990')
        assert len(state()['patients'])==8
        send('15/05/1990'); assert len(state()['patients'])==9
        assert state()['patients'][-1]['name']=='Paciente Teste Aula'
        quick('1'); quick('2'); quick('1'); quick('1'); quick('1'); quick('1')
        assert state()['appointments'][-1]['unit']=='u2'
        action('chat-patient'); expect(page.locator('#patient-name')).to_have_value('Paciente Teste Aula')
        page.locator('#patient-name').fill('Paciente Aula Atualizado'); page.locator('#patient-form button[type=submit]').click()
        action('patient-chat'); expect(page.locator('#chat-name')).to_have_text('Paciente Aula Atualizado')
    test('WhatsApp: recusa de aceite, cadastro novo, data inválida e atualização entre telas', onboard)

    def reminders():
        chat('c4'); action('chat-reminder'); assert_status('Lembrete simulado')
        before=len(state()['conversations'][3]['messages']); action('chat-reminder')
        assert len(state()['conversations'][3]['messages'])==before
        assert_status('já foi enviado')
        action('no-response'); assert_status('já está confirmada')
        chat('c5'); action('chat-reminder'); action('no-response')
        a=next(a for a in state()['appointments'] if a['id']=='a5'); assert a['status']=='booked' and a['presence']=='no-response'
        page.locator('#reminder-kind').select_option('2h'); action('chat-reminder')
        assert next(a for a in state()['appointments'] if a['id']=='a5')['reminders']==['24h','2h']
        quick('5'); quick('1'); assert next(a for a in state()['appointments'] if a['id']=='a5')['presence']=='confirmed'
    test('Lembretes 24h/2h, prevenção de repetição e ausência de resposta sem cancelar', reminders)

    def medical():
        tab('Médico'); page.locator('[data-medical="a4"]').click(); action('complete')
        assert next(a for a in state()['appointments'] if a['id']=='a4')['status']=='done'
        page.locator('[data-medical="a4"]').click(); action('medical-undo')
        page.locator('[data-medical="a4"]').click(); page.locator('#missed-reason').select_option('Atraso'); action('missed')
        assert next(a for a in state()['appointments'] if a['id']=='a4')['reason']=='Atraso'
        page.locator('#block-date').fill('2026-09-14'); action('block'); assert_status('Bloqueio impedido')
        page.locator('#block-date').fill('2026-09-15'); action('block')
        assert any(b['date']=='2026-09-15' for b in state()['blocks'])
        page.locator('#block-date').fill('2026-09-15'); action('unblock')
        assert not any(b['date']=='2026-09-15' for b in state()['blocks'])
        page.locator('#schedule-table [data-day="1"] [data-grade="active"]').uncheck(); action('save-schedule')
        assert_status('invalidaria a consulta')
        page.locator('#schedule-table [data-day="1"] [data-grade="active"]').check()
        page.locator('#schedule-table [data-day="2"] [data-grade="active"]').uncheck(); action('save-schedule')
        assert not state()['schedules']['d1']['days'][1]['active']
        tab('Agenda'); slot('2026-09-15','09:40'); action('book'); assert_status('Fora do horário')
    test('Médico: efetivada, falta com motivo, reabrir, bloquear, desbloquear e salvar grade', medical)

    def patient_crud():
        tab('Pacientes'); action('new-patient')
        page.locator('#patient-name').fill('Teste Cadastro Aula'); page.locator('#patient-phone').fill('83900000999'); page.locator('#patient-birth').fill('1994-10-12'); page.locator('#patient-consent').check()
        page.keyboard.press('F10'); assert len(state()['patients'])==9
        action('patient-chat'); assert 'Teste Cadastro' in page.locator('#chat-name').inner_text()
        action('chat-patient'); action('delete'); modal_save(); assert len(state()['patients'])==8
        action('delete'); assert_status('possui histórico')
        page.keyboard.press('F3'); page.locator('#search').fill('João'); page.locator('[data-find-patient="p7"]').click()
        expect(page.locator('#patient-name')).to_have_value('João Batista Neves')
        page.locator('#patient-consent').uncheck(); page.locator('#patient-form button[type=submit]').click(); action('patient-chat')
        quick('1'); assert state()['conversations'][6]['step']=='menu'
        assert state()['patients'][6]['consent']
    test('Cadastro: criar, editar, localizar, excluir sem histórico e renovar aceite', patient_crud)

    def menus_staff_slides():
        tab('Gestão'); action('new-staff'); page.locator('#staff-name').fill('Aluno Teste'); page.locator('#staff-login').fill('ALUNO01'); modal_save()
        assert len(state()['staff'])==4
        action('edit-staff'); page.locator('#staff-role').select_option('Gestão'); page.locator('#staff-unit').select_option('all'); modal_save()
        assert state()['staff'][-1]['role']=='Gestão'
        action('audit'); expect(page.locator('#audit-box')).to_be_visible()
        for menu in ['file','tools','reports','help']:
            action(menu); expect(page.locator('#modal')).to_be_visible(); page.keyboard.press('Escape'); expect(page.locator('#modal')).not_to_be_visible()
        action('file')
        with page.expect_download() as download: action('export')
        assert download.value.suggested_filename.endswith('.json'); close_modal()
        action('projector'); assert 'projector' in page.locator('body').get_attribute('class')
        action('projector'); action('slides'); assert 'Tech Solutions' in page.locator('#slide-content').inner_text()
        for _ in range(6): action('slide-next')
        expect(page.locator('#slide-counter')).to_contain_text('7 / 7')
        action('group'); page.locator('#project-company').fill('CliniTech Acadêmica'); page.locator('#project-team').fill('Ana — Front-end\nJoão — Back-end'); page.locator('#project-github').fill('https://github.com/exemplo/projeto'); modal_save()
        expect(page.locator('#slide-content')).to_contain_text('Ana — Front-end')
        page.keyboard.press('ArrowLeft'); expect(page.locator('#slide-counter')).to_contain_text('6 / 7')
        page.evaluate('window.print=()=>{window.__printed=true;}'); action('print-slides')
        assert page.evaluate('window.__printed') and page.locator('#print-deck .print-slide').count()==7
        page.evaluate("window.dispatchEvent(new Event('afterprint'))"); expect(page.locator('#slides')).to_be_visible(); action('close-slides')
        action('print'); assert page.evaluate('window.__printed')
    test('Menus, usuários, perfis, exportação, texto ampliado, slides editáveis e impressão', menus_staff_slides)

    def coverage_visual():
        missing=page.evaluate("[...document.querySelectorAll('[data-action]')].map(b=>b.dataset.action).filter(a=>typeof actions[a]!=='function')")
        assert not missing, missing
        for label,suffix in [('Agenda','agenda'),('Pacientes','pacientes'),('Médico','medico'),('Gestão','gestao'),('Canal WhatsApp','whatsapp')]:
            tab(label); page.screenshot(path=str(ROOT/'qa'/f'depois-{suffix}.png'),full_page=True)
        tab('Agenda'); action('slides'); page.screenshot(path=str(ROOT/'qa'/'depois-slides.png')); action('close-slides')
        page.set_viewport_size({'width':390,'height':844})
        for label in ['Agenda','Pacientes','Médico','Gestão','Canal WhatsApp']:
            tab(label)
            assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth+1'),label
        page.screenshot(path=str(ROOT/'qa'/'depois-celular.png'),full_page=True)
        page.set_viewport_size({'width':1440,'height':1000})
        assert len(errors)==0,errors
    test('Todas as ações têm implementação, revisão das cinco telas e largura móvel', coverage_visual)

    def double_keyboard():
        page.locator('[data-slot="2026-09-14|09:40"]').dblclick()
        expect(page.locator('#modal')).to_be_visible(timeout=3000)
        page.keyboard.press('Escape'); expect(page.locator('#modal')).not_to_be_visible()
        slot('2026-09-14','09:40'); page.keyboard.press('F2'); modal_save()
        assert len(state()['appointments'])==9
        page.keyboard.press('F5'); assert_status('Agenda atualizada')
    test('Duplo clique, F2, F5, F10 e Escape', double_keyboard)

    def extra_controls():
        a=book(); action('reminder'); assert_status('Lembrete registrado')
        action('open-chat'); expect(page.locator('#chat-name')).to_contain_text('Maria')
        page.locator('#chat-input').fill('Rascunho da Maria')
        page.locator('[data-conversation="c5"]').click(); expect(page.locator('#chat-input')).to_have_value('')
        chat(); page.locator('#chat-target').select_option(a['id']); action('chat-reminder')
        assert '24h' in state()['appointments'][-1]['reminders']
        assert not next(x for x in state()['appointments'] if x['id']=='a2')['reminders']
        tab('Agenda'); slot('2026-09-14','08:20')
        page.locator('[data-slot="2026-09-14|08:20"]').focus(); page.keyboard.press('Enter')
        expect(page.locator('#modal-title')).to_have_text('Detalhes da consulta'); close_modal()
        tab('Agenda'); page.get_by_role('tab',name='Agenda',exact=True).focus(); page.keyboard.press('ArrowRight')
        expect(page.locator('#p-pac')).to_be_visible()
        action('fullscreen'); expect(page.locator('html')).to_be_visible()
        page.wait_for_function('!!document.fullscreenElement')
        action('fullscreen'); page.wait_for_function('!document.fullscreenElement')
        page.evaluate('window.print=()=>{window.__printed=true}')
        action('reports'); action('print-management'); assert page.evaluate('window.__printed')
        action('tools'); action('reset'); modal_save()
        assert len(state()['appointments'])==8 and len(state()['patients'])==8
        expect(page.locator('#p-agenda')).to_be_visible()
    test('Lembrete por consulta, rascunho isolado, Enter, abas por teclado, tela cheia e restauração', extra_controls)

    def cancelled_and_slides():
        slot('2026-09-17','09:20'); action('cancel'); modal_save()
        chat('c7'); action('view-chat-appointment')
        expect(page.locator('#p-pac')).to_be_visible()
        expect(page.locator('#history-table')).to_contain_text('Cancelada')
        action('slides')
        for index in range(7):
            assert page.locator('#slide-content h2').inner_text()
            page.screenshot(path=str(ROOT/'qa'/f'slide-{index+1}.png'))
            if index < 6: action('slide-next')
        action('close-slides')
    test('Consulta cancelada abre o histórico e os sete slides são apresentados', cancelled_and_slides)

    fresh()
    browser.close()

report={'tests':results,'passed':sum(r['result']=='PASS' for r in results),'failed':sum(r['result']=='FAIL' for r in results),'browser_errors':errors}
(ROOT/'qa'/'resultado-testes.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'passed':report['passed'],'failed':report['failed'],'errors':errors},ensure_ascii=False),flush=True)
raise SystemExit(1 if report['failed'] or errors else 0)
