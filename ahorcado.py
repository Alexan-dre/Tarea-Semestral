#PARTE 2
import random
def Parte2(Base):
    palabrasecreta=random.choice(Base)
    casillas=['_']*len(palabrasecreta)
    contarfallos=0
    Letrasusadas=[]
    return palabrasecreta, casillas, contarfallos, Letrasusadas

def desplegar_casillas(L):
    print(' '.join(L))
#PARTE 3
