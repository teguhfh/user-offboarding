
### 1 - Credential Type LDAP


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


### 2 - Credential Type m365


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




### 3 - Credential Type google workspace


Input configuration


```
fields:
  - id: gws_service_account_json
    type: string
    label: Service Account JSON Key
    secret: true
    multiline: true
    help_text: "Paste the full contents of the service account JSON key file"
  - id: gws_admin_email
    type: string
    label: Admin Email (for impersonation)
    help_text: "Super admin email that the service account will impersonate"
required:
  - gws_service_account_json
  - gws_admin_email
```


Injector configuration
```
file:
  template: "{{ gws_service_account_json }}"
extra_vars:
  gws_admin_email: "{{ gws_admin_email }}"
  gws_service_account_key_path: "{{ tower.filename }}"
```




### 4 - Credential Type Gitlab


Input configuration


```
fields:
  - id: gitlab_url
    type: string
    label: GitLab URL
    help_text: "Base URL of your GitLab instance, e.g. https://gitlab.internal.domain"
  - id: gitlab_admin_token
    type: string
    label: Admin Access Token
    secret: true
    help_text: "Personal Access Token with 'api' scope and admin privileges"
required:
  - gitlab_url
  - gitlab_admin_token
```


Injector configuration
```
extra_vars:
  gitlab_url: "{{ gitlab_url }}"
  gitlab_admin_token: "{{ gitlab_admin_token }}"

```
