class Membro:
    def __init__(self, nome, dataDeNascimento):
        self.__nome = nome
        self.__dataDeNascimento = dataDeNascimento
        self.__disciplina = []

    def getRelacionamento(self):
        return __class__.__name__
    
    def addDisciplina (self,disciplina):
        if self.__disciplina.count(disciplina) == 0:
            # nao tem nada
            self.__disciplina.append(disciplina)
            return True
        else:
            # ja tem
            return False

    def removeDisciplina(self,disciplina):
        if self.__disciplina.count(disciplina) == 0:
            # nao tem nada
            return False
        else:
            # tem
            self.__disciplina.remove(disciplina)
            return True

    def getDisciplinas(self):
        return self.__disciplina
    
    def getDisciplina(self, disciplina):
        return self.__disciplina.count(disciplina) != 0


class Professor(Membro):
    def __init__(self, nome, dataDeNascimento, salário):
        super().__init__(nome, dataDeNascimento)
        self.__salário = float(salário)

    def getRelacionamento(self):
        return __class__.__name__

    def getSalário(self):
        return self.__salário
    
    def setSalário(self, salário):
        self.__salário = float(salário)

class Aluno(Membro):
    def __init__(self, nome, dataDeNascimento, matrícula):
        super().__init__(nome, dataDeNascimento)
        self.__matrícula = int(matrícula)

    def getRelacionamento(self):
        return __class__.__name__

    def getMatrícula(self):
        return self.__matrícula
    
    def setMatrícula(self, matrícula):
        self.__matrícula = int(matrícula)