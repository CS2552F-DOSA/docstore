import os
import json
import time

test_prepare_content = True
PORT = "9999"

test_numbers = 100


get_count = 0
get_time_cost = 0.0

post_count = 0
post_time_cost = 0.0

# prepare original_file and write to storage
if test_prepare_content:
    file = open("original_file", "w")
    file.write('{"lines": ["')
    for i in range(2):
        file.write("aabbcc11112222333344445555")

    file.write('"]}')
    file.close()
    os.system("curl -X POST -H 'Content-Type: application/json' -d '@original_file' http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")


for i in range(test_numbers):
    # get previous_file from storage
    start_time = time.time()
    get_result = os.popen("curl http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")
    get_time_cost += time.time() - start_time
    get_count += 1

    output = get_result.read()
    print("|" + output + "|")
    print(type(output))


    print("-------------------")

    json_result = json.loads(output)

    lines = json_result["lines"]

    print(lines)





    # generate new file and write to storage
    lines.append(">>> newlines <<<")


    print(lines)

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



    request_str = '\'{"lines": ' + list_to_str(lines) + '}\''

    print(request_str)


    new_request = "curl -X POST -H 'Content-Type: application/json' -d " + request_str + " http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330"

    print("\n" + new_request + "\n")

    start_time = time.time()
    os.system("curl -X POST -H 'Content-Type: application/json' -d " + request_str + " http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")
    post_time_cost += time.time() - start_time
    post_count += 1


    # check the file from storage
    start_time = time.time()
    get_result = os.system("curl http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")
    get_time_cost += time.time() - start_time
    get_count += 1

    print(get_result)


# compute time cost
print("\n\n\n\n")
print("**************************************************************************************************")
print("GET avg time: ", get_time_cost / get_count)
print("POST avg time: ", post_time_cost / post_count)