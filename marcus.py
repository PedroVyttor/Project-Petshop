conta = [['marcus','1234'],['vyttor','2121'],['thiago','2112']]
email = [['calanggjogos@gmail.com'],['muitolegal@gmail.com'],['euamominhaex@email.com']]

print('----SELECIONE UMA DAS OPÇÕES DE LOGIN----')
print('[1] LOGIN')
print('[2] CADASTRO')
print('[3] SAIR')
op = int(input('selecione uma das opções acima: '))


if op == 1:
    while nome or senha in senha:
        nome = input('coloque seu nome de usuario')
        senha = input('coloque sua senha')
        if nome in conta and senha in conta:
           print('logado com sucesso')

qtde = 0
if op == 2:
    while qtde ==0:
        nome = input('coloque seu nome de usuario')s
        senha = input('coloque sua senha')
        email = input('coloque seu email')
        conta.extend([nome,senha])
        if '@' in email:
           if 'email' or "gmail"in email:
               if ".com" in email:
                   print('sucesso ao se cadastrar')
                   qtde+=1


    else:
        print('ouve um problema com seu email, tente novamente')
