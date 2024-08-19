from PIL import Image
url = input("ingrese la url de una imagen:")
abrir= Image.open(url)
abrir.show()
width,height = abrir.size
print(f"ancho:{width}")
print(f"alto:{height}")
print(f"nombre del archivo:{abrir.filename}")
print(f"formato de la imagen:{abrir.format}")
abrir.save(url)