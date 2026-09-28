# Atividade 5 - Maquina de Turing que reconhece 0^n 1^n
#
# Como funciona: troco o primeiro 0 por A, corro para a direita ate
# achar o primeiro 1 e troco por B. Volto para o comeco e repito.
# Quando nao tiver mais 0, confiro se sobrou algum 1. Se nao sobrou, aceita.
#
# Pra rodar: python maquina_de_turing.py        (roda os 3 testes)
#            python maquina_de_turing.py 0011   (roda so a palavra que eu passar)

import sys

VAZIO = " "

# regras[estado][simbolo] = (escreve, anda, vai_para)
# anda: +1 = direita, -1 = esquerda
regras = {
    "inicio": {
        "0": ("A", +1, "procura_1"),
        "B": ("B", +1, "confere"),
    },
    "procura_1": {
        "0": ("0", +1, "procura_1"),
        "B": ("B", +1, "procura_1"),
        "1": ("B", -1, "volta"),
    },
    "volta": {
        "0": ("0", -1, "volta"),
        "B": ("B", -1, "volta"),
        "A": ("A", +1, "inicio"),
    },
    "confere": {
        "B": ("B", +1, "confere"),
        VAZIO: (VAZIO, +1, "aceita"),
    },
}


def rodar(palavra):
    fita = list(palavra) + [VAZIO]
    pos = 0
    estado = "inicio"
    caminho = [estado]

    print("Entrada:", palavra)
    while estado != "aceita":
        if pos >= len(fita):
            fita.append(VAZIO)
        simbolo = fita[pos]

        # desenho da fita com a cabeca marcada embaixo
        print(f"  {estado:<10} |{'|'.join(fita)}|")
        print(f"  {'':<10}  {'  ' * pos}^")

        if simbolo not in regras[estado]:
            print("  nao tem regra para", estado, "lendo", repr(simbolo))
            print("Resultado: REJEITA\n")
            return "REJEITA", caminho

        escreve, anda, estado = regras[estado][simbolo]
        fita[pos] = escreve
        pos = pos + anda
        caminho.append(estado)

    print(f"  {estado:<10} |{'|'.join(fita)}|")
    print("Resultado: ACEITA\n")
    return "ACEITA", caminho


testes = sys.argv[1:] or ["01", "00001111", "011"]

for t in testes:
    resultado, caminho = rodar(t)

    # tiro as repeticoes seguidas pra ficar mais facil de ler
    resumido = []
    for e in caminho:
        if not resumido or resumido[-1] != e:
            resumido.append(e)
    print("Estados percorridos:", " -> ".join(resumido))
    print("-" * 50)
