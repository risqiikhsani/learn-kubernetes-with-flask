minikube start

kubectl apply -f allfilename.yaml
kubectl get all
kubectl get pods

minikube service flask-app-service

if the deployment points to latest docker tag, and want to get latest update from the dockerhub.
Kubernetes will not automatically pull the new version unless you explicitly trigger an update.
kubectl rollout restart deployment <deployment-name>


if we have hpa, we delete the replicas in deployment
