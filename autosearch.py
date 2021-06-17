import time
import numpy as np
import pytesseract
from PIL import Image
import pyscreenshot as GrabImage
import cv2
import os
import pyautogui as pg

def CalcImageHash(img1):
    image = cv2.imread(img1)
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    avg = gray_image.mean()
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)

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
pg.moveTo(441, 488)
pg.click(441, 488)
time.sleep (2)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
filename1 = 'Image1.png'
filename1accept = 'Image1accept.png'
filename1acceptnew = 'Image1acceptnew.png'
filename1accepttime = 'Image1accepttime.png'
acceptone1 = 'Image1acceptone.png'
acceptone2 = 'Image3acceptone.png'
filename1right = 'Image1right.png'
filename2accright = 'Image1rightacc.png'
filename1yach1 = 'Image1yach1.png'
filename1yach2 = 'Image1yach2.png'
filename1nepr1 = 'Image1nepr1.png'
filename1nepr2 = 'Image1nepr2.png'
filename1search = 'Image1search.png'
filename1raccept = 'Image1raccept.png'
filename1racceptnew = 'Image1racceptnew.png'
last_time = time.time()
swap = 0
print("hello")
index2 = 1
swaptime = 0
cicl = 0
pg.moveTo(2300, 47)
pg.click(2300, 47)
pg.moveTo(2040, 1011)
pg.click(2040, 1011)

#Поиск времени
while(cicl == 0):
    swaptime = 0
    Left = -1
    screen1 = np.array(GrabImage.grab(bbox=(474, 33, 510, 50))) #Загрузка проверки на 0:50
    last_time = time.time()
    cv2.imwrite(filename1,screen1)
    img1 = cv2.imread('Image1.png')
    text = pytesseract.image_to_string(img1)
    index1 = text.find("00:50")
    index11 = text.find("00:51")
    index111 = text.find("00:52")
    screen1accept = np.array(GrabImage.grab(bbox=(260, 280, 381, 321))) #Загрузка принятия(без времени)
    cv2.imwrite(filename1accept, screen1accept)
    img2acc = cv2.imread('Image1accept.png')
    hash1accept = CalcImageHash("Image1accept.png")  # Присваивается Хэш фотки
    hash2accept = CalcImageHash("Image2accept.png")
    screen1acceptnew = np.array(GrabImage.grab(bbox=(260, 280, 381, 321)))  # Загрузка принятия(без времени)
    cv2.imwrite(filename1acceptnew, screen1acceptnew)
    img2accnew = cv2.imread('Image1acceptnew.png')
    hash1acceptnew = CalcImageHash("Image1acceptnew.png")
    hash2acceptnew = CalcImageHash("Image2acceptnew.png")

    screen1raccept = np.array(GrabImage.grab(bbox=(2182, 279, 2299, 316))) #Загрузка принятия(без времени)
    cv2.imwrite(filename1raccept, screen1raccept)
    rimg2acc = cv2.imread('Image1raccept.png')
    hash1raccept = CalcImageHash("Image1raccept.png")  # Присваивается Хэш фотки
    hash2raccept = CalcImageHash("Image2raccept.png")
    screen1racceptnew = np.array(GrabImage.grab(bbox=(2182, 279, 2299, 316)))  # Загрузка принятия(без времени)
    cv2.imwrite(filename1racceptnew, screen1racceptnew)
    rimg2accnew = cv2.imread('Image1racceptnew.png')
    hash1racceptnew = CalcImageHash("Image1racceptnew.png")
    hash2racceptnew = CalcImageHash("Image2racceptnew.png")
    screen1search = np.array(GrabImage.grab(bbox=(601, 37, 640, 58)))
    cv2.imwrite(filename1search, screen1search)
    img1search = cv2.imread('Image1search.png')
    text2 = pytesseract.image_to_string(img1search)
    index6 = text2.find("00:50")
    index66 = text2.find("00:51")
    index666 = text2.find("00:52")
    screen1nepr1 = np.array(GrabImage.grab(bbox=(483, 33, 636, 56)))
    cv2.imwrite(filename1nepr1, screen1nepr1)
    img1nepr1 = cv2.imread('Image1nepr1.png')
    hash1nepr1 = CalcImageHash("Image1nepr1.png")
    hash2nepr1 = CalcImageHash("Image2nepr1.png")
    screen1nepr2 = np.array(GrabImage.grab(bbox=(601, 37, 640, 58)))
    cv2.imwrite(filename1nepr2, screen1nepr2)
    img1nepr2 = cv2.imread('Image1nepr2.png')
    hash1nepr2 = CalcImageHash("Image1nepr2.png")
    hash2nepr2 = CalcImageHash("Image2nepr2.png")
    if hash1nepr1 == hash2nepr1 or hash1nepr2 == hash2nepr2:
        screen1right = np.array(GrabImage.grab(bbox=(2342, 477, 2497, 500)))
        cv2.imwrite(filename1right, screen1right)
        img1right = cv2.imread('Image1right.png')
        text = pytesseract.image_to_string(img1right)
        index5 = text.find("OTMEHA")
        if index5 == -1:
            print('Не найдено2')
        else:
            print('Найдено2')
            time.sleep(3)
            pg.moveTo(2300, 47)
            pg.click(2300, 47)
            pg.moveTo(2419, 487)
            pg.click(2419, 487)
            pg.moveTo(2310, 43)
            pg.moveTo(2040, 1011)
            pg.click(2040, 1011)
        print("Ждем")
        screen1right = np.array(GrabImage.grab(bbox=(2342, 477, 2497, 500)))
        cv2.imwrite(filename1right, screen1right)
        img1right = cv2.imread('Image1right.png')
        text = pytesseract.image_to_string(img1right)
        indexot = text.find("OTMEHA")
        if indexot == -1:
            print('Не найдено2')
        else:
            print('Найдено2')
            pg.moveTo(2300, 47)
            pg.click(2300, 47)
            pg.moveTo(2419, 487)
            pg.click(2419, 487)
            pg.moveTo(2310, 43)
            pg.moveTo(2040, 1011)
            pg.click(2040, 1011)
        time.sleep(61)
        pg.moveTo(441, 488)
        pg.click(441, 488)
        pg.moveTo(2040, 1011)
        pg.click(2040, 1011)
        swap = 0
    Skip = -1
    Left = 1
    coin = 0
    index3 = -1
    if hash1accept == hash2accept or hash1acceptnew == hash2acceptnew:
        index2 = 0
        print("Accept")
        screenacceptone = np.array(GrabImage.grab(bbox=(310, 334, 333, 348)))  # Загрузка проверки accepttime
        cv2.imwrite(acceptone1, screenacceptone)
        img1accone = cv2.imread('Image1acceptone.png')
        hash1acceptone = CalcImageHash("Image1acceptone.png")  # Присваивается Хэш фотки
        hash2acceptone = CalcImageHash("Image2acceptone.png")
        screen2acceptone = np.array(GrabImage.grab(bbox=(310, 334, 333, 348)))  # Загрузка проверки accepttime
        cv2.imwrite(acceptone2, screen2acceptone)
        img2accone = cv2.imread('Image3acceptone.png')
        hash3acceptone = CalcImageHash("Image3acceptone.png")  # Присваивается Хэш фотки
        hash4acceptone = CalcImageHash("Image4acceptone.png")

        if hash1acceptone == hash2acceptone or hash3acceptone == hash4acceptone:
            print("Нажать отмена")
            Skip = 0
            index2 = 0
            #Проверка на свою катку
        screen2accright = np.array(GrabImage.grab(bbox=(2227, 330, 2254, 348)))
        cv2.imwrite(filename2accright, screen2accright)
        img2rightaccept = cv2.imread('Image1rightacc.png')
        hash1rightacc = CalcImageHash("Image1rightacc.png")  # Присваивается Хэш фотки
        hash2rightacc = CalcImageHash("Image2rightacc.png")
        if hash1accept == hash2accept and hash1raccept == hash2raccept or hash1acceptnew == hash2acceptnew and hash1raccept == hash2raccept or hash1accept == hash2accept and hash1racceptnew == hash2racceptnew or hash1acceptnew == hash2acceptnew and hash1racceptnew == hash2racceptnew:
        #if hash1rightacc == hash2rightacc and:
            print("ПРИНЯТЬ 2 стороны")
            time.sleep(0.5)
            pg.moveTo(316, 300)
            pg.click(316, 300)
            time.sleep(0.5)
            pg.moveTo(2241, 299)
            pg.click(2241, 299)
            pg.moveTo(2310, 43)
            time.sleep(4)
            pg.moveTo(2040, 1011)
            pg.click(2040, 1011)
            #1 принятие проверяется
            screen1yach1 = np.array(GrabImage.grab(bbox=(173, 284, 306, 320)))
            cv2.imwrite(filename1yach1, screen1yach1)
            imgyach1 = cv2.imread('Image1yach1.png')
            hash1yach1 = CalcImageHash("Image1yach1.png")  # Присваивается Хэш фотки
            hash2yach1 = CalcImageHash("Image2yach1.png")
            screen1yach2 = np.array(GrabImage.grab(bbox=(2090, 286, 2246, 322)))
            cv2.imwrite(filename1yach2, screen1yach2)
            imgyach2 = cv2.imread('Image1yach1.png')
            hash1yach2 = CalcImageHash("Image1yach2.png")  # Присваивается Хэш фотки
            hash2yach2 = CalcImageHash("Image2yach2.png")
            if hash1yach1 == hash2yach1 and hash1yach2 == hash2yach2:
                print("ПРИНЯТЬ ВСЕ ОКНА")
                sleep = 0.3
                time.sleep(sleep)
                pg.moveTo(325, 781)
                time.sleep(sleep)
                pg.click(325, 781)
                time.sleep(sleep)
                pg.moveTo(333, 1258)
                time.sleep(sleep)
                pg.click(333, 1258)
                time.sleep(sleep)
                pg.moveTo(962, 1261)
                time.sleep(sleep)
                pg.click(962, 1261)
                time.sleep(sleep)
                pg.moveTo(960, 780)
                time.sleep(sleep)
                pg.click(960, 780)
                time.sleep(sleep)
                pg.moveTo(1600, 780)
                time.sleep(sleep)
                pg.click(1600, 780)
                time.sleep(sleep)
                pg.moveTo(1600, 1260)
                time.sleep(sleep)
                pg.click(1600, 1260)
                time.sleep(sleep)
                pg.moveTo(2244, 1260)
                time.sleep(sleep)
                pg.click(2244, 1260)
                time.sleep(sleep)
                pg.moveTo(2244, 779)
                time.sleep(sleep)
                pg.click(2244, 779)
                time.sleep(sleep)
                break
    if index2 == 0:
        screen1accepttime = np.array(GrabImage.grab(bbox=(310, 334, 333, 348)))  # Загрузка проверки accepttime
        cv2.imwrite(filename1accepttime, screen1accepttime)
        img3acctime = cv2.imread('Image1accepttime.png')
        hash1accepttime = CalcImageHash("Image1accepttime.png")  # Присваивается Хэш фотки
        hash2accepttime = CalcImageHash("Image2accepttime.png")
        if hash1accepttime == hash2accepttime:
            print("Нашло тайм")
            index3 = 0
    if coin == 0:
        if index1 == 0 or index11 == 0 or index111 == 0 or index6 == 0 or index66 == 0 or index666 == 0:
            index1 = 0
            index11 = 0
            index111 = 0
            index6 = 0
            index66 = 0
            index666 = 0
            print('Найдено1')
            swap = 1
            coin = 1
            swaptime = 1
        else:
            print('Не найдено1')
            #break
            #cv2.destroyAllWindows()
    if coin == 1 and index3 == 0 or coin == 1 and index2 == -1 or swap == 1 and index3 == 0 or swaptime == 1:
        print ('Нажмем на другой стороне')
        Left = 0
    if Skip == 0:
        screen1right = np.array(GrabImage.grab(bbox=(2342, 477, 2497, 500)))
        cv2.imwrite(filename1right, screen1right)
        img1right = cv2.imread('Image1right.png')
        text = pytesseract.image_to_string(img1right)
        index4 = text.find("OTMEHA")
        if index4 == -1:
            print('Не найдено2')
        else:
            print('Найдено2')
            pg.moveTo(2300, 47)
            pg.click(2300, 47)
            pg.moveTo(2419, 487)
            pg.click(2419, 487)
            pg.moveTo(2310, 43)
            pg.moveTo(2040, 1011)
            pg.click(2040, 1011)
    if  Left == 0:
        screen1right = np.array(GrabImage.grab(bbox=(2342, 477, 2497, 500)))
        cv2.imwrite(filename1right, screen1right)
        img1right = cv2.imread('Image1right.png')
        text = pytesseract.image_to_string(img1right)
        index4 = text.find("OTMEHA")
        if index4 == -1:
            print('Не найдено2')
            pg.moveTo(2300, 47)
            pg.click(2300, 47)
            pg.moveTo(2419, 487)
            pg.click(2419, 487)
            pg.moveTo(2310, 43)
            pg.moveTo(2040, 1011)
            pg.click(2040, 1011)
        else:
            print('Найдено2')
        pg.moveTo(2300, 47)
        pg.click(2300, 47)
        pg.moveTo(2040, 1011)
        pg.click(2040, 1011)
