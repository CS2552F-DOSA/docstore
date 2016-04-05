FROM mic92/sharelatex-base
RUN apt install -y redis-server && mkdir /data
VOLUME /data/
WORKDIR /data/
EXPOSE 6379
ADD entrypoint /entrypoint
ADD redis.conf /etc/redis.conf
ENTRYPOINT ["/entrypoint"]
CMD ["redis-server"]
