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
    def __init__(self): #Metodo construtor
        #Atributos de instancia 
        self.nome = ""
        self.idade = 0

    #metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."
    
#Declarando Objeto
g1 = Gafanhoto()
g1.nome = "Luccas"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 53
g2.aniversario()
print(g2.mensagem())