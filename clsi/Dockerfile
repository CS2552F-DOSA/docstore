FROM mic92/sharelatex-nodejs
ADD src /app
RUN mkdir -p /app/{compiles,caches} && \
    chown -R node /app/{compiles,caches} && \
    apt-get update --fix-missing && \
    apt install -y texlive texlive-latex-extra qpdf latexmk
RUN npm install --save pg pg-hstore git+https://github.com/Mic92/metrics-sharelatex.git && npm install && grunt install
ADD settings.coffee /app/config/settings.coffee
USER node
