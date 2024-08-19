from PIL import Image
imagen = Image.open("img/mapache.jpg")
imagen.show()

mapacheImg = Image.open('img/mapache.jpg')
mapachetCopyIm = mapacheImg.copy()

faceImg = mapacheImg.crop((335, 345, 565, 560))
faceImg.size
(230, 215)
mapacheImg.paste(faceImg, (0, 0))
mapacheImg.paste(faceImg, (400, 500))
mapacheImg.save('mapache.jpg')