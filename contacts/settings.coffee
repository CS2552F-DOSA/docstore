http = require('http')
http.globalAgent.maxSockets = 300

module.exports =
	metrics:
		statsd:
			host: "telegraf"

	internal:
		contacts:
			port: 3000
			host: "0.0.0.0"

	mongo:
		url: 'mongodb://mongo/sharelatex'
