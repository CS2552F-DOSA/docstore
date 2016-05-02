FROM mic92/sharelatex-base

RUN apt install -y nodejs-legacy git-core python make npm && \
    useradd -d /app -m node && \
    npm install -g grunt-cli
WORKDIR "/app"
ENV SHARELATEX_CONFIG=/app/config/settings.coffee
EXPOSE 3000
ADD node-run /etc/services.d/node/run
ENTRYPOINT ["/init"]
