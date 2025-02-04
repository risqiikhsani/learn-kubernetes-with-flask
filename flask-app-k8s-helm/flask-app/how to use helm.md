
helm install flask-app .
minikube service flask-app-service
helm upgrade flask-app .
helm rollback flask-app 1
helm list --all-namespaces
helm uninstall flask-app
helm uninstall flask-app