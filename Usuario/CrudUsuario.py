
#Criar

def usuario(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._criarUsuario)

def criarUsuario(db):
    query = ("CREATE (object: usuario {nome: $nomeUsu, email: $emailUsu, cpf: $cpfUsu, estado: $estadoUsu, cidade: $cidadeUsu, rua: $ruaUsu, numero: $numeroUsu})")

    nomeUsu = input("Nome: ")
    emailUsu = input("Email: ")
    cpfUsu = input("CPF: ")
    print("\n---- Endereço ----")
    estadoUsu = input("Estado: ")
    cidadeUsu = input("Cidade: ")
    ruaUsu = input("Rua: ")
    numeroUsu = input("Número: ")

    result = db.run(query, nomeUsu=nomeUsu, emailUsu=emailUsu, cpfUsu=cpfUsu, estadoUsu=estadoUsu, cidadeUsu=cidadeUsu, ruaUsu=ruaUsu, numeroUsu=numeroUsu)

    print("Usuário criado com sucesso!")
    return [{"object": row["object"]["nome"]["email"]["cpf"]["estado"]["cidade"]["rua"]["numero"]} for row in result]


#Buscar

def buscarUsuarios(db):
    query = "MATCH (u:usuario) RETURN u"
    result = db.run(query)
    return [print([row]) for row in result]

def buscarUsuario(db):
    cpfUsu = input("Insira o CPF do usuário que deseja encontrar: ")
    query = "MATCH (u:usuario) WHERE u.cpf = $cpfUsu RETURN u"
    result = db.run(query, cpfUsu=cpfUsu)
    return [print([row]) for row in result]

#atualizar


def atualizarUsuario(db):
        cpfUsu = input("Insira o CPF do usuário que deseja atualizar: ")

        print('''
                1 - Nome
                2 - Email
                3 - CPF
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
        elif option == "3": option = "cpf"
        elif option == "4": option = "estado"
        elif option == "5": option = "cidade"
        elif option == "6": option = "rua"
        elif option == "7": option = "numero"

        new= input("Insira o novo valor: ")

        query = ("MATCH (u:usuario) WHERE u.cpf = $cpfUsu SET u." + option + " = $new")

        print("Usuário atualizado com sucesso!")

        db.run(query, cpfUsu = cpfUsu, option=option, new=new)


def deletarUsuario(db):
        cpfUsu = input("Insira o CPF do usuário a ser deletado: ")
        query = "MATCH (u:usuario) WHERE u.cpf = $cpfUsu DETACH DELETE u"
        print("Usuário deletado com sucesso")
        db.run(query, cpfUsu=cpfUsu)
