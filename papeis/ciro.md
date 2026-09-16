# Papel Profissional — Desenvolvedor Front-end

**Integrante:** Ciro Junior

**Empresa fictícia:** Tech Solutions

**Projeto:** ClinAgenda

**Papel:** Desenvolvedor Front-end

## O que faz

O desenvolvedor Front-end transforma os fluxos e as interfaces planejadas em telas que as pessoas conseguem utilizar. Trabalha com a apresentação das informações, os formulários, as interações e o retorno visual de cada ação.

No ClinAgenda, essa área permite que recepção, médicos e gestão operem a agenda e acompanhem as consultas por meio do painel web.

## Justificativa da escolha

A escolha considera a afinidade com a área, seguindo o critério de distribuição registrado pelo grupo. O Front-end é necessário porque as regras de agendamento precisam chegar ao usuário por telas compreensíveis. Minha contribuição se concentra em transformar essa proposta em interações demonstráveis e manter as informações coerentes entre os módulos.

## Principais responsabilidades

- construir as telas de agenda, pacientes, médico e gestão;
- implementar formulários e ações de agendar, remarcar, cancelar e confirmar presença;
- apresentar mensagens de sucesso, erro e confirmação;
- atualizar os registros exibidos depois de cada operação;
- manter o paciente selecionado coerente com a conversa no canal simulado;
- cuidar da navegação por teclado, dos rótulos e da adaptação da interface;
- combinar com o Back-end o formato dos dados e o tratamento das respostas da API.

A validação na interface ajuda o usuário, mas a aplicação real das regras e do controle de acesso deverá ocorrer também no servidor.

## Conhecimentos e competências

- **HTML:** estrutura das páginas, campos e elementos semânticos.
- **CSS:** apresentação, disposição dos elementos e adaptação a diferentes telas.
- **JavaScript:** eventos, validações, estado e atualização da interface.
- **Acessibilidade:** foco visível, rótulos, teclado e mensagens compreensíveis.
- **HTTP e JSON:** comunicação futura com a API.
- **Git e GitHub:** organização das alterações e revisão em equipe.
- Comunicação, atenção aos detalhes, resolução de problemas e colaboração.

## Entregas e situação atual

Como apoio adicional à atividade, foi preparado um [protótipo demonstrativo em HTML](../prototipo/clinagenda.html), com CSS e JavaScript no mesmo arquivo. Ele demonstra os fluxos com dados fictícios salvos no navegador.

Minha documentação inclui a [postagem individual](../linkedin/ciro.md), o [guia da contribuição e roteiro de dois minutos](../docs/10-contribuicao-frontend-ciro.md) e [instruções dos testes](../qa/README.md).

Em uma evolução real, o Front-end também entregaria a integração com a API, tratamento de sessão, carregamento e falhas de conexão. Esses recursos não estão implementados no protótipo.

## Contribuição para o ClinAgenda

Ao remarcar uma consulta, o usuário precisa visualizar o novo horário e entender o resultado da operação. Na demonstração, agenda, histórico e conversa refletem as mudanças. Ao trocar de paciente no canal simulado de WhatsApp, o nome, as mensagens e as opções também mudam.

Isso permite apresentar como uma interface integrada pode ajudar na organização da clínica. Não foram medidos benefícios em clínicas reais.

## Relação com outros profissionais

- **Product Owner:** alinhar prioridades, regras e critérios de aceite.
- **UI/UX:** implementar os fluxos e revisar a clareza das telas.
- **Back-end:** definir pedidos, respostas e erros da futura API.
- **Banco de Dados:** alinhar, junto ao Back-end, quais informações as telas precisam apresentar e preservar.
- **Equipe:** testar os fluxos e revisar acessibilidade e uso responsável dos dados.

## Caso essa função não fosse considerada

As pessoas não teriam uma interface adequada para operar o sistema. Mesmo com regras e dados organizados, ações pouco claras poderiam causar erros de seleção, dificuldade para localizar consultas e dúvidas sobre o resultado de um agendamento.

## Limitações e cuidados

O HTML é uma demonstração local, não um sistema de produção. WhatsApp, lembretes e perfis são simulados; não há login real, banco central ou integração externa. A checagem local de horários não garante proteção contra reservas feitas por vários usuários simultaneamente.

Usar somente dados fictícios. Os recursos de teclado e legibilidade são cuidados implementados, não uma certificação de acessibilidade. O protótipo é opcional: o objetivo acadêmico continua sendo documentar a proposta e a colaboração entre as áreas.

## Referências de estudo

- [MDN — módulos de formação em desenvolvimento web](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core): fundamentos de HTML, CSS, JavaScript, acessibilidade e versionamento.
- [W3C — referência rápida WCAG 2.2](https://www.w3.org/WAI/WCAG22/quickref/): apoio para revisar teclado, foco, identificação dos campos e apresentação de erros.

Referências consultadas em 16/09/2026.
