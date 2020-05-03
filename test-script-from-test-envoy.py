import os
import json
import time
import requests

test_prepare_content = True
PORT = "9999"
post_url = "http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330"
get_url = "http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330"
headers = {'content-type': 'application/json', 'fid_timestamp_unix_ns': '10'}


begin_with_large_file = False

test_numbers = 500
initial_file_lines = 100000


def request_get(url, param):
    fails = 0
    text = ""
    while True:
        try:
            if fails >= 20:
                break
 
            ret = requests.get(url=url, params=param, timeout=10)
 
            if ret.status_code == 200:
                text = json.loads(ret.text)
            else:
                continue
        except:
            fails += 1
            print('fails: ', fails)
        else:
            break
    return text
 
def request_post(url, param):
    # print("request_post")
    fails = 0
    text = ""

    while True:
        try:
            if fails >= 20:
                break

 
            headers = {'content-type': 'application/json'}
            ret = requests.post(url, json=param, headers=headers, timeout=10)

            text = json.loads(ret.text)

 
            if ret.status_code == 200:
                text = json.loads(ret.text)
            else:
                continue
        except:
            fails += 1
            print('fails: ', fails)
        else:
            break
    return text


get_count = 0
get_time_cost = 0.0

post_count = 0
post_time_cost = 0.0

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
    file = open("original_file", "w")
    file.write('{"lines": ["')
    for i in range(2):
        file.write("")

    file.write('"]}')
    file.close()
    # os.system("curl -X POST -H 'Content-Type: application/json' -d '@original_file' http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")

    initial_content = '1234'
    if begin_with_large_file:
        for i in range(initial_file_lines):
            initial_content += ">>>> large file <<<<"
    
    request_param = {'lines': [initial_content]}
    
    # ret = requests.post(post_url, json=request_param)

    ret = requests.post(post_url, json=request_param, headers=headers, timeout=10)
    # print("ret ", ret.status_code)




for i in range(test_numbers):
    if i % 50 == 0:
        print("\n\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> test round: ", i + 1, ", total round ", test_numbers)
    # get previous_file from storage
    start_time = time.time()
    # get_result = os.popen("curl http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")
    ret = requests.get(url=get_url, timeout=10)    
    get_time_cost += time.time() - start_time
    get_count += 1

    # output = get_result.read()
    # print("|" + output + "|")
    # print(type(output))
    # print("-------------------")

    # print(output)
    # json_result = json.loads(output)
    text = json.loads(ret.text)
    lines = text["lines"]
    # print(lines)

    # generate new file and write to storage
    lines.append(">>> newlines <<<")
    # print(lines)

    request_str = '{"lines": ' + list_to_str(lines) + '}'

    # print(request_str)

    # new_request = "curl -X POST -H 'Content-Type: application/json' -d " + request_str + " http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330"

    # print("\n" + new_request + "\n")
    request_param = json.loads(request_str)
    start_time = time.time()
    # _ = os.popen("curl -X POST -H 'Content-Type: application/json' -d " + request_str + " http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")
    ret = requests.post(post_url, json=request_param, headers=headers, timeout=10)
    # print("ret ", ret.status_code)
    post_time_cost += time.time() - start_time
    post_count += 1

    # # check the file from storage
    # start_time = time.time()
    # get_result = os.popen("curl http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")
    # get_time_cost += time.time() - start_time
    # get_count += 1

    # print(get_result)


# compute time cost
os.system("sleep 1")
if test_numbers > 0:
    print("\n\n\n\n")
    print("**************************************************************************************************")
    print("total round: ", test_numbers)
    print("GET avg time: ", get_time_cost / get_count)
    print("POST avg time: ", post_time_cost / post_count)
    print("**************************************************************************************************")