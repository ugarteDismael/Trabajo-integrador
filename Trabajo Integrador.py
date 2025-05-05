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
    print(f"\nPalabra: {estado}")
    print(f"Vidas restantes: {vidas}")
    print(f"Letras incorrectas: {' '.join(letras_incorrectas)}")
