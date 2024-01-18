import cv2
import numpy as np


def find_events(screenshot, template_path):
    # Загрузка шаблона изображения
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    if template is None:
        raise FileNotFoundError(f"Не удалось загрузить шаблон из {template_path}")

    # Получение размеров шаблона
    h, w = template.shape[:2]

    # Сравнение скриншота с шаблоном
    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
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

