primeiro_valor = float(input("Digite o primeiro valor: "))
segundo_valor = float(input("Digite o segundo valor: "))

if primeiro_valor > segundo_valor:
    print("O maior valor é o primeiro valor, que é:", primeiro_valor)
elif segundo_valor > primeiro_valor:
    print("O maior valor é o segundo valor, que é:", segundo_valor)
else:
    print("Os valores são iguais.")