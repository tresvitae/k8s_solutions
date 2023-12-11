# HELM
> package manager for Kubernetes
> distubute yaml files though privete/pubic repositories
> versioning

artifacthub.io
chartmuseum.com

> templating
{{ .Values.service.name }} from values.yaml

## Install
helm upgrade -i podinfo oci://ghcr.io/stefanprodan/charts/podinfo

## Download and modify
helm pull oci://registry-1.docker.io/bitnamicharts/mysql --untar
made changes, eg. in values.yaml
helm template mysql-db ../mysql

helm diff revision podinfo
### Revision with previous version
helm plugin install https://github.com/databus23/helm-diff
helm diff revision podinfo NO_VERSION

helm rollback podinfo NO_VERSION

helm list
helm delete mysql-db

## Wordpress examples with own changes:
mkcert --key-file key.pem --cert-file cert.pem wordpress.127.0.0.1.nip.io
kubectl create secret tls blog-tls --key key.pem --cert cert.pem

helm upgrade -i blog oci://registry-1.docker.io/bitnamicharts/wordpress --version=16.1.33 --values=values.yaml

minikube tunnel