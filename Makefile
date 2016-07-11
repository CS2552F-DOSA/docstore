all: build
upload: build
	ruby scripts/upload-container.rb docker-compose.yml
.apt-cacher: apt-cacher-ng/Dockerfile
	cd apt-cacher-ng && docker build --build-arg http_proxy -t mic92/apt-cacher-ng .
	touch .apt-cacher
build: .apt-cacher .build
.build: docker-compose.yml $(wildcard */Dockerfile)
	docker ps | grep -q apt-cacher-ng || docker run -d -p 3142:3142 --restart=always -v /data/apt:/var/apt-cacher-ng --name apt-cacher-ng mic92/apt-cacher-ng
	docker-compose build
	touch .build
rancher-compose: docker-compose.yml
	ruby scripts/convert-compose-v2.rb docker-compose.yml > rancher-compose/sharelatex/docker-compose.yml
	cd rancher-compose/sharelatex && rancher-compose up --upgrade --pull --batch-size 99
