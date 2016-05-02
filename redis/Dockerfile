FROM mic92/sharelatex-base
RUN apt install -y redis-server && mkdir /data
VOLUME /data/
WORKDIR /data/
EXPOSE 6379
ADD redis.conf /etc/redis.conf
ADD redis-run /etc/services.d/redis/run
ADD redis-init /etc/cont-init.d/redis-db
ENTRYPOINT ["/init"]
CMD ["redis-server"]
