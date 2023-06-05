from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
"""Observação: carrinho será uma lista de dicionário, o qual contém
a chave como sendo o produto (código, nome, valor) e o valor como
sendo a quantidade"""
carrinho: List[Dict[Produto, int]] = []


def main():
    menu()

def menu():
    print('===========================')
    print('===== Rodrigues Shop ======')
    print('===========================')

    print('Seleciona uma das opções abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto(s)')
    print('3 - Comprar produto(s)')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao = int(input('\nOpção: '))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('\nObrigado, volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('\nOpção inválida!')
        sleep(1)
        print("\n")
        menu()

def cadastrar_produto():
    print("\n")
    print('Cadastrar produto')
    print('=================')

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))

    produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'\nO produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    print("\n")
    menu()

def listar_produtos():
    if len(produtos) > 0:
        print('\nListagem de produtos')
        print('====================')
        for produto in produtos:
            print(produto)
            print('------------------')
            sleep(1)
    else:
        print('\nAinda não existem produtos cadastrados.')
    sleep(2)
    print("\n")
    menu()

def comprar_produto():
    if len(produtos) > 0:
        print('\n====== Produtos disponíveis ======')
        for produto in produtos:
            print(produto)
            print('----------------------------------')
            sleep(1)

        print('\nInforme o código do produto que deseja adicionar ao carrinho: ')
        codigo = int(input('Código: '))

        produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho = False
                for item in carrinho:
                    quantidade = item.get(produto)
                    if quantidade:
                        item[produto] = quantidade + 1
                        print(f'\nO produto {produto.nome} agora possui {quantidade + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        print("\n")
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'\nO produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    print("\n")
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'\nO produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                print("\n")
                menu()
        else:
            print(f'\nO produto com código {codigo} não foi encontrado.')
        sleep(2)
        print("\n")
        menu()

    else:
        print('\nNão existem produtos para vender.')
    sleep(2)
    print("\n")
    menu()

def visualizar_carrinho():
    if len(carrinho) > 0:
        print('\nProduto no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
    else:
        print('\nAinda não existem produtos no carrinho.')
    sleep(2)
    print("\n")
    menu()

def fechar_pedido():
    if len(carrinho) > 0:
        valor_total = 0

        print('\nProdutos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('---------------------')
                sleep(1)
        print(f'\nO valor total do pedido é de {formata_float_str_moeda(valor_total)}')
        print('\n ======== Volte sempre! ========')
        carrinho.clear()
        sleep(5)
    else:
        print('\nAinda não existem produtos no carrinho.')
    sleep(2)
    print("\n")
    menu()
def pega_produto_por_codigo(codigo):
    prod = None
    
    for produto in produtos:
        if produto.codigo == codigo:
            prod = produto
    return prod

if __name__ == '__main__':
    main()
