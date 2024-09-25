# Makefile for Python Template Project

# Variables
docker_image_name ?= python-template
docker_image_tag ?= v1.0.0
dockerfile_path = deploy/Dockerfile
docker_compose_file = deploy/docker-compose.yml
docker_image_full_name = $(docker_image_name):$(docker_image_tag)

# Phony Targets
.PHONY: all build build-ufw build-nocache run reset help

# Default Target
all: help

# Build Docker Image
build:
	docker build -f $(dockerfile_path) -t $(docker_image_full_name) .

# Build Docker Image with China Mirror
build-ufw:
	docker build --build-arg USE_CHINA_MIRROR=true -f $(dockerfile_path) -t $(docker_image_full_name) .

# Build Docker Image without Cache
build-nocache:
	docker build --no-cache -f $(dockerfile_path) -t $(docker_image_full_name) .

# Run Docker Containers
run:
	docker-compose -f $(docker_compose_file) up -d

# Reset Environment
reset:
	git pull
	docker-compose -f $(docker_compose_file) down
	docker rmi $(docker_image_full_name) || true
	$(MAKE) build
	docker-compose -f $(docker_compose_file) up -d

# Display Help
help:
	@echo "可用命令:"
	@awk 'BEGIN {FS = ":.*?## "}; /^[^#[:space:]].*:.*?## / { printf "  %-15s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
