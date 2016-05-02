FROM mic92/sharelatex-nodejs
ADD src /app
ADD ./seed.coffee /app/app/coffee/
RUN npm install --save git+https://github.com/Mic92/metrics-sharelatex.git && \
    npm install && \
    grunt install && \
    chown -R node /app/data && \
    mkdir -p /app/data/{dumpFolder,logs,pdfs,uploads,zippedProjects} \
    apt install zip unzip
ADD settings.coffee /app/config/settings.coffee
