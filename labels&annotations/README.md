## LABELS

> Key Value data for developers.
> Does not store any data to the kubernetes.
> Orginize objects to the group.

# see labels in pod
kubectl describe pod nginx
kubectl get pods --show-labels
kubectl get pods --show-labels tier=backend
kubectl get pods --show-labels --selector 'tier in (frontend, backend)'


## ANNOTATIONS

> Used to configuration data in objects, like version, commit, checksum, nginx ingress controller, cert manager, cloud integrations, autoscaler

# see annotations
kubectl descrive pod nginx
kubectl get pods -o=json | jq '.items[0].metadata.annotations'