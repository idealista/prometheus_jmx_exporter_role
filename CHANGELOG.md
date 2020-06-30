# prometheus_jmx_exporter_role changelog

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).


## [Unreleased](https://github.com/idealista/prometheus_jmx_exporter_role/tree/develop)
### Fixed
- *[#52](https://github.com/idealista/prometheus_jmx_exporter_role/issues/52) Fixed systemd unit file* @frantsao

## [2.1.1](https://github.com/idealista/prometheus_jmx_exporter_role/tree/2.1.1)
[Full Changelog](https://github.com/idealista/prometheus_jmx_exporter_role/compare/2.1.0...2.1.1)
### Fixed
- *[#48](https://github.com/idealista/prometheus_jmx_exporter_role/issues/48) Added service privateTmp option* @frantsao

## [2.1.0](https://github.com/idealista/prometheus_jmx_exporter_role/tree/2.1.0)
[Full Changelog](https://github.com/idealista/prometheus_jmx_exporter_role/compare/2.0.0...2.1.0)
### Added
- *[#44](https://github.com/idealista/prometheus_jmx_exporter_role/issues/44) Upgraded to ansible 2.9, molecule 3 and goss 0.3.11* @frantsao
- *[#44](https://github.com/idealista/prometheus_node_exporter_role/issues/44) Fixed systemd service configuration (changes default behaviour)* @frantsao

## [2.0.0](https://github.com/idealista/prometheus_jmx_exporter_role/tree/2.0.0)
[Full Changelog](https://github.com/idealista/prometheus_jmx_exporter_role/compare/1.5.1...2.0.0)
### Added
- *[#29](https://github.com/idealista/prometheus_jmx_exporter_role/issues/29) Add way to provide custom configuration* @jnogol

### Changed
- *[#30](https://github.com/idealista/prometheus_jmx_exporter_role/issues/30) Migrate tests to Molecule v2.19 and Goss v0.3.6. Ansible minimum version 2.4.5.0* @jnogol

### Deleted
- *Delete logrotate configuration* @jnogol

## [1.5.1](https://github.com/idealista/prometheus_jmx_exporter_role/tree/1.5.1)
[Full Changelog](https://github.com/idealista/prometheus_jmx_exporter_role/compare/1.5.0...1.5.1)
### Fixed
- *[#26](https://github.com/idealista/prometheus_jmx_exporter_role/issues/26) Group variable is not used when skeleton paths are created* @sorobon

## [1.5.0](https://github.com/idealista/prometheus_jmx_exporter_role/tree/1.5.0)
[Full Changelog](https://github.com/idealista/prometheus_jmx_exporter_role/compare/1.4.0...1.5.0)
### Added
- *[#23](https://github.com/idealista/prometheus_jmx_exporter_role/issues/23) JMX Exporter classpath is now configurable* @dortegau

## [1.4.0](https://github.com/idealista/prometheus_jmx_exporter_role/tree/1.4.0)
[Full Changelog](https://github.com/idealista/prometheus_jmx_exporter_role/compare/1.3.1...1.4.0)
### Added
- *[#19](https://github.com/idealista/prometheus_jmx_exporter_role/issues/19) Upgrade to install latest jmx_exporter version (0.2.0)* @dortegau

## [1.3.1](https://github.com/idealista/prometheus_jmx_exporter_role/tree/1.3.1)
[Full Changelog](https://github.com/idealista/prometheus_jmx_exporter_role/compare/1.3.0...1.3.1)
### Fixed
- *[#15](https://github.com/idealista/prometheus_jmx_exporter_role/issues/15) Fix logrotate script problem* @jnogol

### Added
- *Use Idealista's Java-Debian-Ansible Docker image* @jnogol
- *Add .github folder* @jnogol

## [1.3.0](https://github.com/idealista/prometheus_jmx_exporter_role/tree/1.3.0)
[Full Changelog](https://github.com/idealista/prometheus_jmx_exporter_role/compare/1.2.0...1.3.0)
### Added
- *[#7](https://github.com/idealista/prometheus_jmx_exporter_role/issues/7) Add TravisCI and Ansible Galaxy integration* @jnogol
- *[#8](https://github.com/idealista/prometheus_jmx_exporter_role/issues/8) Add debug with Vagrant and Jconsole* @jnogol
- *[#12](https://github.com/idealista/prometheus_jmx_exporter_role/issues/12) Copy only one config file to the exporter in case there are more than one* @jnogol

## [1.2.0](https://github.com/idealista/prometheus_jmx_exporter_role/tree/1.2.0)
[Full Changelog](https://github.com/idealista/prometheus_jmx_exporter_role/compare/1.1.1...1.2.0)
### Added
- *[#1](https://github.com/idealista/prometheus_jmx_exporter_role/issues/1) Add xmx/xms params* @jmonterrubio

## [1.1.1](https://github.com/idealista/prometheus_jmx_exporter_role/tree/1.1.1)
[Full Changelog](https://github.com/idealista/prometheus_jmx_exporter_role/compare/1.1.0...1.1.1)
### Added
- *Exporter refactor* @jmonterrubio

## [1.1.0](https://github.com/idealista/prometheus_jmx_exporter_role/tree/1.1.0)
### Added
- *Using Systemd, decreasing the number of metrics generated for Java & Tomcat*
