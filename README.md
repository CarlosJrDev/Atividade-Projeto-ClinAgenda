# Atividade-Projeto-ClinAgenda

## Sobre o projeto

O **ClinAgenda** é uma proposta acadêmica de plataforma integrada para auxiliar uma rede de clínicas populares na organização de agendamentos, prevenção de conflitos de horários, envio de lembretes aos pacientes e acompanhamento dos atendimentos realizados.

A proposta busca substituir o uso fragmentado de telefone, mensagens e planilhas por uma solução centralizada, com uma única agenda e informações organizadas em um mesmo ambiente.

> **Empresa fictícia:** Tech Solutions 
> **Produto:** ClinAgenda

---

## Problema identificado

A rede de clínicas utiliza diferentes meios para registrar e acompanhar os agendamentos. Como essas informações não estão integradas, podem ocorrer:

- conflitos de horários;
- perda ou duplicidade de informações;
- dificuldade para remarcar ou cancelar consultas;
- falhas na comunicação com pacientes;
- aumento de faltas por ausência de lembretes;
- dificuldade para acompanhar atendimentos realizados;
- dificuldade para gerar informações confiáveis para a gestão.

---

## Solução proposta

O ClinAgenda será uma **plataforma web integrada**, complementada por um **chatbot no WhatsApp** para os pacientes.

A solução terá três grupos principais de usuários:

- **Pacientes:** utilizarão principalmente o chatbot no WhatsApp para consultar horários, agendar, confirmar, remarcar ou cancelar consultas.
- **Médicos:** utilizarão um painel web para consultar a agenda, definir disponibilidade, bloquear datas e registrar o status dos atendimentos.
- **Recepção/Gestão:** utilizará um painel web para administrar pacientes, médicos, unidades, especialidades, agendas e informações gerenciais.

Todos os canais utilizarão a mesma base de dados, reduzindo o risco de informações divergentes.

---

## Principais funcionalidades

- cadastro de unidades, especialidades, médicos e pacientes;
- configuração de disponibilidade dos médicos;
- agenda centralizada;
- prevenção de conflitos de horários;
- agendamento, remarcação e cancelamento;
- chatbot no WhatsApp;
- lembretes automáticos;
- confirmação de presença;
- registro de consulta efetivada ou não efetivada;
- histórico de atendimentos;
- relatórios e indicadores;
- controle de acesso por perfil.

---

## MVP — primeira versão

A primeira versão do projeto será priorizada da seguinte forma:

1. Cadastro de unidades, especialidades, médicos e pacientes.
2. Disponibilidade dos médicos e agenda centralizada.
3. Regra de prevenção de conflito de horários.
4. Painel da recepção para agendar, remarcar e cancelar.
5. Chatbot no WhatsApp.
6. Lembretes automáticos.
7. Registro do status das consultas.
8. Histórico de atendimentos.
9. Relatórios e indicadores.

A agenda e suas regras são priorizadas antes do chatbot, pois os demais canais dependem de uma base de agendamento consistente.

---

## Equipe

| Integrante | Papel |
|---|---|
| Carlos Alberto | Back-end |
| Hélio Vieira | UI/UX |
| Vitor Araújo | Banco de Dados |
| Ciro Junior | Front-end |
| Leonardo Pereira | Product Owner |

Os papéis foram definidos em uma reunião on-line realizada no **Microsoft Teams em 13/09/2026**. Cada integrante escolheu sua área considerando sua afinidade com a respectiva área/stack e as necessidades do projeto.

---

## Organização no GitHub

Cada integrante trabalhará em uma branch própria.

Sugestão de branches:


main
    CarlosAlberto
    HelioVieira
    VitorAraújo
    CiroJunior
    LeonardoPereira


Ao concluir sua contribuição, o integrante deverá abrir um **Pull Request** para que o conteúdo seja revisado antes do merge na branch `main`.

A branch `main` será utilizada como versão consolidada e apresentada do projeto.

---

## Estrutura da documentação


Atividade-Projeto-ClinAgenda/
│
├── README.md
│
└── docs/
    ├── 01-empresa-e-contexto.md
    ├── 02-problema.md
    ├── 03-proposta-solucao.md
    ├── 04-funcionalidades-e-mvp.md
    ├── 05-equipe-e-papeis.md
    ├── 06-organizacao-do-trabalho.md
    ├── 07-seguranca-privacidade-acessibilidade.md
    ├── 08-beneficios-riscos-limitacoes.md
    └── 09-escopo-do-projeto.md


Posteriormente, as contribuições individuais poderão ser adicionadas em pastas específicas para os papéis profissionais e as postagens do LinkedIn.

---

## Documentação

- [Empresa e contexto](docs/01-empresa-e-contexto.md)
- [Problema](docs/02-problema.md)
- [Proposta de solução](docs/03-proposta-solucao.md)
- [Funcionalidades e MVP](docs/04-funcionalidades-e-mvp.md)
- [Equipe e papéis](docs/05-equipe-e-papeis.md)
- [Organização do trabalho](docs/06-organizacao-do-trabalho.md)
- [Segurança, privacidade e acessibilidade](docs/07-seguranca-privacidade-acessibilidade.md)
- [Benefícios, riscos e limitações](docs/08-beneficios-riscos-limitacoes.md)
- [Escopo do projeto](docs/09-escopo-do-projeto.md)

---

## Status

Projeto em fase de documentação e planejamento acadêmico.

Não faz parte desta atividade desenvolver o sistema funcional. O objetivo é apresentar uma proposta coerente de solução, demonstrando como diferentes áreas profissionais colaborariam no desenvolvimento do produto.
