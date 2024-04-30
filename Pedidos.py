from Clientes import Clientes
from typing import list
from Produtos import Produtos

class Pedidos:
    def __init__(self , IdPedido:int ,Cliente : Clientes  ,ValorTotal : float ,FormaPagamento : str , Parcelas : int) -> None:
        self.numeropedido = IdPedido
        self.cliente = Cliente
        self.produtos = list[Produtos]
        self.valortotal = ValorTotal
        self.formapgto = FormaPagamento
        self.parcelas = Parcelas
    
    def AdicionarProduto(self,produto:Produtos, quantidade : int) -> None:
        pass

    def RemoverProduto(self,produto:Produtos, quantidade : int) -> None:
        pass

    def ValorTotal(self) -> None:
        pass
