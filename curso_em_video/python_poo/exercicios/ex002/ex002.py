"""
Declaração de classe 

class MinhaClasse:
- Atributos
- Metodos 

Declaração dos Objetos
obj = MinhaClasse() / aqui estamos instanciando o objeto - metodo construtor def __int__(self):

"""
#Declarando Classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade

    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome,  idade)
    """
    def __init__(self, nome = "", idade = 0): #Metodo construtor
        #Atributos de instancia 
        self.nome = nome
        self.idade = idade

    #metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1
    
    def __str__(self): #Dunder Methood
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."
    
#Declarando Objeto
g1 = Gafanhoto("Luccas", 17)
g1.aniversario()
print(g1)


g2 = Gafanhoto("Mauro", 53)
g2.aniversario()
print(g2)


print(g1.__doc__) #Dunder Attribute
