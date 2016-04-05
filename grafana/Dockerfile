FROM mic92/sharelatex-base
RUN curl -L "https://grafanarel.s3.amazonaws.com/builds/grafana_2.6.0_amd64.deb" > /tmp/grafana.deb && \
      apt-get install -y adduser libfontconfig && \
      dpkg -i /tmp/grafana.deb
WORKDIR /usr/share/grafana
ADD grafana.ini /etc/grafana/grafana.ini
ADD entrypoint /entrypoint
EXPOSE 3000
ENTRYPOINT ["/entrypoint"]
