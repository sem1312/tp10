import time
from PIL import Image
from busqueda_imagen import busqueda_en_imagen

def crear_imagen_prueba(tamano: tuple, tonos: dict) -> Image.Image:
    imagen = Image.new('RGB', tamano, color=0)
    pixeles = imagen.load()
    for (x, y), tono in tonos.items():
        pixeles[x, y] = (tono, tono, tono)
        
    return imagen

imagenes = [
    (crear_imagen_prueba((100, 100), {(10, 10): 128}), 'Imagen 100x100'),
    (crear_imagen_prueba((500, 500), {(250, 250): 64}), 'Imagen 500x500'),
    (crear_imagen_prueba((1000, 1000), {(500, 500): 192}), 'Imagen 1000x1000')
]

for imagen, descripcion in imagenes:
    start_time = time.time()
    resultado = busqueda_en_imagen(imagen, 128)
    end_time = time.time()
    print(f"{descripcion}: {end_time - start_time:.4f} segundos")