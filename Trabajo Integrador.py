import random

def elegir_palabra():
    palabras = ['teclado', 'monitor', 'computadora', 'programacion', 'python']
    return random.choice(palabras)

def mostrar_estado(palabra_secreta, letras_adivinadas, vidas, letras_incorrectas):
    estado = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado += letra
        else:
            estado += '_ '
    
    print("\nPalabra:", estado)
    print("Vidas restantes:", vidas)
    letras_como_texto = ''
    for letra in letras_incorrectas:
        letras_como_texto += letra + ' '
    
    print("Letras incorrectas:", letras_como_texto)
