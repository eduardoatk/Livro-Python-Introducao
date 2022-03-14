from clientes import Cliente
from contas import Conta
#from bancos import Banco

joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria Silva", "555-4321")
jose = Cliente("José Vargas", "999-4875")

conta_joao = Conta(joão, 5523, 5000)
conta_maria = Conta(maria, 8544, 9000)
conta_joao_jose = Conta([joão, jose], 500)

print(joão.nome)
print(maria.nome)
print(jose.nome)

conta_joao.resumo()
conta_joao.saque(1000)
conta_joao.resumo()
conta_joao.saque(50)
conta_joao.resumo()
conta_joao.deposito(200)
conta_joao.resumo()
conta_joao.extrato()
conta_joao.saque(5000)