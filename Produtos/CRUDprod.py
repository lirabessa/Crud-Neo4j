#Criar

def criarProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._criarProduto)

@staticmethod
def _criarProduto(db):
    query = ("CREATE (object: produto {nome: $nomeProd, quantidade: $quantProd, status: $statusProd, preço: $precoProd, vendedor: $cnpjVend})")

    nomeProd = input("Nome: ")
    quantProd = input("Quantidade: ")
    statusProd = input("Status: ")
    precoProd = input("Preço: ")
    print("\n---- Vendedor ----")
    cnpjVend = input("CNPJ do vendedor: ")

    result = db.run(query, nomeProd=nomeProd, quantProd=quantProd, statusProd=statusProd, precoProd=precoProd, cnpjVend=cnpjVend)

    print("Produto criado com sucesso!")
    return [{"object": row["object"]["nome"]["quantidade"]["status"]["preco"]["vendedor"]} for row in result]


#Bucar
def buscarProdutos(self):
    with self.driver.session(database="neo4j") as session:
        session.read_transaction(self._buscarProdutos)

@staticmethod
def _buscarProdutos(db):
    query = "MATCH (p:produto) RETURN p"
    result = db.run(query)
    return [print([row]) for row in result]

def buscarProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._buscarProduto)
    
@staticmethod
def _buscarProduto(db):
    nomeProd = input("Insira o nome do produto que deseja encontrar: ")
    query = "MATCH (p:produto) WHERE p.nome = $nomeProd RETURN p"
    result = db.run(query, nomeProd=nomeProd)
    return [print([row]) for row in result]

#Atualizar

def atualizarProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self.__atualizarProduto)

@staticmethod
def _atualizarProduto(db):
    nomeProd = input("Insira o nome do produto que deseja atualizar: ")

    print('''
            1 - Nome
            2 - Quantidade
            3 - Status
            4 - Preço
            5 - CNPJ do Vendedor
        ''')
    
    option = input("Insira o número da opção que deseja atualizar: ")

    while int(option) < 1 or int(option) > 7:
        print("Opção inválida")
        option = input("Insira outra opção: ")

    if option == "1": option = "nome"
    elif option == "2": option = "quantidade"
    elif option == "3": option = "status"
    elif option == "4": option = "preço"
    elif option == "5": option = "cnpjVend"

    new= input("Insira o novo valor: ")

    query = ("MATCH (p:produto) WHERE p.nome = $nomeProd SET p." + option + " = $new")

    print("Produto atualizado com sucesso!")

    db.run(query, nomeProd=nomeProd, option=option, new=new)

#Deletar

def deletarProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self._deletarProduto)

@staticmethod
def _deletarProduto(db):
    nomeProd = input("Insira o nome do produto a ser deletado: ")
    query = "MATCH (p:produto) WHERE p.nome = $nomeProd DETACH DELETE p"
    print("Produto deletado com sucesso")
    db.run(query, nomeProd=nomeProd)