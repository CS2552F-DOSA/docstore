FROM mic92/sharelatex-base
RUN apt install -y nginx-core
EXPOSE 80
ADD sharelatex /etc/nginx/sites-enabled/default
ADD nginx.conf /etc/nginx/nginx.conf
ENTRYPOINT ["nginx", "-c", "/etc/nginx/nginx.conf"]
