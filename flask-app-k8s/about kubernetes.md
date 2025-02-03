namespace
    Purpose: Used to divide cluster resources between multiple users or applications. They enable resource isolation.
    Use Case: Run development, staging, and production environments in the same cluster but isolate them.
ingress
    Purpose: Manages external HTTP/HTTPS access to services within the cluster. Provides a way to expose multiple services behind a single external IP or domain name.
    Use Case: Route traffic to multiple services (e.g., API, frontend) based on paths or hostnames.
pv and pvc
    Purpose: Used for managing storage in Kubernetes. PV is the storage resource; PVC is a request for storage by a pod.
    Use Case: Persistent storage for databases, file uploads, etc.
statefulset
    Purpose: Manages stateful applications, such as databases or applications requiring stable network IDs.
    Key Differences from Deployments: Pods in StatefulSets have stable, unique network identities and persistent storage.
    Use Case: Deploy databases like MySQL, Cassandra, or any application requiring stable disk or pod identities.
deamonset
    Purpose: Ensures that a copy of a pod runs on every node in the cluster.
    Use Case: Log collection (e.g., Fluentd), monitoring agents (e.g., Prometheus node exporter).
jobs and cronjobs
    Purpose: Run a single task or process to completion (e.g., data migration, backups).
    Purpose: Schedule recurring tasks (e.g., database backups, cleanup jobs).
network policies
    Purpose: Controls how pods communicate with each other and other network endpoints. Enforces network security.
    Use Case: Restrict traffic to/from specific pods or namespaces.
customresoucedefinition
    Purpose: Extend Kubernetes functionality by defining custom resources.
    Use Case: Create domain-specific abstractions for your application (e.g., ArgoCD, Prometheus Operator).
service
    a. ClusterIP
        Default Service Type: Exposes the service only inside the cluster.
        Use Case: Internal communication between services.
    b. NodePort
        Purpose: Exposes the service on a static port on each node's IP.
        Use Case: Access the service externally without using a load balancer.
    c. LoadBalancer
        Purpose: Exposes the service externally using a cloud provider's load balancer.
        Use Case: Allow external traffic to reach the pods.
        Notes: Requires a cloud provider like AWS, GCP, or Azure.
    d. ExternalName
        Purpose: Maps a service to an external DNS name.
        Use Case: Redirect traffic to an external service.


Others :
Service Mesh (e.g., Istio, Linkerd) for advanced service-to-service communication.
Kubernetes Monitoring and Logging: Tools like Prometheus, Grafana, Fluentd, and ELK Stack.
Helm Charts: Package management for Kubernetes.
Kubernetes Security: RBAC, PodSecurityPolicies, and secrets management.
Kubernetes Operators: Automate application-specific tasks.  