# Atividade 7 — Sistema especialista com aprendizado supervisionado

> Aula 13 (09/11). A professora pediu para adaptar o notebook do orientador de
> estudos para um problema nosso. Usei a minha parte do squad 5: a **fila de
> cadastros** que o administrador do repositório de TCCs precisa validar.

- Notebook: [`fila_de_cadastros.ipynb`](fila_de_cadastros.ipynb)
- Abrir no Colab: [link](https://colab.research.google.com/github/JulyAtaides/IA_-KADIDJA-/blob/main/atividades/atividade-07-aprendizado-supervisionado/fila_de_cadastros.ipynb)
- Dataset: [`dataset_fila_de_cadastros.csv`](dataset_fila_de_cadastros.csv)

---

## Resumo do que eu fiz

Primeiro a árvore de decisão olha três coisas do cadastro (quantas palavras tem
o nome, se o e-mail tem o nome da pessoa e quantos números tem no e-mail) e
diz se ele tem cara de **validado** ou **recusado**.

Depois essa resposta vira um fato. O sistema especialista junta esse fato com
o que o administrador sabe (se ele já confirmou que a pessoa é da faculdade) e
escolhe uma das quatro regras: validar, confirmar antes, conferir com a pessoa
ou recusar com motivo.

A árvore é a parte que aprende com os dados. As regras fui eu que escrevi.

## Resultado

| | |
|:--|:--|
| Dataset | 20 cadastros simulados (10 validados, 10 recusados) |
| Treino / teste | 15 / 5 |
| Acurácia | 100% nos 5 de teste |
| O que a árvore aprendeu | e-mail sem o nome da pessoa → recusado; nome com 1 palavra → recusado |

Fiquei desconfiada dos 100%, porque são só 5 casos e fui eu que inventei os dados.
Na conclusão do notebook eu falo disso e do risco de o sistema ser injusto com
quem tem nome curto.

---

[Voltar ao início](../../README.md)
