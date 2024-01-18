#свои библиотеки
from FunAdb import *
from Functional import *
from FunJson import *

import time

def main():
    start_time = int(time.time())
    array = create_array_from_json("MapData.json")
    while True:
        screenshot = get_screenshot()
        quest_events = find_events(screenshot, "template/Complite.png")
        if quest_events:
            for x, y in quest_events:
                end_time = int(time.time())
                print("complite in coordinate x: " + str(x) + " y:" + str(y) + " time:" + str(end_time - start_time))
                start_time = int(time.time())
                name = find_template(array, x, y)
                print("name task:",name)
                if name != None:
                    tap_screen(x, y)
                    time.sleep(1)
                    switch_case(name)
                break
        else:
            print("expect")
        time.sleep(1)

main()
