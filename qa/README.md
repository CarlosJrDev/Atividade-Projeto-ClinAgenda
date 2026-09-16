# Verificação do protótipo

Os testes são material complementar à contribuição de Front-end. Não são necessários para abrir o HTML ou cumprir o enunciado.

## Repetir a verificação

Com Python instalado, executar na raiz do repositório, preferencialmente em ambiente virtual:

```sh
python -m pip install playwright
python -m playwright install chromium
python qa/test_demo.py
```

O teste abre o HTML em um perfil temporário do Chromium, usa dados fictícios e produz `qa/resultado-testes.json` e capturas locais. As capturas e o ambiente virtual ficam fora do versionamento.

## Cobertura e limites

Os cenários exercem cadastro, agenda, alterações, conflitos locais, filtros, conversas, lembretes simulados, médico, gestão, persistência, atalhos e slides. O relatório corresponde ao HTML distribuído; a identificação do arquivo está em `versao-testada.json`.

A simulação de uma vaga ocupada entre a oferta do bot e a confirmação é sequencial e local. Não testa concorrência distribuída, servidor, API externa do WhatsApp ou proteção de dados reais. Os testes de impressão verificam o acionamento da interface, não a saída de uma impressora física. A largura móvel exercitada é 390 px; não há certificação de acessibilidade.
