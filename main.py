from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable

class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

if __name__ == "__main__":
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://28b53049.databases.neo4j.io"
    user = "neo4j"
    password = "dTDdFn1aIcA3NpmBMqUac66V0VGl9nZt5GigXszWVc0"
    app = App(uri, user, password)

    loop = True
while loop:
    print('''  
    1 - CRUD Usuario \n 
    2 - CRUD Produto\n
    3 - CRUD Vendedor\n
    4 - CRUD Compra\n
    ''')
    opcao = input(str("Escolha uma opção para fazer o crud: "))
    match opcao:
        case '1':
            print('''  
                1 - Cadastrar Usuario \n 
                2 - Atualizar Usuario \n
                3 - Buscar Usuario \n
                4 - Buscar todos Usuarios \n
                5 - Deletar Usuario \n
                0 - Sair \n ''')
            opcaoUsuario = input(str("Escolha uma opção: "))
        
            match opcaoUsuario:
                case '1':
                    CrudUsuario. (meuBanquinho)
                case '2':
                    atualizarUsuario.atualizarUsuario(meuBanquinho)
                case '3':
                    buscarUsuario.procurarUsuario(meuBanquinho)
                case '4':
                    buscarUsuario.procurarTodesUsuario(meuBanquinho)
                case '5':
                    deletarUsuario.deletarUsuario(meuBanquinho)
                case '0':
                    loop = False

        case '2':
            print('''  
                1 - Cadastrar Produto \n 
                2 - Atualizar Produto \n
                3 - Buscar Produto \n
                4 - Buscar todos os Produtos \n
                5 - Deletar Produtos \n
                0 - Sair \n ''')
            opcaoProduto = input(str("Escolha uma opção: "))
        
            match opcaoProduto:
                case '1':
                    cadastrarProduto.cadastrarProduto(meuBanquinho)
                case '2':
                    atualizarProduto.atualizarProduto(meuBanquinho)
                case '3':
                    buscarProduto.procurarProduto(meuBanquinho)
                case '4':
                    buscarProduto.procurarTodesProduto(meuBanquinho)
                case '5':
                    deletarProduto.deletarProduto(meuBanquinho)
                case '0':
                    loop = False
                
        case '3':
            print('''  
                1 - Cadastrar Vendedor \n 
                2 - Atualizar Vendedor \n
                3 - Buscar Vendedor \n
                4 - Buscar todos os Vendedor \n
                5 - Deletar Vendedor \n
                0 - Sair \n ''')
            opcaoVendedor = input(str("Escolha uma opção: "))
        
            match opcaoVendedor:
                case '1':
                    cadastrarVendedor.cadastrarVendedor(meuBanquinho)
                case '2':
                    atualizarVendedor.atualizarVendedor(meuBanquinho)
                case '3':
                    buscarVendedor.procurarVendedor(meuBanquinho)
                case '4':
                    buscarVendedor.procurarTodesVendedor(meuBanquinho)
                case '5':
                    deletarVendedor.deletarVendedor(meuBanquinho)
                case '0':
                    loop = False
        

        case '4':
            print('''  
                1 - Cadastrar Compra \n 
                2 - Atualizar Compra \n
                3 - Buscar Compra \n
                4 - Buscar todas as Compra \n
                5 - Deletar Compra \n
                0 - Sair \n ''')
            opcaoCompra = input(str("Escolha uma opção: "))
        
            match opcaoCompra:
                case '1':
                    cadastrarCompra.cadastrarCompra(meuBanquinho)
                case '2':
                    atualizarCompra.atualizarCompra(meuBanquinho)
                case '3':
                    buscarCompra.procurarCompra(meuBanquinho)
                case '4':
                    buscarCompra.procurarTodesCompra(meuBanquinho)
                case '5':
                    deletarCompra.deletarCompra(meuBanquinho)
                case '0':
                    loop = False
        

    app.close()