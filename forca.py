import random

def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")

    arquivo = open("frutas.txt", "r")
    fruta = [linha.strip() for linha in arquivo]
    arquivo.close()
    palavra_secreta = fruta[random.randrange(len(fruta))].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    print(letras_acertadas)
    tentativas = 0

    while not enforcou and not acertou:
        chute = input("Qual letra?")
        chute = chute.strip().upper()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            desenha_forca(tentativas)
        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas
        print("************************************************")
        print(letras_acertadas)
        print("************************************************")

    if not acertou:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("     _______________")
        print("    /               \ ")
        print("   /                 \ ")
        print("/ /                   \ \ ")
        print("\ |   XXXX     XXXX   |/")
        print("  |   XXXX     XXXX   |")
        print("  |   XXX       XXX   |")
        print("  |                   |")
        print("  \__      XXX      __/")
        print("    |\     XXX     /|")
        print("    | |           | |")
        print("    | I I I I I I I |")
        print("    |  I I I I I I  |")
        print("    \_             _/")
        print("      \_         _/")
        print("        \_______/")
    else:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
