import os
from re import search
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_kubectl_krew(host, AnsibleVars):
    # Confirm that Krew is installed
    krew_bin_path = AnsibleVars['krew_bin_path']
    cmd = host.run(f"{krew_bin_path} version")
    assert cmd.rc == 0

    cmd = host.run(f"{krew_bin_path} list")
    print(AnsibleVars)
    krew_plugins = AnsibleVars['krew_plugins']
    
    # Confirm Plugins are present    
    for plugin in krew_plugins:
        assert search(plugin, cmd.stdout) != None
