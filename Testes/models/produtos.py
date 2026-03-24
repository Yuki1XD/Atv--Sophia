class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
    

    def adicionar (self, valor):
        self.quantidade += valor
    

    def remove (self, valor):
        self.quantidade -= valor
    

    def mostrar_dados(self):
        print(f"\nNome:{self.nome}")
        print (f"quantidade:{self.quantidade}\n")

