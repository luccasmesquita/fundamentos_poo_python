casa = float(input('valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de. R${:.2f} em {} anos, a prestação sera de R${:.2f}'.format(casa, anos, prestacao))

if prestacao <= minimo:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo NEGADO')