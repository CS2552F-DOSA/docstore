# Sharelatex for docker

```
$ git clone git@gitlab.com:Mic92/sharelatex-docker.git
$ git submodule update --init
```

- first deploy servers with ansible

- Get docker & docker-compose

```
  $ ansible-playbook --become -i /etc/ansible/hosts /etc/ansible/site.yml
  $ make build
  $ make upload # to registry deployed with ansible
  # seed database with test users
  $ docker exec -ti sharelatex_web_1 bash
  $ node app/js/seed.js
```

- Rancher

http://localhost:8080/env/1a5/api -> register api api key



```bash
docker exec -it container-id-of-docstore bash
```

Post(update)

```bash
curl -X POST -H 'Content-Type: application/json' -d '{"lines": [1234]}' http://localhost:3000/project/5620bece05509b0a7a3cbc61/doc/111122223330
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
```

Delete

```bash
curl -X DELETE http://localhost:3000/project/5620bece05509b0a7a3cbc61/doc/111122223330
```

