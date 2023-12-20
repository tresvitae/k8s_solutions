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

