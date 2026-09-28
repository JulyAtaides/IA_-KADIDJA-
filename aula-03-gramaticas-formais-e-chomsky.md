# 📖 Aula 3 — Gramáticas Formais e Hierarquia de Chomsky

> Minhas anotações da aula 3. Aqui a gente aprofundou gramática (que já tinha
> aparecido na aula 1) e viu como o Chomsky separa as gramáticas em tipos.

---

## 🎯 O que eu preciso saber ao terminar a aula

- Identificar as **4 partes** de uma gramática `G = (V, T, P, S)`;
- Saber a diferença entre `→` e `⇒`;
- Fazer uma **derivação** passo a passo;
- Saber quando a derivação **terminou**;
- Diferenciar gramática **regular** de **livre de contexto**;
- Entender a **Hierarquia de Chomsky**.

---

## 1. As partes de uma gramática

```
G = (V, T, P, S)
```

| Letra | Nome | O que é |
|:--:|:--|:--|
| `V` | Variáveis (não terminais) | as letras maiúsculas que vão sendo trocadas |
| `T` | Terminais | os símbolos que ficam na palavra final |
| `P` | Produções | as regras |
| `S` | Símbolo inicial | por onde a derivação começa |

> ⚠️ Na aula 1 apareceu `G = (N, Σ, P, S)`. É a mesma coisa com outros nomes:
> `N` = `V` e `Σ` = `T`. Fiquei confusa no começo, mas é só o nome que muda.

**Exemplo da aula:**

```
G = ({S}, {a, b}, P, S)
P:  S → aS
    S → b
```

---

## 2. `→` e `⇒` não são a mesma coisa

- `→` é a **regra** (faz parte da gramática). Lê "produz".
- `⇒` é o **passo** que eu faço na derivação. Lê "deriva em".

```
S → aS     é a regra
S ⇒ aS     é o que eu fiz agora usando a regra
```

---

## 3. Derivação

Sempre começo pelo `S` e vou trocando até não sobrar nenhuma variável.

Gerando `aab` com `S → aS | b`:

```
S ⇒ aS ⇒ aaS ⇒ aab
```

- `S → aS` coloca um `a` e deixa o `S` pra continuar;
- `S → b` coloca o `b` e **acaba**, porque não devolve variável.

> 💡 **Quando termina?** Quando não tem mais nenhuma letra maiúscula na linha.
> `aaS` ainda não é palavra! `aab` é.

---

## 4. Gramática regular (tipo 3)

As regras só podem ter **um terminal seguido de no máximo uma variável**, e a
variável tem que ficar **na ponta**:

```
S → aS | b      ✅ regular
```

Gera `{b, ab, aab, aaab, ...}`, ou seja, `aⁿb`.

---

## 5. Gramática livre de contexto (tipo 2)

Aqui a única exigência é: do lado **esquerdo** tem que ter **uma variável
sozinha**. Do lado direito pode ter qualquer coisa.

```
S → aSb | ε     ✅ livre de contexto (o S está no MEIO)
```

```
S ⇒ aSb ⇒ aaSbb ⇒ aabb
```

Cada passo coloca um `a` na esquerda **e** um `b` na direita juntos, então
sempre sai a mesma quantidade: `aⁿbⁿ`.

---

## 6. Hierarquia de Chomsky

| Tipo | Nome | Regra |
|:--:|:--|:--|
| 3 | Regular | terminal + no máximo 1 variável na ponta |
| 2 | Livre de contexto | lado esquerdo = 1 variável sozinha |
| 1 | Sensível ao contexto | lado esquerdo pode ter símbolos em volta da variável |
| 0 | Irrestrita | sem restrição |

Um tipo fica **dentro** do outro:

```
Tipo 3 ⊂ Tipo 2 ⊂ Tipo 1 ⊂ Tipo 0
```

> ⚠️ Toda regular também é livre de contexto! Mas na hora de classificar eu
> respondo a classe **mais apertada** (o número maior).

---

## 7. Como eu classifico

```
1. Todas as regras têm UMA variável sozinha do lado esquerdo?
      não → não é nem 2 nem 3
      sim → é pelo menos livre de contexto (tipo 2)

2. Em TODAS as regras a variável da direita está na ponta?
      sim → regular (tipo 3)
      não → livre de contexto (tipo 2)
```

Basta **uma** regra fora do formato pra não ser regular.

---

## 8. Resumo para a prova

| Conceito | Resumo rápido |
|:--|:--|
| **`G = (V, T, P, S)`** | variáveis, terminais, produções, inicial |
| **`→`** | regra (produz) |
| **`⇒`** | passo da derivação (deriva em) |
| **Terminou** | quando não sobra variável |
| **Regular** | `S → aS \| b` (variável na ponta) |
| **Livre de contexto** | `S → aSb \| ε` (variável no meio) |
| **Chomsky** | 3 ⊂ 2 ⊂ 1 ⊂ 0 |

---

## 📌 Checklist da Aula 3

- [ ] Sei dizer quem é V, T, P e S;
- [ ] Sei a diferença entre `→` e `⇒`;
- [ ] Consigo derivar uma palavra;
- [ ] Sei quando a derivação acabou;
- [ ] Sei classificar regular x livre de contexto;
- [ ] Sei a ordem dos tipos de Chomsky.

✅ Atividade da aula: [Atividade 3 — Gramáticas Formais e Hierarquia de Chomsky](atividades/atividade-03-gramaticas-formais-e-chomsky.md)

---

[⬅️ Voltar ao início](README.md)
