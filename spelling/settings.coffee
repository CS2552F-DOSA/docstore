module.exports = Settings =
	metrics:
		statsd:
			host: "telegraf"
	internal:
		spelling:
			port: 3000
			host: "0.0.0.0"
	redis:
		port:6379
		host:"redis"
		password:""
	mongo:
		url : 'mongodb://mongo/sharelatex'


	healthCheckUserId: "53c64d2fd68c8d000010bb5f"
