import sys
from PIL import Image, ImageDraw, ImageFont
 
# Verifica que el usuario haya proporcionado un nombre de archivo
if len(sys.argv) < 2:
    print("Uso: python script.py imagen.jpg")
    sys.exit(1)
 
# Nombre del archivo proporcionado por el usuario
img_path = sys.argv[1]
 
# Carga la imagen
img = Image.open(img_path)
 
# Prepara el objeto para dibujar
draw = ImageDraw.Draw(img)
 
# Intenta cargar una fuente, o usa una por defecto si no se especifica
try:
    font = ImageFont.truetype("arial.ttf", 36)  # Ajusta el tamaño de la fuente según tus necesidades
except IOError:
    font = ImageFont.load_default()
 
# Tamaños para la cuadrícula
width, height = img.size
step_x = width / 36  # 36 líneas verticales para 360°
step_y = height / 18  # 18 líneas horizontales para 180°
 
# Centro de la imagen
center_x, center_y = width / 2, height / 2
 
# Color amarillo para la cuadrícula y el texto
yellow_color = (255, 255, 0)
 
# Dibuja líneas verticales y números
for i in range(-18, 19):
    x = center_x + (i * step_x)
    if x >= 0 and x <= width:
        draw.line((x, 0, x, height), fill=yellow_color)
        if i % 1 == 0 and i != 0:
            draw.text((x, center_y), str(i * 10), fill=yellow_color, font=font)
 
# Dibuja líneas horizontales y números
for i in range(-9, 10):
    y = center_y + (i * step_y)
    if y >= 0 and y <= height:
        draw.line((0, y, width, y), fill=yellow_color)
        if i % 1 == 0 and i != 0:
            draw.text((center_x, y), str(i * 10), fill=yellow_color, font=font)
 
# Genera el nombre del archivo de salida
output_file = f"{img_path.rsplit('.', 1)[0]}_rejilla.jpg"
 
# Guarda la imagen modificada
img.save(output_file)
 
print(f"Imagen guardada como: {output_file}")