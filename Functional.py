from FunAdb import *

import cv2
import numpy as np
import time


def find_events(screenshot, template_path):
    # Загрузка шаблона изображения
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    if template is None:
        raise FileNotFoundError(f"Не удалось загрузить шаблон из {template_path}")

    # Получение размеров шаблона
    h, w = template.shape[:2]

    # Сравнение скриншота с шаблоном
    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.75
    loc = np.where(res >= threshold)

    found_coordinates = []
    for pt in zip(*loc[::-1]):
        center_coordinates = (pt[0] + w // 2, pt[1] + h // 2)
        found_coordinates.append(center_coordinates)

    return found_coordinates

def find_template(array, x, y):
    for i in range(0, len(array), 3):
        x_item, y_item = array[i], array[i + 1]
        if x_item < 0 or y_item < 0:  # Пропускаем координаты с отрицательными значениями
            continue
        if abs(x_item - x) <= 40 and abs(y_item - y) <= 40:
            return array[i + 2]
    return None

def switch_case(name):
    if name == "Quest":
        while True:
            screenshot = get_screenshot()
            quest_events = find_events(screenshot, "template/Claim.png")
            if quest_events:
                for x, y in quest_events:
                    tap_screen(x, y)
                    print("tap:", x,y)
                    time.sleep(1)
                    tap_screen(550, 2100)
                    print("tap", 550,2100)
                    time.sleep(1)
                    return 1
            else:
                print("Expect Quest")
    elif name == "Shop":
        while True:
            screenshot = get_screenshot()
            quest_events = find_events(screenshot, "template/Free.png")
            if quest_events:
                for x, y in quest_events:
                    tap_screen(x, y)
                    print("tap:", x,y)
                    time.sleep(1)
                    tap_screen(1020, 2230)
                    print("tap:", 1020,2230)
                    return 1
            else:
                print("Expect Shop Claim")

