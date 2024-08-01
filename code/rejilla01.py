from PIL import Image, ImageDraw, ImageFont
 
# Carga tu imagen
img_path = 'tu_imagen_aquí.jpg'  # Asegúrate de cambiar esto por la ruta de tu imagen
img = Image.open(img_path)
 
# Prepara el objeto para dibujar
draw = ImageDraw.Draw(img)
 
# Intenta cargar una fuente, o usa una por defecto si no se especifica
try:
    font = ImageFont.truetype("arial.ttf", 24)  # Cambia el tamaño de fuente según necesites
except IOError:
    font = ImageFont.load_default()
 
# Tamaños para la cuadrícula
width, height = img.size
step_x = width / 36  # 36 líneas verticales para 360°
step_y = height / 18  # 18 líneas horizontales para 180°
 
# Centro de la imagen
center_x, center_y = width / 2, height / 2
 
# Dibuja líneas verticales y números
for i in range(-18, 19):  # Ajustado para centrar en 0,0
    x = center_x + (i * step_x)
    if x >= 0 and x <= width:
        draw.line((x, 0, x, height), fill="white")
        if i % 1 == 0 and i != 0:  # Cada 10 grados, excluyendo el centro
            draw.text((x, center_y), str(i * 10), fill="white", font=font)
 
# Dibuja líneas horizontales y números ajustados para el eje Y
for i in range(-9, 10):  # Ajustado para centrar en 0,0
    y = center_y - (i * step_y)  # Ajuste para que los valores positivos estén hacia arriba
    if y >= 0 and y <= height:
        draw.line((0, y, width, y), fill="white")
        # Ajuste de la colocación del texto para evitar superposición con las líneas
        text_y = y - 10 if i < 0 else y + 5
        if i % 1 == 0:  # Cada 10 grados
            text = str(i * 10)
            draw.text((center_x, text_y), text, fill="white", font=font)
 
# Guarda la imagen modificada
img.save('imagen_con_cuadricula_numerada_centro_ajustado_y.jpg')