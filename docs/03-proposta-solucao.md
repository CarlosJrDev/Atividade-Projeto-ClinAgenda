# Proposta de solução

## Formato escolhido

O grupo propõe o **ClinAgenda**, uma plataforma web integrada com três grupos principais de acesso e um chatbot no WhatsApp.

O formato foi escolhido para combinar facilidade de acesso com centralização das informações.

## Usuários

### Paciente

O paciente utilizará principalmente o chatbot no WhatsApp.

Poderá:

- consultar especialidades;
- consultar médicos e horários;
- realizar agendamento;
- remarcar consultas;
- cancelar consultas;
- confirmar presença;
- receber lembretes;
- consultar próximos agendamentos.

### Médico

O médico utilizará um painel web.

Poderá:

- definir sua disponibilidade;
- bloquear datas;
- consultar sua agenda;
- visualizar informações necessárias ao atendimento;
- registrar se a consulta foi efetivada ou não efetivada.

### Recepção e gestão

A recepção e a gestão utilizarão um painel web.

Poderão:

- cadastrar unidades;
- cadastrar especialidades;
- cadastrar médicos;
- cadastrar funcionários;
- cadastrar pacientes;
- agendar em nome do paciente;
- consultar agendas;
- acompanhar históricos;
- acessar indicadores e relatórios de acordo com o perfil de acesso.

## Fluxo de agendamento pelo paciente

1. O paciente entra em contato com o número da rede pelo WhatsApp.
2. O sistema identifica o paciente ou realiza um cadastro simplificado.
3. O paciente seleciona unidade, especialidade e médico.
4. O sistema consulta os horários disponíveis na agenda centralizada.
5. O paciente escolhe um horário.
6. O sistema registra a reserva e envia uma confirmação.
7. Lembretes são enviados antes da consulta.
8. O paciente pode confirmar ou cancelar.
9. Após a consulta, o médico registra o status do atendimento.

## Fluxo alternativo

Pacientes que não utilizem WhatsApp poderão continuar utilizando telefone ou atendimento presencial.

Nesses casos, a recepção fará o agendamento pelo painel web.

A diferença é que todos os canais utilizarão a **mesma agenda**, evitando que cada canal mantenha um controle independente.

## Regra central contra conflitos

Cada combinação de médico, data e horário poderá possuir apenas um agendamento válido.

A confirmação da vaga deverá ocorrer de forma segura no sistema para impedir que duas solicitações simultâneas ocupem o mesmo horário.

Caso o horário já esteja ocupado, o sistema deverá informar a indisponibilidade e apresentar outras opções.
