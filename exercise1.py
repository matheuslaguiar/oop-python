class Funcionário:
  def __init__(self, nome, salário):
    self.__nome= nome
    self.__salário= float(salário)
   
  def aumentarSalário(self, percentualDeAumento):
    self.__salário += percentualDeAumento * self.__salário /100

  def getNome(self):
    return self.__nome

  def getSalário(self):
    return self.__salário
 

class Empresa:
  qtdDeFuncionários = 0 
  def __init__(self):
    self.__listaDeFuncionarios = []

  def contratar(self, nome, salário):
    funcionário = Funcionário(nome, salário)
    self.__listaDeFuncionarios.append(funcionário)
    self.qtdDeFuncionários += 1

  def demitir(self,nome):
    for funcionário in self.__listaDeFuncionarios:
      if funcionário.getNome() == nome:
        self.__listaDeFuncionarios.remove(funcionário)
        self.qtdDeFuncionários -= 1

  def darAumento(self, nome, percentualDeAumento):
    for funcionário in self.__listaDeFuncionarios:
      if funcionário.getNome() == nome:
        pos = self.__listaDeFuncionarios.index(funcionário)
        self.__listaDeFuncionarios[pos].aumentarSalário(percentualDeAumento)

  def consultarSalário(self, nome):
    for funcionário in self.__listaDeFuncionarios:
      if funcionário.getNome() == nome:
        return funcionário.getSalário()

  def quantidadeDeFuncionários(self):
    return self.qtdDeFuncionários