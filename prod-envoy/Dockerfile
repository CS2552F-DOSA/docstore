# FROM tiancanyu/envoy-filters:v2
# ADD dist/envoy /usr/local/bin/envoy
# ADD ./Envoy-Filters /source
# ADD ./prod-envoy.yaml /etc/envoy.yaml
# WORKDIR /source

# RUN bazel build //:envoy
# # RUN bazel-bin/envoy -c dosa_server.yaml -l info 2>&1
# CMD ["bazel-bin/envoy", "-c", "dosa_server.yaml", "-l", "info", "2>&1"]
# # CMD ["sleep(100)"]

FROM csci2952fmicrocow/prod-storage-envoy:latest
# CMD ["bazel-bin/envoy", "-c", "dosa_server.yaml"]
# ADD ./prod-envoy.yaml /etc/envoy.yaml

RUN /usr/local/bin/envoy -c /etc/envoy.yaml -l debug --service-cluster proxy
CMD tail -f /dev/null