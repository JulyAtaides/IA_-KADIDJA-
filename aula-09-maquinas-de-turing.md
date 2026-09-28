# 📖 Aula 09 — Máquinas de Turing

> Aula remota. O material foi o vídeo **Akitando #86 — O Computador de Turing
> e Von Neumann: Por que calculadoras não são computadores?**. Essas são as
> anotações que eu fiz assistindo.

---

## 🎯 O que eu preciso saber ao terminar a aula

- O que é uma Máquina de Turing e suas partes;
- Como ela funciona passo a passo;
- O que é "Turing completo";
- O que é o problema da parada;
- Por que calculadora não é computador.

---

## 1. De onde veio

O Turing publicou a ideia em **1936**. Ele se inspirou numa **máquina de
escrever**: tem o papel, o lugar onde a próxima letra cai e poucas
configurações (maiúscula/minúscula).

Ele imaginou uma versão "turbinada": uma fita que nunca acaba e uma cabeça que
também **lê e apaga**, não só escreve.

---

## 2. As partes

| Parte | O que faz |
|:--|:--|
| **Fita** | infinita, dividida em casinhas; é a entrada, a memória e a saída |
| **Cabeça** | lê a casinha, escreve e anda 1 casa (esquerda/direita) |
| **Estados** | em qual "situação" a máquina está; são finitos |
| **Alfabeto** | os símbolos que podem ir na fita |
| **Transições** | as regras: estado + símbolo lido → escreve, anda, novo estado |

---

## 3. Funcionamento

A cada passo ela faz sempre a mesma coisa:

1. lê o símbolo;
2. procura a regra;
3. escreve;
4. anda;
5. muda de estado.

Ela **para** quando chega no estado de aceitação ou quando não tem regra pra
situação (aí rejeita).

> 💡 Exemplo do vídeo: somar 1 num número binário. A máquina vai até o fim do
> número, volta trocando 1 por 0 (o "vai um") e quando acha um 0 escreve 1.

---

## 4. Turing completo

É quando uma linguagem consegue fazer **tudo** que uma Máquina de Turing faz.

- ✅ Python, Java, C, até Brainfuck
- ❌ Regex, HTML, XML

A regex não é porque não tem memória e só anda pra frente (bem o que eu vi na
unidade 3!).

---

## 5. Problema da parada

O Turing provou que **não existe** um programa que olhe qualquer outro
programa e diga se ele vai parar ou ficar em loop infinito.

> ⚠️ Não é que ainda não descobriram. É **provado** que é impossível. Então
> existem problemas que nenhum computador resolve.

---

## 6. Calculadora x computador

| Máquina | Por que era "só calculadora" |
|:--|:--|
| Babbage | programa nos cartões, números na máquina, separados |
| Zuse (Z3) | não tinha "se... então" de verdade |
| Colossus | feito só pra quebrar uma cifra da guerra |
| ENIAC | pra mudar de tarefa tinha que trocar os cabos |

O **Von Neumann** (1945) juntou **programa e dados na mesma memória**. Aí pra
trocar de tarefa é só carregar outro programa. Isso é o computador moderno.

```
Turing       → a teoria (o que dá pra computar)
Von Neumann  → a prática (como construir)
```

---

## 7. Resumo para a prova

| Conceito | Resumo rápido |
|:--|:--|
| **Máquina de Turing** | fita + cabeça + estados + regras |
| **Para quando** | chega no aceita ou não tem regra (rejeita) |
| **Turing completo** | faz tudo que uma Máquina de Turing faz |
| **Problema da parada** | impossível saber se qualquer programa para |
| **Von Neumann** | programa e dados juntos na memória |

---

## 📌 Checklist

- [ ] Sei as 5 partes da máquina;
- [ ] Sei explicar um passo dela;
- [ ] Sei o que é Turing completo;
- [ ] Sei explicar o problema da parada;
- [ ] Sei por que o ENIAC era "calculadora".

✅ Atividade da aula: [Atividade 5 — Máquinas de Turing](atividades/atividade-05-maquina-de-turing/README.md)

---

[⬅️ Voltar ao início](README.md)
