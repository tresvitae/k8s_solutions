# Node
> pod location in nodes

minikube delete && minikube start --nodes 4
kubectl label node minikube-m02 color=blue && kubectl label node minikube-m03 color=green
kubectl label node minikube pool=m01 && kubectl label node minikube-m02 pool=m02 && kubectl label node minikube-m03 pool=m03 && kubectl label node minikube-m04 pool=m04

spec:
  nodeSelector:
    color: blue