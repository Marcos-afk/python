class Fun:
    def __init__(self, nome, cpf, sal):
        self._nome = nome
        self._cpf = cpf
        self._sal = sal

    def dep(self, valor):
        if valor > 0:
            self._sal = self._sal + valor
        else:
            print('Erro! Valor inválido')

    def sac(self, valor):
        if self._sal >= valor:
            self._sal = self._sal - valor
        else:
            print('Erro! valor acima do saldo')

    def exi(self):
        print('\n Nome : {}'.format(self._nome))
        print('\n CPF  : {}'.format(self._cpf))
        print('\n Salario : {}'.format(self._sal))


class Gen(Fun):
    def __init__(self, nome, cpf, sal, pas):
        Fun.__init__(self, nome, cpf, sal)
        self._pas = pas

    def aut(self, senha):
        if senha == self._pas:
            print('Acesso permitido')
            return True
        else:
            print('Acesso negado')
            return False

    def updt(self, fun):
        fun._nome = input('Novo nome: ')
        fun._cpf = input('Novo cpf: ')
        fun._sal = float(input('Novo salário: '))


gen = Gen('Jose Carlos', '622-765-987-03', 2000.0, 'admin')
fun1 = Fun('Aluisio', '675-987-322-04', 400.0)

print('1 - Funcionario  ou 2 - Gerente')
cont = int(input())
if cont == 1:
    esc = 0
    while esc != 4:
        esc = int(input('1 - exibir , 2 - sacar , 3 - depositar , 4 - sair:  '))
        if esc == 1:
            fun1.exi()
        elif esc == 2:
            val = float(input('Valor a ser sacado: '))
            fun1.sac(val)
        elif esc == 3:
            val = float(input('A valor a ser depositado: '))
            fun1.dep(val)
        elif esc == 4:
            esc = 4
else:
    sen = input('Senha do gerente: ')
    if gen.aut(sen):
        esc = 0
        while esc != 5:
            esc = int(input('1 - exibir , 2 - sacar , 3 - depositar , 4 - atualizar ,5 - sair:  '))
            if esc == 1:
                gen.exi()
            elif esc == 2:
                val = float(input('Valor a ser sacado: '))
                gen.sac(val)
            elif esc == 3:
                val = float(input('A valor a ser depositado: '))
                gen.dep(val)
            elif esc == 4:
                gen.updt(fun1)
                fun1.exi()






