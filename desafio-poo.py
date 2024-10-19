from abc import ABC, abstractclassmethod,
abstractproperty
from datetime import datetime

class Cliente:
    def  __init__(self, endereço):
        self.endereço = endereço
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Pessoafisica(Cliente): 
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self.saldo= 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero 
    
    @property
    def agencia(self):
        return self._agencia 
    
    @property
    def cliente(self):
        return self._cliente
    

    @property
    def historico(self):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você nao tem saldo suficiente. @@@")
        
        elif valor > 0:
            self.saldo -= valor 
            print("\n Saque realizado")
            return True
        
        else:
            print("\n@@@ Operação falhou! Valor inválido. @@@")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor 
            print("\n Deposito realizado!")
        else:
            print("\n@@@ Operação falhou! Você nao tem saldo suficiente. @@@")
            return False
        
        return True 

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)    
        self.limite = limite
        self.limite_saques = limite_saques 
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
            transacoes if transacao["tipo"] = Saque.__name__]
        )
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self 
        limite_saques

        if excedeu_limite
            print

            

