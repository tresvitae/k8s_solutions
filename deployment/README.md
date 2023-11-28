## DEPLOYMENT
> Kind of controller of k8s pods. Monitoring stan of contoller to keep state of pods as desired, eg. 5 running pods if one of them break, recreate it. 

# get deployment
kubectl get deployment
kubectl get pods

# destroy one pod
kubectl delete pod nginx-deployment-123456789


## ReplicaSet

> In structure in Worker Node looks:
![alt text](https://www.goglides.dev/images/DxLD59TaM3uCYYvv91BxJV803XHWXI5APfkcYOdRvlQ/w:880/mb:500000/ar:1/aHR0cHM6Ly93d3ct/Z29nbGlkZXMtZGV2/LnMzLmFtYXpvbmF3/cy5jb20vdXBsb2Fk/cy9hcnRpY2xlcy93/azI5d2ptMWR2Nng5/NHdxcWF5bi5wbmc)

# example
kubectl get rs
kubectl get pods -w
kubectl set image deployment/nginx-deployment nginx=nginx:1.25.0
kubectl get rs