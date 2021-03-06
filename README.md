# Role Name

Ansible role to deploy [RedELK](https://github.com/outflanknl/RedELK/) server components.

## Requirements

There is no specific requirement for this module.

## Role Variables

The following variables can be modified:

| Variable                        | Description                                                                                                                                                                  | Default value                      |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `es_version`                    | Elastic version                                                                                                                                                              | `7.9.2`                            |
| `es_elastic_password`           | ElasticSearch users                                                                                                                                                          | `elastic`                          |
| `es_logstash_system_password`   | ElasticSearch `logstash_system` user's password                                                                                                                              | `logstash_system`                  |
| `es_kibana_password`            | ElasticSearch `kibana` user's password                                                                                                                                       | `kibana`                           |
| `es_redelk_user`                | ElasticSearch RedELK username                                                                                                                                                | `redelk`                           |
| `es_redelk_password`            | ElasticSearch RedELK user's password                                                                                                                                         | `redelk`                           |
| `es_redelk_ingest_password`     |                                                                                                                                                                              | `redelk`                           |
| `es_kibana_encryptionKey`       | Kibana encryption key (32 char alphanumeric)                                                                                                                                 | `sLOVUK5MLv0VDhKsMlQcjgAaSMLXLLVy` |
| `optsec_dir`                    | Base directory for components install (where customer data will be stored) - allows to store on an encrypted partition/disk                                                  | `/opt`                             |
| `redelk_user`                   | RedELK SSH username (used to sync data between RedELK monitoring server and the clients)                                                                                     | `redelk`                           |
| `ssh_keys_path`                 | Local path to store ssh keys                                                                                                                                                 | `ssh_keys`                         |
| `redelk_cert_path`              | Local path to store RedELK certificates                                                                                                                                      | `certificates/redelk`              |
| `redelk_repo_path`              | Local path to the RedELK git repository. will be cloned if doesn't exist                                                                                                     | `RedELK`                           |
| `redelk_repo`                   | RedELK docker image repository                                                                                                                                               | `outflanknl`                       |
| `redelk_version`                | RedELK version to install (ignored if the git repository defined in `redelk_repo_path` is already cloned)                                                                    | `maindev`                          |
| `redelk_install_type`           | (`full` or `limited`) If `full`, Jupyter notebooks and BloodHound/Neo4J will be installed as well                                                                            | `full`                             |
| `redelk_alarm_Verbosity`        |                                                                                                                                                                              | `0`                                |
| `redelk_alarm_interval`         |                                                                                                                                                                              | `3600`                             |
| `redelk_alarm_tempDir`          |                                                                                                                                                                              | `/tmp`                             |
| `customer_ips`                  | List of customer's IP addresses                                                                                                                                              | `[]`                               |
| `redteam_ips`                   | List of Red Team's IP addresses                                                                                                                                              | `[]`                               |
| `unknown_ips`                   | List of Unknown IP addresses                                                                                                                                                 | `[]`                               |
| `domains`                       | List of domain names used for the exercise                                                                                                                                   | `[]`                               |
| `redelk_client_connection_mode` | Sets how RedELK clients connects to filebeat `direct` (client connects to RedELK server IP directly) or `reverse` (reverse SSH tunnel is made from RedELK server to clients) | `reverse`                          |
| `monitor_hosts`                 | Set to true to support monitoring hosts (metricbeat, packetbeat, ...)                                                                                                        | `false`                            |
| `redelk_alarms`                 | Alarm configuration dict (cf. config.json in RedELK repo for possible options)                                                                                               | ``                                 |
| `redelk_notifications`          | Alarm notifications dict (cf. config.json in RedELK repo for possible options)                                                                                               | ``                                 |

## Dependencies

There is no specific dependency for this module.

## Example Playbook

```yaml
- name: Gather facts from all hosts
  hosts: all
  gather_facts: True

- name: Apply redelk-server role to monitoring server(s)
  hosts: monitoring
  gather_facts: True
  tags:
    - monitoring
  roles:
    - redelk-server
```

## License

BSD 3-Clause

## Author Information

Lorenzo Bernardi / [@fastlorenzo](https://twitter.com/fastlorenzo)
