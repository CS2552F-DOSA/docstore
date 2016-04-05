FROM ubuntu:trusty
ENV DEBIAN_FRONTEND=noninteractive
ADD apt.conf /etc/apt/apt.conf
RUN rm /var/lib/apt/lists/* -rvf && \
    apt update && \
    apt install -y curl && \
    curl -L "https://github.com/tianon/gosu/releases/download/1.0/gosu" > /usr/local/bin/gosu && \
    chmod +x /usr/local/bin/gosu
