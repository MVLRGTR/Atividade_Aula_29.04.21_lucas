from Pedidos import Pedidos

class Clientes:
    def __init__(self,Nome:str , Endereco : str , Telefone : str , Cpf : int ,Senha : str) -> None:
        self.nome = Nome
        self.endereco = Endereco
        self.telefone =Telefone
        self.cpf = Cpf
        self.senha = Senha
        pass
    
    def ColocarPedido(self,pedido:Pedidos) -> None:
        pass

    def RemoverPedido(Self , pedido:Pedidos) ->None:
        pass
