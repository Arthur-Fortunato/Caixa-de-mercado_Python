from processar_arquivo import *
from util import *
from nota_fiscal import *
from datetime import datetime 

def iniciar_atendimento(produtos, cliente, total_clientes):
    carrinho_compras = []
    while True:
        produto = escolher_produto(produtos)
        quantidade = quantidade_produto_escolhido(produto)
        baixa_estoque(produto, quantidade)
        carrinho_compras.append([produto[0], produto[1], quantidade, produto[3], quantidade * produto[3]])
        continuar_compra = input("Quer comprar mais produtos? ([S]im ou digite qualquer outra letra para gerar a nota fiscal da compra): ").upper()
        if (continuar_compra != 'S'):
            break
    total_compra = sum(item[4] for item in carrinho_compras) 
    total_clientes.append([cliente, total_compra])
    gerar_nota_fiscal(carrinho_compras, cliente, total_compra)

def fechar_caixa(total_clientes, produtos):
    print("\n----- FECHAMENTO DO CAIXA -----")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    total_vendas = 0
    for cliente, total in total_clientes:
        total_vendas += total
    print(tabulate(total_clientes, headers=["Cliente", "Total de Compra"], tablefmt="github"))
    print(f"\nTotal de vendas realizadas: R${total_vendas}")
    listar_produtos_sem_estoque(produtos) 
    print("------------------------")