import json
import os

folder_path = "C:/Users/CRS/Desktop/JSON PUNE"

files = os.listdir(folder_path)
for file in files:
    with open(f"{folder_path}/{file}", 'r') as f:
        json_file = json.load(f)
        json_file['id'] = file.replace(r".json",r"")
        f.seek(0)
    with open(f"{folder_path}/{file}", "w") as file:
        json.dump(json_file, file, indent=2)