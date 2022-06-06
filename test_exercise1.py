from exercise1 import Empresa

empresa = Empresa()
ret = 0
if(empresa.quantidadeDeFuncionários()==0):
    ret += 1
empresa.contratar('José', 1000)
if(empresa.quantidadeDeFuncionários()==1):
    ret += 1
empresa.contratar('Ana', 15600)
if(empresa.quantidadeDeFuncionários()==2):
    ret += 1
if(empresa.consultarSalário('José')==1000):
    ret += 1
empresa.darAumento('José', 10)
if(empresa.consultarSalário('José')==1100):
    ret += 1
empresa.demitir('Ana')
if(empresa.quantidadeDeFuncionários()==1):
    ret += 1
empresa.demitir('José')
if(empresa.quantidadeDeFuncionários()==0):
    ret += 1
if(ret==7):
    print('Sua implementação está correta.')
else:
    print('Sua implementação NÃO está correta.')