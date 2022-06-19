import numpy as np
from exercise3 import extrairNúmerosImpares
from exercise3 import extrairNúmerosPares
a = np.array([0,1,2,3,4,5,6,7,8,9])

ret = True
if ( (extrairNúmerosPares(a) != np.array([0,2,4,6,8])).all()):
    ret = False

if(ret == True):
    print('Teste 1: Implementação está correta.')
else:
    print('Teste 1: Implementação NÃO está correta.')
    
ret = True
if ( (extrairNúmerosImpares(a) != np.array([1,3,5,7,9])).all()):
    ret = False

if(ret == True):
    print('Teste 2: Implementação está correta.')
else:
    print('Teste 2: Implementação NÃO está correta.')