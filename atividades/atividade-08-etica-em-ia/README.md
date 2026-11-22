# Atividade 8 — Ética e implicações em IA (A1)

> Aula de 16/11. Análise ética do sistema especialista que fiz em grupo com o João Gabriel
> na [atividade 7](../atividade-07-aprendizado-supervisionado/README.md) (squad 5).

---

## 1. Leitura e vídeo

**Artigo:** LACERDA JÚNIOR, F. P. *Da proibição à governança: uso ético da inteligência artificial
generativa na educação superior: uma revisão integrativa (2023–2026)*. Revista Foco, v. 19, n. 8, 2026.

A questão de integridade que eu separei foi a da **autoria**. O artigo diz que a ferramenta não
pode ser autora porque não responde pelo que entrega, então quem assina é responsável pelo
conteúdo. Também diz que a declaração precisa contar qual ferramenta foi usada, para quê e até
onde ela ajudou, porque sem isso não dá para avaliar como o trabalho foi feito.

**Vídeo:** IEA-USP, *O Estado da Arte em Ética na Inteligência Artificial* (2026), trecho de
**6:10 a 6:58**. A ideia que eu levei: ética não é só cumprir uma lista de regras, e não adianta
perguntar só se o sistema é exato; é preciso ver a instituição e as pessoas em volta dele. Ele usa
a comparação de que o alinhamento começa no primeiro traço da pintura, e não é um verniz no final.
No nosso caso, isso quer dizer que a revisão do administrador tem que fazer parte do sistema desde
o começo.

## 2. Análise ética do projeto

**O projeto.** O squad 5 está fazendo o repositório público de TCCs dos cursos de TI da UDF. Eu
cuidei do cadastro, da validação e dos perfis (BL-11, BL-12, BL-20) e o João da fila da curadoria
(BL-35, BL-36). O nosso sistema especialista ajuda o administrador a decidir o que fazer com os
cadastros não validados e ajuda a curadoria a saber o que conferir em cada TCC. Quem pode ser
afetado são as pessoas que se cadastram (orientadores, coordenação e curadoria) e os alunos que
têm o TCC analisado. A IA entra em duas árvores de decisão: uma prevê se o cadastro tem cara de
`validado` ou `recusado` e a outra se o TCC tem cara de `aprovada` ou `rejeitada`. As regras de
acesso (R5 a R8), de data (R9) e de duplicidade (R10) são regras de negócio do squad e não dependem
de previsão; as regras R1 a R4 e R11 e R12 usam a previsão junto com o que a pessoa informa.

| Aspecto | Situação no projeto | Quem pode ser afetado | O que fizemos ou faríamos |
|:--|:--|:--|:--|
| Privacidade e dados | O cadastro guarda nome, e-mail e data de nascimento. | Quem se cadastra. | O modelo só usa contagens (palavras do nome, números no e-mail), os dados são inventados e o squad apaga cadastro parado em 30 dias (RN-36). |
| Viés e equidade | A árvore aprendeu que nome de uma palavra e e-mail sem nome levam a "recusado". | Quem tem nome curto, nome estrangeiro registrado diferente ou e-mail de setor. | Testar cadastros iguais mudando só o tamanho do nome; a R3 manda falar com a pessoa antes de recusar; recusar exige motivo (RN-36). |
| Transparência | O administrador pode achar que a previsão já é a decisão. | Quem se cadastra. | A saída mostra a previsão, a regra, os fatos usados e o aviso de que é só uma recomendação. |
| Supervisão e responsabilidade | Um cadastro válido pode ser recusado por erro do modelo. | Quem se cadastra e, depois, a curadoria, que fica sem pessoas para analisar. | Quem decide é sempre o administrador (RF13). A pessoa recusada recebe o motivo por e-mail e pode se cadastrar de novo. |
| Impacto social | A fila de cadastros anda mais rápido e a curadoria começa a trabalhar antes. | Ajuda o administrador e os alunos; prejudica quem for recusado sem motivo real. | O protótipo não mexe no sistema real e só seria usado depois de testar com decisões reais e com autorização da faculdade. |

## 3. Debate e dilema ético

**Dilema:** o modelo diz "recusado" para alguém com nome de uma palavra só, e o administrador tem
vários cadastros perto de completar 30 dias.

* **Seguir o modelo:** a fila anda, mas uma pessoa da faculdade pode ter o cadastro apagado só por
  causa do nome.
* **Usar o modelo só como sugestão:** dá mais trabalho, mas ninguém é recusado só por um padrão, e
  quem for recusado sabe o motivo e pode contestar.

Ficamos com a segunda, que é o que as regras R2 e R3 fazem.

### Reflexão individual: Julyane Ataides

Eu manteria a decisão de o administrador dar sempre a última palavra e mudaria os dados de
treino: colocaria mais exemplos de nomes curtos e de e-mails de setor que foram validados, porque
hoje a linha 20 aparece uma vez só e a árvore erra ela mesmo estando no treino. O argumento que
mais me influenciou foi o do vídeo, de que o cuidado tem que estar no sistema desde o começo e não
ser colocado no final. Para saber se a medida funciona, eu compararia quantos cadastros o modelo
marcou como "recusado" e o administrador acabou validando, separando por tamanho do nome.

## 4. Declaração de uso de sistemas de IA

**IA incorporada ao projeto.** O projeto utiliza duas árvores de decisão (`DecisionTreeClassifier`,
scikit-learn) junto com um sistema especialista de regras para recomendar o que fazer na fila de
cadastros e na fila da curadoria do repositório de TCCs. Na minha parte, o sistema recebe contagens
do cadastro (palavras do nome, se o e-mail tem o nome, números no e-mail), os dias na fila e se o
vínculo da pessoa já foi confirmado, e gera a regra aplicada, a recomendação, o prazo restante e a
explicação. Verificamos o funcionamento com treino e teste, acurácia e matriz de confusão, a
exceção da linha 20, três casos novos e a troca de um fato por vez. As limitações são os dados
simulados e poucos, os rótulos criados por nós e o risco de viés contra nomes curtos ou fora do
padrão. A revisão cabe ao administrador (cadastros) e à curadoria (TCCs).

**IA utilizada na elaboração do trabalho.** Utilizei o Claude (Anthropic, modelo Opus) para juntar
a minha parte e a do João em um notebook só, revisar os textos e conferir se a entrega seguia o que
a professora pediu. Aproveitei sugestões de organização do código e da base de regras e ajustes de
redação depois de conferir as regras R1 a R8 com o que implementamos no squad 5
(`contas/services.py` e `docs/requirements.md`), rodar o notebook inteiro e ver se os resultados
batiam com a análise. Assumo a responsabilidade pelas escolhas, verificações e conteúdo da entrega.

---

[Voltar ao início](../../README.md)
