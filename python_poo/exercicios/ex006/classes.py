from abc import ABC,  abstractmethod
class Pessoa(ABC):
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade  = idade

    def fazer_aniversario(self):
        self.idade += 1
    
    @abstractmethod
    def estudar(self):
        pass
        

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        pass
    
    def estudar(self):
        print(f"{sel.nome} esta estudando")


class Professor(Pessoa):
    def __init__(self, nome, idade, nivel, especialidade):
        super().__init__(nome, idade)
        self.nivel = nivel
        self.especialidade = especialidade

    def dar_aula(self):
        pass

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade}")


class Funcionaria(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor 

    def bater_ponto(self):
        pass

    def estudar(self):
        print(f"{self.nome} se especializa para a area de {self.setor}")