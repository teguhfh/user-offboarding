
### Credential Type LDAP


Input configuration


```
fields:
  - id: ldap_server_uri
    type: string
    label: LDAP Server URI
    help_text: e.g. ldaps://192.168.222.29:636
  - id: ldap_bind_dn
    type: string
    label: Bind DN
  - id: ldap_bind_password
    type: string
    label: Bind Password
    secret: true
required:
  - ldap_server_uri
  - ldap_bind_dn
  - ldap_bind_password

```


Injector configuration
```
extra_vars:
  ldap_bind_dn: '{{ ldap_bind_dn }}'
  ldap_server_uri: '{{ ldap_server_uri }}'
  ldap_bind_password: '{{ ldap_bind_password }}'

```


### Credential Type m365


Input configuration


```
fields:
  - id: m365_tenant_id
    type: string
    label: Tenant ID
    help_text: Directory (tenant) ID from Azure App Registration
  - id: m365_client_id
    type: string
    label: Client ID
    help_text: Application (client) ID from Azure App Registration
  - id: m365_client_secret
    type: string
    label: Client Secret
    secret: true
    help_text: Client secret value generated in Certificates & secrets
required:
  - m365_tenant_id
  - m365_client_id
  - m365_client_secret
```


Injector configuration
```
extra_vars:
  m365_client_id: '{{ m365_client_id }}'
  m365_tenant_id: '{{ m365_tenant_id }}'
  m365_client_secret: '{{ m365_client_secret }}'

```
