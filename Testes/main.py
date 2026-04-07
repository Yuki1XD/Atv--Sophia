from services.estoque import executar_rotas

print(executar_rotas("/produtos", "Post", {"nome": "PI do 5 periodo", "quantidade": 0}))

print(executar_rotas("/produtos", "Post", {"nome": "PI do 5 periodo", "quantidade": 2}))

print(executar_rotas("/produtos", "Post", {"nome": "PI do 2 periodo", "quantidade": 3}))

print(executar_rotas("/produtos", "Get"))

print(executar_rotas("/produtos/buscar", "Get", {"nome": "PI do 5 periodo"}))

print(executar_rotas("/produtos/atualizar", "Put", {"nome": "PI do 5 periodo", "quantidade": 5}))

print(executar_rotas("/produtos", "Get"))

print(executar_rotas("/produtos/delete", "Delete", {"nome": "PI do 5 periodo"}))

print(executar_rotas("/produtos", "Get"))


