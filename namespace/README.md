# NAMESPACE
> split workgroups to smaller logical resources.
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

