FROM mic92/sharelatex-nodejs
ADD src /app
RUN npm install && grunt install && npm install --save https://github.com/Mic92/metrics-sharelatex/archive/master.tar.gz
ADD settings.coffee /app/config/settings.coffee
VOLUME ["/data"]
RUN chown -R node /app/user_files /app/uploads /app/template_files
ADD filestore-init /etc/cont-init.d/02-filestore-init
