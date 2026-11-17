# Tempo de implementação com e sem IA

Projeto final da disciplina Métodos de Computação Experimental e Quantitativa (MCEQ), Engenharia de Software, PUC-Campinas, 2º semestre de 2026.

**Equipe:** Anderson Lucas do Nascimento Gondim, Daniel Henrique Inoue Jange, Pedro Facine Nery

## Pergunta de pesquisa

Em tarefas reais de desenvolvimento open-source, o uso permitido de ferramentas de IA generativa por desenvolvedores experientes altera o tempo total de implementação das issues, em comparação ao desenvolvimento sem IA?

- H0: não há diferença na média do log do tempo total de implementação, por desenvolvedor, entre tarefas com IA e sem IA
- H1 (bilateral): há diferença

Desenho: pareado por desenvolvedor (16 desenvolvedores fizeram tarefas nas duas condições).

## Dados

- **Origem:** METR, estudo "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (Becker et al., 2025, arXiv:2507.09089)
- **Repositório original:** https://github.com/METR/Measuring-Early-2025-AI-on-Exp-OSS-Devs
- **Arquivo usado:** `data_complete.csv` (246 tarefas, 16 desenvolvedores)
- **Data de acesso:** 16/11/2026
- **Licença:** o repositório original não declara licença. Por isso o arquivo não é redistribuído aqui: o script `baixar_dados.py` baixa direto da fonte.
- **Tipo de estudo:** experimento publicado (cada tarefa foi sorteada para ser feita com ou sem IA)

## Como reexecutar

1. Instalar as bibliotecas: `pip install -r requirements.txt`
2. Baixar os dados: `python baixar_dados.py` (o arquivo vai para `dados/brutos/`)
3. Rodar a análise: [a definir]

## Estrutura

```
baixar_dados.py    script que baixa os dados da fonte original
requirements.txt   bibliotecas usadas
dados/brutos/      dados originais, criados pelo script (não editar à mão)
dados/limpos/      dados limpos, gerados pela análise
```
