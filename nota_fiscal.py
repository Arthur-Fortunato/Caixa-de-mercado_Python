from datetime import datetime
from tabulate import tabulate

def gerar_nota_fiscal(carrinho_compras, cliente, total_compra):
    tabela = []
    for i, item in enumerate(carrinho_compras, start=1):
        tabela.append([i, item[1], item[2], item[3], item[4]])
    print("\n----- NOTA FISCAL -----")
    print(f"Cliente {cliente}")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(tabulate(tabela, headers=["Item", "Produto", "Quantidade", "Preço Unitário", "Total"], tablefmt="github"))
    print(f"\nItens: {len(carrinho_compras)}")
    print(f"Total: R${total_compra}")
    print("------------------------")