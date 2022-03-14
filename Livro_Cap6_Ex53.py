# Uso de discionários

estoque = { "tomate": [ 1000, 2.30],
            "alface": [ 500, 0.45],
            "batata": [ 2001, 1.20],
            "feijão": [ 100, 1.50] }
venda = [ ["tomate", 5], ["batata", 10], ["alface",5] ]
total = 0
print("Vendas:\n")
for operação in venda:
    produto, quantidade = operação  # Operação de desempacotamento. Como operação é uma lista com dois elementos,
                                    # ao escrevermos produto, quantidade temos o primeiro elemento de operação
                                    # atribuído a produto; e o segundo, a quantidade.
    preço = estoque[produto][1]
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f\n" % (produto, quantidade,preço,custo))
    estoque[produto][0] -= quantidade
    total += custo
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])
