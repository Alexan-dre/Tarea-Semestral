#Integrantes:
#Belmar Araus, Benjamín Alexander
#Mendoza Faúndez, Daniel Helaman
#Penroz Gallardo, Erick Alexander
#Rivera Vásquez, Felipe Andrés

import json
import random
#Parte 1: Ingreso de palabras y validación
#al ingresar texto vacío se termina el pedir palabras

    #poner lista de palabras
with open("spanishc-t.json", "r", encoding="utf-8")as trabajo:
    fuente=json.load(trabajo)
   
    #Normalización de palabras
def tildes(t):
    t=t.replace("á", "a")
    t=t.replace("é", "e")
    t=t.replace("í", "i")
    t=t.replace("ó", "o")
    t=t.replace("ú", "u")
    t=t.replace("ü", "u")  
    t=t.replace("Á", "A")
    t=t.replace("É", "E")
    t=t.replace("Í", "I")
    t=t.replace("Ó", "O")
    t=t.replace("Ú", "U")
    t=t.replace("Ü", "U")
    
    return t

    #crear lista
lista=[]
    
    #comprobar palabras(comparar con el json, hacerlas minusculas, procesar tildes, asegurar el uso de solo letras, no repetir palbras ingresadas)
while True:
    palabraog=input('Ingresa una palabra (Enter para terminar):').strip()
    palabraog=palabraog.lower()
    if palabraog=="":
        if len(lista)==0:
            print('No se ingresaron palabras')
            continue
        else:
            break

    palabra2=tildes(palabraog)
    k=0
    for l in palabra2:
        if l not in "qwertyuiopasdfghjklñzxcvbnm":
            print("Solo puede ingresar letras.")
            k=1
            break
    if k==1:
        continue
    if palabra2 in fuente:
        if palabraog not in lista:
            lista.append(palabraog)
        else: 
            print("La palabra ya fue ingresada.")
    
    #extra agregar palabras que no esten en el diccionario
    else:
        print("No se puede garantizar que la palabra sea real.")
        r=input("¿Desea usarla de todas formas?: (si/no)")
        r=r.lower()
        r=tildes(r)
        if r=="si" or r=="s":
            if palabraog not in lista:
                lista.append(palabraog)
            else:
                print("La palabra ya fue ingresada.")

    #imprimir lista de palabras ingresadas 
print("Lista completada.")

#Parte 2: Inicialización del juego.
#Se selecciona una palabra al azar y se preparan las variables de control
def Parte2(Base):
    palabrasecreta=random.choice(Base).upper()
    casillas=['_']*len(palabrasecreta)
    contarfallos=0
    letrasusadas=[]
    return palabrasecreta, casillas, contarfallos, letrasusadas
#PARTE 3: Ciclo de turnos
def turno (palabrasecreta, casillas, contarfallos, letrasusadas):
 # condicion, fallos < 10 y que aun queden letras por adivinar
 while contarfallos < 10 and "_" in casillas:
    
    # pedimos palabra por consola
    letra_ingresada = input("Adivina una letra: ").upper().strip()
    if len(letra_ingresada) !=1 or letra_ingresada not in 'QWERTYUIOPASDFGHJKLÑZXCVBNM':
        print('Ingresa solo una letra del abecedario')
        continue
    if letra_ingresada in letrasusadas:
        print('Ya usaste esta letra')
        continue
    letrasusadas.append(letra_ingresada)
    
    i = 0
    n = len(palabrasecreta)
    acierto = False
    
    # con un ciclo while recorremos la palabra 
    while i < n:
        if tildes(palabrasecreta[i]) == tildes(letra_ingresada):    #validamos que la letra ingresada este en la palabra
            casillas[i] = palabrasecreta[i] #letra_ingresada
            acierto = True
        
        # Incrementar el contador para seguir recorriendo la palabra
        i = i + 1
        
    # verificamos que en caso de que la letra no este en la palabra para aumentar el contador de fallos 
    if acierto == False:
        contarfallos = contarfallos + 1
        
    ganador(casillas, palabrasecreta, contarfallos)
    if "_" not in casillas or contarfallos==10:
        break
    print(" ".join(casillas))
    print(f"Letras usadas: {letrasusadas}")
    print(f"Fallos: {contarfallos}/10\n")
    
    
 return casillas, contarfallos
#Parte 4: Fin del juego.

def Palabracompleta(letrascorrectas,palabrasecreta):
    for i in palabrasecreta:
        if i not in letrascorrectas:
            return False
    return True

def Mostrarahorcado(contador):
    L= ["""
    ___________________
    |  /               
    | /                
    |/                 
    |                  
    |                  
    |                  
    |                  
    |                  
    |                  
    """ 
    ,
    """
    ___________________
    |  /          |    
    | /                
    |/                 
    |                  
    |                  
    |                  
    |                  
    |                  
    |                  
    """
    ,
    """
    ___________________
    |  /          |    
    | /           |    
    |/                 
    |                  
    |                  
    |                  
    |                  
    |                  
    |                  
    """
    ,
    """
    ___________________
    |  /          |    
    | /           |    
    |/            |    
    |                  
    |                  
    |                  
    |                  
    |                  
    |                  
    """
    ,
    """
    ___________________
    |  /          |    
    | /           |    
    |/            |    
    |            ( )   
    |                  
    |                  
    |                  
    |                  
    |                  
    """
    , 
    """
    ___________________
    |  /          |    
    | /           |    
    |/            |    
    |            ( )   
    |             |    
    |                  
    |                  
    |                  
    |                  
    """ 
    , 
    r"""
    ___________________
    |  /          |    
    | /           |    
    |/            |    
    |            ( )   
    |            \|   
    |                  
    |                  
    |                  
    |                  
    """ 
    , 
    r"""
    ___________________
    |  /          |    
    | /           |    
    |/            |    
    |            ( )   
    |            \|/   
    |                  
    |                  
    |                  
    |                  
    """ 
    , 
    r"""
    ___________________
    |  /          |    
    | /           |    
    |/            |    
    |            ( )   
    |            \|/   
    |             |    
    |                  
    |                  
    |                  
    """
    , 
    r"""
    ___________________
    |  /          |    
    | /           |    
    |/            |    
    |            ( )   
    |            \|/   
    |             |    
    |            /     
    |                  
    |                  
    """ 
    ,
    r"""
    ___________________
    |  /          |    
    | /           |    
    |/            |    
    |            ( )   
    |            \|/   
    |             |    
    |            / \   
    |                  
    |                  
    """ ]
    # Selecciona y despliega la figura ASCII correspondiente al índice del contador de fallos.
    print(L[contador])
    

def ganador (letrascorrectas, palabrasecreta, contador):
    if Palabracompleta(letrascorrectas, palabrasecreta):
        Mostrarahorcado(contador)
        print(" ".join(casillas))
        print (f"\nFelicidades, ganaste humano, la palabra era: {palabrasecreta}")
        
    elif contador==10:
        Mostrarahorcado(10)
        print(f"Fallos: {contador}/10\n")
        print(f"Perdiste, ganó el computador, la palabra era: {palabrasecreta}")
    else:
        Mostrarahorcado(contador)

#Integración de las partes:

jugar=True
while jugar:
    palabrasecreta, casillas, contarfallos, letrasusadas=Parte2(lista)
    Mostrarahorcado(0)
    print(" ".join(casillas))
    casillas, contarfallos=turno (palabrasecreta, casillas, contarfallos, letrasusadas)
    r=input("¿Jugar de nuevo?: (si/no)").strip()
    jugar=tildes(r.lower()) in ('si','s')

