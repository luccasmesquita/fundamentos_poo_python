from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda não tem 18 anos, ainda falta {} anos para o alistamento ')
elif idade > 18:
    saldo  
    print('Voce ja deveria ter se alistado ha {} anos')