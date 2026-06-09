"""função é uma "rotina"  para criar uma função usamos a palavra def
  eu consigo passar parametros para  dentro das funcoes

  uma função é um conjunto de bloco de comandos que executam alguma ação ou tarefa

  exemplo de função
def(funcao) mostrar_linha():
    print("------------------------------")

mostrar_linha()
print("Cadastro de funcionarios")
mostrar_linha()
"""
def mostrarLinha(text):
    print("-"*len(text))
    print(text)
    print("-"*len(text))



mostrarLinha("Cadastro de funcionarios")
mostrarLinha("Luccas")

print(" ############## Novo exemplo ##############")

############## outro exemplo 
a = 4
b = 5
s = a + b
print(s)

def soma(a, b):
    s = a + b
    print(s)


soma(4,5)

#### criando pacotes na função
print(" ############## pacotes ##############")

def contador(*num):
    print(num)


contador(5, 7, 3, 1, 4)
contador(2, 1, 7)
contador(6, 8)

print(" ############## empacoradores com listas ##############")
def dobra(lst):
    pos = 0  
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

