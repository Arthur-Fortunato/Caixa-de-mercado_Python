def escolher_produto(produtos):
    while True:
        produto_escolhido = entrar_inteiro("Escolha um produto (1 - 5): ")
        produto = consultar_produto(produtos, produto_escolhido)
        if (produto is None):
            print("Erro: produto não cadastrado. Tente novamente.")
        elif(produto[2] == 0):
            print("Erro: Estoque insuficiente.")
        else:
            return produto

def quantidade_produto_escolhido(produto):
    quantidade_disponivel = produto[2]
    quantidade_desejada = entrar_inteiro("Escolha a quantidade desejada: ") 
    while (quantidade_desejada > quantidade_disponivel) or (quantidade_desejada <= 0): 
            print(f"Erro: quantidade deve ser maior que zero e não ultrapassar o estoque")
            quantidade_desejada = entrar_inteiro("Escolha a quantidade desejada: ") 
    return quantidade_desejada

def baixa_estoque(produto, quantidade):
        if (produto[2] >= quantidade):
            produto[2] -= quantidade
            print(f"{produto[1]} atualizado: {produto[2]} unidades restantes.")
        else:
            print("Erro: Estoque insuficiente.")

def listar_produtos_sem_estoque(produtos):
    produtos_sem_estoque = []
    for produto in produtos:
        if(produto[2] == 0):
            produtos_sem_estoque.append(produto[1])
    if (produtos_sem_estoque):
        print("\n----- PRODUTOS SEM ESTOQUE -----")
        for produto in produtos_sem_estoque:
            print(produto)
    else:
        print("\nNão há produtos sem estoque.")

def entrar_inteiro(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except:
            print("Erro: valor inválido")
    return num

def consultar_produto(produtos, num_prod):
    for produto in produtos:
        if (produto[0] == num_prod):
            return produto
    return None
    