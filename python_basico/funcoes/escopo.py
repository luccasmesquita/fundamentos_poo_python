#toda vez que declaramos uma variavel no escopo global ela vai para o topo do programa
# n = 2 - é como se ela fosse declarada aqui na ponta da pagina
def teste():
    x = 8
    #a variavel X tem um escopo local
    print(f'Na função teste, n vale {n}')

#Programa principal 
n = 2
# a variavel N tem um escopo global 
print(f"No programa principal, n valor {n}")