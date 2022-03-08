# Role Name

Ansible role to deploy [RedELK](https://github.com/outflanknl/RedELK/) server components.

## Requirements

There is no specific requirement for this module.

## Role Variables

The following variables can be modified:

| Variable | Description | Default value |
|----------|-------------|---------------|
| `es_version` | Elastic version | `7.16.3` |
| `es_elastic_password` | ElasticSearch users | `elastic` |
| `es_logstash_system_password` | ElasticSearch `logstash_system` user's password | `logstash_system` |
| `es_kibana_password` | ElasticSearch `kibana` user's password | `kibana` |
| `es_redelk_user` | ElasticSearch RedELK username | `redelk` |
| `es_redelk_password` | ElasticSearch RedELK user's password | `redelk` |
| `es_redelk_ingest_password` |  | `redelk` |
| `es_kibana_encryptionKey` | Kibana encryption key (32 char alphanumeric) | `sLOVUK5MLv0VDhKsMlQcjgAaSMLXLLVy` |
| `neo4j_password` | Neo4J password (user: neo4j) | `BloodHound` |
| `optsec_dir` | Base directory for components install (where customer data will be stored) - allows to store on an encrypted partition/disk | `/opt` |
| `docker_dir` | Docker directory | `/var/lib/docker` |
| `redelk_user` | RedELK SSH username (used to sync data between RedELK monitoring server and the clients) | `redelk` |
| `external_domain` | External domain name to expose RedELK interface on. Will also be used to request Let's Encypt certificate | `localhost` |
| `le_email` | Let's Encrypt email address | `` |
| `le_enable` | Use Let's Encrypt to request certificate for external_domain | `true` |
| `ssh_keys_path` | Local path to store ssh keys | `ssh_keys` |
| `redelk_cert_path` | Local path to store RedELK certificates | `certificates/redelk` |
| `certs_dir_nginx` | Path to folder containing certificates in Nginx container | `/etc/nginx/certs` |
| `certs_dir_nginx_local` |  | `./mounts/certbot/conf/live/localhost` |
| `certs_dir_nginx_ca` | Path to folder containing the CA certificate in Nginx container | `/etc/nginx/ca_certs` |
| `certs_dir_nginx_ca_local` | Local path to folder containing certificates. Replace `localhost` with the same value as `external_domain`
Local path to folder containing the CA certificate | `./mounts/certs/ca` |
| `tls_nginx_crt_path` | Path to the certificate file in Nginx container | `/etc/letsencrypt/live/{{ external_domain }}/fullchain.pem` |
| `tls_nginx_key_path` | Path to the private key file in Nginx container | `/etc/letsencrypt/live/{{ external_domain }}/privkey.pem` |
| `tls_nginx_ca_path` | Path to the CA file in Nginx container | `/etc/nginx/ca_certs/ca.crt` |
| `redelk_repo_path` | Local path to the RedELK git repository. will be cloned if doesn't exist | `RedELK` |
| `redelk_repo` | RedELK docker image repository | `outflanknl` |
| `redelk_version` | RedELK version to install (ignored if the git repository defined in `redelk_repo_path` is already cloned) | `master` |
| `redelk_install_type` | (`full` or `limited`) If `full`, Jupyter notebooks and BloodHound/Neo4J will be installed as well | `full` |
| `redelk_loglevel` | Log level of the RedELK daemon. Default `WARNING` | `WARNING` |
| `redelk_alarm_interval` |  | `3600` |
| `redelk_alarm_tempDir` |  | `/tmp` |
| `customer_ips` | List of customer's IP addresses | `[]` |
| `redteam_ips` | List of Red Team's IP addresses | `[]` |
| `unknown_ips` | List of Unknown IP addresses | `[]` |
| `domains` | List of domain names used for the exercise | `[]` |
| `redelk_client_connection_mode` | Sets how RedELK clients connects to filebeat `direct` (client connects to RedELK server IP directly) or `reverse` (reverse SSH tunnel is made from RedELK server to clients) | `reverse` |
| `monitor_hosts` | Set to true to support monitoring hosts (metricbeat, packetbeat, ...) | `false` |
| `redelk_alarms` | Alarm configuration dict (cf. config.json in RedELK repo for possible options) | `` |
| `  alarm_dummy` |  | `` |
| `    enabled` |  | `false` |
| `    interval` |  | `300` |
| `  alarm_filehash` |  | `` |
| `    enabled` |  | `true` |
| `    vt_api_key` |  | `<<INSERT_API_KEY>>` |
| `    ibm_basic_auth` |  | `Basic <<REPLACE>>` |
| `    ha_api_key` |  | `<<INSERT_API_KEY>>` |
| `    interval` |  | `360` |
| `  alarm_httptraffic` |  | `` |
| `    enabled` |  | `true` |
| `    interval` |  | `310` |
| `    notify_interval` |  | `86400  # Only notify on the same IP hit every 24h by default` |
| `  alarm_useragent` |  | `` |
| `    enabled` |  | `true` |
| `    interval` |  | `320` |
| `redelk_notifications` | Alarm notifications dict (cf. config.json in RedELK repo for possible options) | `` |
| `  email` |  | `` |
| `    enabled` |  | `false` |
| `    smtp` |  | `` |
| `      host` |  | `mail.bernardi.be` |
| `      port` |  | `587` |
| `      login` |  | `redelk@bernardi.be` |
| `      pass` |  | `<<SMTP_PASS>>` |
| `    from` |  | `redelk@bernardi.be` |
| `    to` |  | `` |
| `      - "redelk@bernardi.be"` |  | `- "redelk@bernardi.be` |
| `  msteams` |  | `` |
| `    enabled` |  | `false` |
| `    webhook_url` |  | `` |
| `  slack` |  | `` |
| `    enabled` |  | `false` |
| `    webhook_url` |  | `` |
| `redelk_enrich` | Enrichment scripts dict (cf. config.json in RedELK repo for possible options) | `` |
| `  enrich_csbeacon` |  | `` |
| `    enabled` |  | `true` |
| `    interval` |  | `300` |
| `  enrich_greynoise` |  | `` |
| `    enabled` |  | `true` |
| `    interval` |  | `310` |
| `    cache` |  | `86400` |
| `  enrich_tor` |  | `` |
| `    enabled` |  | `true` |
| `    interval` |  | `360` |
| `    cache` |  | `360` |
| `  enrich_iplists` |  | `` |
| `    enabled` |  | `true` |
| `    interval` |  | `330` |
| `  enrich_synciplists` |  | `` |
| `    enabled` |  | `true` |
| `    interval` |  | `360` |

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
