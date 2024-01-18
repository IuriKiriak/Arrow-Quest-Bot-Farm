import json
FileName = "MapData.json"

def read_json_file(FileName, name_filter):
    with open(FileName, "r", encoding="utf-8") as file:
        data = json.load(file)
        filtered_data = [item for item in data if item["name"] == name_filter]
        print("file read")
    return filtered_data

def write_json_file(FileName, data):
    with open(FileName, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print("file written")

def Variable(FileName):
    data = read_json_file()
    for item in data:
        name = item["name"]
        x = item["coordinate"]["x"]
        y = item["coordinate"]["y"]
        time = item["time"]
        print("Var save:\n name:" + name + "X:" + x + "Y:" + y + "Time:" + time)

def New_Veriable(FileName, new_data):
    data = read_json_file(FileName)
    data.append(new_data)
    write_json_file(FileName, data)


def create_array_from_json(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    array = []
    for item in data:
        array.extend([item["coordinate"]["x"], item["coordinate"]["y"], item["name"]])

    return array