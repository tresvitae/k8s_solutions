#

## Notes
https://github.com/kodekloudhub/certified-kubernetes-administrator-course/tree/master/docs

### ectd
key-value storage on default port 2379

export ETCDCTL_API=3
etcdctl snapshot save 
etcdctl endpoint health
etcdctl get
etcdctl put

kubectl get pods -n kube-system
kubectl exec etcd-master -n kube-system etcdctl get / --prefix -keys-only
kubectl exec etcd-master -n kube-system -- sh -c "ETCDCTL_API=3 etcdctl get / --prefix --keys-only --limit=10 --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt  --key /etc/kubernetes/pki/etcd/server.key


# communication on kube-apiserver
kube-apiserver > scheduler > kube-apiserver > Worker Nodes > kube-apiserver > etcd

## API commands
```
curl -X POST /api/v1/namespaces/default/pods ...[other]
```

## kube-apiserver options
cat /etc/kubernetes/manifests/kube-apiserver.yaml
cat /etc/systemd/system/kube-apiserver.service
ps -aux | grep kube-apiserver

# Controller-Manager
- monitore the state of nodes and remediate situation
Node Monitor Period is 5s
cat /etc/systemd/system/kube-controller-manager.service

## View kube-controller-manager
cat /etc/kubernetes/manifests/kube-controller-manager.yaml
cat /etc/systemd/system/kube-controller-manager.service
ps -aux | grep kube-controller-manager

# kube-scheduler
decides which worker node use to deploy pods based on its requests and limits
cat /etc/kubernetes/manifests/kube-scheduler.yaml
ps -aux | grep kube-scheduler

# kubelet
deploy pods
ps -aux | grep kubelet

# kube-proxy



# Pods


# ReplicaSet
create desired number of pods and keep it, scale pods

# Deployment
ReplicaSet + updates on applited configuration like (= create new ReplicaSet):
kubectl edit deployment/nginx
kubectl rollout

# Service
expose apps, forward requests
- NodePort in range 30000 - 32767 
- ClusterIp for fronted/backend traffic in cluster
- LoadBalancer
kubectl expose port-forward

# Namespace
kubectl config set-context $(kubectl config current-context) --namespace=dev
kns
mysql.connect("db-service.dev.svc.cluster.local")
               SERVICE-NAME.NAMESPACE.SERVICE.DOMAIN


### kubectl run
Create an NGINX Pod
kubectl run nginx --image=nginx

Generate POD Manifest YAML file (-o yaml). Don't create it(--dry-run)
kubectl run nginx --image=nginx --dry-run=client -o yaml

### kubectl create
Create a deployment
kubectl create deployment --image=nginx nginx

Generate Deployment YAML file (-o yaml). Don't create it(--dry-run)
kubectl create deployment --image=nginx nginx --dry-run=client -o yaml

Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run) and save it to a file.
kubectl create deployment --image=nginx nginx --replicas=5 --dry-run=client -o yaml > nginx-deployment.yaml

Create a Service named redis-service of type ClusterIP to expose pod redis on port 6379:
kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml

Create a Service named nginx of type NodePort to expose pod nginx's port 80 on port 30080 on the nodes:
kubectl expose pod nginx --type=NodePort --port=80 --name=nginx-service --dry-run=client -o yaml

Create a pod and service ClusterIP with target port 80 and expose it:
kubectl run httpd --image=httpd:alpine --port=80 --expose=true

