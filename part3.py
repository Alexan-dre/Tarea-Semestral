def turno (palabrasecreta, casillas, contarfallos, letrasusadas):
 # condicion, fallos < 10 y que aun queden letras por adivinar
 while contarfallos < 10 and "_" in casillas:
    
    # pedimos palabra por consola
    letra_ingresada = input("Adivina una letra: ").upper()
    letrasusadas.append(letra_ingresada)
    
    i = 0
    n = len(palabrasecreta)
    acierto = False
    
    # con un ciclo while recorremos la palabra 
    while i < n:
        if palabrasecreta[i] == letra_ingresada:    #validamos que la letra ingresada este en la palabra
            casillas[i] = letra_ingresada
            acierto = True
        
        # Incrementar el contador para seguir recorriendo la palabra
        i = i + 1
        
    # verificamos que en caso de que la letra no este en la palabra para aumentar el contador de fallos 
    if acierto == False:
        contarfallos = contarfallos + 1
        

    print(" ".join(casillas))
    print(f"Letras usadas: {letrasusadas}")
    print(f"Fallos: {contarfallos}/10\n")
    
 return casillas, contarfallos