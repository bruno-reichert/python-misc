salarios = [1500.00, 2300.50, 1800.75, 3200.00, 2750.25, 4000.00, 2900.00, 3100.50, 2200.00, 2600.75]
total_gastos = sum(salarios)
print(f"Total gasto com pagamento de salários: R$ {total_gastos:.2f}")

# método 2: usando loop
total_gastos_loop = 0
for salario in salarios:
    total_gastos_loop += salario
print(f"Total gasto com pagamento de salários (usando loop): R$ {total_gastos_loop:.2f}")