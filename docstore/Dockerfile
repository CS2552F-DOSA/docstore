FROM mic92/sharelatex-nodejs
ADD src /app
RUN npm install --save git+https://github.com/Mic92/metrics-sharelatex.git && npm install && grunt install
ADD settings.coffee /app/config/settings.coffee
USER node
