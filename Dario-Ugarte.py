import random

def elegir_palabra():
    palabras = ['teclado', 'monitor', 'python', 'gabinete', 'mouse']
    return random.choice(palabras)

def mostrar_palabra(palabra, letras_adivinadas, intentos):
    resultado = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += '_ '
    print("Palabra:", resultado)
    print("Intentos:", intentos)
    print("***" * 10)

#Comienzo del juego
palabra = elegir_palabra()
letras_adivinadas = []
intentos = 6

print("¡Bienvenido al juego!")

while intentos > 0:
    mostrar_palabra(palabra, letras_adivinadas, intentos)
    letra = input("Ingresa una letra: ").lower()
    if letra == 'salir':
        print("Adios")
        break    

    if len(letra) != 1 or not letra.isalpha():
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
    for l in palabra:
        if l not in letras_adivinadas:
            completo = False
            break

    if completo:
        print(f"\n¡Ganaste! La palabra era: {palabra}")
        break

else:
    print(f"\nPerdiste. La palabra era: {palabra}")
