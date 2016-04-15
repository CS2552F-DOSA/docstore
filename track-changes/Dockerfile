FROM nodejs
ADD src /app
RUN sed -ie \
  's|git+https://github.com/sharelatex/metrics-sharelatex.git[^"]\+|git+https://github.com/Mic92/metrics-sharelatex.git|g' \
  /app/package.json
RUN npm install && grunt install
ADD settings.coffee /app/config/settings.coffee
USER node
