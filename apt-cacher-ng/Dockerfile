# Build: docker build -t apt-cacher .
# Run: docker run -d -p 3142:3142 --name apt-cacher-ng mic92/apt-cacher-ng
FROM ubuntu:trusty

VOLUME ["/var/cache/apt-cacher-ng"]
RUN apt-get update && apt-get install -y apt-cacher-ng
ADD apt.conf /etc/apt/apt.conf
RUN echo "Proxy: $http_proxy\nPassThroughPattern: .*" >> /etc/apt-cacher-ng/acng.conf

EXPOSE 3142
CMD chmod 777 /var/cache/apt-cacher-ng && /etc/init.d/apt-cacher-ng start && tail -f /var/log/apt-cacher-ng/*
