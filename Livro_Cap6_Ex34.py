'''
Vejamos uma situação na qual temos que selecionar os elementos de uma lista
de forma a copiá-los para outras duas listas. Para simplificar o problema, imagine
que os valores estejam inicialmente na lista V, mas que devam ser copiados para
a P, se forem pares; ou para a I, se forem ímpares.
'''

V = [9,8,7,12,0,13,21]
P = []
I = []

for e in V:
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)

print("Lista:", V)
print("Pares:", P)
print("Ímpares:", I)
