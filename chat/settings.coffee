module.exports =
	metrics:
		statsd:
			host: "telegraf"

	internal:
		chat:
			host: "0.0.0.0"
			port: 3000
	
	apis:
		web:
			url: "http://web:3000"
			user: "sharelatex"
			pass: "password"

	mongo:
		url : 'mongodb://mongo/sharelatex'

	redis:
		web:
			host: "redis"
			port: "6379"
			password: ""
