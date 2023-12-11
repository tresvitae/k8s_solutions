## INGRESS
expose many applications, and reduce additional costs using Ingress instead LoadBalancer.
Ingress use routing rule in Ingress Controller. It is a collection of rules that allow inbound connec­tions to reach the cluster services.

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

## INGRESS WITH TLS
install mkcert from https://github.com/FiloSottile/mkcert
mkcert --key-file key.pem --cert-file cert.pem podinfo.127.0.0.1.nip.io httpbin.127.0.0.1.nip.io
kubectl create secret tls ingress-tls --key key.pem --cert cert.pem
kubectl apply -f ingress.yaml (with TLS)
minikube tunnel