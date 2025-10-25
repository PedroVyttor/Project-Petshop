lista = []

print("---- Produtos ----\n Categorias:\n 1 - Playground / Brinquedos\n 2 - Móveis e Acessórios\n 3 - Ração (seca ou úmida)\n 4 - Tipos de Alimentos Naturais e Petiscos")
select = int(input("\nSelecione a categoria que deseja: "))

if select == 1:
    print("Playground / Brinquedos")
    print("1 - {}   |  {} unid.  |   Valor: R${}    |     Observação: {}")
    print("2 - {}   |  {} unid.  |   Valor: R${}    |     Observação: {}")
    print("0 - Voltar")
    selec = int(input("Selecione o produto: "))

    if selec == 1:
        confirm = input("Confirmar seleção? {produto selecionado}" )
        if confirm == "sim" or confirm == "si" or confirm == "s":

    if selec == 0:



if select == 2:
    print("Móveis e Acessórios")
    print("1 - {}   |  {} unid.  |   Valor: R${}    |     Observação: {}")
    print("2 - {}   |  {} unid.  |   Valor: R${}    |     Observação: {}")
    print("0 - Voltar")
    print("Selecione o produto:")

if select == 3:
    print("Ração (seca ou úmida)")
    print("1 - {}   |  {} unid.  |   Valor: R${}    |     Observação: {}")
    print("2 - {}   |  {} unid.  |   Valor: R${}    |     Observação: {}")
    print("0 - Voltar")
    print("Selecione o produto:")

if select == 4:
    print("Tipos de Alimentos Naturais e Petiscos")
    print("1 - {}   |  {} unid.  |   Valor: R${}    |     Observação: {}")
    print("2 - {}   |  {} unid.  |   Valor: R${}    |     Observação: {}")
    print("0 - Voltar")
    print("Selecione o produto:")
