FROM nodejs
ADD src /app
RUN mkdir -p /app/{compiles,caches} && \
    chown -R node /app/{compiles,caches} && \
    apt install -y texlive texlive-latex-extra qpdf latexmk && \
    npm install --save pg pg-hstore && \
    npm install && \
    grunt install
ADD settings.coffee /app/config/settings.coffee
USER node
