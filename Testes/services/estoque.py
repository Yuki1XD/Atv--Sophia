from Testes.models.produtos import Produto

class Estoque:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, nome, quantidade):
        produto = Produto(nome, quantidade)
        self.produtos.append(produto)
        if produto.quantidade <= 0:
            return "Quantidade inválida."
        if produto.nome in [p.nome for p in self.produtos]:
            return "Produto já existe no estoque."
        return {"mensagem": "Produto adicionado", "status": "sucesso"}
    
    def listar_produtos(self):
        return [p.to_dict() for p in self.produtos]
    
    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto.to_dict()
            return "Produto não encontrado."
        
    def atualizar_quantidade(self, nome, nova_quantidade):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                produto.quantidade = nova_quantidade
                return {"mensagem": "Quantidade atualizada", "status": "sucesso"}
            return "Produto não encontrado"
    
    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                self.produtos.remove(produto)
                return {"mensagem": "Produto removido", "status": "sucesso"}
            return "Produto não encontrado"

estoque = Estoque()

## Get = listar
## Post = Criar
## Put = atualizar
## Delete = remover

## simulação dessas rotas de uma API

def get_produtos():
    return estoque.listar_produtos()

def post_produto(nome, quantidade):
    return estoque.adicionar_produto(nome, quantidade)

def get_produto_por_nome(nome):
    return estoque.buscar_produto(nome)

def put_produto(nome, quantidade):
    return estoque.atualizar_quantidade(nome, quantidade)

def delete_produto(nome):
    return estoque.remover_produto(nome)

def executar_rotas(rota, metodo, dados=None):
    if rota == "/produtos" and metodo == "Get":
        return get_produtos()

    if rota == "/produtos" and metodo == "Post":
        return post_produto(dados["nome"], dados["quantidade"])
    
    if rota == "/produtos/buscar" and metodo == "Get":
        return get_produto_por_nome(dados["nome"])    

    if rota == "/produtos/atualizar" and metodo == "Put":
        return put_produto(dados["nome"], dados["quantidade"])

    if rota == "/produtos/delete" and metodo == "Delete":
        return delete_produto(dados["nome"])   
