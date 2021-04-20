#!/bin/sh

BUILD_DATE=$(date -u +'%Y-%m-%d-%H:%M:%S')
CODE_NAME='xenial'
LIBGLVND_VERSION='v1.1.0'
JETPACK_VERSION='4.4.1'
TAG="jetpack-$JETPACK_VERSION-$CODE_NAME"

sudo ln -dfs ../../jetson-containers/dst .

# Use tar to dereference the symbolic links from the current directory, and then pipe them all to the docker build - command.
tar -czh . | docker build - \
  --build-arg REPOSITORY=arm64v8/ubuntu \
  --build-arg TAG=$CODE_NAME \
  --build-arg LIBGLVND_VERSION=$LIBGLVND_VERSION \
  --build-arg BUILD_VERSION=$JETPACK_VERSION \
  --build-arg BUILD_DATE=$BUILD_DATE \
  --tag=jetson-agx/opengl:$TAG

