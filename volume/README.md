## VOLUMES
> Persistent Volume Claim (size, access mode, storage class)
>> Persistent Volume (static) > minikube host path
>> Storage Class (dynamic) > AWS EBS, minikube host, GCE Persistent Disk

kubectl get pv
kubectl get pvc

## STORAGE CLASS

kubectl get storageclass


## USE Secrets and ConfigMap
> 2 options in specification of pod:
- configMap / secretName,
-  with items
>3 posibilites of volumeMounts:
- all data from volumes
- specific data from volumes
- subPath

Persis­ten­tVo­lum­eClaim (PVC) is a request for storage by a user.

Persis­ten­tVolume (PV) is a piece of storage in the cluster that has been provis­ioned by an admini­str­ator.