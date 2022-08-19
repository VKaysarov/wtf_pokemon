import os
from PIL import Image, ImageDraw # Подключим необходимые библиотеки. 

for filename in os.listdir("pokemons"):
# filename = "084_2.png"
	image = Image.open("pokemons/" + filename) # Открываем изображение.
	width = image.size[0] # Определяем ширину. 
	height = image.size[1] # Определяем высоту. 	

	for i in range(width):
		for j in range(height):
			color = image.getpixel((i, j))

			r = color[0]
			g = color[1]
			b = color[2]
			a = color[3]
			# if r == 0 and g == 0 and b == 0 and a == 0:
			# 	image.putpixel((i, j), (255, 255, 255))
			# else: 
			# 	image.putpixel((i, j), (0, 0, 0))
			if a == 0:
				image.putpixel((i, j), (255, 255, 255))
			else: 
				image.putpixel((i, j), (0, 0, 0))

	image.save("new_pokemons/" + filename)
	



