all: build
upload: build
	ruby scripts/upload-container.rb docker-compose.yml
build: .build
.build: docker-compose.yml $(wildcard */Dockerfile)
	docker-compose build
	touch .build
rancher-compose: docker-compose.yml
	ruby scripts/convert-compose-v2.rb docker-compose.yml > rancher-compose/sharelatex/docker-compose.yml
	cd rancher-compose/sharelatex && rancher-compose up --upgrade --pull --batch-size 99
