FROM mic92/sharelatex-nodejs
ADD src /app
RUN npm install && grunt install && npm install --save https://github.com/Mic92/metrics-sharelatex/archive/master.tar.gz
ADD settings.coffee /app/config/settings.coffee
