salario = float(input('Digite o salário fixo do funcionário: '))
horas_trabalhadas = int(input('Digite o número de horas trabalhadas no mês: '))
valor_hora = salario / horas_trabalhadas
print(f'O valor da hora trabalhada é: R$ {valor_hora:.2f}')