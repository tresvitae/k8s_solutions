## INGRESS
expose many applications, and reduce additional costs using Ingress instead LoadBalancer.
Ingress use routing rule in Ingress Controller

Traffic > LB > Ingress managed LB > Ingress Controller > routing rule > services

minikube addons enable ingress
kubectl get ns
kubectl get pods -n ingress-nginx

## services for  API test
kubectl apply -f deployment.yaml
minikube service podinfo
minikube service httpbin

## Ingress
kubectl get ingressclasses.networking.k8s.io
kubectl apply -f ingress.yaml
minikube tunnel
kubectl get ingress