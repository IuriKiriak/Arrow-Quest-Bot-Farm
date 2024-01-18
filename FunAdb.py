import os
import subprocess
import cv2
import numpy as np

# Функция для получения абсолютного пути к adb
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

#функция сохранения скришота (нужна для отладки x/y)
def save_screenshot():
    image = get_screenshot()
    file_path = "screenshot.png"
    try:
        cv2.imwrite(file_path, image)
        print("screen save")
    except:
        print("screen not saved")


# Функция для симуляции клика на экране
def tap_screen(x, y):
    adb_path = get_adb_path()
    subprocess.run([adb_path, "shell", "input", "tap", str(x), str(y)])