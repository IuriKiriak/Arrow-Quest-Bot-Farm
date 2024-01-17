import os
import subprocess
import cv2
import numpy as np
import time

# Функция для получения абсолютного пути к ADB
def get_adb_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    adb_path = os.path.join(script_dir, "adb", "adb")
    return adb_path

# Функция для получения скриншота напрямую в Python
def get_screenshot():
    adb_path = get_adb_path()
    result = subprocess.run([adb_path, "exec-out", "screencap", "-p"], stdout=subprocess.PIPE)
    image = np.asarray(bytearray(result.stdout), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

# Функция для симуляции клика на экране
def tap_screen(x, y):
    adb_path = get_adb_path()
    subprocess.run([adb_path, "shell", "input", "tap", str(x), str(y)])

# Функция поиска событий (шаблонов)
def find_events(screenshot, templates_folder):
    found_coordinates = []
    for template_name in os.listdir(templates_folder):
        template_path = os.path.join(templates_folder, template_name)
        template = cv2.imread(template_path)
        h, w = template.shape[:2]
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            center_coordinates = (pt[0] + w // 2, pt[1] + h // 2)
            found_coordinates.append(center_coordinates)
    return found_coordinates

# Главная функция

def main():
    while True:
        screenshot = get_screenshot()

        # Обработка шаблонов из папки 'quest'
        quest_events = find_events(screenshot, "quest")
        if quest_events:
            for x, y in quest_events:
                print("Найдено событие в 'quest' на позиции:", x, y)
                tap_screen(x, y)
                time.sleep(1)  # Задержка после каждого клика
                # Обработка шаблонов из папки 'template'
                template_events = find_events(screenshot, "template")
                if template_events:
                    for x, y in template_events:
                        print("Найдено событие в 'template' на позиции:", x, y)
                        tap_screen(x, y)
                        time.sleep(1)  # Задержка после каждого клика
                        break
                else:
                    print("В папке 'template' события не найдены")
                break
        else:
            print("ожидание выполнения задания")
        time.sleep(3)

main()