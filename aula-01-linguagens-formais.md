# 📖 Aula 1 — Linguagens Formais

> Minhas anotações da aula. Resumo dos conceitos + mapa mental + checklist
> para revisar antes da prova.

---

## 📌 Resumo para a prova

### 🔹 Alfabeto
`Σ` = conjunto de símbolos.

Exemplo:
```
Σ = {a, b}
```

### 🔹 Cadeia
Uma sequência de símbolos pertencentes ao alfabeto.

Exemplo:
```
ab
```

### 🔹 Palavra vazia
```
ε
```
Possui zero símbolos:
```
|ε| = 0
```

### 🔹 Σ*
Todas as cadeias finitas possíveis sobre `Σ`, **incluindo ε**.
```
Σ* = {ε, a, b, aa, ab, ba, bb, ...}
```

### 🔹 Linguagem
Um conjunto de cadeias:
```
L ⊆ Σ*
```

### 🔹 Prefixo
Começa no **início** da palavra.

Para `ab`:
```
{ε, a, ab}
```

### 🔹 Sufixo
Termina no **final** da palavra.

Para `ab`:
```
{ε, b, ab}
```

### 🔹 Gramática
Define regras para gerar palavras.

Exemplo:
```
S → aS | ε
```

### 🔹 O símbolo →
- Em **gramáticas**: produz / gera
- Em **lógica**: implica / se... então

### 🔹 O símbolo |
Nas regras de produção significa **OU**.

Exemplo:
```
S → aS | ε
```
Significa: **S produz `aS` ou `ε`**.

---

## 🧠 Mapa mental

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

## ✅ Checklist da Aula 1

Antes de avançar para a próxima aula, verificar se consigo explicar:

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

[⬅️ Voltar ao início](README.md)
