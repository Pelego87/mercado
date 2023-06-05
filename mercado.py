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

    opcao = int(input())

    if opcao == 1:
        cadastrar_produto
    elif opcao == 2:
        listar_produtos
    elif opcao == 3:
        comprar_produto
    elif opcao == 4:
        visualizar_carrinho
    elif opcao == 5:
        fechar_pedido
    elif opcao == 6:
        print('Obrigado, volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()

def cadastrar_produto():
    print('Cadastrar produto')
    print('=================')

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))

    produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produtos():
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('====================')
        for produto in produtos:
            print(produto)
            print('------------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()

def comprar_produto():
    pass

def visualizar_carrinho():
    pass

def fechar_pedido():
    if len(carrinho) > 0:
        valor_total = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('---------------------')
                sleep(1)
        print(f'O valor total do pedido é de {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()

def pega_produto_por_codigo(codigo):
    prod = None
    
    for produto in produtos:
        if produto.codigo == codigo:
            prod = produto
    if prod:
        return prod
    else:
        print('Não produto cadastrado com o código informado.')
        sleep(2)
        menu()

if __name__ == '__main__':
    main()
