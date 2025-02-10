from VarType import codigo

fruta = input('Digite o nome de uma fruta: ')
print(fruta)

#Inputs not string
código = int(input('Digite o código do funcionário: '))
nome = input('Digite o nome do funcionário: ')
salario = float(input('Informe o salário: '))
ativo = True

print('Código: %d'%código)
print('Nome: %s'%nome)
print('Salário: %.2f '%salario)
print('Ativo: %r'%ativo)