import numpy as np

def extrairNúmerosImpares(v):
    return v[v%2 != 0]

def extrairNúmerosPares(v):
    return v[v%2 == 0]