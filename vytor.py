lista = []

print("---- Produtos ----")
print("Categorias:")
print("1 - Playground / Brinquedos")
print("2 - Móveis e Acessórios")
print("3 - Ração (seca ou úmida)")
print("4 - Tipos de Alimentos Naturais e Petiscos")

select = int(input("\nSelecione a categoria que deseja: "))



#Playground / Brinquedos
if select == 1:
    nome1, qtd1, valor1, obs1 = "Bola de borracha resistente", 30, 19.90, "Ideal para cães de médio porte" #ADM ALTERA ESSA PARTE
    nome2, qtd2, valor2, obs2 = "Arranhador com sisal", 10, 89.90, "Gatos adultos e filhotes" #ADM ALTERA ESSA PARTE

    print("\nPlayground / Brinquedos:")
    print(f"1 - {nome1}   |  {qtd1} unid.  |   Valor: R${valor1}    |   Obs: {obs1}")
    print(f"2 - {nome2}   |  {qtd2} unid.  |   Valor: R${valor2}    |   Obs: {obs2}")
    print("0 - Voltar")

    selec = int(input("\nSelecione o produto: "))

    if selec == 1:
        confirm = input(f"Confirmar seleção de '{nome1}'? (s/n): ").lower()
        if confirm in ["s", "sim"]:
            lista.append(nome1)
            print(f"{nome1} adicionado à lista!")
        else:
            print("Seleção cancelada.")
    elif selec == 2:
        confirm = input(f"Confirmar seleção de '{nome2}'? (s/n): ").lower()
        if confirm in ["s", "sim"]:
            lista.append(nome2)
            print(f"{nome2} adicionado à lista!")
        else:
            print("Seleção cancelada.")
    elif selec == 0:
        print("Voltando ao menu...")
    else:
        print("Opção inválida.")



#Móveis e Acessórios
elif select == 2:
    nome1, qtd1, valor1, obs1 = "Cama ortopédica", 10, 199.00, "Espuma de alta densidade" #ADM ALTERA ESSA PARTE
    nome2, qtd2, valor2, obs2 = "Bebedouro automático", 12, 129.00, "Mantém a água fresca" #ADM ALTERA ESSA PARTE

    print("\nMóveis e Acessórios:")
    print(f"1 - {nome1}   |  {qtd1} unid.  |   Valor: R${valor1}    |   Obs: {obs1}")
    print(f"2 - {nome2}   |  {qtd2} unid.  |   Valor: R${valor2}    |   Obs: {obs2}")
    print("0 - Voltar")

    selec = int(input("\nSelecione o produto: "))

    if selec == 1:
        confirm = input(f"Confirmar seleção de '{nome1}'? (s/n): ").lower()
        if confirm in ["s", "sim"]:
            lista.append(nome1)
            print(f"{nome1} adicionado à lista!")
        else:
            print("Seleção cancelada.")
    elif selec == 2:
        confirm = input(f"Confirmar seleção de '{nome2}'? (s/n): ").lower()
        if confirm in ["s", "sim"]:
            lista.append(nome2)
            print(f"{nome2} adicionado à lista!")
        else:
            print("Seleção cancelada.")
    elif selec == 0:
        print("Voltando ao menu...")
    else:
        print("Opção inválida.")



#Ração
elif select == 3:
    nome1, qtd1, valor1, obs1 = "Golden Special Cães Adultos", 15, 189.90, "Raças médias" #ADM ALTERA ESSA PARTE
    nome2, qtd2, valor2, obs2 = "Whiskas Gatos Adultos", 10, 129.00, "Gatos adultos" #ADM ALTERA ESSA PARTE

    print("\nRação (seca ou úmida):")
    print(f"1 - {nome1}   |  {qtd1}kg  |   Valor: R${valor1}    |   Recomendado: {obs1}")
    print(f"2 - {nome2}   |  {qtd2}kg  |   Valor: R${valor2}    |   Recomendado: {obs2}")
    print("0 - Voltar")

    selec = int(input("\nSelecione o produto: "))

    if selec == 1:
        confirm = input(f"Confirmar seleção de '{nome1}'? (s/n): ").lower()
        if confirm in ["s", "sim"]:
            lista.append(nome1)
            print(f"{nome1} adicionado à lista!")
        else:
            print("Seleção cancelada.")
    elif selec == 2:
        confirm = input(f"Confirmar seleção de '{nome2}'? (s/n): ").lower()
        if confirm in ["s", "sim"]:
            lista.append(nome2)
            print(f"{nome2} adicionado à lista!")
        else:
            print("Seleção cancelada.")
    elif selec == 0:
        print("Voltando ao menu...")
    else:
        print("Opção inválida.")



#Alimentos Naturais / Petiscos
elif select == 4:
    nome1, qtd1, valor1, obs1 = "Biscoito integral sabor carne", 50, 29.90, "Cães pequenos e médios" #ADM ALTERA ESSA PARTE
    nome2, qtd2, valor2, obs2 = "CatNip Snack", 40, 27.90, "Gatos adultos" #ADM ALTERA ESSA PARTE

    print("\nTipos de Alimentos Naturais e Petiscos:")
    print(f"1 - {nome1}   |  {qtd1} unid.  |   Valor: R${valor1}    |   Recomendado: {obs1}")
    print(f"2 - {nome2}   |  {qtd2} unid.  |   Valor: R${valor2}    |   Recomendado: {obs2}")
    print("0 - Voltar")

    selec = int(input("\nSelecione o produto: "))

    if selec == 1:
        confirm = input(f"Confirmar selecao de '{nome1}'? (s/n): ").lower()
        if confirm in ["s", "sim"]:
            lista.append(nome1)
            print(f"{nome1} adicionado a lista!")
        else:
            print("Seleção cancelada.")
    elif selec == 2:
        confirm = input(f"Confirmar selecao de '{nome2}'? (s/n): ").lower()
        if confirm in ["s", "sim"]:
            lista.append(nome2)
            print(f"{nome2} adicionado a lista!")
        else:
            print("Selecao cancelada.")
    elif selec == 0:
        print("Voltando ao menu...")
    else:
        print("Opcão inválida.")

else:
    print("Categoria inválida.")

print("\nLista final de produtos selecionados:", lista)
