class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for p in self.produtos:
            print(p.nome, p.quantidade)

    def buscar_produto(self, nome):
        for p in self.produtos:
            if p.nome.lower() == nome.lower():
                return p
        return None

    def atualizar_quantidade(self, nome, nova_quantidade):
        for p in self.produtos:
            if p.nome.lower() == nome.lower():
                p.quantidade = nova_quantidade
                return p
            return None
