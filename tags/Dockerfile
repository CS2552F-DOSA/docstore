FROM nodejs
ADD src /app
RUN npm install && grunt install
ADD settings.coffee /app/config/settings.coffee
USER node
