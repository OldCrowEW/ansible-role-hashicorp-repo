import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rhel_repo(host):
    rhel_repo = host.file('/etc/yum.repos.d/hashicorp.repo')

    assert rhel_repo.exists
    assert rhel_repo.is_file
