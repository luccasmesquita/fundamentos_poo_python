from classes import Aluno, Professor, Funcionaria

def main():
    a1 = Aluno("Jose", 17, "Python", "T01")
    a1.fazer_aniversario
    a1.fazer_matricula

    p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
    p1.dar_aula

    f1 = Funcionaria("Clausia", 27, "Secretaria", "Secretaria")
    f1.bater_ponto

if __name__ == "__main__":
    main()