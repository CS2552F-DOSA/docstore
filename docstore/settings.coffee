http = require('http')
http.globalAgent.maxSockets = 300

module.exports =
	internal:
		docstore:
			port: 3000
			host: "0.0.0.0"

	mongo:
		url: 'mongodb://mongo/sharelatex'

	docstore:
		healthCheck:
			project_id: "5620bece05509b0a7a3cbc61"
	#	s3:
	#		key: ""
	#		secret: ""
	#		bucket: "something"

	max_doc_length: 2 * 1024 * 1024 # 2mb
