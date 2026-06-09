class Pessoa:
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade  = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome, idade, nivel, especialidade):
        super().__init__(nome, idade)
        self.nivel = nivel
        self.especialidade = especialidade

    def dar_aula(self):
        pass


class Funcionaria(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor 

    def bater_ponto(self):
        pass


a1 = Aluno("Jose", 17, "Python", "T01")