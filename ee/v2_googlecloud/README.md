








[admin01@devbsqdciansac01 v2_googlecloud]$ podman login devbsqdcianspg01.bjj.lan --tls-verify=false
Authenticating with existing credentials for devbsqdcianspg01.bjj.lan
Existing credentials are valid. Already logged in to devbsqdcianspg01.bjj.lan
[admin01@devbsqdciansac01 v2_googlecloud]$





VERSION="2.0"

ansible-builder build -t ee-offboarding:${VERSION} -v 3
podman tag ee-offboarding:${VERSION} ee-offboarding:latest

podman tag ee-offboarding:${VERSION} devbsqdcianspg01.bjj.lan/ee-offboarding:${VERSION}
podman tag ee-offboarding:latest devbsqdcianspg01.bjj.lan/ee-offboarding:latest

podman push devbsqdcianspg01.bjj.lan/ee-offboarding:${VERSION} --tls-verify=false
podman push devbsqdcianspg01.bjj.lan/ee-offboarding:latest --tls-verify=false

podman push devbsqdcianspg01.bjj.lan/ee-offboarding:1.0 --tls-verify=false