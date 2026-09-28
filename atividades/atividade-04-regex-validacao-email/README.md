# 📝 Atividade 4 — Regex para validação de e-mail

> Unidade 3 — Expressões Regulares. Essa foi a primeira atividade da matéria
> em que a gente escreveu código de verdade. Resolvi primeiro no caderno e
> depois passei pra cá.

📄 Código: [`validador_email.py`](validador_email.py)
📖 Resumo da aula: [Expressões Regulares](../../aula-expressoes-regulares.md)

---

## 📖 Resumo da aula

A aula foi sobre **expressões regulares** (regex). O que eu entendi:

- Uma regex é um **padrão** que descreve um conjunto de palavras, ou seja,
  uma **linguagem**.
- Ela não gera palavras igual a gramática. Ela **recebe** uma palavra e diz
  se **pertence ou não** à linguagem.
- Regex e gramática regular descrevem as mesmas linguagens: as do **tipo 3**
  da Hierarquia de Chomsky (a mesma que vimos na atividade 3).

```
gramática regular   →  gera as palavras, começando do S
expressão regular   →  confere se uma palavra pertence à linguagem
```

Os símbolos que eu precisei usar:

| Símbolo | O que significa |
|:--:|:--|
| `^` | começo da palavra |
| `$` | fim da palavra |
| `[...]` | um símbolo qualquer da lista |
| `+` | uma ou mais vezes o que vem antes |
| `{2,}` | duas ou mais vezes |
| `\.` | o ponto de verdade (o `.` sozinho quer dizer "qualquer símbolo") |
| `(?:...)` | agrupa sem guardar |
| `(?!...)` | "na frente **não** pode vir isso" |
| `(?<!...)` | "antes **não** pode ter vindo isso" |

---

## Enunciado

```
Escreva um programa que leia 5 endereços de e-mail e, usando expressão
regular, separe os válidos dos inválidos. Para cada e-mail inválido,
informe o motivo.
```

---

## ✍️ Resolução

Dividi o programa em **três partes**: a regex, a função que explica o erro e a
parte que lê os e-mails e mostra o resultado.

### 1. A regex

```python
padrao_email = re.compile(
    r"^(?!\.)(?!.*\.\.)(?!.*\.@)"
    r"[A-Za-z0-9._+-]+@"
    r"(?:(?!-)[A-Za-z0-9-]+(?<!-)\.)+"
    r"[A-Za-z]{2,}$"
)
```

Escrevi em 4 linhas porque em uma só eu me perdia. O Python junta as strings
sozinho. Cada linha cuida de um pedaço do e-mail:

**Linha 1: o que é proibido no e-mail inteiro**

- `(?!\.)` → não pode começar com ponto (`.ana@x.com`)
- `(?!.*\.\.)` → não pode ter dois pontos seguidos (`an..a@x.com`)
- `(?!.*\.@)` → não pode ter ponto grudado no @ (`ana.@x.com`)

Essas partes não "comem" nenhuma letra, elas só olham e barram.

**Linha 2: o usuário (antes do @)**

- `[A-Za-z0-9._+-]+@` → letras, números, ponto, `_`, `+` ou `-`, **pelo menos
  um**, e depois o `@`.
- Por causa do `+`, se não tiver nada antes do @ (`@gmail.com`) já não passa.
- Deixei o `-` no final da lista porque no meio ele vira intervalo, igual `A-Z`.

**Linha 3: o domínio**

- `[A-Za-z0-9-]+\.` → um pedaço do domínio e um ponto, tipo `gmail.`
- `(?!-)` e `(?<!-)` → o pedaço não pode começar nem terminar com hífen
- o `+` no fim do grupo deixa repetir, então `udf.edu.` também funciona

Como o grupo precisa aparecer **pelo menos uma vez**, o domínio precisa de
pelo menos um ponto. É isso que faz o `ana@dominio` ser reprovado.

**Linha 4: a extensão**

- `[A-Za-z]{2,}$` → só letras, no mínimo duas, e aí termina.
- `com`, `br` passam. `c` ou `c0m` não passam.

### 2. A função `motivo_invalido`

A regex só responde **sim ou não**. Mas o enunciado pede o **motivo**, então
fiz uma função que confere o e-mail aos pouquinhos, com vários `if`, e
devolve a frase do primeiro erro que encontrar.

A ordem dos `if` importa:

1. Primeiro vejo se tem espaço e se tem `@`.
2. Depois se tem **mais de um** `@`. Tem que ser antes do `split("@")`,
   senão o `usuario, dominio = ...` dá erro quando tem 3 pedaços.
3. Depois confiro o usuário: vazio, começa com ponto, termina com ponto.
4. Depois o domínio: vazio, sem ponto, hífen na ponta.
5. Por último a extensão.

O último `return` ("não corresponde ao padrão de email") é pra garantir que
sempre tenha uma resposta, mesmo que eu não tenha pensado em algum erro.

### 3. Lendo os 5 e-mails

```python
for i in range(5):
    email = input(f"Digite o {i + 1}º endereço de email: ")

    if padrao_email.fullmatch(email):
        validos.append(email)
    else:
        invalidos.append((email, motivo_invalido(email)))
```

- Uso duas listas: `validos` e `invalidos`.
- No `invalidos` eu guardo **o e-mail junto com o motivo**, em um par
  `(email, motivo)`, pra depois mostrar os dois.
- O `fullmatch` confere a palavra **inteira**. Se eu usasse só `search`, ele
  aceitaria um pedaço e um e-mail com lixo no final poderia passar.

---

## ✅ Gabarito

**Entrada** (os e-mails que a professora passou):

```
maria@gmail.com
joao.silva@udf.edu.br
pedro.gmail.com
ana@dominio
estudante_01@faculdade.com
```

**Saída:**

```
Emails válidos:
maria@gmail.com
joao.silva@udf.edu.br
estudante_01@faculdade.com

Emails inválidos:
pedro.gmail.com - não possui @
ana@dominio - não possui extensão
```

Por que cada um deu esse resultado:

| E-mail | Resultado | Por quê |
|:--|:--:|:--|
| `maria@gmail.com` | ✅ | tem usuário, @, domínio com ponto e extensão `com` |
| `joao.silva@udf.edu.br` | ✅ | ponto no meio do usuário pode; o domínio repetiu (`udf.` e `edu.`) |
| `pedro.gmail.com` | ❌ | não tem `@` |
| `ana@dominio` | ❌ | o domínio não tem ponto, então não tem extensão |
| `estudante_01@faculdade.com` | ✅ | `_` e número estão liberados no usuário |

> 💡 Rodei o programa com esses 5 e-mails e a saída bateu com o que eu tinha
> feito no caderno: **3 válidos e 2 inválidos**.

---

## ⚠️ Cuidados que anotei

- O `.` sozinho na regex é **qualquer símbolo**. Pra ponto de verdade é `\.`
- Sem o `^` e o `$` a regex aceita só um pedaço da palavra.
- No `print` é `\n` (barra invertida) pra pular linha, e não `/n`.

---

[⬅️ Voltar ao início](../../README.md)
