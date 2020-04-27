FROM tiancanyu/envoy-filters:dev
# ADD dist/envoy /usr/local/bin/envoy
ADD Envoy-Filters /source
ADD prod-envoy.yaml /etc/envoy.yaml
WORKDIR /source

RUN bazel build //:envoy
# RUN bazel-bin/envoy -c dosa_server.yaml -l info 2>&1
CMD ["bazel-bin/envoy", "-c", "dosa_server.yaml", "-l", "info", "2>&1"]
# CMD ["sleep(100)"]