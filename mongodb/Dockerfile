FROM mic92/sharelatex-base

VOLUME /data/db
RUN apt install -y mongodb && \
    chown -R mongodb /data/db
EXPOSE 27017 28017
WORKDIR "/data"
ENTRYPOINT ["mongod"]
