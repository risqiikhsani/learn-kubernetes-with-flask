run in minikube :

    minikube start

    kubectl apply -f allfilename.yaml
    kubectl get all
    kubectl get pods

    minikube service flask-app-service

update the latest container :

    if the deployment points to :latest tag, and want to get latest update with :latest tag from the dockerhub.
    Kubernetes will not automatically pull the new version unless you explicitly trigger an update.
    kubectl rollout restart deployment <deployment-name>

use HPA :
    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
    kubectl apply -f hpa.yaml

    if we have hpa, we delete the replicas in deployment, the pods number automatically scales up or down by hpa.
