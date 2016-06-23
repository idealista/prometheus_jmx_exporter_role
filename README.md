# Prometheus JMX exporter role

Ansible role to install and manage JXM exporter by Prometheus

You can add the exporter as java agent on the running app that expose jmx, you can use it for tomcat, kafka, zookeper, spring boot metrics... pretty much everything running under jvm

Tomcat example:

```yaml
jmx_apps:
  tomcat:
    appName: idealista-tomcat
    file: "{{ tomcat_classpath_path }}"
      block: |
        JAVA_OPTS="$JAVA_OPTS -javaagent:{{ jmx_exporter_root_dir }}/jmx_prometheus_javaagent-{{ jmx_exporter_version }}.jar=9110:{{ jmx_exporter_root_dir }}/tomcat.yml"
      owner: "{{ tomcat_user }}"
      group: "{{ tomcat_group }}"
```

This way you can set the exporter metrics on 9110 port with tomcat.yml options and rules. Check options, rules or default confg files for other apps on jmx_exporter github repo https://github.com/prometheus/jmx_exporter.
