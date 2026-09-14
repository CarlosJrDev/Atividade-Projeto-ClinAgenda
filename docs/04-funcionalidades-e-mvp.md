# Funcionalidades e MVP

## Principais funcionalidades

### Paciente

- cadastro simplificado;
- consulta de unidades;
- consulta de especialidades;
- consulta de médicos;
- consulta de horários disponíveis;
- agendamento;
- remarcação;
- cancelamento;
- lembretes automáticos;
- confirmação de presença;
- consulta dos próximos agendamentos.

### Médico

- configuração da grade semanal;
- definição de horários disponíveis;
- bloqueio de datas;
- consulta da agenda diária;
- visualização dos dados necessários do paciente;
- registro de consulta efetivada;
- registro de consulta não efetivada;
- indicação do motivo quando aplicável.

### Recepção e gestão

- cadastro de unidades;
- cadastro de especialidades;
- cadastro de médicos;
- cadastro de funcionários;
- cadastro de pacientes;
- agenda geral;
- consulta por unidade;
- consulta por médico;
- histórico de atendimentos;
- indicadores;
- controle de perfis de acesso.

## MVP

O MVP corresponde à primeira versão capaz de resolver os problemas mais importantes.

### Prioridade 1 — base cadastral

Desenvolvimento dos cadastros necessários para o funcionamento da solução:

- unidades;
- especialidades;
- médicos;
- pacientes.

### Prioridade 2 — agenda centralizada

Criação da disponibilidade dos médicos, agenda única e regra de prevenção de conflitos.

Essa etapa representa o núcleo do ClinAgenda.

### Prioridade 3 — painel da recepção

A recepção passa a utilizar o sistema para:

- agendar;
- remarcar;
- cancelar.

Nesse estágio, a clínica já pode começar a substituir controles em planilhas.

### Prioridade 4 — chatbot

O chatbot passa a consumir a agenda já consolidada para apresentar horários e registrar solicitações dos pacientes.

### Prioridade 5 — lembretes

Envio de lembretes automáticos e possibilidade de confirmação ou cancelamento.

### Prioridade 6 — acompanhamento do atendimento

Registro do status das consultas pelos médicos.

### Prioridade 7 — indicadores

Criação de históricos, relatórios e indicadores para apoio à gestão.

## Justificativa da ordem

O chatbot não deve ser o primeiro componente desenvolvido porque depende de uma agenda confiável.

Primeiro é necessário garantir que a disponibilidade e as regras de agendamento estejam corretas. Depois, novos canais podem ser integrados à mesma estrutura.
