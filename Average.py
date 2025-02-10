notaA=float(input('Informe a primeira nota: '))
notaB=float(input('Informe a segunda nota: '))

#calc
mediafinal = (notaA + notaB) / 2

#verication
if mediafinal >=7.0:
    print('A Média: %.1f - Aprovado'%mediafinal)
else:
    print('A Média: %.1f - Reprovado'%mediafinal)