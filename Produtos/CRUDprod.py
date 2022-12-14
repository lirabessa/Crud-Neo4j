#Criar


def criarProduto(db):
    query = ("CREATE (object: produto {nome: $nomeProduto, quantidade: $qtdeProduto, preço: $precoProd, vendedor: $cnpjVend})")

    nomeProduto = input("Nome: ")
    qtdeProduto = input("Quantidade: ")
    precoProd = input("Preço: ")
    print("\n---- Vendedor ----")
    cnpjVend = input("CNPJ do vendedor: ")

    result = db.run(query, nomeProduto=nomeProduto, qtdeProduto=qtdeProduto, precoProd=precoProd, cnpjVend=cnpjVend)

    print("Produto criado com sucesso!")
    return [{"object": row["object"]["nome"]["quantidade"]["preco"]["vendedor"]} for row in result]



def buscarProdutos(db):
    query = "MATCH (p:produto) RETURN p"
    result = db.run(query)
    return [print([row]) for row in result]


def buscarProduto(db):
    nomeProd = input("Insira o nome do produto que deseja encontrar: ")
    query = "MATCH (p:produto) WHERE p.nome = $nomeProd RETURN p"
    result = db.run(query, nomeProd=nomeProd)
    return [print([row]) for row in result]

#Atualizar

def atualizarProduto(db):
    nomeProd = input("Insira o nome do produto que deseja atualizar: ")

    print('''
            1 - Nome
            2 - Quantidade
            3 - Preço
            4 - CNPJ do Vendedor
        ''')
    
    option = input("Insira o número da opção que deseja atualizar: ")

    while int(option) < 1 or int(option) > 7:
        print("Opção inválida")
        option = input("Insira outra opção: ")

    if option == "1": option = "nome"
    elif option == "2": option = "quantidade"
    elif option == "3": option = "preço"
    elif option == "4": option = "cnpjVend"

    new= input("Insira o novo valor: ")

    query = ("MATCH (p:produto) WHERE p.nome = $nomeProd SET p." + option + " = $new")

    print("Produto atualizado com sucesso!")

    db.run(query, nomeProd=nomeProd, option=option, new=new)

#Deletar


def deletarProduto(db):
    nomeProd = input("Insira o nome do produto a ser deletado: ")
    query = "MATCH (p:produto) WHERE p.nome = $nomeProd DETACH DELETE p"
    print("Produto deletado com sucesso")
    db.run(query, nomeProd=nomeProd)