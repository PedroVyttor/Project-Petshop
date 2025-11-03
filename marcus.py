#   Projeto Petshop: PETSNOOPY MV (PET...SNOOPY - (Referência ao cachorro Snoopy))
#   Algoritmos e Logica de Programação
#   Dupla: Pedro Vyttor, Marcus Vinicius (Periodo 1)
#   Linguagem: Python

usuarios = []
produtos = [['Caldo de cana', 78, 10], ['Bola de futebol americano', 16, 20], ['Alicate de unha', 384, 15], ['PS5 Dogs Edition', 4, 14374], ['Racao pra Cachorro', 150, 34]]

logado = False
usuario_atual = ''
carrinho = []

while True:
    print('\n ===== MENU PRINCIPAL =====')
    print('1 - Cadastro (Usuario)')
    print('2 - Login (Usuario)')
    print('0 - Sair\n ')

    menu = input('Escolha uma opcao: ')


    if menu == 'admin':
        while True:
         print('\n ===== MENU ADMINISTRATIVO =====')
         print('1 - remover usuarios: ')
         print('2 - gerenciar produtos: ')
         print('3 - gerenciar servicos: ')
         print('0 - Sair\n ')

         menu_admin = input('Escolha uma opcao: ')


         if menu_admin == '1':
            print('1 - remover usuarios')
            print('2 - adicionar usuarios')
            print('0 - Sair\n ')

            selecao = input('Escolha uma opcao: ')

            if selecao == '1':
                login = input('Usuario a ser removido: ')
                if login not in usuarios:
                    print('usuario nao encontrado')
                else:
                    usuarios.pop(login)

            elif selecao == '2':
                add = input('adicionar usuario: ')
                usuarios.extend(add)

            elif selecao == '0':
                print('encerrando operações')

            else:
                print('Comando desconhecido.')

         if menu_admin == '2':
             print('1 - remover produtos')
             print('2 - adicionar produtos: ')
             print('3 - ajustar preços')
             print('0 - Sair\n ')

             selecao = input('Escolha uma opcao: ')

             if selecao == '1':
                remover = input('escolha um produto para remover: ')

                if remover == produtos[i]:
                    print('produto removido')

                else:
                    print('produto nao encontrado')
                    produtos.pop(remover)

                if remover in produtos:
                    produtos.remove(remover)

             if selecao == '2':
                adicionar = input('adicionar produto: ')
                local = int(input('local a ser adicionado: '))
                produtos.insert(local, adicionar)

             if selecao == '3':
                 ajuste = input('ajuste no preço produto: ')
         else:
             print('Comando desconhecido.')

         if menu_admin == '3':
             print('1 - mudar horarios de agendamento')
             print('2 - mudar preços de serviços')
             print('3 - adicionar ou remover serviços')
             print('0 - Sair\n ')


    if menu == '0':
        print('Encerrando sistema... Ate breve.')
        break

    elif menu == '1':
        print('\n--- CADASTRO DE USUARIO ---')

        nome = input('Nome do usuario: ')
        email = input('Email: ')
        senha = input('Senha (minimo 4 digitos): ')

        if '@' not in email or 'gmail' not in email or '.com' not in email:
            print('Email invalido. Deve conter @gmail.com corretamente.')
        elif len(senha) < 4:
            print('A senha nao pode ter menos de 4 digitos')
            while len(senha) < 4:
                print('A senha nao pode ter menos de 4 digitos')
                senha = input('digite a senha novamente: ')
        else:
            existe = False
            for u in usuarios:
                if email == u[1]:
                    existe = True
            if existe:
                print('Este email ja esta cadastrado.')
            else:
                usuarios.append([nome, email, senha])
                print('Usuario cadastrado com sucesso!')

    elif menu == '2':
        print('\n--- LOGIN ---')

        if len(usuarios) == 0:
            print('Nenhum usuario registrado.')
            continue

        nome_login = input('Nome do usuario: ')
        senha_login = input('Senha: ')

        achou = False
        for u in usuarios:
            if nome_login == u[0] and senha_login == u[2]:
                achou = True
                usuario_atual = u[0]
                logado = True
                print('\nBem vindo ao PETSNOOPY MV.')

        if not achou:
            print('Usuario nao encontrado ou senha errada.')
            continue

        while logado:
            print('\n --- PETSNOOPY MV ---')
            print('1 - Buscar Produtos')
            print('2 - Agendar Servicos')
            print('3 - Carrinho de Compras e Servicos Agendados')
            print('0 - Sair')
            opc = input('Escolha: ')

            if opc == '0':
                print('Saindo da conta...')
                logado = False
                carrinho = []

            elif opc == '1':
                print('\n--- PRODUTOS DISPONIVEIS ---')
                for i in range(len(produtos)):
                    print((i+1), '-', produtos[i][0], 'x', produtos[i][1], 'R$', produtos[i][2])

                print('0 - Voltar')
                escolha = input('Selecione o numero do produto: ')

                if escolha == '0':
                    continue

                escolha_num = 0
                valido = True
                for dig in escolha:
                    if dig < '0' or dig > '9':
                        valido = False
                if valido:
                    escolha_num = int(escolha)

                if escolha_num >= 1 and escolha_num <= len(produtos):
                    qtd = int(input('Quantidade desejada: '))
                    if qtd <= produtos[escolha_num - 1][1] and qtd > 0:
                        total = qtd * produtos[escolha_num - 1][2]
                        print('Total: R$', total)
                        confirmar = input('Confirmar compra? (s/n): ').lower()

                        if confirmar == 's':
                            produtos[escolha_num - 1][1] -= qtd
                            carrinho.append([qtd, produtos[escolha_num - 1][0], total])
                            print('Adicionado ao carrinho.')
                        else:
                            print('Compra cancelada.')
                    else:
                        print('Quantidade invalida.')
                else:
                    print('Produto inexistente.')

            elif opc == '2':
                print('\n--- SERVICOS DISPONIVEIS ---')
                print('1 - Tosa     (Corte e cuidado com o pelo do pet)')
                print('2 - Banho    (Limpeza completa do pet)')
                print('3 - Exame    (Avaliacao veterinaria. Detecta possiveis doenças e fazer analises se necessario.)')
                print('4 - Adoçao   (Processo de adocao responsavel)')
                print('0 - Voltar')

                servico = input('Escolha o servico: ')

                if servico == '1':
                    print('Servico agendado: Tosa')
                    carrinho.append([1, 'Servico: Tosa', 50])
                elif servico == '2':
                    print('Servico agendado: Banho')
                    carrinho.append([1, 'Servico: Banho', 30])
                elif servico == '3':
                    print('Servico agendado: Exame')
                    carrinho.append([1, 'Servico: Exame', 70])
                elif servico == '4':
                    print('Processo de adocao iniciado')
                    carrinho.append([1, 'Servico: Adocao', 0])
                elif servico == '0':
                    pass
                else:
                    print('Opcao invalida.')

            elif opc == '3':
                print('\n--- CARRINHO DE COMPRAS E SERVICOS AGENDADOS ---')
                if len(carrinho) == 0:
                    print('Carrinho vazio.')
                else:
                    soma_total = 0
                    for item in carrinho:
                        qtd = item[0]
                        nome_item = item[1]
                        preco_item = item[2]
                        soma_total += preco_item
                        print('-', qtd, 'x', nome_item, 'R$', preco_item)

                    print('\nTotal geral: R$', soma_total)
                    pagar = input('Deseja pagar agora? (s/n): ').lower()

                    if pagar == 's':
                        logado = False
                        carrinho = []
                        print('\nPagamento realizado. Obrigado!')

            else:
                print('Comando desconhecido.')

    else:
        print('Opcao invalida. Tente novamente.')
