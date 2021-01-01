import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# TODO: Test for expected apt-key
# def test_apt_key(host):
#     apt_key = host.run('APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1 \
#         apt-key list --list-signatures | \
#             grep -q DA418C88A3219F7B')

#     assert apt_key.result == 'exit_status=0'


def test_apt_repo(host):
    apt_repo = host.file
    (' /etc/apt/sources.list.d/apt_releases_hashicorp_com.list')

    assert apt_repo.exists
    assert apt_repo.is_file
