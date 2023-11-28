## PODS COMMUNICATION
# get pods IP and check connection
kubectl get pods -o wide
kubectl -it exec toolbox -- bash
curl http://10.244.0.46:5000

http http://10-244-0-46.default.pod.cluster.local:5000/pods/env-vars


## SERVICE

> no mapping accross Worker nodes is required. It handle by Kubernetes engine.
> DNS tool

## Typy servicow:
1. ClusterIP - only visible in Cluster
2. 

# Deploy service end check connection
kubectl exec -it toolbox -- bash
http http://app:8080/pods/env-vars
check HOSTNAME