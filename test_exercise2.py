from exercise2 import Aluno, Professor

prof = Professor('João Afonso', '12/04/1987', 2000.00)
aluno = Aluno('Tiago Nascimento', '23/12/1997', 1234)
ret = 0
try: 
    prof.__nome
except AttributeError:
    ret += 1
try: 
    prof.__dataDeNascimento
except AttributeError:
    ret += 1
try: 
    prof.__disciplinas
except AttributeError:
    ret += 1
try: 
    prof.__salário
except AttributeError:
    ret += 1
try: 
    aluno.__matrícula
except AttributeError:
    ret += 1
if(prof.getRelacionamento()=='Professor'):
    ret += 1
if(aluno.getRelacionamento()=='Aluno'):
    ret += 1
if(len(prof.getDisciplinas())==0):
    ret += 1
if(prof.addDisciplina('C126')==True):
    ret += 1
if(len(prof.getDisciplinas())==1):
    ret += 1
if(prof.addDisciplina('C126')==False):
    ret += 1
if(prof.removeDisciplina('C126')==True):
    ret += 1
if(len(prof.getDisciplinas())==0):
    ret += 1
if(prof.removeDisciplina('C126')==False):
    ret += 1
if(prof.getSalário()==2000.00):
    ret += 1
prof.setSalário(4000.00)
if(prof.getSalário()==4000.00):
    ret += 1
if(len(aluno.getDisciplinas())==0):
    ret += 1
if(aluno.addDisciplina('C126')==True):
    ret += 1
if(len(aluno.getDisciplinas())==1):
    ret += 1
if(aluno.addDisciplina('C126')==False):
    ret += 1
if(aluno.removeDisciplina('C126')==True):
    ret += 1
if(len(aluno.getDisciplinas())==0):
    ret += 1
if(aluno.removeDisciplina('C126')==False):
    ret += 1
if(aluno.getMatrícula()==1234):
    ret += 1
aluno.setMatrícula(5678)
if(aluno.getMatrícula()==5678):
    ret += 1
if(ret==25):
    print('Sua implementação está correta.')
else:
    print('Sua implementação NÃO está correta.')
