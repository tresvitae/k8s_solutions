## PODS COMMUNICATION
# get pods IP and check connection
kubectl get pods -o wide
kubectl -it exec toolbox -- bash
curl http://10.244.0.46:5000

http http://10-244-0-46.default.pod.cluster.local:5000/pods/env-vars