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