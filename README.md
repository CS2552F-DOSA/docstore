# Sharelatex for docker

Post(update)

```bash
curl -X POST -H 'Content-Type: application/json' -d '{"lines": ["1234"]}' http://localhost:3000/project/5620bece05509b0a7a3cbc61/doc/111122223330
# 5620bece05509b0a7a3cbc61 is project id
# 111122223333 is the doc id
# 1234 is the content to be posted

curl -X POST -H 'Content-Type: application/json' -d '@original_file' http://localhost:3000/project/5620bece05509b0a7a3cbc61/doc/111122223330



curl -X POST -H 'Content-Type: application/json' -d '{"lines": ["1234"]}' http://localhost:9999/project/5620bece05509b0a7a3cbc61/doc/111122223330
# 5620bece05509b0a7a3cbc61 is project id
# 111122223333 is the doc id
# 1234 is the content to be posted
```

Put (not support here)

```bash
curl -v -X PUT -d '{"lines": [1234]}' http://localhost:3000/project/5620bece05509b0a7a3cbc61/doc/111122223330
```

Get

```bash
curl -v http://localhost:3000/project/5620bece05509b0a7a3cbc61/doc/111122223330

curl -v http://localhost:9999/project/5620bece05509b0a7a3cbc61/doc/111122223330
```

Delete

```bash
curl -X DELETE http://localhost:3000/project/5620bece05509b0a7a3cbc61/doc/111122223330
```

test with script

```bash
# inside the envoy container
apt update && apt install curl vim -y python3-pip && pip3 install --upgrade requests

python3 test-script.py
```

![Screen Shot 2020-04-26 at 18.38.30](img/Screen%20Shot%202020-04-26%20at%2018.38.30.png)
