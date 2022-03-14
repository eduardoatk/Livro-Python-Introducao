from clientes import Cliente
from contas import Conta
from bancos import Banco

joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria Silva", "555-4321")
jose = Cliente("José Vargas", "999-4875")

conta_joao = Conta(joão, 5000)
conta_maria = Conta(maria, 9000)
conta_joao_jose = Conta([joão, jose], 500)

tatu = Banco("Banco Tatu S.A.")

tatu.abre_conta(conta_joao)
tatu.abre_conta(conta_maria)
tatu.abre_conta(conta_joao_jose)

tatu.lista_contas()
