import numpy as np

def extrairNÃºmerosImpares(v):
    return v[v%2 != 0]

def extrairNÃºmerosPares(v):
    return v[v%2 == 0]