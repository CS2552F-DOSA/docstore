Path = require('path')
TMP_DIR = Path.resolve(Path.join(__dirname, "../../", "tmp"))

module.exports =
	metrics:
		statsd:
			host: "telegraf.local"

	mongo:
		url: 'mongodb://mongo/sharelatex'
	internal:
		trackchanges:
			port: 3000
			host: "0.0.0.0"
	apis:
		documentupdater:
			url: "http://docstore:3000"
		docstore:
			url: "http://docstore:3000"
		web:
			url: "http://web:3000"
			user: "sharelatex"
			pass: "password"
	redis:
		web:
			host: "redis"
			port: 6379
			pass: ""

	trackchanges:
		s3:
			key: ""
			secret: ""
		stores:
			doc_history: ""


	path:
		dumpFolder:   Path.join(TMP_DIR, "dumpFolder")
