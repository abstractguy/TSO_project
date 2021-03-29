DOC     = /usr/share/doc/cuda
VAR     = /var/cuda

RELEASE ?= r32.4
#TAG     ?= r32.4.3
TAG     ?= r32.4.4
CUDA    ?= 10.2
L4T_CUDA_REGISTRY   ?= "nvcr.io/nvidian/nvidia-l4t-cuda"
L4T_BASE_REGISTRY   ?= "nvcr.io/nvidian/nvidia-l4t-base"
#L4T_CUDA_REGISTRY   ?= "localhost:5000/nvidia-l4t-cuda"
#L4T_BASE_REGISTRY   ?= "localhost:5000/nvidia-l4t-base"

BUILD_DATE=$(date -u +'%Y-%m-%d-%H:%M:%S')
CODE_NAME='xenial'
LIBGLVND_VERSION='v1.1.0'
JETPACK_VERSION='4.4.1'
#TAG="jetpack-$JETPACK_VERSION-$CODE_NAME"

include $(CURDIR)/common.mk

all: image

image:
	mkdir -p ${CURDIR}/dst
	podman build $(DOCKER_BINFMT_MISC) -t $(L4T_CUDA_REGISTRY):$(TAG) \
		--build-arg "RELEASE=${RELEASE}" --build-arg "CUDA=$(CUDA)" \
		-f ./Dockerfile.cuda ./
	podman run -t $(DOCKER_BINFMT_MISC) -v $(CURDIR)/dst:/dst $(L4T_CUDA_REGISTRY):$(TAG) sh -c 'cp -r /usr/local/cuda/* /dst'
	podman build $(DOCKER_BINFMT_MISC) -t $(L4T_BASE_REGISTRY):$(TAG) \
		--build-arg "RELEASE=$(RELEASE)" \
		--build-arg "CUDA=$(CUDA)" \
		--build-arg REPOSITORY=arm64v8/ubuntu \
		--build-arg TAG=$CODE_NAME \
		--build-arg LIBGLVND_VERSION=$LIBGLVND_VERSION \
		--build-arg BUILD_VERSION=$JETPACK_VERSION \
		--build-arg BUILD_DATE=$BUILD_DATE \
		-v $(CURDIR)/dst:/dst \
		-f ./Dockerfile.ml.test .
#		-f ./Dockerfile.l4t.test .
#		-f ./Dockerfile.l4t .

	bash scripts/docker_build_ml.sh all ${TAG}
	#podman rm `podman ps -a | grep nvcr.io/nvidian/nvidia-l4t-cuda:r32.4.3 | head -n1 | awk '{print $$1;}'`
	#podman rmi `podman images | grep nvcr.io/nvidian/nvidia-l4t-cuda  | head -n1 | awk '{print $$3;}'`
	podman rm `podman ps -a | grep nvcr.io/nvidian/nvidia-l4t-cuda:r32.4.4 | head -n1 | awk '{print $$1;}'`
	podman rmi `podman images | grep nvcr.io/nvidian/nvidia-l4t-cuda  | head -n1 | awk '{print $$3;}'`
	#podman rm `podman ps -a | grep registry.me:5000/nvidia-l4t-cuda:r32.4.3 | head -n1 | awk '{print $$1;}'`
	#podman rmi `podman images | grep registry.me:5000/nvidia-l4t-cuda  | head -n1 | awk '{print $$3;}'`

push:
	podman push nvcr.io/nvidian/nvidia-l4t-base:$(RELEASE)
	#podman push registry.me:5000/nvidia-l4t-base:${RELEASE}
	#docker push registry.me:5000/l4t-ml:${RELEASE}

