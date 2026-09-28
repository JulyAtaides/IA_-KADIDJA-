# 📖 Unidade 3 — Expressões Regulares

> Anotações da aula de expressões regulares (regex). Foi a aula que ligou a
> teoria com código de verdade.

---

## 🎯 O que eu preciso saber ao terminar a aula

- O que é uma expressão regular;
- Onde ela fica na Hierarquia de Chomsky;
- Os símbolos principais (`*`, `+`, `[ ]`, `^`, `$`...);
- Ler uma regex pedaço por pedaço;
- O que a regex **não** consegue fazer.

---

## 1. O que é uma regex

É um **padrão** que descreve uma linguagem. Em vez de listar todas as
palavras, eu escrevo a "forma" delas.

```
padrão:  ab*
aceita:  a, ab, abb, abbb...
recusa:  b, ba, aab
```

> 💡 A gramática **gera** as palavras. A regex **confere** se uma palavra
> pertence ou não.

---

## 2. Regex e Chomsky

A regex descreve exatamente as linguagens **regulares** (tipo 3), as mesmas
da gramática regular da aula 3:

```
S → aS | b     (gramática)
a*b            (regex)
```

As duas querem dizer "vários `a` (ou nenhum) e um `b` no final".

---

## 3. Símbolos que eu mais uso

| Símbolo | Significado | Exemplo |
|:--:|:--|:--|
| `.` | qualquer símbolo | `a.c` → abc, a7c |
| `\.` | o ponto de verdade | `x\.com` |
| `[abc]` | um da lista | `[abc]` → a, b ou c |
| `[a-z]` | um do intervalo | letra minúscula |
| `*` | 0 ou mais vezes | `a*` → ε, a, aa |
| `+` | 1 ou mais vezes | `a+` → a, aa |
| `?` | 0 ou 1 vez | `ab?` → a, ab |
| `{2,}` | 2 ou mais vezes | `[a-z]{2,}` |
| `\|` | ou | `gato\|cão` |
| `^` | começo | |
| `$` | fim | |

> ⚠️ O que eu mais confundi: `*` aceita **zero** vezes, então `a*` aceita a
> palavra vazia. O `+` exige **pelo menos um**.

---

## 4. Lendo uma regex

```
^[A-Z][a-z]+$

^        começa aqui
[A-Z]    uma letra maiúscula
[a-z]+   uma ou mais minúsculas
$        termina aqui
```

Aceita `Maria`, `Brasil`. Recusa `maria`, `MARIA` e `M`.

---

## 5. O que a regex não consegue

A regex **não tem memória**, então ela não consegue contar.

```
0ⁿ1ⁿ   (mesma quantidade de 0 e 1)   ❌ regex não consegue
0*1*   (quantos 0 e 1 quiser)         ✅ consegue
```

Pra `0ⁿ1ⁿ` precisa de algo mais forte, e isso aparece na aula 09 com a
Máquina de Turing.

---

## 6. Resumo para a prova

| Conceito | Resumo rápido |
|:--|:--|
| **Regex** | padrão que reconhece linguagem regular (tipo 3) |
| **`*` x `+`** | `*` aceita zero, `+` precisa de um |
| **`.` x `\.`** | qualquer símbolo x ponto de verdade |
| **`^` e `$`** | prendem no começo e no fim |
| **Limite** | não conta, então `0ⁿ1ⁿ` não dá |

---

## 📌 Checklist

- [ ] Sei explicar o que é regex;
- [ ] Sei que ela é tipo 3;
- [ ] Sei a diferença de `*` e `+`;
- [ ] Sei pra que servem `^` e `$`;
- [ ] Sei por que ela não reconhece `0ⁿ1ⁿ`.

✅ Atividade da aula: [Atividade 4 — Regex para validação de e-mail](atividades/atividade-04-regex-validacao-email/README.md)

---

[⬅️ Voltar ao início](README.md)
