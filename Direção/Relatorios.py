from typing import list
from Pedidos import Pedidos
from Produtos import Produtos

class RelatorioVendas:
    def __init__(self, vendas: list[Pedidos],filtros:str) -> None:
        self.vendas = vendas
    
    def MostrarRelat(self):
        pass

class RelatorioEstoque:
    def __init__(self, produtos: list[Produtos],filtros:str) -> None:
        self.produtos = produtos
    
    def MostrarRelat(self):
        pass