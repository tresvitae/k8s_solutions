> Key Value data for developers.
> Does not store any data to the kubernetes.
> Orginize objects to the group.

# see labels in pod
kubectl describe pod nginx
kubectl get pods --show-labels
kubectl get pods --show-labels tier=backend
kubectl get pods --show-labels --selector 'tier in (frontend, backend)'