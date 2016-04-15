FROM mic92/sharelatex-base

RUN apt install -y git-core && \
    curl -L "https://storage.googleapis.com/golang/go1.6.linux-amd64.tar.gz" | \
      tar -C /usr/local -xzf - && \
    mkdir /root/go && \
    export GOPATH=/root/go &&\
    /usr/local/go/bin/go get github.com/influxdata/kapacitor/cmd/kapacitor \
                       github.com/influxdata/kapacitor/cmd/kapacitord && \
    cp "$GOPATH/bin/kapacitor" "$GOPATH/bin/kapacitord" /usr/local/bin && \
    rm -rf /usr/local/go "$GOPATH" && \
    apt remove -y git-core
ADD kapacitor.conf /etc/kapacitor.conf

CMD ["kapacitord" "-config" "/etc/kapacitor.toml"]
