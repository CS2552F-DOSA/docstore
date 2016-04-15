FROM nodejs
ADD src /app
RUN npm install --save git+https://github.com/Mic92/metrics-sharelatex.git && npm install && grunt install
RUN chown -R node /app/data && apt install zip unzip
ADD settings.coffee /app/config/settings.coffee
ADD entrypoint /entrypoint
ENTRYPOINT ["/entrypoint"]
