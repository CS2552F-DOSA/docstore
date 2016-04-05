FROM nodejs
ADD src /app
RUN npm install && grunt install
ADD settings.coffee /app/config/settings.coffee
RUN chown -R node /app/user_files /app/uploads /app/template_files
ADD entrypoint /entrypoint
ENTRYPOINT ["/entrypoint"]
