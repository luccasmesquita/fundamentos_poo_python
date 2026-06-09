"""
variaveis são espaços na memoria do computador
variaveis simples é que cabe so um elemtno na memoria
variaveis compostas é que cabe varios elementos dentro da mesma variavel

existem 3 tipos de variaveis compostas: Tuplas, Listas e dicionario 
() Tupla
[] Listas
{} Dicionario

as tuplas são IMUTAVEIS, depois de declaradas, nao da pra alterar 
"""

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #isso é uma tupla
print(lanche)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
    
#for comida in lanche:
 #   print(f'Eu vou comer {comida}')

print('Comi pra caramba')