![Logo](logo.gif)

[![Build Status](https://travis-ci.org/idealista/prometheus_jmx_exporter_role.png)](https://travis-ci.org/idealista/prometheus_jmx_exporter_role)

# Prometheus JMX Exporter Ansible role

This ansible role installs a Prometheus Node Exporter in a debian environment.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install an [Prometheus JMX Exporter](https://github.com/prometheus/jmx_exporter) server in a Debian system.

*Note:* Beginning with the 3.0 version, the default behaviour is the service sending logs to systemd's journal instead to a log file. You can change it modifying the necessary ansible vars (see defaults/main.yml)
### Prerequisities

Ansible 2.9.x.x version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [vagrant-hostmanager](https://github.com/devopsgroup-io/vagrant-hostmanager)) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```yml
- src: idealista.prometheus_jmx_exporter_role
  version: 2.1.0
  name: prometheus_jmx_exporter
```

Install the role with ansible-galaxy command:

```sh
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```yml
---
- hosts: someserver
  roles:
    - role: prometheus_jmx_exporter
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

### Providing custom configuration

Starting from role version 2.x.x, in order to provide custom JMX Exporter configuration, set `jmx_exporter_config_template_path` to the template in your playbook that is the configuration file. For example: 

```yml
jmx_exporter_config_template_path: "{{ playbook_dir }}/templates/jmx_exporter/config/jmx_config.yml"
```

In previous versions, this variable pointed to a **folder** instead of a **file**. If you are using this role since version 1.x, you may check our [migration guide](https://github.com/idealista/prometheus_jmx_exporter_role/wiki#v1x-to-v2-migration-guide)

## Testing

### Install dependencies

```sh
$ pipenv sync
```

For more information read the [pipenv docs](https://docs.pipenv.org/).

### Testing

```sh
$ pipenv run molecule test 
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.9.9-green.svg)
![Molecule](https://img.shields.io/badge/molecule-3.0.4-green.svg)
![Goss](https://img.shields.io/badge/goss-0.3.11-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/prometheus_jmx_exporter_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/prometheus_jmx_exporter_role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
