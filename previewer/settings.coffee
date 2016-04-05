http = require('http')
http.globalAgent.maxSockets = 300

module.exports =
	internal:
		previewer:
			port: 3000
			host: "0.0.0.0"

	mongo:
		url: 'mongodb://mongo/sharelatex'

	#previewer:
	#	s3:
	#		key: ""
	#		secret: ""
	#		bucket: "something"
