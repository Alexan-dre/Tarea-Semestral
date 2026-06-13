# LLamado a una funcion para ver si la palabra esta completa o no (segun las otras partes del codigo)
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
    """
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
    """
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
    """
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
    """
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
    """
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
    # El contador deberia iterar en otra funcion por lo cual aqui solo contemple que se imprima segun la iteracion del contador
    print(L[contador])
    

def ganador (letrascorrectas, palabrasecreta, contador):
    if Palabracompleta(letrascorrectas, palabrasecreta):
        Mostrarahorcado(contador)
        print (f"Felicidades, ganaste, la palabra era: {palabrasecreta}")
    elif contador==10:
        Mostrarahorcado(10)
        print(f"Perdiste, la palabra era: {palabrasecreta}")
    else:
        Mostrarahorcado(contador)

    
