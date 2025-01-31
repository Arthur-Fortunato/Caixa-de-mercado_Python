from util import *

def exibir_menu():
    print("-----MENU-----")
    print("[1] - Iniciar atendimento")
    print("[2] - Fechar caixa")

def entrar_opcao():
    while True:
        exibir_menu()
        opcao = entrar_inteiro("Entre com a opção: ")
        if((opcao < 1) or (opcao > 2)):
            print("Erro: opção inválida")
        else:
            break
    return opcao