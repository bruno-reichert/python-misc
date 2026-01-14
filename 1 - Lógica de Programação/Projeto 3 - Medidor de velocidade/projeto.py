vel_limite = float(input("Digite o limite de velocidade da via em km/h: "))
vel_carro = float(input("Digite a velocidade do carro em km/h: "))

if vel_carro > 0:
    if vel_carro <= vel_limite:
        print("Dentro do limite de velocidade. Boa viagem!")
    elif vel_carro <= vel_limite + 10:
        print(f"Multa leve! Você excedeu o limite de velocidade em {vel_carro - vel_limite} km/h.")
    elif vel_carro <= vel_limite + 20:
        print(f"Multa grave! Você está muito acima do limite de velocidade em {vel_carro - vel_limite} km/h.")
    else:
        print(f"Multa gravíssima! Reduza sua velocidade imediatamente. Você excedeu o limite em {vel_carro - vel_limite} km/h.")
else:
    print("Velocidade inválida. Por favor, insira uma velocidade positiva.")