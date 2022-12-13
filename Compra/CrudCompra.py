#Criar

def criarCompra(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._criarCompra)

@staticmethod
def _criarCompra(db):
    query = ("CREATE (object: compra {id: $idComp, status: $statusComp, formaPagamento: $formaPagamentoComp, precoTotal: $precoTotal, produto: $nomeProd, quantidade: $quantComp, vendedor: $cnpjVend, usuario: $cpfUsu})")

    idComp = input("ID da compra: ")
    statusComp = input("Status da compra: ")
    formaPagamentoComp = input("Forma de pagamento: ")
    precoTotal = input("Preço total: ")
    print("\n---- Produto ----")
    nomeProd = input("Nome do produto: ")
    quantComp = input("Quantidade: ")
    print("\n---- Vendedor ----")
    cnpjVend = input("CNPJ do vendedor: ")
    print("\n---- Usuário ----")
    cpfUsu = input("CPF do usuário: ")

    result = db.run(query, idComp=idComp, statusComp=statusComp, formaPagamentoComp=formaPagamentoComp, precoTotal=precoTotal, nomeProd=nomeProd, quantComp=quantComp, cnpjVend=cnpjVend, cpfUsu=cpfUsu)

    print("Compra criada com sucesso!")
    return [{"object": row["object"]["id"]["status"]["formaPagamento"]["precoTotal"]["produto"]["quantidade"]["vendedor"]["usuario"]} for row in result]


#Buscar
def buscarCompras(self):
    with self.driver.session(database="neo4j") as session:
        session.read_transaction(self._buscarCompras)

@staticmethod
def _buscarCompras(db):
    query = "MATCH (c:compra) RETURN c"
    result = db.run(query)
    return [print([row]) for row in result]

def buscarCompra(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._buscarCompra)
    
@staticmethod
def _buscarCompra(db):
    idCompra = input("Insira o ID da compra que deseja encontrar: ")
    query = "MATCH (c:compra) WHERE c.id = $idCompra RETURN c"
    result = db.run(query, idCompra=idCompra)
    return [print([row]) for row in result]

#Atualozar
def atualizarCompra(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._atualizarCompra)

@staticmethod
def _atualizarCompra(db):
    idCompra = input("Insira o ID da compra que deseja atualizar: ")

    new= input("Insira o novo valor: ")

    query = ("MATCH (c:compra) WHERE c.id = $idCompra SET c.status = $new")

    print("Compra atualizada com sucesso!")

    db.run(query, idCompra=idCompra, new=new)

#Deletar
    def deletarCompra(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self._deletarCompra)

    @staticmethod
    def _deletarCompra(db):
        idCompra = input("Insira o ID da compra a ser deletado: ")
        query = "MATCH (c:compra) WHERE c.id = $idCompra DETACH DELETE c"
        print("Compra deletada com sucesso")
        db.run(query, idCompra=idCompra)