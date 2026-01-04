import os
import json

def append_json_line(base_path, date_str, filename, payload):
    directory = os.path.join(base_path, date_str)
    os.makedirs(directory, exist_ok=True)
    
    file_path = os.path.join(directory, filename)
    
    with open(file_path, "a") as f:
        f.write(json.dumps(payload) + "\n")