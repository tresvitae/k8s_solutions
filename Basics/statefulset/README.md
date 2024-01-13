# STATEFULSET
> part of deployment services
> 1 master pod && N slave pods
> convenient name concept with iteration: 'app-stateful-set-0' pod for service 'app-stateful-set' in namespace 'default' DNS will be: <pod-name>.<svc-name>.<ns>.<cluster.local>

## Used for:
- databases
- known number of pods

# HEADLESS 
> does not have IP for cluster
> get all IP of your pods using Cluster DNS
> ClusterIP, headless

kubectl apply -f headless.yaml
k exec -it toolbox -- bash
nslookup;
dig app.default.svc.cluster.local A
dig app-headles.default.svc.cluster.local A
