#!/usr/bin/env bash

#export LOCAL_REGISTRY_BASE="localhost:5000"
#export LOCAL_REGISTRY_NAME="registry.me:5000"
export IMAGE_USER="arm64v8"
export IMAGE_NAME="ubuntu"
export IMAGE_TAG="18.04"

sudo apt-get update -qq && \
sudo apt-get install -qq -y software-properties-common uidmap && \
sudo add-apt-repository -y --remove ppa:projectatomic/ppa; \
#sudo apt-get install -qq -y ssh-askpass openssh-server && \
sudo add-apt-repository -y ppa:projectatomic/ppa && \
sudo apt-get update -qq && \
sudo apt-get -qq -y install podman && \
#sudo echo "ssh:localhost:allow" >> /etc/hosts.allow && \
#sudo echo "sshd:localhost:allow" >> /etc/hosts.allow && \
#ssh-copy-id ${USER}@$(docker network inspect --format='{{range .IPAM.Config}}{{.Gateway}}{{end}}' bridge) && \
#echo "AllowTcpForwarding yes" >> /etc/ssh/sshd_config && \
#echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config && \
#echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \
#sudo service sshd reload && \
#sudo service ssh restart && \
#ssh-keygen -t rsa -b 8192 && \
#cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
#eval $(ssh-agent -s) && \
#ssh-add ~/.ssh/id_rsa && \
#docker context create remote --docker "host=ssh://${USER}@$(docker network inspect --format='{{range .IPAM.Config}}{{.Gateway}}{{end}}' bridge)"; \
#docker context use remote; \
#docker context use default; \
ps axf | grep docker | grep -v grep | awk '{print "kill -9 " $1}' | sudo sh; \
sudo rm /var/run/docker.pid; \
sudo systemctl start docker && \
sleep 10
#echo "REPO=${LOCAL_REGISTRY_NAME}/l4t" > .env && \
#echo "DOCKER_HOST=ssh://${USER}@$(docker network inspect --format='{{range .IPAM.Config}}{{.Gateway}}{{end}}' bridge)" >> .env && \
#echo "127.0.0.1	localhost	registry.me" >> /etc/hosts && \
#sudo mkdir -p /var/lib/registry && \
podman container stop registry; \
podman container rm -v registry; \
#docker run -d \
#           -p 5000:5000 \
#           --restart=always \
#           --name=registry \
#           -v /mnt/registry:/var/lib/registry \
#           registry:2

#sudo bash -c "echo '[registries.search]' > /etc/containers/registries.conf" && \
#sudo bash -c "echo \"registries = ['localhost:5000', 'registry.me:5000', 'nvcr.io', 'docker.io']\" >> /etc/containers/registries.conf" && \
#sudo bash -c "echo '[registries.insecure]' >> /etc/containers/registries.conf" && \
#sudo bash -c "echo \"registries = ['localhost:5000', 'registry.me:5000']\" >> /etc/containers/registries.conf" && \
#podman run --privileged \
#           -d \
#           --name registry \
#           -p 5000:5000 \
#           -v /var/lib/registry:/var/lib/registry \
#           --restart=always \
#           registry:2 && \
sudo bash -c "echo '[registries.search]' > /etc/containers/registries.conf" && \
sudo bash -c "echo 'registries = [\'nvcr.io\', \'docker.io\']' > /etc/containers/registries.conf" && \
sudo bash -c "echo '[registries.insecure]' > /etc/containers/registries.conf" && \
sudo bash -c "echo 'registries = [\'nvcr.io\', \'docker.io\']' > /etc/containers/registries.conf"
#[registries.search]
#registries = ['nvcr.io', 'docker.io']
#[registries.insecure]
#registries = ['nvcr.io', 'docker.io']
#sudo bash -c "echo \"registries = ['localhost:5000', 'registry.me:5000', 'nvcr.io', 'docker.io']\" >> /etc/containers/registries.conf" && \
#sudo bash -c "echo '[registries.insecure]' >> /etc/containers/registries.conf" && \
#sudo bash -c "echo \"registries = ['localhost:5000', 'registry.me:5000']\" >> /etc/containers/registries.conf"

#sleep 10

#podman pull ${IMAGE_USER}/${IMAGE_NAME}:${IMAGE_TAG} && \
#podman tag ${IMAGE_USER}/${IMAGE_NAME}:${IMAGE_TAG} ${LOCAL_REGISTRY_BASE}/${IMAGE_NAME}:${IMAGE_TAG} && \
#podman tag ${IMAGE_USER}/${IMAGE_NAME}:${IMAGE_TAG} ${LOCAL_REGISTRY_NAME}/${IMAGE_NAME}:${IMAGE_TAG} && \
#podman push ${LOCAL_REGISTRY_BASE}/${IMAGE_NAME}:${IMAGE_TAG} && \
#podman push ${LOCAL_REGISTRY_NAME}/${IMAGE_NAME}:${IMAGE_TAG} && \
#podman image rm ${IMAGE_USER}/${IMAGE_NAME}:${IMAGE_TAG} && \
#podman image rm ${LOCAL_REGISTRY_BASE}/${IMAGE_NAME}:${IMAGE_TAG} && \
#podman pull ${LOCAL_REGISTRY_NAME}/${IMAGE_NAME}:${IMAGE_TAG} && \

#docker pull ${IMAGE_USER}/${IMAGE_NAME}:${IMAGE_TAG} && \
#docker tag ${IMAGE_USER}/${IMAGE_NAME}:${IMAGE_TAG} ${LOCAL_REGISTRY_BASE}/${IMAGE_NAME}:${IMAGE_TAG} && \
#docker tag ${IMAGE_USER}/${IMAGE_NAME}:${IMAGE_TAG} ${LOCAL_REGISTRY_NAME}/${IMAGE_NAME}:${IMAGE_TAG} && \
#docker push ${LOCAL_REGISTRY_BASE}/${IMAGE_NAME}:${IMAGE_TAG} && \
#docker push ${LOCAL_REGISTRY_NAME}/${IMAGE_NAME}:${IMAGE_TAG} && \
#docker image remove ${IMAGE_USER}/${IMAGE_NAME}:${IMAGE_TAG} && \
#docker image remove ${LOCAL_REGISTRY_BASE}/${IMAGE_NAME}:${IMAGE_TAG} && \
#docker pull ${LOCAL_REGISTRY_NAME}/${IMAGE_NAME}:${IMAGE_TAG} && \
RELEASE=32.4 && TAG=32.4.4 && sudo make image && \
sudo make push




#sudo podman rmi -a --force
