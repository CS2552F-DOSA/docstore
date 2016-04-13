Path = require "path"

module.exports =
	metrics:
		statsd:
			host: "telegraf.local"

	# Options are passed to Sequelize.
	# See http://sequelizejs.com/documentation#usage-options for details
	mysql:
		clsi:
			database: "clsi"
			username: "clsi"
			password: "clsi"
			host: "postgres"
			dialect: "postgres"

	path:
		compilesDir:  Path.resolve(__dirname + "/../compiles")
		clsiCacheDir: Path.resolve(__dirname + "/../cache")
		synctexBaseDir: (project_id) -> Path.join(@compilesDir, project_id)

	# clsi:
	# 	commandRunner: "docker-runner-sharelatex"
	# 	docker:
	# 		image: "quay.io/sharelatex/texlive-full"
	# 		env:
	# 			PATH: "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/texlive/2013/bin/x86_64-linux/"
	# 			HOME: "/tmp"
	# 		modem:
	# 			socketPath: false
	# 		user: "tex"

	internal:
		clsi:
			port: 3000
			host: "0.0.0.0"

	apis:
		clsi:
			url: "http://clsi:3000"
			
	smokeTest: false
