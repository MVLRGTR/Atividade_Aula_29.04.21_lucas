from Clientes import Clientes
from typing import list

class Pedidos:
    def __init__(self , IdPedido:int ,Cliente : Clientes ,Produtos: list[Produtos] ,ValorTotal : float ,FormaPagamento : str , Parcelas : int) -> None:
        self.numeropedido = IdPedido
        self.cliente = Cliente
        self.produtos = Produtos
        self.valortotal = ValorTotal
        self.formapgto = FormaPagamento
        self.parcelas = Parcelas
    
    def AdicionarProduto(self,produto:Produto, quantidade : int) -> None:
        pass

    def RemoverProduto(self,produto:Produto, quantidade : int) -> None:
        pass

    def ValorTotal(self) -> None:
        pass
