# 📖 Aula 1 — Linguagens Formais e Gramáticas

> Minhas anotações da primeira aula. Escrevi com as minhas palavras pra fixar
> os conceitos: alfabetos, cadeias, linguagens e gramáticas. No fim tem o
> resumo pra prova, o mapa mental e o checklist do que preciso saber explicar.

---

## 🎯 O que eu preciso saber ao terminar a aula

- Entender o que é um **alfabeto**;
- Reconhecer **cadeias / palavras**;
- Saber o que é a **palavra vazia** `ε`;
- Identificar **prefixos** e **sufixos**;
- Entender o que é uma **linguagem formal**;
- Ler a notação `L ⊆ Σ*`;
- Entender como funciona uma **gramática formal**;
- Interpretar **regras de produção**;
- **Gerar palavras** a partir de uma gramática.

---

## 1. Operadores lógicos

Antes de entrar nas linguagens, a professora revisou os operadores da lógica.
São quatro que preciso decorar:

| Símbolo | Nome | Como eu leio |
|:--:|:--|:--|
| `¬` | Negação | "não" |
| `∧` | Conjunção (E) | "e" |
| `∨` | Disjunção (OU) | "ou" |
| `→` | Implicação | "implica" / "se... então" |

**Exemplo meu** — vou usar duas frases pra testar:

```
p = "Estudei para a prova."
q = "Fui bem na prova."
```

- `¬p` → "Não estudei para a prova."
- `p ∧ q` → "Estudei para a prova **e** fui bem na prova." (só é verdade se as duas forem verdade)
- `p ∨ q` → "Estudei para a prova **ou** fui bem na prova." (basta uma ser verdade)
- `p → q` → "**Se** estudei para a prova, **então** fui bem na prova."

> ⚠️ **Cuidado com o `→`:** ele muda de sentido dependendo de onde aparece.
> Na **lógica** = implicação. Na **gramática** (mais pra frente) = produz/gera.

---

## 2. Palavra vazia — `ε`

A palavra vazia é escrita como `ε` (lê-se **épsilon**). É uma cadeia que **não
tem nenhum símbolo**. O tamanho dela é zero:

```
|ε| = 0
```

Comparando tamanhos:

```
|abc| = 3      (três símbolos)
|ε|   = 0      (nenhum símbolo)
```

> ⚠️ **Não confundir:** `ε` **não** é espaço em branco. Espaço é um símbolo;
> `ε` é a ausência total de símbolos.

---

## 3. Prefixos e sufixos

Usando a palavra `ab`:

**Prefixo** = pedaço que começa **no início** da palavra.

```
Prefixos(ab) = {ε, a, ab}
```

**Sufixo** = pedaço que termina **no final** da palavra.

```
Sufixos(ab) = {ε, b, ab}
```

🧠 **Meu macete:**
- Prefi**xo** → começa no come**ço**.
- Sufi**xo** → termina no fi**m**.
- O `ε` sempre entra nos dois (é prefixo **e** sufixo de qualquer palavra).

| Palavra | Prefixos | Sufixos |
|:--:|:--|:--|
| `ab` | ε, a, ab | ε, b, ab |

---

## 4. Alfabeto — `Σ`

Um **alfabeto** é um conjunto **finito** de símbolos. Escrevo como `Σ`
(lê-se **sigma**).

```
Σ = {a, b}
```

Esse alfabeto tem 2 símbolos (`a` e `b`). Com eles dá pra montar várias
palavras:

```
a, b, aa, ab, ba, bb, aaa, aab, aba, ...
```

---

## 5. `Σ*` — todas as cadeias possíveis

`Σ*` é o conjunto de **todas** as cadeias finitas que dá pra formar com os
símbolos do alfabeto, **incluindo o `ε`**.

Com `Σ = {a, b}`:

```
Σ* = {ε, a, b, aa, ab, ba, bb, aaa, ...}
```

**Tem limite de tamanho?** Não. As palavras podem crescer para sempre
(`a`, `aa`, `aaa`, ...).

Pra um alfabeto de 2 símbolos, a quantidade de cadeias de cada tamanho é `2ⁿ`:

| Tamanho (n) | Quantidade (2ⁿ) |
|:--:|:--:|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |

> 📌 **Sacada importante:** `Σ*` é **infinito**, mas cada palavra dentro dele
> tem tamanho **finito**.

---

## 6. Linguagem formal — `L`

Uma **linguagem formal** é um conjunto de palavras montadas a partir do
alfabeto. A definição é:

```
L ⊆ Σ*
```

Lê-se: "**L é um subconjunto de sigma estrela**". Ou seja, `L` é uma
**seleção** de palavras que já existem em `Σ*`.

Juntando as peças:
- `Σ` → o alfabeto (os símbolos).
- `Σ*` → todas as palavras possíveis.
- `L` → só as palavras que eu escolhi de `Σ*`.

**Exemplo** com `Σ = {a, b}`:

```
L = {a, ab, abb, abbb}      → como só usa a e b, então L ⊆ Σ*
```

A linguagem pode ser:
- **Finita** → `L = {ε, a, ab}` (dá pra contar).
- **Infinita** → `L = {a, aa, aaa, ...}` (não acaba).

---

## 7. Gramática formal

Uma **gramática** é o conjunto de regras que **gera** as palavras de uma
linguagem. O formato geral é:

```
G = (N, Σ, P, S)
```

| Elemento | O que é |
|:--:|:--|
| `N` | Não terminais (símbolos "provisórios", que ainda vão ser trocados) |
| `Σ` | Terminais (símbolos "definitivos", do alfabeto) |
| `P` | Produções (as regras) |
| `S` | Símbolo inicial (por onde começa) |

Gramática do exemplo:

```
G = ({S}, {a}, {S → aS | ε}, S)
```

Lendo peça por peça:
- Não terminal: `{S}`
- Terminal: `{a}`
- Produções: `S → aS | ε`
- Símbolo inicial: `S`

---

## 8. Regras de produção

A regra `S → aS | ε` na verdade são **duas** opções, separadas pelo `|`:

```
S → aS      (troca S por  a  seguido de S)
S → ε       (troca S por nada / encerra)
```

O símbolo `|` significa **OU**. Então: **"S pode virar `aS` ou `ε`"**.

---

## 9. Como ler o `→`

Como já anotei lá em cima, o `→` depende do contexto:

- **Em gramática** → "produz", "gera", "deriva em".
  `S → aS` = "S produz aS".
- **Em lógica** → "implica", "se... então".
  `p → q` = "se p, então q".

---

## 10. Derivação de palavras

Derivar = aplicar as regras, começando **sempre** pelo símbolo inicial `S`,
até sobrar só terminais.

**Gerando `ε`:**
```
S → ε
```

**Gerando `a`:**
```
S → aS → aε → a
```

**Gerando `aa`:**
```
S → aS → aaS → aaε → aa
```

**Gerando `aaa`:**
```
S → aS → aaS → aaaS → aaaε → aaa
```

🧠 Reparei no padrão: cada `S → aS` acrescenta um `a`, e o `S → ε` é o que
"fecha" a palavra.

---

## 11. Linguagem gerada

Juntando todas as derivações possíveis, essa gramática gera:

```
L(G) = {ε, a, aa, aaa, aaaa, ...}
```

Que também dá pra escrever de forma compacta:

```
L(G) = {aⁿ | n ≥ 0}
```

Ou seja: **qualquer quantidade de `a`, incluindo zero** (o caso de zero `a`
é justamente o `ε`).

---

## 12. Atividades práticas

Resolvi as duas em arquivos separados:

- ✅ [Atividade 1 — Prefixos e Sufixos](atividades/atividade-01-prefixos-e-sufixos.md)
- ✅ [Atividade 2 — Gramática](atividades/atividade-02-gramatica.md)

---

## 13. Resumo para a prova

| Conceito | Resumo rápido |
|:--|:--|
| **Alfabeto `Σ`** | Conjunto finito de símbolos. Ex.: `Σ = {a, b}`. |
| **Cadeia** | Sequência de símbolos do alfabeto. Ex.: `ab`. |
| **Palavra vazia `ε`** | Cadeia sem símbolos. `|ε| = 0`. |
| **`Σ*`** | Todas as cadeias finitas sobre `Σ`, incluindo `ε`. |
| **Linguagem `L`** | Conjunto de cadeias: `L ⊆ Σ*`. |
| **Prefixo** | Começa no início. Para `ab`: `{ε, a, ab}`. |
| **Sufixo** | Termina no final. Para `ab`: `{ε, b, ab}`. |
| **Gramática** | Regras para gerar palavras. Ex.: `S → aS | ε`. |
| **`→`** | Gramática: produz/gera. Lógica: implica / se... então. |
| **`|`** | Nas produções significa **OU**. `S → aS | ε`. |

---

## 14. 🧠 Mapa mental

```
                    LINGUAGENS FORMAIS
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
      ALFABETO           CADEIA          LINGUAGEM
          │                │                │
          │                │                └── L ⊆ Σ*
          │                │
          │                └── ε = cadeia vazia
          │
          └── Σ
               │
               └── Σ* = todas as cadeias
                           │
                           ▼
                       GRAMÁTICA
                           │
                           ▼
                    Regras de produção
                           │
                           ▼
                      S → aS | ε
                           │
                           ▼
                ε, a, aa, aaa, ...
```

---

## 📌 Checklist da Aula 1

Consigo explicar cada um destes?

- [ ] O que é um alfabeto `Σ`;
- [ ] O que é uma cadeia;
- [ ] O que significa `ε`;
- [ ] Por que `|ε| = 0`;
- [ ] O que é um prefixo;
- [ ] O que é um sufixo;
- [ ] O que significa `Σ*`;
- [ ] Se `Σ*` possui limite de tamanho;
- [ ] O que é uma linguagem formal `L`;
- [ ] O que significa `L ⊆ Σ*`;
- [ ] O que é uma gramática formal;
- [ ] O que são terminais e não terminais;
- [ ] O que é uma regra de produção;
- [ ] Como ler `S → aS | ε`;
- [ ] Como gerar palavras usando uma gramática.

---

## 🚀 Conceito-chave (pra não esquecer)

O **alfabeto** dá os símbolos → as **cadeias** são formadas com esses símbolos
→ `Σ*` junta todas as cadeias possíveis → a **linguagem** escolhe algumas
dessas cadeias → a **gramática** define as regras que geram as cadeias da
linguagem.

---

[⬅️ Voltar ao início](README.md)
