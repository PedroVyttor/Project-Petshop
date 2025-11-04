#Projeto Petshop: PETSNOOPY MV (referência ao cachorro Snoopy)
#Algoritmos e Logica de Programação
#Dupla: Pedro Vyttor, Marcus Vinicius (periodo 1)
#Linguagem: Python

usuarios = [['fulano','fulano@gmail.com','12345']]
produtos = [['Petiscos de carne', 48, 15],['Bola de corda', 29, 12],['Escova de Pelo', 50, 22],['Casaco Pet Snoopy G', 16, 39],['Guia para Passeio', 61, 20]]
servicos = [['Tosa', 50],['Banho', 30],['Exame', 70]]
datas_servicos = []

logado = False
usuario_atual = ''
carrinho = []

while True:
    print('\n===== MENU PRINCIPAL =====')
    print('1 - Cadastro')
    print('2 - Login')
    print('0 - Sair\n')

    menu = input('Escolha uma opcao: ')

#----------------------------------------------------------------------------------------------------------------------#
    if menu == 'admin':
        email = input('Email do admin: ')
        senha = input('Senha: ')

        if email == 'admin@gmail.com' and senha == 'admin':
            while True:
                print('\n--- ADMINISTRADOR ---')
                print('1 - Usuarios')
                print('2 - Produtos')
                print('3 - Servicos')
                print('0 - Sair')

                adm = input('Opcao: ')

                if adm == '1':
                    print('\n1 - Adicionar Usuario')
                    print('2 - Remover Usuario')
                    print('3 - Listar Usuarios')
                    print('0 - Voltar')
                    op = input('Opcao: ')

                    if op == '1':
                        nome = input('Nome: ')
                        email = input('Email: ')
                        senha = input('Senha: ')
                        usuarios.append([nome, email, senha])
                        print('Usuario adicionado!')

                    elif op == '2':
                        email = input('Email do usuario: ')
                        for u in usuarios:
                            if email == u[1]:
                                usuarios.remove(u)
                                print('Usuario removido!')
                                break

                    elif op == '3':
                        print('\n--- USUARIOS CADASTRADOS ---')
                        if len(usuarios) == 0:
                            print('Nenhum usuario cadastrado.')
                        else:
                            for u in usuarios:
                                print(u[0], '-', u[1])

                elif adm == '2':
                    print('\n1 - Adicionar Produto')
                    print('2 - Remover Produto')
                    print('3 - Atualizar Estoque/Preco')
                    print('0 - Voltar')
                    op = input('Opcao: ')

                    if op == '1':
                        nome = input('Nome do produto: ')
                        qtd = int(input('Estoque: '))
                        preco = float(input('Preco: '))
                        produtos.append([nome, qtd, preco])
                        print('Produto adicionado!')

                    elif op == '2':
                        nome = input('Nome do produto: ')
                        for p in produtos:
                            if nome == p[0]:
                                produtos.remove(p)
                                print('Produto removido!')
                                break
                        else:
                            print('Produto nao encontrado.')

                    elif op == '3':
                        print('\n--- PRODUTOS CADASTRADOS ---')
                        for i in range(len(produtos)):
                            print(i+1, '-', produtos[i][0], '| Estoque:', produtos[i][1], '| Preco: R$', produtos[i][2])
                        n = int(input('Numero do produto: '))
                        if n >= 1 and n <= len(produtos):
                            produtos[n-1][1] = int(input('Novo estoque: '))
                            produtos[n-1][2] = float(input('Novo preco: '))
                            print('Produto atualizado!')
                        else:
                            print('Numero invalido.')

                elif adm == '3':
                    print('\n1 - Adicionar Servico')
                    print('2 - Remover Servico')
                    print('3 - Datas')
                    print('0 - Voltar')
                    op = input('Opcao: ')

                    if op == '1':
                        nome = input('Nome: ')
                        preco = float(input('Preco: '))
                        servicos.append([nome, preco])
                        print('Servico adicionado!')

                    elif op == '2':
                        nome = input('Nome do servico: ')
                        for s in servicos:
                            if nome == s[0]:
                                servicos.remove(s)
                                print('Servico removido!')
                                break
                        else:
                            print('Servico nao encontrado.')

                    elif op == '3':
                        print('Datas:', datas_servicos)
                        print('1 - Adicionar Data')
                        print('2 - Remover Data')
                        d = input('Opcao: ')
                        if d == '1':
                            datas_servicos.append(input('Nova: '))
                        elif d == '2':
                            rem = input('Remover: ')
                            if rem in datas_servicos:
                                datas_servicos.remove(rem)
                                print('Removida!')
                            else:
                                print('Nao encontrada')

                elif adm == '0':
                    break
        else:
            print('Acesso negado!')
        continue
#----------------------------------------------------------------------------------------------------------------------#

    if menu == '0':
        print('Encerrando sistema...')
        break

    elif menu == '1':
        print('\n--- CADASTRO DE USUARIP ---')
        nome = input('Nome: ')
        email = input('Email: ')
        senha = input('Senha: ')

        if '@' not in email or 'gmail' not in email or '.com' not in email:
            print('Email invalido.')
        elif len(senha) < 4:
            print('Senha muito curta.')
        else:
            usuarios.append([nome, email, senha])
            print('Usuario cadastrado!')

    elif menu == '2':
        print('\n--- LOGIN ---')
        nome_login = input('Nome: ')
        senha_login = input('Senha: ')

        for u in usuarios:
            if nome_login == u[0] and senha_login == u[2]:
                logado = True
                usuario_atual = u[0]
                print('\nBem vindo ao PETSNOOPY MV!')
                break
        else:
            print('Usuario nao encontrado.')
            continue

        while logado:
            print('\n--- PETSNOOPY MV ---')
            print('1 - Buscar Produtos')
            print('2 - Agendar Servicos')
            print('3 - Carrinho (produtos e serviços)')
            print('0 - Sair')
            opc = input('Escolha: ')

            if opc == '0':
                print('Saindo da conta...')
                logado = False
                carrinho = []

            elif opc == '1':
                print('\n--- PRODUTOS DISPONIVEIS ---')
                for i in range(len(produtos)):
                    print(i+1, '-', produtos[i][0], 'x', produtos[i][1], 'R$', produtos[i][2])
                print('0 - Voltar')
                escolha = input('Numero do produto: ')
                if escolha == '0':
                    continue
                n = int(escolha)
                if n >= 1 and n <= len(produtos):
                    qtd = int(input('Quantidade: '))
                    if qtd <= produtos[n-1][1] and qtd > 0:
                        total = qtd * produtos[n-1][2]
                        print('Total: R$', total)
                        c = input('Confirmar (s/n): ')
                        if c == 's' or c == 'sim' or c == 'si' or c == 'yes' or c == 'y':
                            produtos[n-1][1] -= qtd
                            carrinho.append([qtd, produtos[n-1][0], total])
                            print('Adicionado ao carrinho!')
                    else:
                        print('Quantidade invalida.')
                else:
                    print('Produto inexistente.')

            elif opc == '2':
                print('\n--- SERVICOS DISPONIVEIS ---')
                for i in range(len(servicos)):
                    print(i+1, '-', servicos[i][0], 'R$', servicos[i][1])
                print('0 - Voltar')
                escolha = input('Numero do servico: ')
                if escolha == '0':
                    continue
                n = int(escolha)
                if n >= 1 and n <= len(servicos):
                    nome_servico = servicos[n-1][0]
                    preco_servico = servicos[n-1][1]
                    carrinho.append([1, '\nServico: ' + nome_servico, preco_servico])
                    print('Servico agendado:', nome_servico)
                else:
                    print('Numero invalido.')

            elif opc == '3':
                print('\n--- CARRINHO ---')
                if len(carrinho) == 0:
                    print('Carrinho vazio.')
                else:
                    total = 0
                    for item in carrinho:
                        print('-', item[0], 'x', item[1], 'R$', item[2])
                        total += item[2]
                    print('Total geral: R$', total)
                    p = input('Pagar agora? (s/n): ')
                    if p == 's':
                        carrinho = []
                        logado = False
                        print('Pagamento realizado. Obrigado!')
    else:
        print('Opcao invalida.')
