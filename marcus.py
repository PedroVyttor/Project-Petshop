contas = [['marcus','1234','muitolegal@gmail.com'],['vyttor','2121','calanggjogos@gmail.com'],['thiago','2112','euamominhaex@email.com']]
qtde=0

print('----SELECIONE UMA DAS OPÇÕES DE LOGIN----')
print('[1] LOGIN')
print('[2] CADASTRO')
print('[3] SAIR')

op = int(input('selecione uma das opções acima: '))


if op == 1:
    nome = input('digite seu nome: ')
    senha = input('digite sua senha: ')
    email_user = input('digite seu email: ')
    if '@'and '.com' in email_user:
        for conta in contas:
            if nome == conta[0] and senha == conta[1] and email_user == conta[2]:
                print('login feito com sucesso!')
                break
    if nome and senha and email_user not in contas:
        while conta not in contas:
            print('nome, senha ou email incompativeis, tente novamente: ')
            nome = input('digite seu nome: ')
            senha = input('digite sua senha: ')
            email_user = input('digite seu email: ')



        else :
            print('login feito com sucesso!')






if op == 2:
    nome = input('digite seu nome: ')
    senha = input('digite sua senha: ')
    email_user = input('digite seu email: ')
    if '@'and '.com' in email_user:
        contas.extend(nome, senha, email_user)
        print('cadastro feito com sucesso!')

    else:
        nome = input('digite seu nome novamente: ')
        senha = input('digite sua senha novamente: ')
        email_user = input('digite seu email novamente: ')
        contas.extend(nome, senha, email_user)
        print('cadastro feito com sucesso!')
