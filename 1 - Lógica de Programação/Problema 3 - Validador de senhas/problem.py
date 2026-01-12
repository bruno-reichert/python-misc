senhas = ['Abc123!', 'password', 'A1b2C3d4$', 'Short1!', 'NoSpecialChar1', 'Valid$Pass123', '12345', 'ValidPass!@#', 'Too$hort1', 'LongEnoughButNoSpecial123', 'abc', 'ABC123!@#', 'aB1!']

for senha in senhas:
    if len(senha) < 6:
        print(f'Senha "{senha}" inválida: deve ter pelo menos 6 caracteres.')
    else:
        print(f'Senha "{senha}" válida.')