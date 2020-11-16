class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo = self._saldo - valor
        else:
            print(' Erro! Valor acima do Saldo')

    def depositar(self, valor):
        if valor > 0:
            self._saldo = self._saldo + valor
        else:
            print('Erro! Valor inválido')

    def exibir(self):
        print('\n Titular : {}'.format(self._titular))
        print('\n Número  : {}'.format(self._numero))
        print('\n Saldo   : {}'.format(self._saldo))
        print('\n Limite  : {}'.format(self._limite))


conta = Conta('1234-5', 'Marcos Andre', 300.00, 100.00)
conta.exibir()
print('-----------------')
conta.depositar(500)
conta.exibir()
print('-----------------')
conta.sacar(200)
print('-----------------')
conta.exibir()
