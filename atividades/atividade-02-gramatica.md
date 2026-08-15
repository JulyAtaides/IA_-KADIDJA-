# 📝 Atividade 2 — Gramática

## Enunciado

Considere:
```
G = ({S}, {a}, {S → aS | ε}, S)
```

**Pergunta:** Liste 3 palavras geradas.

---

## ✍️ Resolução

A regra é `S → aS | ε`, ou seja, cada vez que aparece `S` eu posso trocar por
`aS` (coloca um `a` e continua) **ou** por `ε` (para de gerar).

Aplicando a regra passo a passo:

- `S → ε` &nbsp;→ gera **`ε`**
- `S → aS → aε` &nbsp;→ gera **`a`**
- `S → aS → aaS → aaε` &nbsp;→ gera **`aa`**

---

## ✅ Gabarito

Uma resposta possível:
```
ε
a
aa
```

Outras possibilidades:
```
aaa
aaaa
aaaaa
...
```

> 💡 A gramática gera qualquer quantidade de `a` (inclusive nenhum, que é `ε`).

---

[⬅️ Voltar ao início](../README.md)
