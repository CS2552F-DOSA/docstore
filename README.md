# Sharelatex for docker

- Get docker & docker-compose

```
  $ ansible-playbook --become -i /etc/ansible/hosts /etc/ansible/site.yml
  $ docker-compose up
  $ docker exec -ti sharelatex_web_1 grunt create-admin-user --email joerg@higgsboson.tk
  $ docker run -d -p 5000:5000 --restart=always --name registry -v /data/registry:/var/lib/registry registry:2
```

- Rancher

http://localhost:8080/env/1a5/api -> api key
