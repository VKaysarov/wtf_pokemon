import os
import cv2
import keyboard
import const_wtf
import time

from PIL import Image, ImageGrab


def screen():
    # screen = ImageGrab.grab((604, 279, 804, 479))  # grab(x1, y1, x2, y2) 1600 900
    screen = ImageGrab.grab((764, 369, 964, 569)) # grab(x1, y1, x2, y2) 1920 1080
    screen.save(sreen_name, 'PNG')

# Функция вычисления хэша
def CalcImageHash(FileName):
    image = cv2.imread(FileName) # Прочитаем картинку
    resized = cv2.resize(image, (8,8), interpolation = cv2.INTER_AREA) # Уменьшим картинку
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) # Переведем в черно-белый формат
    avg = gray_image.mean() # Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0) # Бинаризация по порогу
    
    # Рассчитаем хэш
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"
            
    return _hash
 
def CompareHash(hash1, hash2):
    l = len(hash1)
    i = 0
    count = 0
    while i < l:
        if hash1[i] != hash2[i]:
            count = count + 1
        i = i + 1
    return count

sreen_name = 'screen.png'

# Убираем синие полосы на фоне
def imageGray():
    image = Image.open(sreen_name) # Открываем изображение.
    width = image.size[0] # Определяем ширину. 
    height = image.size[1] # Определяем высоту.  

    for i in range(width):
        for j in range(height):
            color = image.getpixel((i, j))

            r = color[0]
            g = color[1]
            b = color[2]
            # a = color[3]
            if r == 0 and g == 0 and b == 0:
              image.putpixel((i, j), (0, 0, 0))
            else: 
              image.putpixel((i, j), (255, 255, 255))
                
    image.save(sreen_name)

# ====================================== Сравниваем изображения ======================================

def wtf_pokemon():
    img_dir = "pokemons_v3/"
    pokemon_list = const_wtf.pokemon_list
    hash1 = CalcImageHash(sreen_name)

    for filename in os.listdir(img_dir):
        name_img = img_dir + filename
        hash2 = CalcImageHash(name_img)
        result = CompareHash(hash1, hash2)

        if result < 2:
            print(pokemon_list[filename] + " - " + str(result))

def main():
    start_time = time.time()
    print("===========Script Start===========")
    screen()
    imageGray()
    wtf_pokemon()
    print("===========Script End===========")
    print("\n")
    end_time = time.time()
    print(f"It took {end_time-start_time:.2f} seconds to compute")

keyboard.add_hotkey('O', main)
keyboard.wait('Ctrl + Q') # Exit script
    

# Before
# 2.72, 4.27, 3.52, 2.42, 4.09, 2.49, 3.41, 4.78, 3.13, 4.29 | min - 2.42, max - 4.78

# After
# ...