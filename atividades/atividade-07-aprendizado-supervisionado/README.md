# Atividade 7 — Sistema especialista com aprendizado supervisionado

> Aula 13 (09/11). A professora pediu para adaptar o notebook do orientador de
> estudos para um problema nosso. Fiz em grupo com o João Gabriel, porque somos
> do mesmo squad (squad 5, repositório de TCCs) e cada um cuidou de uma fila do
> sistema. Juntamos as duas partes em um notebook só.

- Notebook do grupo: [`Triagem_Curadoria_TCC.ipynb`](Triagem_Curadoria_TCC.ipynb)
- Abrir no Colab (link oficial do grupo, o mesmo da ficha da A1): [link](https://colab.research.google.com/github/SungJiinwoo/Inteligencia_Artificial_Linguagens_Formais_e_Automatos/blob/main/Unidade5_SistemasEspecialistas/Triagem_Curadoria_TCC.ipynb)
- Datasets: [`dataset_fila_de_cadastros.csv`](dataset_fila_de_cadastros.csv) (minha parte) e
  [`dataset_triagem_tcc.csv`](dataset_triagem_tcc.csv) (parte do João)

---

## Como dividimos

No squad 5 eu fiquei com o cadastro, a validação e os perfis (BL-11, BL-12 e BL-20), e o João com a
fila de pendentes e a análise do TCC pela curadoria (BL-35 e BL-36). As duas coisas se encaixam:
só consegue abrir a fila da curadoria quem teve o cadastro **validado** pelo administrador e
recebeu o perfil **Curadoria**.

| Parte | O que faz | Quem fez |
|:--|:--|:--|
| Fila de cadastros | árvore de decisão prevê `validado` ou `recusado`; regras R1 a R4 dizem o que o administrador faz | eu |
| Fila da curadoria | árvore de decisão prevê `aprovada` ou `rejeitada`; regras R8 a R11 dizem o que a curadoria confere | João |
| Ligação entre as duas | regras R5 a R7: cadastro não validado, perfil errado ou TCC enviado pela própria pessoa bloqueiam a análise | nós dois |

## Resultado

| | Fila de cadastros | Fila da curadoria |
|:--|:--|:--|
| Dataset | 20 cadastros simulados (10 e 10) | 24 TCCs simulados (12 e 12) |
| Treino / teste | 15 / 5 | 18 / 6 |
| Acurácia | 100% | 83,3% |

Continuo desconfiada dos 100% da minha parte: são só 5 casos e fui eu que inventei os dados com
uma regra simples. O que mais me preocupa é o sistema ser injusto com quem tem nome curto ou
e-mail fora do padrão, e por isso a decisão final continua com o administrador. Isso está na
seção 10 do notebook e na [atividade de ética](../atividade-08-etica-em-ia/README.md).

---

[Voltar ao início](../../README.md)
