# Aula 11 - Agentes Inteligentes

**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos  
**Professora:** Kadidja Valéria  
**Aluna:** Julyane Ataides  
**Turma:** N1  
**Data:** 19/10/2026

---

## Resumo da aula

Nesta aula estudamos o Capítulo 2, sobre agentes inteligentes. Vimos como eles funcionam, como recebem informações do ambiente e como escolhem as ações que vão realizar.

Entendi que um agente inteligente não precisa ser apenas um robô. Pode ser também um programa ou até uma pessoa, desde que consiga perceber o ambiente e agir nele.

## 1. Agentes inteligentes

Um agente recebe informações do ambiente por meio de sensores e realiza ações usando atuadores.

Alguns exemplos:

- **Pessoa:** usa os olhos e ouvidos para perceber e as mãos e pernas para agir.
- **Robô:** pode usar câmeras e sensores para receber informações e motores para se movimentar.
- **Programa:** recebe dados e pode responder mensagens ou executar comandos.

O que entendi é que o agente percebe o que está acontecendo e, a partir disso, realiza uma ação.

## 2. Percepção e histórico

A percepção é a informação que o agente recebe em determinado momento.

Já o histórico é o conjunto de informações que ele recebeu até aquele instante.

Isso é importante porque uma mesma situação pode exigir decisões diferentes dependendo do que aconteceu antes.

Também vimos a diferença entre função e programa de agente.

- **Função de agente:** define a ação de acordo com o histórico de percepções.
- **Programa de agente:** coloca esse comportamento em funcionamento.

## 3. Racionalidade

Aprendi que ser racional não significa acertar sempre.

Um agente racional tenta escolher a melhor ação possível com as informações que possui naquele momento.

A racionalidade depende de quatro fatores:

1. Medida de desempenho.
2. Conhecimento prévio.
3. Ações disponíveis.
4. Histórico de percepções.

Um exemplo é o jogador de pôquer, que pode tomar uma boa decisão e mesmo assim perder.

Também vimos que a medida de desempenho precisa avaliar o resultado que realmente queremos alcançar.

## 4. Exemplo do aspirador

O exemplo do aspirador ajudou a entender melhor as decisões dos agentes.

Ele funciona em dois locais, A e B, e segue algumas regras:

- Se encontrar sujeira, aspira.
- Se estiver em A e estiver limpo, vai para B.
- Se estiver em B e estiver limpo, vai para A.

O problema é que ele pode continuar andando entre os locais mesmo quando os dois já estiverem limpos.

Com isso, entendi que nem sempre seguir uma regra fixa é suficiente. Em algumas situações, guardar informações anteriores ajuda o agente a tomar decisões melhores.

## 5. Modelo PEAS

O PEAS serve para descrever a tarefa de um agente.

- **P - Performance:** como o desempenho será avaliado.
- **E - Environment:** ambiente onde o agente atua.
- **A - Actuators:** como o agente realiza suas ações.
- **S - Sensors:** como ele recebe informações.

No exemplo do aspirador:

- **P:** manter o ambiente limpo, considerando tempo e energia.
- **E:** cômodos, sujeira e obstáculos.
- **A:** rodas e sistema de aspiração.
- **S:** sensores de posição, sujeira e proximidade.

Entendi que o PEAS ajuda a organizar o que o agente precisa fazer e quais recursos vai utilizar.

## 6. Classificação dos ambientes

Também estudamos que os ambientes podem ter características diferentes.

**Completamente observável:** o agente consegue perceber todas as informações importantes.

**Parcialmente observável:** algumas informações não estão disponíveis.

**Agente único:** não existem outros agentes tomando decisões que influenciem diretamente a tarefa.

**Multiagente:** outros agentes podem influenciar os resultados.

**Determinístico:** o estado e a ação definem o próximo estado.

**Estocástico:** existe incerteza sobre os resultados das ações.

**Episódico:** cada decisão pode ser avaliada separadamente.

**Sequencial:** uma decisão influencia as próximas.

**Estático:** o ambiente não muda enquanto o agente decide.

**Dinâmico:** o ambiente continua mudando.

**Semidinâmico:** o ambiente não muda, mas o tempo influencia o desempenho.

**Discreto:** possui estados ou ações separados.

**Contínuo:** envolve valores que mudam continuamente.

**Conhecido:** o agente sabe como suas ações afetam o ambiente.

**Desconhecido:** o agente precisa aprender como o ambiente funciona.

Alguns exemplos vistos foram o xadrez, o pôquer, o futebol e o tênis.

Uma coisa importante que aprendi foi que conhecer as regras de um ambiente não significa conseguir observar tudo o que acontece nele.

## 7. Tipos de agentes

Estudamos quatro tipos principais.

### Agente reativo simples

Escolhe a ação com base no que percebe no momento, seguindo regras.

Exemplo: se o aspirador encontra sujeira, ele limpa.

### Agente baseado em modelo

Guarda informações anteriores e mantém uma ideia do estado do ambiente.

Exemplo: o aspirador lembra quais locais já foram limpos.

### Agente baseado em objetivos

Escolhe suas ações pensando em alcançar uma meta.

Exemplo: um programa que procura uma rota para chegar a determinado destino.

### Agente baseado em utilidade

Compara os resultados possíveis para escolher a opção mais vantajosa.

Exemplo: escolher uma rota levando em consideração tempo, gastos e riscos.

A principal diferença que entendi é que alguns agentes seguem regras, enquanto outros conseguem considerar informações anteriores, objetivos e diferentes resultados antes de agir.

## 8. Aprendizagem e autonomia

A aprendizagem permite que um agente melhore suas decisões com a experiência.

O material apresentou quatro partes do agente com aprendizagem:

- **Elemento de desempenho:** escolhe as ações.
- **Crítico:** avalia os resultados.
- **Elemento de aprendizagem:** melhora o comportamento.
- **Gerador de problemas:** propõe experiências para conseguir novas informações.

Também aprendemos sobre autonomia, que é quando o agente passa a depender mais da própria experiência e não somente das regras colocadas pelo programador.

Um exemplo é o aspirador que aprende quais lugares costumam acumular mais sujeira.

## 9. Relação com autômatos

No final, vimos que os agentes também podem ser relacionados aos autômatos.

Um agente pode utilizar estados internos para guardar informações importantes do que aconteceu antes.

Quando recebe uma percepção, pode mudar de estado e realizar uma ação.

Um exemplo seria um agente que passa pelos estados de verificar, agir e parar.

Entendi que os autômatos podem ajudar a representar comportamentos mais simples dos agentes, usando estados e transições.

## O que aprendi com a aula

O principal que aprendi foi que um agente inteligente precisa perceber o ambiente e escolher suas ações de acordo com a situação.

Também entendi que uma decisão racional não significa que o resultado sempre será positivo, porque o agente nem sempre possui todas as informações.

O exemplo do aspirador ajudou bastante a perceber a importância do histórico e da medida de desempenho.

Outro ponto importante foi o PEAS, que serve para organizar a tarefa de um agente, e a classificação dos ambientes, que ajuda a entender por que cada situação pode exigir um tipo diferente de agente.

## Material utilizado

- Russell e Norvig - Capítulo 2: Agentes inteligentes.
- Slides da aula de 19/10/2026 - Professora Kadidja Valéria, UDF.
