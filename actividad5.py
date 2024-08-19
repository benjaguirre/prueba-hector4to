from PIL import Image
import os 

def img():
    ruta_foto = input("ingrese la ruta de la foto: ")
    foto = Image.open(ruta_foto)
    foto.show()
def marc():
    print(" ingrese una de las 4 opciones (superior izquierda, superior derecha, inferior izquierda, inferior derecha)")
    opciones=input()
    if opciones == 'superior izquierda':
        print('hola')
    elif opciones == 'superior derecha':
        print('hola2')
    elif opciones == 'inferior izquierda':
        print('hola3')
    elif opciones == 'inferior derecha':
        print('hola4')
    else:
        print('no has puesto una ubicacion para la marca de agua')

marc()

