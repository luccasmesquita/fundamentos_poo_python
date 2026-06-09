def maior(*num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'Foram informados {cont} valoresd ao todo')
    print(f'o maior valor informado foi {maior}.')


#programa principal 
maior(2, 9, 4, 5, 7, 1)
