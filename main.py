from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable
import Usuario.CrudUsuario as criarUsuario
import Usuario.CrudUsuario as atualizarUsuario
import Usuario.CrudUsuario as buscarUsuario
import Usuario.CrudUsuario as buscarTodesUsuarios
import Usuario.CrudUsuario as deletarUsuario
import Produtos.CRUDprod as atualizarProduto
import Produtos.CRUDprod as buscarProduto
import Produtos.CRUDprod as buscarTodesProduto
import Produtos.CRUDprod as cadastrarProduto
import Produtos.CRUDprod as deletarProduto
import Vendendor.CrudVendedor as cadastrarVendedor
import Vendendor.CrudVendedor as buscarVendedor
import Vendendor.CrudVendedor as buscarTodesVendedor
import Vendendor.CrudVendedor as atualizarVendedor
import Vendendor.CrudVendedor as deletarVendedor
import Compra.CrudCompra as cadastrarCompra
import Compra.CrudCompra as buscarCompra
import Compra.CrudCompra as atualizarCompra
import Compra.CrudCompra as deletarCompra


class App:

    def __init__(self, uri, user, password):
        driver = GraphDatabase.driver(uri, auth=(user, password))
        global session 
        session = driver.session ()

    def close(self):
        
        self.driver.close()

if __name__ == "__main__":
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
                    criarUsuario.criarUsuario (session)
                case '2':
                    atualizarUsuario.atualizarUsuario(session)
                case '3':
                    buscarUsuario.buscarUsuario(session)
                case '4':
                    buscarTodesUsuarios.buscarUsuarios(session)
                case '5':
                    deletarUsuario.deletarUsuario(session)
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
                    cadastrarProduto.criarProduto(session)
                case '2':
                    atualizarProduto.atualizarProduto(session)
                case '3':
                    buscarProduto.buscarProduto(session)
                case '4':
                    buscarTodesProduto.buscarProdutos(session)
                case '5':
                    deletarProduto.deletarProduto(session)
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
                    cadastrarVendedor.vendedor(session)
                case '2':
                    atualizarVendedor.atualizarVendedor(session)
                case '3':
                    buscarVendedor.buscarVendedor(session)
                case '4':
                    buscarTodesVendedor.buscarVendedores(session)
                case '5':
                    deletarVendedor.deletarVendedor(session)
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
                    cadastrarCompra.criarCompra(session)
                case '2':
                    atualizarCompra.atualizarCompra(session)
                case '3':
                    buscarCompra.buscarCompra(session)
                case '4':
                    buscarCompra.buscarCompras(session)
                case '5':
                    deletarCompra.deletarCompra(session)
                case '0':
                    loop = False