import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
ARQ = str(DIR_CUR) + "\\produtos.csv"

def ler_produtos():
    produtos = []
    try:
        with (open(ARQ, "r", encoding="UTF-8") as arquivo):
            linha = arquivo.readline()
            while (linha != ""):
                linha = linha.strip("\n")
                campos = linha.split(",")
                id = int(campos[0])
                nome = campos[1]
                estoque = int(campos[2])
                preco = float(campos[3])
                produto = [id, nome, estoque, preco]
                produtos.append(produto)
                linha = arquivo.readline()
    except:
        print("Erro: leitura do arquivo")
    return produtos

def salvar_produtos(produtos):
    try:
        with open(ARQ, "w", encoding="UTF-8") as arquivo:
            for produto in produtos:
                arquivo.write(f"{produto[0]},{produto[1]},{produto[2]},{produto[3]}\n")
    except:
        print("Erro: erro na gravação do arquivo")
