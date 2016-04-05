all: build
upload: build
	ruby scripts/upload-container.rb docker-compose.yml
build: .build
.build: docker-compose.yml $(wildcard */Dockerfile)
	docker-compose build
	touch .build
rancher-compose: docker-compose.yml
	ruby scripts/convert-compose-v2.rb docker-compose.yml > rancher/sharelatex/docker-compose.yml
	cd rancher/sharelatex && rancher-compose up -u -p --batch-size 99
