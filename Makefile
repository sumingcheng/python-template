docker_image_name ?= python-template
docker_image_tag ?= v1.0.0

dockerfile_path = deploy/Dockerfile
docker_image_full_name = $(docker_image_name):$(docker_image_tag)

build:
	docker build -f $(dockerfile_path) -t $(docker_image_full_name) .

build-ufw:
	docker build --build-arg USE_CHINA_MIRROR=true -f $(dockerfile_path) -t $(docker_image_full_name) .

build-nocache:
	docker build --no-cache -f $(dockerfile_path) -t $(docker_image_full_name) .

run:
	docker-compose -f deploy/docker-compose.yml up -d

reset:
	git pull
	docker-compose -f deploy/docker-compose.yml down
	docker rmi $(docker_image_full_name) || true
	$(MAKE) build
	docker-compose -f deploy/docker-compose.yml up -d

help:
	@echo "可用命令"
	@echo "  build          构建 Docker 镜像"
	@echo "  build-ufw      使用中国镜像源构建 Docker 镜像"
	@echo "  build-nocache  不使用缓存构建 Docker 镜像"
	@echo "  run            启动服务"
	@echo "  reset          重置并重新构建和启动服务"
	@echo "  help           显示帮助信息"

.PHONY: build build-ufw build-nocache run reset help