numero = int(input("Digite um número para calcular o fatorial: "))


if numero >= 0 and type(numero) == int:
    fatorial = 1
    if numero == 0:
        fatorial = 1
    else:
        while numero > 1:
            print(f'Calculando: {fatorial} * {numero}')
            fatorial *= numero
            print(f'Intermediário: {fatorial}')
            numero -= 1
    print("O fatorial é:", fatorial)
else:
    if numero < 0:
        print("Fatorial não é definido para números negativos.")
    elif type(numero) != int:
        print("Por favor, insira um número inteiro válido.")