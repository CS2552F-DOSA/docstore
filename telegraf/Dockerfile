FROM mic92/sharelatex-base

RUN apt update && apt install -y git-core build-essential && \
    curl -L "https://storage.googleapis.com/golang/go1.6.linux-amd64.tar.gz" | \
        tar -C /usr/local -xzf - && \
    mkdir -p /root/go/src/github.com/influxdata/ && \
    export GOPATH=/root/go PATH=/usr/local/go/bin:$PATH &&\
    git clone https://github.com/mic92/telegraf $GOPATH/src/github.com/influxdata/telegraf && \
    make -C $GOPATH/src/github.com/influxdata/telegraf && \
    cp "$GOPATH/bin/telegraf" /usr/local/bin && \
    rm -rf /usr/local/go "$GOPATH" && \
    curl -sL https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 > /usr/local/bin/jq && \
    chmod +x /usr/local/bin/jq && \
    mkdir /etc/telegraf.d
ADD telegraf.conf /etc/telegraf.conf
EXPOSE 8125
ADD telegraf-run /etc/services.d/telegraf/run
ADD update-host-list /etc/services.d/update-host-list/run
ENTRYPOINT ["/init"]
