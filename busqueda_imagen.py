from PIL import Image

def busqueda_en_imagen(imagen: Image.Image, tono: int) -> dict:
    if not (0 <= tono <= 255):
        raise ValueError("El tono debe estar en el rango de 0 a 255.")

    ancho, alto = imagen.size
    pixeles = imagen.load()
    resultado = {}

    for y in range(alto):
        for x in range(ancho):
            if pixeles[x, y] == tono:
                resultado[(x, y)] = tono

    return resultado
