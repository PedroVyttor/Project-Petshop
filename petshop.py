#       ---- Projeto Petshop ----
#   Algoritmos e Lógica de Programação
#   Dupla: Pedro Vyttor, Marcus Vinicius (Periodo 1)
#   Linguagem: Python




#Descrição da estrutura:
##---------MENU (USUARIO)-----------

# 1 - Cadastro (Usuário)
# 2 - Login (Usuário)
# 0 - Sair


# -------------------------------
# 1 - CADASTRO (USUÁRIO)
# -------------------------------
# 1 - Nome do usuário:
# 2 - Email:
#       - deve conter (@), (gmail) e (.com)
#       - não pode ser igual a um email já cadastrado
# 3 - Senha:
#       - não pode ter menos de 4 dígitos
# 4 - Todas as entradas devem ser tratadas com ".lower()"
# --------------------------------


# -------------------------------
# 2 - LOGIN (USUÁRIO)
# -------------------------------
# 1 - Inserir nome de usuário:
# 2 - Inserir senha:
# 3 - Verificação do usuário:
#       - Deve corresponder a um usuário existente da lista
# --------------------------------


# -------------------------------
# --- TELA INICIAL (USUÁRIO) ---
# -------------------------------
# 1 - Buscar Produtos
# 2 - Agendar Serviços
# 0 - Sair
# --------------------------------


# 1 - BUSCAR PRODUTOS
# --------------------------------
# Exibir lista de produtos disponíveis:
#       1 - Caldo de cana                      x1   R$10,00
#       2 - Bola de futebol americano          x9   R$0,05
#       3 - Alicate de unha                    x384   R$156,00
#
# Selecionar produto: [número]
#       0 - Voltar
#
# Após selecionar:
#       - Digitar a quantidade desejada
#       - Confirmar compra: [Sim / Não]
#             -> Se "Sim": produto adicionado à lista
#             -> Se "Não": volta para seleção de produto
#
# Exemplo após compra:
#       1 - Caldo de cana                      x0   R$10,00
#       2 - Bola de futebol americano          x9   R$0,05
#       3 - Alicate de unha                    x384   R$156,00
#
# Criar lista personalizada:
#       - while:
#             -> "Qual item deseja adicionar à lista:" (ex: 1 32 3 7 68)
#             -> "Deseja adicionar outro item?" (sim/não)
#             -> "Finalizar lista" (encerra loop)
# --------------------------------


# 2 - AGENDAR SERVIÇOS
# --------------------------------
# (Acessível após login)
# 1 - Tosa       (explicar o serviço)
# 2 - Banho      (explicar o serviço)
# 3 - Exame      (explicar o processo)
# 4 - Adoção     (explicar o processo)
# --------------------------------


# 3 - COMPRAR PRODUTOS (dentro do menu logado)
# --------------------------------
# ----------- PRODUTOS DISPONÍVEIS ------------
# 1 - BLA BLA BLA
# 2 - Chevrolet Corsa
# 3 - Toyota Hilux
#
# Selecionar produto(s): [ex: 2 3]
#       - Aceitar apenas números
#       - Se houver símbolos (: ; , .), desconsiderar
#
# Confirmar compra? [Sim / Não]
#       -> Se "Sim":
#             - Exibir lista dos produtos selecionados
#             - Mostrar preço individual e valor total
#       -> Se "Não":
#             - Voltar à lista de produtos
#
# Caso entrada inválida (ex: 1223, aslsajdas, etc):
#       -> Exibir: "Comando desconhecido"
# --------------------------------


# 4 - DEVOLUÇÃO (Opcional)
# --------------------------------
# O usuario pode solicitar devolução
# O administrador é responsável por resolver
# --------------------------------







# #---------Menu (ADMINISTRATIVO)-----------
# 1 - Cadastro (admin)
# 2 - Login (admin)
# 0 - Sair

#CADASTRO
# 1 - nome:
# 2 - email:
# 3 - senha:
# 4 - "key": 4 digitos

#LOGIN
# 1 - email:
# 2 - senha:
# 3 - "key": 4 digitos
#
#           ---Tela inicial (Admin)---
            #1 - Gerenciar admins
            #2 - gerenciar usuarios
            #3 - controle de produtos
            #4 - servicos
            #0 - sair
                #1 - Gerenciar Administradores
                        #- cadastrar admin (nome, email, senha, chave de 4 digitos)
                        #- listar administradores
                        #- excluir administradores


                #2 - Gerenciar Usuários
                        #- Listar todos os usuarios cadastrados
                        #- Cadastrar usuario (adm ou cliente)
                        #- buscar usuario por nome ou email
                        #- bloquear usuario
                        #- visualizar historico de compras do usuario (opcional)

                #3 - Controle de Produtos
                        #- Adicinoar produto (nome, descrição, quantidade, valor)
                        #- Editar produto (alterar nome, preço ou estoque)
                        #- Remover produto
                        #- Listar todos os produtos (mostrar em lista, nome, quantidade e preço)
                        #- Buscar produto (por nome, preço sla)

                #4 - Serviços
                        #- Cadastrar serviço (nome, descriçao e preco)
                        #- Editar serviço
                        #- excluir servico
                        #- listar todos os servicos
                        #- visualizar agendamentos de servicos (cliente, data, tipo de servico sla)

                #0 - Sair

