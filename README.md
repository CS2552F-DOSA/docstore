# Sharelatex for docker

- first deploy servers with ansible

- Get docker & docker-compose

```
  $ ansible-playbook --become -i /etc/ansible/hosts /etc/ansible/site.yml
  $ make build
  $ make upload # to registry deployed with ansible
  $ docker exec -ti sharelatex_web_1 grunt create-admin-user --email joerg@higgsboson.tk
```

- Rancher

http://localhost:8080/env/1a5/api -> api key
