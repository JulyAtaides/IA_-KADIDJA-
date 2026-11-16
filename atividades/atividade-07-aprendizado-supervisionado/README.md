# 📝 Atividade 7 — Sistema especialista com aprendizado supervisionado

> Aula 13 (09/11). A professora pediu para adaptar o notebook do orientador de
> estudos para um problema nosso. Usei a minha parte do squad 5: a **fila de
> cadastros** que o administrador do repositório de TCCs precisa validar.

📓 Notebook: [`fila_de_cadastros.ipynb`](fila_de_cadastros.ipynb)
▶️ Abrir no Colab: [link](https://colab.research.google.com/github/JulyAtaides/IA_-KADIDJA-/blob/main/atividades/atividade-07-aprendizado-supervisionado/fila_de_cadastros.ipynb)
🗃️ Dataset: [`dataset_fila_de_cadastros.csv`](dataset_fila_de_cadastros.csv)

---

## 💭 A ideia

```
dados do cadastro  →  árvore de decisão  →  previsão (validado / recusado)
                                                    │
o administrador confirma o vínculo? (sim / não) ────┤
                                                    ▼
                                         regras R1 a R4  →  o que fazer
```

- A **árvore** aprende com os dados (a parte que "aprende sozinha").
- As **regras** fui eu que escrevi (a parte do sistema especialista).
- A previsão do modelo vira um **fato** que as regras usam.

## ✅ Resultado

| | |
|:--|:--|
| Dataset | 20 cadastros simulados (10 validados, 10 recusados) |
| Treino / teste | 15 / 5 |
| Acurácia | 100% nos 5 de teste |
| O que a árvore aprendeu | e-mail sem o nome da pessoa → recusado; nome com 1 palavra → recusado |

> 💡 Os 100% não provam nada: são poucos casos e dados simulados. Expliquei
> isso no notebook, junto com o risco de viés (nome curto não quer dizer
> cadastro falso).

---

[⬅️ Voltar ao início](../../README.md)
