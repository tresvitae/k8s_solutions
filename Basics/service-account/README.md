# SERIVCE ACCOUNT
> RBAC for resources
> identity for processes that run in a Pod, and maps to a ServiceAccount object. 

kubectl get sa
kubectl create token test-sa # Create JSON token

kubectl apply -f service-account.yaml
kubectl get secret test-sa-secret -o jsonpath='{.data.token}' | base64 --decode

kubectl exec -it -- bash
cat /var/run/secrets/kubernetes.io/serviceaccount/token
./kubeapi.sh /api/v1


# RBCA
> authorization and authentication of resources in Kubernetes
> Role + RoleBinding for specified namespace
> Role + RoleBinding  NOT possible to create
> ClusterRole + RoleBinding to create one role in selected namespaces at once
> Role + ClusterRoleBinding  NOT possible to create
> ClusterRole + ClusterRoleBinding to create role for hole cluster

kubectl apply -f rbac.yaml
k get role
k get rolebinding
k get clusterrole

./kubeapi.sh /api/v1/namespaces/default/pods

