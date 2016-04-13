Path = require('path')
http = require('http')
http.globalAgent.maxSockets = 300

module.exports =
	internal:
		documentupdater:
			host: "0.0.0.0"
			port: 3000

	apis:
		web:
			url: "http://web:3000"
			user: "sharelatex"
			pass: "password"
		trackchanges:
			url: "http://track-changes:3000"

	redis:
		web:
			port:"6379"
			host:"redis"
			password:""
		zip:
			minSize: 10*1024
			writesEnabled: false
	
	max_doc_length: 2 * 1024 * 1024 # 2mb

	mongo:
		url: 'mongodb://mongo/sharelatex'
