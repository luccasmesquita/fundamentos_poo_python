# DOCSTRING é uma ajuda iterativa, é basicamente uma string de documentação

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print("FIM")

#help(contador)

#parametros opcionais
def somar(a=0, b=0, c=0):
    #informando valor padrão para que o parametro seja opcional
    """
    -> Faz a soma de tres valorews e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor

    """
    s = a + b + c
    print(f'A. soma. vale {s}')

somar(3, 2, 5)
somar(3, 2)