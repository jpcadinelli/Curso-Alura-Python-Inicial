import random

def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil, (2) Médio e (3) Difícil.")
    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}.".format(rodada, total_tentativas))
        chute_str = input("Digite o número 1 e 100: ")
        print("Você digitou ", chute_str)
        chute_int = int(chute_str)

        if chute_int < 1 or chute_int > 100:
            print("Você deve digitar um número entre 1 e 100.")
            continue

        pontos -= abs(numero_secreto - chute_int)
        if numero_secreto == chute_int:
            print('Você acertou!')
            break
        elif numero_secreto < chute_int:
            print('Você errou! O seu chute foi maior que o número secreto.')
        else:
            print('Você errou! O seu chute foi menor que o número secreto.')

    print(f'Fim do Jogo! O número era {numero_secreto} e você fez {pontos} pontos.')


if __name__ == "__main__":
    jogar()
