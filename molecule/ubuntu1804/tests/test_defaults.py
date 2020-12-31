import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rhel_repo(host):
    apt_repo = host.file
    (' /etc/apt/sources.list.d/apt_releases_hashicorp_com.list')

    assert apt_repo.exists
    assert apt_repo.is_file
