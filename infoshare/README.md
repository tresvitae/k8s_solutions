# Infoshare notes

## use kind to manage clusters
kind create cluster --config cluster.yaml

## Cluster in HA using kind
kind create cluster --config cluster-ha.yaml
kind get nodes --name basic-ha

### get running processes on master-node
docker ps
docker exec -it <basic-ha-control-plane> bash
ps axufw

### check healthy of control plane
CLUSTER_IP=$(kctl config view -o jsonpath='{.clusters[].cluster.server}')
while true; do; curl -k $CLUSTER_IP/healthz; sleep 1; echo ""; done

## Objects list and descryption
kctl api-resources
kctl explain pods
kctl explain pods.metadata.clusterName

# Imperative deployment
kctl create namespace nginx
kns nginx
kctl create deployment nginx --image=nginx
kctl get rs, deployment, pods

## create busybox
kctl apply -f https://git.io/vPieo

## Port forward
kctl port-forward pod/<POD_NAME> 8080:80
kctl port-forward deployment/nginx 8080:80

## revision, rollback of deployments/daemonsets/statefulsets
kctl rollout history deployment nginx
kctl rollout undo deploy nginx

## RollingStrategy
- Recreate
- RollingUpdate


# Volumen

## emptyDir
Share temporary data, while pods are running, between coinainers. Do not store data after kill. Used for cache.

## hostPath
Mount files from host where pods are running. Store data after kill the pod.
Share storage data between pods in the same host.

### emptyDir/hostPath with readOnly 
set in volumeMounts in containers to read only data from chosen container. Used for security.