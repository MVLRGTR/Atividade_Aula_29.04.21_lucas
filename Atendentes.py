from Dados import Dados,DadosCadastro
from Clientes import Clientes
from Pedidos import Pedidos

class Atendentes:

    def _init_(self,nome,Id) -> None:
        self.nome = nome
        self.Idatendente = Id
    
    def verificaCadastroCliente(self , ClienteDados:Dados) -> bool:
        pass

    def CadastrarCliente(self,ClienteDados:DadosCadastro) -> Clientes:
        pass

    def GerarSenha(self)-> str :
        pass

    def VerificarSenha(self,senha : str) -> bool :
        pass

    def CriarPedido(self,cliente:Clientes ,pedido :Pedidos) -> None:
        if(self.VerificarSenha('senha_qui')==True):
            pass
        else:
            print('Informar erro de senha')
        pass

    
    