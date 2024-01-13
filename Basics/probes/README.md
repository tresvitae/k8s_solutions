# PROBES
> health checks
> check if pod is healthy and works as desired

## 3 types:
- Readiness probe - check if pod is ready and start handling traffic. Used for Service engine
- Liveness probe - check if pod is still running
- Startup probe - for long running startup pods used with readiness and liveness that tells them to do not work until startup probe will give them signal.

## Handlers
- Exec
- tcpSocket
- httpGet
- gRPC