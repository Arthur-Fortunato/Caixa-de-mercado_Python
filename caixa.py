from processar_arquivo import *
from menu import *
from atendimento import *

produtos = ler_produtos()
total_clientes = []
cliente = 1
while True:
    opt = entrar_opcao()
    if(opt == 1):
        iniciar_atendimento(produtos, cliente, total_clientes)
        cliente += 1
    elif (opt == 2):
        fechar_caixa(total_clientes, produtos)
        salvar_produtos(produtos)
        break
    else:
        print("Erro: opção inválida")