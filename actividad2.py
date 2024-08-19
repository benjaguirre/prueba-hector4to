from PIL import Image

rutaimagen = "img/mapache.jpg"
imagen = Image.open(rutaimagen)
imagen.show()

imagen.save("img/copia/mapcache.jpg")