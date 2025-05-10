import random

def elegir_palabra():
    palabras = ['teclado', 'monitor', 'python', 'gabinete', 'mouse']
    return random.choice(palabras) #elige una palabra al azar

def mostrar_palabra(palabra, letras_adivinadas, intentos):#palabra escogida, letras adivinadas, vidas restantes
    resultado = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra #recorre la palabra y cuando encuentra una letra que coincida la agrega
        else:
            resultado += ' _ '#si no encuentra una letra que coincida agrega un guion
    print("***" * 10)#para separar los intentos usa ***********
    print("Palabra:", resultado)
    print("Intentos:", intentos)


#Comienzo del juego
palabra = elegir_palabra()#elige una palabra al azar
letras_adivinadas = []#inicializa las letras adivinadas
intentos = 6 

print("¡Bienvenido al juego!")

while intentos > 0:
    mostrar_palabra(palabra, letras_adivinadas, intentos) #llamo a la funcion con los parametros anteriores
    letra = input("Ingresa una letra: ").lower()    #lower() cambia la letra ingresada a minuscula
    if letra == 'salir':
        print("Adios")
        break    

    if len(letra) != 1 or not letra.isalpha():  #El método .isalpha() verifica si todos los caracteres de una cadena son letras del alfabeto (sin números, espacios ni símbolos).
        print("Ingresar solo una letra")
        continue

    if letra in letras_adivinadas:
        print("Ya usaste esa letra.")
        continue

    if letra in palabra:
        print("Letra correcta")
        letras_adivinadas.append(letra)
    else:
        print("Letra incorrecta")
        intentos -= 1


    completo = True
    for l in palabra:   #recorro cada letra de la palabra
        if l not in letras_adivinadas:  #si la letra no esta en las letras adivinadas significa que no adivino todas las letras
            completo = False
            break

    if completo:
        print(f"\n¡Ganaste! La palabra era: {palabra}")
        break

else:
    print(f"\nPerdiste. La palabra era: {palabra}")
