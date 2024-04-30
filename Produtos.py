class Produtos:
    def __init__(self, codigo: int, nome: str, QuantidadeEstoque: int, Preco: float) -> None:
        self.codigo = codigo
        self.nome = nome
        self.quantidadeEstoque = QuantidadeEstoque
        self.precoUnitario = Preco