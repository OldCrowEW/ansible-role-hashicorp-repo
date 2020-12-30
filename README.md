# ansible-role-hashicorp-repo

![Workflow Molecule Badge](https://github.com/OldCrowEW/ansible-role-hashicorp-repo/workflows/Molecule%20Test/badge.svg?event=push)


This role deploys the Official Hashicorp Linux Repos. Expected usage of this role is via an Ansible dependencies call:

    dependencies:
        - oldcrowew.hashicorp_repo


## Role Variables
This role is written in a way that all tasks are flexible via variables found in [defaults/main.yml](https://github.com/OldCrowEW/ansible-role-hashicorp-repo/blob/master/defaults/main.yml)

## Requirements
None.

## License

BSD

## Author Information

John Favorite