FROM nodejs
ADD src /app
RUN npm install && \
    npm rebuild && \
    grunt install && \
    chown -R node /app/data && \
    apt install zip unzip
ADD settings.coffee /app/config/settings.coffee
ADD entrypoint /entrypoint
ENTRYPOINT ["/entrypoint"]
