














[root@host ~]# subscription-manager repos \
--enable ansible-automation-platform-2.6-for-rhel-9-x86_64-rpms


# login

podman login registry.redhat.io


[root@aap10 user-offboarding]# podman login aap10.mii.lab --tls-verify=false
Username: admin
Password:
Login Succeeded!
[root@aap10 user-offboarding]#

# login 

[root@aap10 user-offboarding]# podman login registry.redhat.io
Username: teguh.fihaiman@mii.co.id
Password:
Login Succeeded!





# build

local 
  135  ansible-builder build -t ee-offboarding:latest -v 2
  136  podman images
  137  podman run -it --rm ee-offboarding:latest bash
  138  podman images
  139  podman tag localhost/ee-offboarding:latest aap10.mii.lab/ee-offboarding:latest
  140  podman login aap10.mii.lab
  141  podman push aap10.mii.lab/ee-offboarding:latest


ansible-builder build -t ee-offboarding:1.0 -v 3


$ ansible-navigator run playbook-test.yml   --eei localhost/ee-offboarding:1.0 \                                                                                    --eei localhost/ee-offboarding:1.0 \
  --pp never \
  -m stdout


podman tag localhost/ee-offboarding:1.0 \
test-ansible.preprod-bjj.net/ee-offboarding:1.0


podman push test-ansible.preprod-bjj.net/ee-offboarding:1.0