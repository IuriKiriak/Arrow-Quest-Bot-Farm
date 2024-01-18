import json
FileName = "MapData.json"

def Read_Json_File(FileName, name_filter):
    with open(FileName, "r", encoding="utf-8") as file:
        data = json.load(file)
        filtered_data = [item for item in data if item["name"] == name_filter]
        print("file read")
    return filtered_data

def Write_Json_File(FileName, data):
    with open(FileName, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print("file written")

def Variable(FileName):
    data = Read_Json_File()
    for item in data:
        name = item["name"]
        x = item["coordinate"]["x"]
        y = item["coordinate"]["y"]
        time = item["time"]
        print("Var save:\n name:" + name + "X:" + x + "Y:" + y + "Time:" + time)

def New_Veriable(FileName, new_data):
    data = Read_Json_File(FileName)
    data.append(new_data)
    Write_Json_File(FileName, data)