from Produtos import Produtos
from typing import list

class Fornecedor:
    def __init__(self, nome: str, contato: str, produtosFornecidos: list[Produtos]) -> None:
        self.nome = nome
        self.contato = contato
        self.produtosFornecidos = produtosFornecidos

class PedidoReposicao:
    def __init__(self, produtos: list[Produtos], fornecedores: list[Fornecedor]) -> None:
        self.produtos = produtos
        self.fornecedores = fornecedores
    
    def RealizarPedido(self) -> None:
        pass

class SetorCompras:
    def gerarPedidoReposicao(self, produto: Produtos) -> PedidoReposicao:
        pass
