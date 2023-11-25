## build app for API to see environments.

# verify
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

# build & deploy to minikube
docker build --tag app:1.0.0 .
docker run -p 5000:5000 app:1.0.0
minikube image build -t app:1.0.0 .
minikube image ls

# run pod
kubectl apply -f config.yaml
kubectl port-forward pods/env-app 5000:5000

# check 
localhost:5000/pods/env-vars