FROM mic92/sharelatex-base

RUN curl -L "https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz" \
      | tar -xz -C / && \
    curl https://s3.amazonaws.com/get.influxdb.org/chronograf/chronograf_0.12.0_amd64.deb > /tmp/chronograf.deb && \
    dpkg -i /tmp/chronograf.deb
ADD config.toml /opt/chronograf/config.toml
ADD 02-chronograf-db /etc/fix-attrs.d/02-chronograf-db
ADD chronograf-run /etc/services.d/chronograf/run
VOLUME ["/data/chronograf"]
EXPOSE 10000
ENTRYPOINT ["/init"]
