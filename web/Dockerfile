FROM mic92/sharelatex-nodejs
ADD src /app
RUN curl -L "https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz" \
      | tar -xz -C / && \
    apt install zip unzip
RUN npm install --save git+https://github.com/Mic92/metrics-sharelatex.git && npm install && grunt install && chown -R node /app/data
ADD settings.coffee /app/config/settings.coffee
ADD entrypoint /entrypoint
ADD web-run /etc/services.d/web/run
ENTRYPOINT ["/init"]
