# Papel Profissional — Desenvolvedor Back-end

**Integrante:** Carlos Alberto  
**Projeto:** ClinAgenda  
**Papel:** Desenvolvedor Back-end

## O que faz

O desenvolvedor Back-end é responsável pelas regras de negócio e pelo processamento das informações do sistema. Ele faz a ligação entre as interfaces utilizadas pelos usuários e o banco de dados.

No ClinAgenda, o Back-end seria responsável por garantir que operações como agendamento, remarcação e cancelamento funcionem corretamente.

## Principais responsabilidades

No projeto, suas principais responsabilidades seriam:

- desenvolver as regras de agendamento;
- validar disponibilidade de médicos e horários;
- impedir conflitos de consultas;
- controlar o acesso às informações;
- integrar o sistema ao banco de dados;
- fornecer dados para o painel web e para o chatbot;
- registrar o status dos atendimentos.

Uma das responsabilidades mais importantes seria evitar que dois pacientes consigam reservar o mesmo médico no mesmo horário.

## Conhecimentos e competências

Para exercer essa função, são importantes conhecimentos em:

- lógica de programação;
- programação orientada a objetos;
- APIs REST;
- banco de dados e SQL;
- segurança e controle de acesso;
- Git e versionamento.

Também são importantes organização, raciocínio lógico, capacidade de resolver problemas e comunicação com outras áreas.

Em uma futura implementação do ClinAgenda, poderiam ser utilizados **Java e Spring Boot** para desenvolver uma API REST.

## Possíveis entregas

O desenvolvedor Back-end poderia produzir:

- API REST do sistema;
- regras de agendamento;
- validação de conflitos de horários;
- integração com banco de dados;
- autenticação e controle de acesso;
- integração com o chatbot;
- testes das regras de negócio.

## Contribuição para o ClinAgenda

O Back-end ajudaria a centralizar as regras do sistema.

Por exemplo, se um paciente tentar marcar uma consulta pelo chatbot ao mesmo tempo em que a recepção tenta utilizar aquele horário, o sistema deverá verificar a disponibilidade antes de confirmar o agendamento.

Isso ajuda a reduzir conflitos, duplicidades e inconsistências entre os diferentes canais utilizados pela clínica.

## Relação com outros profissionais

O Back-end trabalharia principalmente com:

- **Product Owner:** para compreender as regras e prioridades do produto;
- **UI/UX:** para entender os fluxos que precisam ser atendidos pelo sistema;
- **Front-end:** para definir a comunicação entre as telas e a API;
- **Banco de Dados:** para organizar o armazenamento e a integridade das informações.

## Caso essa função não fosse considerada

Sem o Back-end, o sistema não teria uma área central responsável por aplicar as regras de negócio, validar os agendamentos e integrar as interfaces ao banco de dados.

Isso poderia gerar conflitos de horários, informações inconsistentes e regras diferentes entre o painel web e o chatbot.