Create a Docker Volume
docker volume create myvolume

Check volumes:

docker volume ls

Inspect volume details:

docker volume inspect myvolume
Attach Volume to a Container
While creating a container
docker run -d --name mycontainer -v myvolume:/app/data nginx
myvolume → Docker volume name
/app/data → path inside container

Example:

docker run -it --name ubuntu-container -v myvolume:/data ubuntu

This attaches myvolume to /data inside the container.

Attach Existing Volume to Existing Container

You cannot directly attach a volume to a running container. You must stop/remove and recreate the container with -v.

Example:

docker stop mycontainer
docker rm mycontainer

docker run -d --name mycontainer -v myvolume:/app/data nginx
Delete Docker Volume
Delete all unused volumes:

docker volume prune
Remove Container with Volume
docker rm -v mycontainer

This removes the container and its anonymous volumes.

Useful command to see mounted volumes:

docker inspect mycontainer

or

docker container inspect mycontainer
Delete one volume:

docker volume rm myvolume





installation of minicube

 7 curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    8  chmod +x kubectl
    9  mv kubectl /usr/local/bin/
   10  kubectl version --client
   11  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
   12  install minikube-linux-amd64 /usr/local/bin/minikube
   13  minikube version
   14  minikube start --driver=docker
   15  kubectl cluster-info
   16  minikube start --driver=docker --force
   17  kubectl cluster-info
   18  kubectl get nodes
   19  eval $(minikube docker-env)
