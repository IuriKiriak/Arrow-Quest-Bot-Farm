#свои библиотеки
from FunJson import *
from FunAdb import *
from Functional import *
import time

def main():
    start_time = int(time.time())
    while True:
        screenshot = get_screenshot()
        quest_events = find_events(screenshot, "./template/complite.png")
        if quest_events:
            for x, y in quest_events:
                end_time = int(time.time())
                print("complite in coordinate x: " + str(x) + " y:" + str(y) + " время ожидания:" + str(end_time - start_time))
                start_time = int(time.time())
                tap_screen(x,y)
                time.sleep(1)  # Задержка после каждого клика
        else:
            print("expect")

#
main()
