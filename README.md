Ansible Krew
=========

Ansible Role for installing the Kubectl Krew tool and managing Kubernetes packages

Requirements
------------

N/A

Role Variables
--------------

Role Variables:
- krew_bin_path: "optional string:"
- krew_user: "string: name of user to have plugins installed"
- krew_version: "string: version of krew to install. 'latest' can be used to choose the current version"
- krew_plugins: "list: all krew plugins to install"

Examples:
```yaml
krew_bin_path: "/usr/local/bin/kubectl-krew"
krew_user: mwasher
krew_version: latest
krew_plugins: 
  - "strace"
```

Dependencies
------------

- geerlingguy.guy : `git` is required and may need to be installed 


Example Playbook
----------------
```yaml
- name: Ensure Krew and Plugins are present
  hosts: all
  roles:
    - role: geerlingguy.git
  tasks:
  - include_role:
      name: michaelwasher.krew
    vars:
      krew_user: mwasher
      krew_version: "v0.4.2"
      krew_plugins: 
      - "strace"
```

License
-------

Apache2.0

Author Information
------------------

Name: Michael Washer
[Website](michael-washer.dev) [LinkedIn](https://www.linkedin.com/in/michael-washer) [Github](https://github.com/MichaelWasher)
