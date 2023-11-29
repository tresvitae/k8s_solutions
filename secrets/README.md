## SECRETS
> store secrets values
> use ConfigMap for common values

## Imperative
kubectl get secrets
kubect create secret generic NAME --from-file=credentials.env
                                  --from-literal=key1=supersecret
kubectl get secret NAME -o json | jq '.data.NAME'
echo Y3l0cnluYQ== | base64 -d

## Declarative
kubectl apply -f secrets.yaml
kubectl get secret app-secrets -o json | jq '.data'

# Types of secrets
1. opaque - generic
2. (docker config secrets) kubernetes.io/dockercfg - access data for Docker Iamge Registry
3. kubernetes.io/service-account-token - store token secrets
4. kubernetes.io/tls - certificates
5. kubernetes.io/basic-auth - store username and password
6. kubernetes.io/ssh-auth
7. bootstrap.kubernetes.io/token - adding clusters/nodes
