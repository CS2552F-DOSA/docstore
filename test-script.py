import os
import json

test_prepare_content = False
PORT = "9999"

# prepare original_file and write to storage
if test_prepare_content:
    file = open("original_file", "w")
    file.write('{"lines": ["')
    for i in range(2):
        file.write("aabbcc11112222333344445555")

    file.write('"]}')
    file.close()
    os.system("curl -X POST -H 'Content-Type: application/json' -d '@original_file' http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")


# get original_file from storage

get_result = os.popen("curl http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")
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

os.system("curl -X POST -H 'Content-Type: application/json' -d " + request_str + " http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")


# check the file from storage

get_result = os.system("curl http://localhost:" + PORT + "/project/5620bece05509b0a7a3cbc61/doc/111122223330")

print(get_result)