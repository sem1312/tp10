import py5
from PIL import Image
from busqueda_imagen import busqueda_en_imagen

def visualizar_resultados(imagen: Image.Image, resultados: dict) -> None:
    py5.size(imagen.width, imagen.height)
    py5.load_pixels()

    for (x, y), tono in resultados.items():
        py5.pixels[x + y * imagen.width] = py5.color(255, 0, 0)

    py5.update_pixels()
    py5.save_frame("resultado.png")

imagen_prueba = Image.new('L', (100, 100), color=0)
resultado = busqueda_en_imagen(imagen_prueba, 128)
visualizar_resultados(imagen_prueba, resultado)
