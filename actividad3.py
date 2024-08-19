from PIL import Image


ruta_imagen = input("Ingresa la ruta de la imagen: ")
angulo_rotacion = int(input("Ingresa el ángulo de rotación (en grados): "))

imagen = Image.open(ruta_imagen)

imagen_rotada = imagen.rotate(angulo_rotacion, expand=True)

imagen_rotada.show()

nombre_archivo = ruta_imagen.split('/')[-1]
nombre_sin_extension, extension = nombre_archivo.split('.')

copia = f"{nombre_sin_extension}Rot{angulo_rotacion}.{extension}"

imagen_rotada.save(copia)

print(f"Imagen rotada guardada como {copia}")
