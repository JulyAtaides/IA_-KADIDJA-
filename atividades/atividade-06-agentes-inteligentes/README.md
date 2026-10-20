Aula 11 - Agentes inteligentes
Disciplina: Inteligência Artificial, Linguagens Formais e Autômatos
Professora: Kadidja Valéria
Aluna: Julyane Ataides - Turma N1
Aula: 19/10/2026
Minhas anotações da aula
Nessa aula a gente estudou o Capítulo 2, sobre agentes inteligentes. Pelo que entendi, um agente é algo que recebe informações do ambiente e faz alguma ação com base nisso. Pode ser uma pessoa, um robô ou até um programa de computador.
O que eu aprendi
- Sensores e atuadores: os sensores servem para perceber o ambiente e os atuadores para fazer as ações. No exemplo do aspirador, ele percebe onde tem sujeira e pode aspirar ou mudar de lugar.
- Percepção e histórico: percepção é a informação recebida naquele momento. O histórico é tudo que o agente percebeu antes. Isso faz diferença porque às vezes ele precisa lembrar do que já aconteceu.
- Função e programa de agente: a função mostra qual ação deve ser feita de acordo com as percepções. Já o programa é o que coloca isso para funcionar na máquina.
- Agente racional: não é um agente que sempre acerta. É aquele que tenta escolher a melhor ação com as informações que tem. Um jogador de pôquer pode jogar bem e ainda perder.
- Medida de desempenho: é a forma de avaliar se o agente está indo bem. No aspirador, não adianta só contar quanta sujeira ele aspirou. Importa manter os lugares limpos, sem gastar energia à toa.
- Autonomia e aprendizagem: o agente pode melhorar conforme ganha experiência, sem depender só das regras que recebeu no começo.
PEAS
Também aprendi a descrever a tarefa de um agente usando o PEAS:
- P: medida de desempenho, ou seja, o que conta como um bom resultado.
- E: ambiente onde ele age.
- A: atuadores, que são os meios de agir.
- S: sensores, que são os meios de perceber o ambiente.
Um exemplo é o aspirador: seu desempenho envolve limpeza, energia e tempo; o ambiente são os cômodos; os atuadores são as rodas e a aspiração; e os sensores verificam posição e sujeira.
Tipos de ambientes
Uma parte importante foi entender que nem todo ambiente funciona do mesmo jeito:
- Completamente ou parcialmente observável: se o agente consegue perceber tudo o que importa ou não.
- Agente único ou multiagente: se ele atua sozinho ou se outras pessoas/agentes também tomam decisões, como no futebol.
- Determinístico ou estocástico: se dá para saber o resultado da ação ou se existe incerteza.
- Episódico ou sequencial: se uma decisão é independente ou influencia o que vem depois.
- Estático ou dinâmico: se o ambiente fica parado enquanto ele decide ou continua mudando.
- Discreto ou contínuo: se os valores são separados, como pontos, ou mudam continuamente, como posição e velocidade.
- Conhecido ou desconhecido: se o agente já conhece como o ambiente funciona ou ainda precisa aprender.
Tipos de agentes
- Reativo simples: faz a ação olhando só a situação atual, seguindo uma regra.
- Baseado em modelo: guarda informações para ter uma ideia melhor do que está acontecendo.
- Baseado em objetivos: escolhe ações pensando numa meta.
- Baseado em utilidade: compara opções para decidir qual traz um resultado melhor, considerando coisas como tempo e custo.
- Com aprendizagem: usa a experiência e os resultados anteriores para melhorar as próximas decisões.
Relação com autômatos
Na parte de autômatos, entendi que podemos representar um agente simples usando estados e transições. Por exemplo, ele pode estar esperando, avaliando uma situação ou encerrando a tarefa. Quando recebe uma informação nova, muda de estado e faz uma ação. Só que poucos estados não conseguem mostrar todos os detalhes de uma situação real.
O que ficou mais claro para mim
O principal que tirei da aula é que a melhor ação depende da situação e das informações disponíveis. Não basta seguir uma regra sempre do mesmo jeito. O exemplo do aspirador ajudou a entender isso: se ele ficar andando entre dois lugares já limpos, pode acabar gastando energia sem necessidade.
Atividade
No arquivo Word desta pasta estão as respostas dos exercícios 2.3, 2.4 e 2.5, além da parte de autômatos.
Material utilizado
- Russell e Norvig, Capítulo 2 - Agentes inteligentes, disponibilizado para a aula.
- Slides Agentes Inteligentes, aula de 19/10/2026, professora Kadidja Valéria.
