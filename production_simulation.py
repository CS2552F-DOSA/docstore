import os
import json
import time
import requests
import random

test_prepare_content = True
PORT = "9999"
project_url = "http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/"

headers = {'content-type': 'application/json'}


interval_min = 5 # 5 seconds
interval_max = 20 # 20 seconds

file_ids = ["111122223330", "111122223331", "111122223332", "111122223333", "111122223334"]


begin_with_large_file = False

test_numbers = 500
initial_file_lines = 5




# in order to fit the format of shell curl command, does not use the str() in python, uses custom function instead.
def list_to_str(l):
    ret = "["
    list_size = len(l)
    for i in range(list_size):
        ret += "\"" + str(l[i]) + "\""
        if i+1 != list_size:
            ret += ", "
    ret += "]"
    return ret

# prepare original_file and write to storage
if test_prepare_content:
    for fid in file_ids:
        file = open("original_file", "w")
        file.write('{"lines": ["')
        for i in range(2):
            file.write("")

        file.write('"]}')
        file.close()

        initial_content = '1234'
        if begin_with_large_file:
            for i in range(initial_file_lines):
                initial_content += ">>>> large file <<<<"
        
        request_param = {'lines': [initial_content]}
        
        current_url = project_url + fid
        ret = requests.post(current_url , json=request_param, headers=headers, timeout=10)


while True:
    file_index = random.randint(0, len(file_ids) - 1)
    cur_url = project_url + file_ids[file_index]
    print("file to be modified this round: ", file_ids[file_index])

    ret = requests.get(url=cur_url, timeout=10)    

    text = json.loads(ret.text)
    lines = text["lines"]

    # generate new file and write to storage
    lines.append(">>> newlines <<<")
    
    if len(lines) > 0 and random.randint(0, 2) == 0:
        del lines[random.randint(0, len(lines))]


    request_str = '{"lines": ' + list_to_str(lines) + '}'
    request_param = json.loads(request_str)

    ret = requests.post(cur_url, json=request_param, headers=headers, timeout=10)

    current_interval = random.randint(interval_min, interval_max)

    print("sleep for ", str(current_interval))

    os.system("sleep " + str(current_interval))