# encoding: iso-8859-1

string = 'Um tigre, dois tigres, três tigres'
print(string.replace('tigre', 'gato'))

numero = 1800
print("{0:10.2f}".format(numero))
print("R$ {0:0.2f} reais".format(numero))
print("{0:b}".format(numero)) # formata como binário
print("{0:X}".format(numero)) #formata como hexadecimal
print("{0:o}".format(numero)) #formata como octal

num2 = float(1275.92)
print("{:n}".format(num2))
print("{:20.2%}".format(num2))
