#Criar

def vendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._criarVend)

@staticmethod
def _criarVend(db):
    query = ("CREATE (object: vendedor {nome: $nomeVend, email: $emailVend, cnpj: $cnpjVend, estado: $estadoVend, cidade: $cidadeVend, rua: $ruaVend, numero: $numeroVend})")

    nomeVend = input("Nome: ")
    emailVend = input("Email: ")
    cnpjVend = input("CNPJ: ")
    print("\n---- Endereço ----")
    estadoVend = input("Estado: ")
    cidadeVend = input("Cidade: ")
    ruaVend = input("Rua: ")
    numeroVend = input("Número: ")

    result = db.run(query, nomeVend=nomeVend, emailVend=emailVend, cnpjVend=cnpjVend, estadoVend=estadoVend, cidadeVend=cidadeVend, ruaVend=ruaVend, numeroVend=numeroVend)

    print("Vendedor criado com sucesso!")
    return [{"object": row["object"]["nome"]["email"]["cnpj"]["estado"]["cidade"]["rua"]["numero"]} for row in result]

#Buscar
def buscarVendedores(self):
    with self.driver.session(database="neo4j") as session:
        session.read_transaction(self._buscarVendedores)

@staticmethod
def _buscarVendedores(db):
    query = "MATCH (v:vendedor) RETURN v"
    result = db.run(query)
    return [print([row]) for row in result]

def buscarVendedor(self):
    with self.driver.session(database="neo4j") as session:
        session.read_transaction(self._buscarVendedor)

@staticmethod
def _buscarVendedor(db):
    cnpjVend = input("Insira o CNPJ do vendedor que deseja encontrar: ")
    query = "MATCH (v:vendedor) WHERE v.cnpj = $cnpjVend RETURN v"
    result = db.run(query, cnpjVend=cnpjVend)
    return [print([row]) for row in result]

#Atualizar

def atualizarVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._atualizarVendedor)

@staticmethod
def _atualizarVendedor(db):
    cnpjVend = input("Insira o CNPJ do vendedor que deseja atualizar: ")

    print('''
            1 - Nome
            2 - Email
            3 - CNPJ
            4 - Estado
            5 - Cidade
            6 - Rua
            7 - Número
        ''')
    
    option = input("Insira o número da opção que deseja atualizar: ")

    while int(option) < 1 or int(option) > 7:
        print("Opção inválida")
        option = input("Insira outra opção: ")

    if option == "1": option = "nome"
    elif option == "2": option = "email"
    elif option == "3": option = "cnpj"
    elif option == "4": option = "estado"
    elif option == "5": option = "cidade"
    elif option == "6": option = "rua"
    elif option == "7": option = "numero"

    new= input("Insira o novo valor: ")

    query = ("MATCH (v:vendedor) WHERE v.cnpj = $cnpjVend SET v." + option + " = $new")

    print("Vendedor atualizado com sucesso!")

    db.run(query, cnpjVend=cnpjVend, option=option, new=new)

    #deletar
    def deletarVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self._deletarVendedor)

    @staticmethod
    def _deletarVendedor(db):
        cnpjVend = input("Insira o CNPJ do vendedor a ser deletado: ")
        query = "MATCH (v:vendedor) WHERE v.cnpj = $cnpjVend DETACH DELETE v"
        print("Vendedor deletado com sucesso")
        db.run(query, cnpjVend=cnpjVend)