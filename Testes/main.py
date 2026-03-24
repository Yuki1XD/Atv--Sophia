from models.produtos import Produto
from services.estoque import Estoque

estoque = Estoque()

p1 = Produto("Mouse", 10)
p2 = Produto("Teclado", 18)



estoque.adicionar_produto(p1)
estoque.adicionar_produto(p2)


produto_encontrado = estoque.buscar_produto("mouse")

if produto_encontrado:
    print("Produto encontrado")
else:
    print("Produto não encontrado")


atualizar_estoque = estoque.atualizar_quantidade("mouse", 13)

if atualizar_estoque:
    print("Quantidade atualizada com sucesso")
else:
    print("Produto não encontrado")


estoque.listar_produtos()