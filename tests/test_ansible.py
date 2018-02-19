import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/jmxexporter.yml")["ansible_facts"]


def test_jmx_exporter_user(User, Group, AnsibleDefaults):
    assert User(AnsibleDefaults["jmx_exporter_user"]).exists
    assert Group(AnsibleDefaults["jmx_exporter_group"]).exists
    assert User(AnsibleDefaults["jmx_exporter_user"]).group == AnsibleDefaults["jmx_exporter_group"]


def test_jmx_exporter_conf(File, AnsibleDefaults):
    jmx_exporter_config = File(AnsibleDefaults["jmx_exporter_conf_path"] + "/jmx_config.yml")
    assert jmx_exporter_config.is_file
    assert jmx_exporter_config.group == AnsibleDefaults["jmx_exporter_group"]
    assert jmx_exporter_config.user == AnsibleDefaults["jmx_exporter_user"]


def test_jmx_exporter_service(File, Service, Socket, AnsibleVars):
    assert File("/etc/systemd/system/jmx_exporter.service").exists
    port = AnsibleVars["jmx_exporter_port"]
    jmx_enabled = AnsibleVars["jmx_exporter_service_enabled"]
    jmx_state = AnsibleVars["jmx_exporter_service_state"]
    if not jmx_enabled:
        assert not Service("jmx_exporter").is_enabled
    else:
        assert Service("jmx_exporter").is_enabled
    if jmx_state in ["started", "restarted", "reloaded"]:
        assert Service("jmx_exporter").is_running
        assert Socket("tcp://:::" + str(port)).is_listening or Socket("tcp://0.0.0.0:" + str(port)).is_listening
    else:
        assert not Service("jmx_exporter").is_running
        assert not Socket("tcp://:::" + str(port)).is_listening or Socket("tcp://0.0.0.0:" + str(port)).is_listening
