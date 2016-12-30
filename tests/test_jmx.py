import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVarEnabled(Ansible):
    return Ansible("debug", "msg={{ jmx_exporter_enabled }}")["msg"]


@pytest.fixture()
def AnsibleVarState(Ansible):
    return Ansible("debug", "msg={{ jmx_exporter_state }}")["msg"]


def test_jmx_exporter_repo(File, AnsibleDefaults):
    sources = File("/etc/apt/sources.list.d/" + AnsibleDefaults["jmx_exporter_repo_file"] + ".list")
    assert sources.contains(AnsibleDefaults["jmx_exporter_repo"])


def test_jmx_exporter_package(Package, AnsibleDefaults):
    jmx_exporter = Package("jmx_prometheus_httpserver")
    assert jmx_exporter.is_installed


def test_jmx_exporter_user(User, Group, AnsibleDefaults):
    assert User(AnsibleDefaults["jmx_exporter_user"]).exists
    assert Group(AnsibleDefaults["jmx_exporter_group"]).exists
    assert User(AnsibleDefaults["jmx_exporter_user"]).group == AnsibleDefaults["jmx_exporter_group"]
    assert User(AnsibleDefaults["jmx_exporter_user"]).home == "/bin/false"


def test_jmx_exporter_conf(File, AnsibleDefaults):
    jmx_exporter_config = File(AnsibleDefaults["jmx_exporter_config_file"])
    assert jmx_exporter_config.is_file
    assert jmx_exporter_config.group == AnsibleDefaults["jmx_exporter_group"]
    assert jmx_exporter_config.user == AnsibleDefaults["jmx_exporter_user"]


def test_jmx_exporter_service(File, Service, Socket, AnsibleDefaults):
    assert File("/etc/systemd/system/jmx_exporter.service").exists
    if AnsibleVarEnabled == "no":
        assert not Service("jmx_exporter").is_enabled
        assert not Service("jmx_exporter").is_running
        assert not Socket("tcp:0.0.0.0:9110").is_listening
    elif AnsibleVarEnabled == "yes":
        assert Service("jmx_exporter").is_enabled
        if AnsibleVarState in ["started", "restarted", "reloaded"]:
            assert Service("jmx_exporter").is_running
            assert Socket("tcp:0.0.0.0:9110").is_listening
        else:
            assert not Service("jmx_exporter").is_running
            assert not Socket("tcp:0.0.0.0:9110").is_listening
