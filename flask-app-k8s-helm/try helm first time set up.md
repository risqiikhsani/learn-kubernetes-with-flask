first time set up

    helm repo add bitnami https://charts.bitnami.com/bitnami
    helm repo update
    helm install my-nginx bitnami/nginx
    helm list
    helm uninstall my-nginx

customize deployment

    example in values.yaml

    service:
        type: LoadBalancer
        port: 8080
    replicaCount: 3

    helm install my-nginx -f values.yaml bitnami/nginx

upgrade helm release
Modify values.yaml and apply changes:
    helm upgrade my-nginx -f values.yaml bitnami/nginx

rollback helm release
    helm rollback my-nginx 1

uninstall helm release
    helm uninstall my-nginx
