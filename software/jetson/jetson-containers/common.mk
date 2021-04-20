PLATFORM ?= $(shell uname -m)
ifeq ($(PLATFORM),x86_64)
	DOCKER_BINFMT_MISC = $(shell echo "-v /usr/bin/qemu-aarch64-static:/usr/bin/qemu-aarch64-static")
else ifeq ($(PLATFORM),aarch64)
	DOCKER_BINFMT_MISC = $(shell echo "")
else
	$(error Unsupported architecture)
endif

