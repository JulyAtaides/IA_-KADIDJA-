Questões:

1. Alfabeto
2. Palavras sobre um alfabeto
3. Símbolo ou palavra
4. Linguagem
5. Linguagem descrita por um padrão
6. Linguagem vazia e palavra vazia
7. As partes de uma gramática
8. Aplicando uma produção
9. Derivação completa de uma palavra
10. A palavra pode ser gerada
11. Desafio final

---

## 1. Alfabeto

Enunciado:

```
Considere Σ = {a, b, c} e responda:

1. Quantos símbolos existem no alfabeto? São 3 símbolos. É só contar o que está dentro das chaves: a, b e c.
2. Quais são os símbolos? São a, b e c, exatamente os que aparecem dentro das chaves.
3. O símbolo a pertence ao alfabeto? Sim, a ∈ Σ.
4. O símbolo d pertence ao alfabeto? Não, d ∉ Σ.
5. Escreva uma palavra formada por símbolos desse alfabeto. abc
```

---

## 2. Palavras sobre um alfabeto

Enunciado:

```
Considere Σ = {0, 1}.

Classifique cada sequência como palavra válida ou não válida, justificando:

0101 - válida. Todos os símbolos são 0 ou 1, e os dois estão em Σ.
00110 - válida. Todos os símbolos são 0 ou 1, e os dois estão em Σ.
012 - não válida. O 2 não está em Σ, e basta um símbolo de fora para estragar a sequência inteira.
111 - válida. O 1 está em Σ, e repetir o mesmo símbolo pode.
10a - não válida. O a não está em Σ = {0, 1}.
```
---

## 3. Símbolo ou palavra

Enunciado:

```
Considere Σ = {0, 1}.

Determine se as afirmações são verdadeiras ou falsas. Justifique cada resposta.

1. 0 ∈ Σ - Verdadeiro. O 0 é um dos dois símbolos escritos em Σ = {0, 1}.
2. 1 ∈ Σ - Verdadeiro. Mesma coisa, o 1 também está na lista.
3. 01 ∈ Σm- Falso. O 01 tem dois símbolos, então é uma palavra, e não um símbolo sozinho. O
Σ só tem símbolos soltos, que são o 0 e o 1, e o 01 não é um deles.
4. 01 ∈ Σ* - Verdadeiro. O Σ* é o conjunto de todas as palavras que dá pra montar com os símbolos de Σ. Como o 0
e o 1 estão no alfabeto, a palavra 01 pode ser montada e está em Σ*.
5. 2 ∈ Σ - Falso. O 2 não aparece em Σ = {0, 1}. 
6. 101 ∈ Σ* - Verdadeiro. Os três símbolos de 101, que são 1, 0 e 1, estão em Σ.
```
---

## 4. Linguagem

Enunciado:

```
Considere a linguagem L = {0, 01, 011, 0111}.

Determine se cada palavra pertence à linguagem:

1. 0 ∈ L - sim, o 0 está escrito na lista.
2. 01 ∈ L - sim, o 01 está escrito na lista.
3. 0111 ∈ L - sim, o 0111 está escrito na lista.
4. 10 ∈ L - não. O 10 não está na lista. A ordem importa, e aqui o 1 vem antes do 0.
5. 111 ∈ L - não. O 111 não está na lista, e todas as palavras dessa linguagem começam com 0,
  enquanto essa começa com 1.
6. 011 ∈ L - sim, o 011 está escrito na lista.
```
---

## 5. Linguagem descrita por um padrão

Enunciado:

```
Considere L = {bⁿ | n ≥ 1}.

1. Escreva as cinco primeiras palavras.
b
bb
bbb
bbbb
bbbbb

2. Explique o significado de bⁿ.
O bⁿ quer dizer n letras b, e a condição diz que o n começa em 1.
3. A palavra bbbbbb pertence à linguagem?
Sim. Contei as letras e são seis b, então bbbbbb é o mesmo que b⁶. Como 6 ≥ 1, ela obedece a
condição da linguagem.
4. A palavra vazia (ε) pertence à linguagem?
Não, ε ∉ L. O ε é a palavra que não tem símbolo nenhum, ou seja, seria b⁰, com n = 0. Só que a
condição exige n ≥ 1, e o zero não é maior nem igual a 1

``'

```

---

## 6. Linguagem vazia e palavra vazia

Enunciado:

```
Explique, com suas próprias palavras, a diferença entre:

A) L = ∅  é uma caixa vazia. O L = {ε} é uma caixa com uma folha em branco dentro.
B) L = {ε}  é uma linguagem que tem uma palavra, e essa palavra é o ε, que não tem símbolo nenhum. Se
eu perguntar quantas palavras tem aí, a resposta é uma.

Depois responda:

1. Qual delas possui uma palavra? A B, L = {ε}. Tem exatamente uma coisa escrita dentro das chaves, que é o ε. Uma coisa dentro é uma
palavra.
2. Qual delas não possui nenhuma palavra? A A, L = ∅. O ∅ é o símbolo do conjunto vazio, que não tem nada dentro. Sem nada dentro, sem
palavra.
3. Qual é o comprimento da palavra ε? Zero, |ε| = 0. Comprimento é a contagem de símbolos da palavra, e o ε não tem símbolo nenhum para
contar.
```
---

## 7. As partes de uma gramática

Enunciado:

```
Considere G = ({S, A}, {0, 1}, P, S) com P = {S → 0A, A → 1}.

Identifique:

1. O conjunto de variáveis. V = {S, A}.
2. O conjunto de terminais. T = {0, 1}
3. O conjunto de produções. P = {S → 0A, A → 1}
4. O símbolo inicial. É o S
5. Qual palavra pode ser gerada por essa gramática? A palavra 01
```
---

## 8. Aplicando uma produção

Enunciado:

```
Considere S → 0S. Começando com S:

1. Aplique a regra uma vez. S ⇒ 0S
2. Aplique a regra duas vezes. 0S ⇒ 00S
3. Aplique a regra três vezes. 00S ⇒ 000S
4. Escreva a sequência completa de derivação. S ⇒ 0S ⇒ 00S ⇒ 000S
```
---

## 9. Derivação completa de uma palavra

Enunciado:

```
Utilizando G: S → aS | b, gere aaab.

Escreva todos os passos da derivação.
```
Passo a passo:

```
início    S        comecei pelo símbolo inicial, como manda a definição
passo 1   aS       apliquei S → aS, colocou o 1º a e devolveu o S
passo 2   aaS      apliquei S → aS, colocou o 2º a e devolveu o S
passo 3   aaaS     apliquei S → aS, colocou o 3º a e devolveu o S
passo 4   aaab     apliquei S → b, trocou o S por b e encerrou
```
---

## 10. A palavra pode ser gerada

Enunciado:

```
Considere G: S → 0S | 1.

Determine se cada palavra pode ser gerada:

1. 1  Sim, pode ser gerada.
2. 01 Sim, pode ser gerada.
3. 001 Sim, pode ser gerada.
4. 0001 Sim, pode ser gerada.
5. 101 Não pode ser gerada, A palavra começa com 1. Para sair um 1, a única regra é S → 1, e ela apaga o S, ou seja, encerra a
derivação ali.
6. 1001 Não pode ser gerada, A palavra começa com 1. Para sair um 1, a única regra é S → 1, e ela apaga o S, ou seja, encerra a
derivação ali.
---

## 11. Desafio final

Enunciado:

```
Considere G: S → aS | b. Responda sem consultar o gabarito:

1. A palavra b pode ser gerada? sim
2. A palavra ab pode ser gerada? sim
3. A palavra aab pode ser gerada? sim
4. A palavra aaab pode ser gerada? sim
5. A palavra aba pode ser gerada? Não. O problema é o a que vem depois do b.
6. Escreva a derivação completa de aaaab. S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaaaS ⇒ aaaab
7. Descreva, com suas palavras, o padrão das palavras geradas por essa gramática. 
Toda palavra dessa gramática é um monte de a, que pode ser nenhum, com um b no final.
