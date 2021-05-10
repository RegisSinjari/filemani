import json
import os

folder_path = "D:/old_but_gold/pbjson"

files = os.listdir(folder_path)
for file in files:
    with open(f"{folder_path}/{file}", 'r') as f:
        json_file = json.load(f)
        a=file.replace(r".json",r"")
        b=a
        c=b[:8]+'-'
        d=b[8:12]+'-'
        e=b[12:16]+'-'
        fd=b[16:20]+'-'
        g=b[20:]
        json_file['Id'] = c+d+e+fd+g
        f.seek(0)
    with open(f"{folder_path}/{file}", "w") as file:
        json.dump(json_file, file, indent=2)

