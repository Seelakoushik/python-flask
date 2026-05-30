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
   
   14  
   
   15  
   
   16  minikube start --driver=docker --force
   
   17  kubectl cluster-info
   
   18  kubectl get nodes
   
   19  eval $(minikube docker-env)




   27  kubectl apply -f pod.yml
   
   28  kubectl get pods
   
   29  kubectl describe pod hospital-pod
   
   30  kubectl logs hospital-pod
   
   31  kubectl port-forward hospital-pod 5000:5000 --address=0.0.0.0
   
   32  
   
   33  kubectl get pods
   
   34  kubectl delete pod hospital-pod
   
   35  kubectl get pods
   
   36  vim deployment.yml
   
   37  kubectl apply -f deployment.yml
   
   38  kubectl get deployments
   
   39  kubectl get pods

   
   40  kubectl delete pod hospital-deployment-778d477449-lhh78
   
   41  kubectl delete pod hospital-deployment
   
   42  kubectl scale deployment hospital-deployment --replicas=0
   
   43  kubectl get pods
   
  
   58  kubectl port-forward hospital-pod 5000:5000 --address=0.0.0.0
   
   59  ls
   
   60  kubectl apply -f deployment.yml
   
   61  kubectl get deployments
   
   62  kubetcl get pods
   63  kubectl get pods
   64  kubectl delete pod hospital-deployment
   65  kubectl get pods
   66  kubectl delete pod hospital-pod
   67  kubectl get pods
   68  kubectl delete pod hospital-deployment-778d477449-xdh5m
   69  kubectl l get pods
   70  kubectl get pods
   71  kubectl delete pod hospital-deployment-778d477449-8rm54
   72  kubectl get pods
   73  kubectl scale deployment hospital-deployment --replicas=1
   74  kubectl get pods
   75  vim clusterip.yml
   76  cat clusterip.yml
   77  kubectl apply -f clusterip.yml
   78  kubectl get services
   79  vim nodeport.yml
   80  cat nodeport.yml
   81  kubectl appy -f nodeport.yml
   82  kubectl apply -f nodeport.yml
   83  kubectl get svc
   84  kubectl get pods
   85  cat deployment.yml
   86  cat nodeport.yml
   87  vim deployment.yml
   88  vim nodeport.yml
   89  kubectl get pods
   90  kubectl get svc
   91  minikube status
   92  minikube service hospital-nodeport --url
   93  vim loadbalancer.yml
   94  kubectl apply -f loadbalancer.yml
   95  kubectl get svc
   96  vim config.yml
   97  kubectl apply -f config.yml
   98  kubectl get config
   99  kubectl get configmap
  100  vim secret.yml
  101  echo -n "admin" | base64
  102  echo -n "admin123" | base64
  103  kubectl apply -f secret.yml
  104  ls
  105  kubectl get secrets
  106  vim namespace.yml
  107  kubectl apply -f namespace.yml
  108  ls
  109  kubectl apply -f deployment.yml -n hospital-dev
  110  kubectl get pods
  111  kubectl get deployments
  112  kubectl get pods -n hospital-dev
  113  kubectl get deployments -n hopsital-dev
  114  kubectl get deployments -n hospital-dev
  115  kubectl delete deployment hospital-deployment  -n hospital-dev
  116  kubectl 
  117  kubectl apply -f pv.yml
  118  cat > pv.yml
  119  cat pv.yml
  120  cat > pv.yml
  121  cat pv.yml
  122  kubectl apply -f pv.yml
  123  kubectl get pvc
  124  kubectl get pv
  125  kubectl get pods
  126  kubectl delete deployment hospital-deployment
  127  ls
  128  minikube start
  129  kubectl cluster info
  130  kubectl cluster-info
  131  minikube status
  132  minikube start --driver=docker --force
  133  kubectl cluster-info
  134  kubectl get nodes
  135  kubectl get pods
  136  ls
  137  kubectl apply -f pod.yml
  138  kubectl get all resources
  139  kubectl get all
  140  minikube addons enable metrics-server
  141  kubectl get pods -n kube-system
  142  kubectl top nodes
  143  kubectl top pods
  144  kubectl autoscale deployment hospital-deployment --cpu-percent=50 --min=1 --max=3
  145  ls
  146  vim deployment.yml
  147  kubectl apply -f deployment.yml
  148  kubectl get deployments
  149  kubectl get pods
  150  kubectl autoscale deployment hospital-deployment --cpu-percent=50 --min=1 --max=4
  151  kubectl get pods
  152  kubectl delete deployment hospital-deployment
  153  vim deployment.yml
  154  kubectl get pods
  155  kubectl apply -f deployment.yml
  156  kubectl get pods
  157  ls
  158  kubectl get all
  159  kubectl get hpa -w
  160  kubectl run -i --tty load-generator --rm --image=busybox /bin/sh
  161  kubectl get hpa -w
  162  kubectl get pods
  163  kubectl run -i --tty load-generator --rm --image=busybox /bin/sh
  164  kubectl get hpa -w
  165  kubectl get pods
  166  kubectl top pods
  167  kubectl get pods -w
  168  ls
  169  kubectl apply -f namespace.yml
  170  kubectl get all -n hospital-dev
  171  kubectl get namespaces
  172  kubectl apply -f deployment.yml -n hospital-dev
  173  kubectl apply -f nodeport.yml -n hospital-dev
  174  kubectl apply -f pod.yml -n hospital-dev
  175  kubectl get all -n hospital-dev
  176  minikube status
  177  minikube start --driver=docker --force
  178  helm repo add bitnami https://charts.bitnami.com/bitnami
  179  sudo apt update
  180  sudo apt-get install curl gpg apt-transport-https --yes
  181  curl -fsSL https://packages.buildkite.com/helm-linux/helm-debian/gpgkey | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
  182  echo "deb [signed-by=/usr/share/keyrings/helm.gpg] https://packages.buildkite.com/helm-linux/helm-debian/any/ any main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
  183  sudo apt-get update
  184  sudo apt-get install helm
  185  helm version
  186  helm repo add bitnami https://charts.bitnami.com/bitnami
  187  helm repo update
  188  helm search repo nginx
  189  helm install my-nginx bitnami/nginx
  190  kubectl get nginix
  191  kubectl get pods
  192  helm list
  193  helm show values bitnami/nginx
  194  helm template my-nginx bitnami/nginx
  195  kubectl get pods
  196  ls
  197  kubectl apply -f nodeport.yml
  198  kubectl get all
  199  helm upgrade my-nginx bitnami/nginx --set service.type=NodePort
  200  helm status my-nginx
  201  helm uninstall my-nginx
  202  helm list
  203  kubectl get pods
  204  mkdir hospital-chart
  205  cd hospital-chart
  206  vim chart.yml
  207  vim values.yml
  208  ls
  209  cat app.py
  210  ls
  211  cat Dockerfile
  212  systemctl status apache2
  213  systemctl status nginx
  214  sudo apt update
  215  sudo apt install apache2 -y
  216  systemctl status apache2
  217  docker --version
  218  systemctl start docker
  219  systemctl status docker
  220  systemctl enable docker
  221  docker build -t myapp .
  222  history
  223  ls
  224  history
  225  ls
  226  cat pod.yml
  227  ls
  228  cat deployment.yml
  229  ls
  230  cat config.yml
  231  ls
  232  cat secret.yml
  233  ls
  234  cat clusterip.yml
  235  ls
  236  cat loadbalancer.yml 
  237  cat namespace.yml
  238  ls
  239  minikube-linux-amd64
  240  cat minikube-linux-amd64
  241  ls
  242  cat nodeport.yml
  243  ls
  244  cat pv.yml
  245  ls
