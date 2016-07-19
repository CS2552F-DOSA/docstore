FROM mic92/sharelatex-nodejs
ADD src /app
ADD src-overlay /app/app/coffee/
RUN npm install && \
    grunt install && \
    npm install --save git+https://github.com/Mic92/metrics-sharelatex.git && \
    chown -R node /app/data && \
    mkdir -p /app/data/{dumpFolder,logs,pdfs,uploads,zippedProjects} \
    apt install zip unzip

ADD settings.coffee /app/config/settings.coffee
ADD seed-db /etc/cont-init.d/seed-db
