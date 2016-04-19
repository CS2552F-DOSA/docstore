module.exports =
	metrics:
		statsd:
			host: "telegraf"

	redis:
		web:
			host: "redis"
			port: "6379"
			password: ""
			
	internal:
		realTime:
			port: 3000
			host: "0.0.0.0"
			user: "sharelatex"
			pass: "password"
			
	apis:
		web:
			url: "http://web:3000"
			user: "sharelatex"
			pass: "password"
		documentupdater:
			url: "http://doc-updater:3000"
			
	security:
		sessionSecret: "secret-please-change"
		
	cookieName:".sharelatex.local"
	
	max_doc_length: 2 * 1024 * 1024 # 2mb
