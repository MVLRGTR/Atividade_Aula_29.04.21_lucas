from typing import list
from Dados import Dados,DadosCadastro

class Atendentes:

    def _init_(self,nome,Id) -> None:
        self.nome = nome
        self.Idatendente = Id
    
    def verificaCadastroCliente(self , ClienteDados:Dados) -> bool:
        pass

    def CadastrarCliente(self,ClienteDados:DadosCadastro) -> Cliente:
        pass

    def GerarSenha(self)-> str :
        pass

    def VerificarSenha(self,senha : str) -> bool :
        pass

    def CriarPedido(self,cliente:Cliente ,pedido :Pedido) -> None:
        pass
