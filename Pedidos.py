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
        self.status = 'criado'
    
    def AdicionarProduto(self,produto:Produtos, quantidade : int) -> None:
        if(self.VerificaDisponibilidadeProduto(Produtos)==True):
            pass
        else:
            print('informa cliente que o produto para a qunatidade em questão não está disponivél  ')
        
    def RemoverProduto(self,produto:Produtos, quantidade : int) -> None:
        pass

    def ValorTotal(self) -> None:
        pass

    def VerificaDisponibilidadeProduto(self,Produto:Produtos) -> bool:
        pass

    def CheckPagamento(self) -> None:
        pass

    def MudaStatus(self) -> None:
        pass