# Variables
IMAGE_NAME = math-server
ACR_REGISTRY = agent007.azurecr.io
TAG = latest
ARM_TAG = arm-$(TAG)
AMD_TAG = amd-$(TAG)

.PHONY: build build-arm build-amd tag push login clean deploy

# Build Docker image for local ARM testing (for M2 Mac)
build-arm:
	docker build -t $(IMAGE_NAME):$(ARM_TAG) --platform linux/arm64 .

# Build Docker image for AMD64 (for registry)
build-amd:
	docker build -t $(IMAGE_NAME):$(AMD_TAG) --platform linux/amd64 .

# Build both ARM and AMD images
build: build-arm build-amd

# Tag the AMD64 image for ACR
tag: build-amd
	docker tag $(IMAGE_NAME):$(AMD_TAG) $(ACR_REGISTRY)/$(IMAGE_NAME):$(TAG)

# Login to Azure Container Registry
login:
	az acr login --name agent007

# Push the AMD64 image to ACR (requires login first)
push: tag
	docker push $(ACR_REGISTRY)/$(IMAGE_NAME):$(TAG)

# Clean up local images
clean:
	docker rmi -f $(IMAGE_NAME):$(ARM_TAG) || true
	docker rmi -f $(IMAGE_NAME):$(AMD_TAG) || true
	docker rmi -f $(ACR_REGISTRY)/$(IMAGE_NAME):$(TAG) || true

# Build and push AMD64 image in one command (login required first)
deploy: build-amd tag push

# Run the local ARM image for testing in detached mode (background)
run-local: build-arm
	docker run -d -p 5001:5001 --name $(IMAGE_NAME)-container $(IMAGE_NAME):$(ARM_TAG)
	@echo "Container started in background. To view logs: docker logs $(IMAGE_NAME)-container"
	@echo "To stop the container: docker stop $(IMAGE_NAME)-container"
	@echo "To remove the container: docker rm $(IMAGE_NAME)-container"