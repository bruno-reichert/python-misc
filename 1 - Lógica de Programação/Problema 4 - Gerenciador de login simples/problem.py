usuario = 'jhonathan'
senha = 'senha123'
tentativas = 0

input_usuario = input('Digite o nome de usuário: ')
input_senha = input('Digite a senha: ')

while (input_usuario != usuario or input_senha != senha) and tentativas < 3:
    print('Nome de usuário ou senha incorretos. Tente novamente.')
    input_usuario = input('Digite o nome de usuário: ')
    input_senha = input('Digite a senha: ')
    tentativas += 1

if input_usuario == usuario and input_senha == senha:
    print('Login bem-sucedido!')
else:
    print('Número máximo de tentativas excedido. Acesso bloqueado.')