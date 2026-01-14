import random

valor_aleatorio = random.randint(1, 10)
tentativas = 1
acertou = False

while acertou == False and tentativas <= 5:
    try:
        numero_usuario = int(input("Chute um número entre 1 e 10: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue
    if numero_usuario < 1 or numero_usuario > 10:
        print("Por favor, escolha um número dentro do intervalo de 1 a 10.")
    elif numero_usuario < valor_aleatorio:
        print("Tente um número maior.")
    elif numero_usuario > valor_aleatorio:
        print("Tente um número menor.")
    else:
        acertou = True
        print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s)!")
    tentativas += 1
if not acertou:
    print(f"Suas tentativas acabaram. O número correto era {valor_aleatorio}.")