import os
import json
import time
import requests
import random
import string

file_size = "large"  # "middle", "small", "large"
modification_ratio = 0.01
str_len = 10


test_prepare_content = True  # should always be true.
PORT = "9999"
post_url = "http://localhost:" + PORT + \
    "/project/5620bece05509b0a7a3cbc61/doc/111122223337"
get_url = "http://localhost:" + PORT + \
    "/project/5620bece05509b0a7a3cbc61/doc/111122223337"
headers = {'content-type': 'application/json', 'fid_timestamp_unix_ns': '10'}
begin_with_large_file = True


test_numbers = 100
initial_file_lines = 0
if file_size == "large":
    initial_file_lines = 1000
elif file_size == "middle":
    initial_file_lines = 100
else:
    initial_file_lines = 10
# 100, 10000, 100000


def randStr(str_len):
    return ''.join(random.sample(
        string.ascii_letters + string.digits, str_len))


def modify_str_list(str_list):
    modification_num = max(1, modification_ratio * initial_file_lines)
    modifidied_num = 0
    list_len = len(str_list)
    while modifidied_num < modification_num:
        for i in range(list_len):
            if random.random() < modification_ratio:
                modifidied_num += 1
                newline = randStr(str_len)
                while newline == str_list[i]:
                    newline = randStr(str_len)
                str_list[i] = newline
    return str_list


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

            headers = {'content-type': 'application/json',
                       'fid_timestamp_unix_ns': '10'}
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


# in order to fit the format of shell curl command, does not use the str() in python, uses custom function instead.


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


equivalence_data_rate = []
delta_data_rate = []
avg_wall_time_post = []
avg_wall_time_get = []
success_ratios = []

# [1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
for between_interval in [1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]:
    os.system("sleep 0.02")
    print(between_interval)
    get_count = 0
    get_time_cost = 0.0

    post_count = 0
    post_time_cost = 0.0
    total_file_size = 0.0

    successed_post_get_total_cost = 0.0
    post_err_count = 0.0
    # prepare original_file and write to storage
    lines = []
    for i in range(initial_file_lines):
        lines.append(randStr(str_len))
    if test_prepare_content:
        file = open("original_file", "w")
        file.write('{"lines": ["')
        for i in range(1):
            file.write("")

        file.write('"]}')
        file.close()
        os.system("curl -X POST -H 'Content-Type: application/json' -H 'fid_timestamp_unix_ns: 10' -d '@original_file' http://localhost:" +
                  PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223337")

        # initial_content = '1234'
        # if begin_with_large_file:
        #     for i in range(initial_file_lines):
        #         initial_content += "1234"

        # request_param = {'lines': [initial_content]}

        # print(lines)
        request_str = '{"lines": ' + list_to_str(lines) + '}'
        # request_param = '\'{"lines": ' + list_to_str(lines) + '}\''
        request_param = json.loads(request_str)

        # os.system("curl -X POST -H 'Content-Type: application/json' -H 'fid_timestamp_unix_ns: 10' -d \'{\"lines\": [\"1234\"]}' http://localhost:" +
        #   PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223337")

        ret = requests.post(post_url, json=request_param,
                            headers=headers, timeout=10)
        # print("ret ", ret.status_code)
        os.system("sleep 1")

    for i in range(test_numbers):
        # # os.system("sleep 0.5")
        # if i % 50 == 0:
        #     print("\n\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> test round: ",
        #           i + 1, ", total round ", test_numbers)
        # get previous_file from storage
        start_time = time.time()
        # get_result = os.popen("curl http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")
        ret = requests.get(url=get_url, timeout=10)
        cur_get_time_cost = time.time() - start_time
        get_time_cost += cur_get_time_cost
        get_count += 1

        # output = get_result.read()
        # print("|" + output + "|")
        # print(type(output))
        # print("-------------------")

        # print(output)
        # json_result = json.loads(output)
        try:
            # print(ret.text)
            # text = json.loads(ret.text)
            # lines = text["lines"]

            print("between_interval: ", between_interval, " ", len(lines), "\n")

            # generate new file and write to storage
            # lines.append("9999")
            lines = modify_str_list(lines)
            # print(lines)

            request_str = '{"lines": ' + list_to_str(lines) + '}'

            # print(request_str)

            # new_request = "curl -X POST -H 'Content-Type: application/json' -d " + request_str + " http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330"

            # print("\n" + new_request + "\n")
            request_param = json.loads(request_str)
            start_time = time.time()
            # _ = os.popen("curl -X POST -H 'Content-Type: application/json' -d " + request_str + " http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")
            ret = requests.post(post_url, json=request_param,
                                headers=headers, timeout=10)
            # print("ret ", ret.status_code)
            cur_post_time_cost = time.time() - start_time
            post_time_cost += cur_post_time_cost
            post_count += 1

            successed_post_get_total_cost += cur_get_time_cost + cur_post_time_cost

            # # check the file from storage
            # start_time = time.time()
            # get_result = os.popen("curl http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")
            # get_time_cost += time.time() - start_time
            # get_count += 1

            # print(get_result)
        except:  # KeyError, VauleError
            post_err_count += 1

            # compute time cost

    if test_numbers > 0:

        equivalence_data_rate.append((11.0 * initial_file_lines * test_numbers) / (
            successed_post_get_total_cost + between_interval * test_numbers))

        delta_data_rate.append((11.0 * 2 * initial_file_lines * modification_ratio *
                                test_numbers) / (successed_post_get_total_cost + between_interval * test_numbers))

        avg_wall_time_post.append(post_time_cost / post_count)
        avg_wall_time_get.append(get_time_cost / get_count)
        success_ratios.append((test_numbers -
                               post_err_count) * 1.0 / test_numbers)


print("\n\n\n\n")
print("**************************************************************************************************")
print("equivalence_data_rate: ", equivalence_data_rate, "\n")
print("delta_data_rate: ", delta_data_rate, "\n")
print("avg_wall_time_post: ", avg_wall_time_post, "\n")
print("avg_wall_time_get: ", avg_wall_time_get, "\n")
print("success_ratios: ", success_ratios, "\n")


print("**************************************************************************************************")
