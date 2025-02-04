kubectl create namespace prod
kubectl create namespace dev
helm install fromyoutube-prod . --values values.yaml -f values-prod.yaml -n prod
helm install fromyoutube-dev . --values values.yaml -f values-dev.yaml -n dev
helm upgrade fromyoutube-prod . --values values.yaml -f values-prod.yaml -n prod
helm upgrade fromyoutube-dev . --values values.yaml -f values-dev.yaml -n dev
helm rollback fromyoutube-prod 1 -n prod
helm rollback fromyoutube-dev 1 -n dev
helm list --all-namespaces
helm uninstall fromyoutube-prod -n prod
helm uninstall fromyoutube-dev -n dev