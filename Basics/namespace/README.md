# NAMESPACE
> split workgroups to smaller logical resources.
> Kubernetes supports multiple virtual clusters backed by the same physical cluster. These virtual clusters are called namesp­aces.
kubectl get namespace
kubectl get pods --all-namespaces
kubectl get pods -n staging

metadata:
  namespace: staging

## Change working namespace
kubectl config set-context --current --namespace=dev
kubectl config view | grep namespace

# External tools:
![use kns tool](https://github.com/ahmetb/kubectx)
![use ohmyz.sh](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/kube-ps1)
![use theme for Zsh](https://github.com/romkatv/powerlevel10k)

## K8s communication schemes between namespaces
[pod-ip].[namespace].pod.cluster.local
[svc-name].[namespace].svc.cluster.local
[port-name].[port-protocol].[svc].[namespace].svc.cluster.local

kubectl apply -f ns-communication.yaml
kubectl exec -it toolbox -n tools -- bash
http http://app.development.svc.cluster.local:8080/pods/env-vars