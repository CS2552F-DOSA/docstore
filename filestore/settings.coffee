Path = require "path"

module.exports =
	metrics:
		statsd:
			host: "telegraf"

	internal:
		filestore:
			port: 3000
			host: "0.0.0.0"

	filestore:
		# Which backend persistor to use.
		# Choices are
		# s3 - Amazon S3
		# fs - local filesystem
		backend: "fs"
		stores:
		  	# where to store user and template binary files
			#
			# For Amazon S3 this is the bucket name to store binary files in.
			#
			# For local filesystem this is the directory to store the files in.
			# Must contain full path, e.g. "/var/lib/sharelatex/data".
			# This path must exist, not be tmpfs and be writable to by the user sharelatex is run as.
			user_files: Path.resolve(__dirname + "/../user_files")
			public_files: Path.resolve(__dirname + "/../public_files")
			template_files: Path.resolve(__dirname + "/../template_files")
		# if you are using S3, then fill in your S3 details below
		# s3:
		# 	key: ""
		# 	secret: ""

	path:
		uploadFolder: Path.resolve(__dirname + "/../uploads")

	# Filestore health check
	# ----------------------
	# Project and file details to check in persistor when calling /health_check
	# health_check:
	# 	project_id: ""
	# 	file_id: ""
