prato = 5
pilha = list(range(1, prato + 1))
while True:
    print("\nExistem %d pratos na pilha" % len(pilha))
    print("Pilha atual:", pilha)
    print("Digite E para empilhar um novo prato,")
    print("ou D para desempilhar. S para sair.")
    operação = input("Operação (E, D ou S): ").upper()
    if operação == "D":
        if(len(pilha)) > 0:
            lavado = pilha.pop(-1)
            print("Prato %d lavado" % lavado)
        else:
            print("Pilha vazia! Nada para lavar.")
    elif operação == "E":
        prato += 1  # Novo prato
        pilha.append(prato)
    elif operação == "S":
        break
    else:
        print("Operação inválida! Digite apenas E, D ou S!")
