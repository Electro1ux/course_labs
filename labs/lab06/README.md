<div align="center">
<h1><a id="intro">Лабораторная работа №6</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Зуйков_И._О.-8b9aff" alt="Contributor Badge"></a></div>

## Задание

- [x] 1. Необходимо установить `Docker Engine` для Linux

```bash
$ sudo apt-get update

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab06$ sudo apt-get update
[sudo] password for ris:
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [127 kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [3164 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1245 kB]
Get:6 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]
Hit:7 https://deb.nodesource.com/node_22.x nodistro InRelease
Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease
Get:9 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [2903 kB]
Get:10 http://security.ubuntu.com/ubuntu jammy-security/main amd64 c-n-f Metadata [14.1 kB]
Get:11 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1008 kB]
Get:12 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 c-n-f Metadata [22.4 kB]
Fetched 8741 kB in 11s (774 kB/s)
Reading package lists... Done

$ sudo apt-get install -y docker.io

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab06$ sudo apt-get install -y docker.io
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base pigz runc ubuntu-fan
Suggested packages:
  ifupdown aufs-tools btrfs-progs cgroupfs-mount | cgroup-lite debootstrap docker-buildx docker-compose-v2
  docker-doc rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io pigz runc ubuntu-fan
0 upgraded, 8 newly installed, 0 to remove and 55 not upgraded.
Need to get 76.3 MB of archives.
After this operation, 289 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 pigz amd64 2.6-1 [63.6 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy/main amd64 bridge-utils amd64 1.7-1ubuntu3 [34.4 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 runc amd64 1.3.3-0ubuntu1~22.04.3 [8857 kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 containerd amd64 1.7.28-0ubuntu1~22.04.1 [38.5 MB]
Get:5 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 dns-root-data all 2024071801~ubuntu0.22.04.1 [6132 B]
Get:6 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 dnsmasq-base amd64 2.90-0ubuntu0.22.04.1 [374 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 docker.io amd64 28.2.2-0ubuntu1~22.04.1 [28.4 MB]
Get:8 http://archive.ubuntu.com/ubuntu jammy/universe amd64 ubuntu-fan all 0.12.16 [35.2 kB]
Fetched 76.3 MB in 3s (25.4 MB/s)
Preconfiguring packages ...
Selecting previously unselected package pigz.
(Reading database ... 91120 files and directories currently installed.)
Preparing to unpack .../0-pigz_2.6-1_amd64.deb ...
Unpacking pigz (2.6-1) ...
Selecting previously unselected package bridge-utils.
Preparing to unpack .../1-bridge-utils_1.7-1ubuntu3_amd64.deb ...
Unpacking bridge-utils (1.7-1ubuntu3) ...
Selecting previously unselected package runc.
Preparing to unpack .../2-runc_1.3.3-0ubuntu1~22.04.3_amd64.deb ...
Unpacking runc (1.3.3-0ubuntu1~22.04.3) ...
Selecting previously unselected package containerd.
Preparing to unpack .../3-containerd_1.7.28-0ubuntu1~22.04.1_amd64.deb ...
Unpacking containerd (1.7.28-0ubuntu1~22.04.1) ...
Selecting previously unselected package dns-root-data.
Preparing to unpack .../4-dns-root-data_2024071801~ubuntu0.22.04.1_all.deb ...
Unpacking dns-root-data (2024071801~ubuntu0.22.04.1) ...
Selecting previously unselected package dnsmasq-base.
Preparing to unpack .../5-dnsmasq-base_2.90-0ubuntu0.22.04.1_amd64.deb ...
Unpacking dnsmasq-base (2.90-0ubuntu0.22.04.1) ...
Selecting previously unselected package docker.io.
Preparing to unpack .../6-docker.io_28.2.2-0ubuntu1~22.04.1_amd64.deb ...
Unpacking docker.io (28.2.2-0ubuntu1~22.04.1) ...
Selecting previously unselected package ubuntu-fan.
Preparing to unpack .../7-ubuntu-fan_0.12.16_all.deb ...
Unpacking ubuntu-fan (0.12.16) ...
Setting up dnsmasq-base (2.90-0ubuntu0.22.04.1) ...
Setting up runc (1.3.3-0ubuntu1~22.04.3) ...
Setting up dns-root-data (2024071801~ubuntu0.22.04.1) ...
Setting up bridge-utils (1.7-1ubuntu3) ...
Setting up pigz (2.6-1) ...
Setting up containerd (1.7.28-0ubuntu1~22.04.1) ...
Created symlink /etc/systemd/system/multi-user.target.wants/containerd.service → /lib/systemd/system/containerd.service.
Setting up ubuntu-fan (0.12.16) ...
Created symlink /etc/systemd/system/multi-user.target.wants/ubuntu-fan.service → /lib/systemd/system/ubuntu-fan.service.
Setting up docker.io (28.2.2-0ubuntu1~22.04.1) ...
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /lib/systemd/system/docker.service.

$ sudo usermod -aG docker "$USER"
$ sudo systemctl start docker
$ docker pull docker/docker-bench-security

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab06$ docker pull docker/docker-bench-security
Using default tag: latest
latest: Pulling from docker/docker-bench-security
cd784148e348: Pull complete
48fe0d48816d: Pull complete
164e5e0f48c5: Pull complete
378ed37ea5ff: Pull complete
Digest: sha256:ddbdf4f86af4405da4a8a7b7cc62bb63bfeb75e85bf22d2ece70c204d7cfabb8
Status: Downloaded newer image for docker/docker-bench-security:latest
docker.io/docker/docker-bench-security:latest

```

- [x] 2. Проверьте работу докера и сделать скрипт `audit.sh` исполняемым
- [x] 3. Развернуть уязвимое приложение как отдельные стенды

```bash
$ docker compose up -d # основной web, app, postgres

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab06$ docker compose up -d
WARN[0000] /home/ris/course_labs/labs/lab06/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
[+] Running 24/24
 ✔ insecure-db Pulled                                                                                 11.2s
   ✔ 6fe79fe4410f Download complete                                                                    1.7s
   ✔ 3048a283a433 Download complete                                                                    1.9s
   ✔ 1074353eec0d Download complete                                                                    1.2s
   ✔ d2e5feb410e8 Download complete                                                                    1.7s
   ✔ feb143896d95 Download complete                                                                    3.9s
   ✔ 6bfb940eb824 Download complete                                                                    3.5s
   ✔ e76f2995a422 Download complete                                                                    3.9s
   ✔ 137ed19c6b80 Download complete                                                                    4.2s
   ✔ 9582264a43c0 Download complete                                                                    3.1s
   ✔ 97b8e529965a Download complete                                                                    6.1s
   ✔ d3a0dfeb7e38 Download complete                                                                    3.8s
 ✔ app Pulled                                                                                          7.0s
   ✔ dfee10dbf18a Download complete                                                                    2.2s
   ✔ bfff5caeedf0 Download complete                                                                    2.3s
   ✔ 9486ad61224d Download complete                                                                    1.1s
 ✔ vulnerable-web Pulled                                                                              10.3s
   ✔ d145d80cb745 Download complete                                                                    4.4s
   ✔ 567f84da6fbd Download complete                                                                    3.4s
   ✔ 0abf9e567266 Download complete                                                                    3.5s
   ✔ 33f95a0f3229 Download complete                                                                    3.4s
   ✔ da7c973d8b92 Download complete                                                                    0.8s
   ✔ 25f453064fd3 Download complete                                                                    5.0s
   ✔ 085c5e5aaa8e Download complete                                                                    3.4s
[+] Running 4/4
 ✔ Network lab06_default       Created                                                                 0.1s
 ✔ Container insecure-db       Started                                                                 3.6s
 ✔ Container vulnerable-app    Started                                                                 1.5s
 ✔ Container vulnerable-nginx  Started                                                                 2.0s

$ docker-compose -f dvulnerable-app.yml up -d # поверх для vulnerable-web, debug-shell
    -f # file
    up # создает и поднимает файлы из compose
    -d # фоновый режим
    
 ris@DESKTOP-HS8SF48:~/course_labs/labs/lab06$ docker compose -f docker-compose.yml -f vulnerable-app.yml up -d
WARN[0000] /home/ris/course_labs/labs/lab06/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
WARN[0000] /home/ris/course_labs/labs/lab06/vulnerable-app.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
[+] Running 8/8
 ✔ vulnerable-web Pulled                                                                               7.0s
   ✔ 964234ddf75f Download complete                                                                    1.2s
   ✔ f7f0a5b0f147 Download complete                                                                    0.8s
   ✔ 589066960983 Download complete                                                                    2.6s
   ✔ 2e964620d7d0 Download complete                                                                    1.3s
   ✔ 24ca5634560a Download complete                                                                    1.0s
   ✔ 7674eff4effe Download complete                                                                    0.5s
 ✔ debug-shell Pulled                                                                                  3.8s
[+] Running 7/7
 ✔ Container debug-shell                                                     Started                   1.4s
 ✔ Container insecure-db                                                     Started                   1.6s
 ✔ Container vulnerable-app                                                  Started                   2.1s
 ✔ Container vulnerable-nginx                                                Recreated                 0.9s
 ! debug-shell Published ports are discarded when using host network mode                              0.0s
 ! vulnerable-web Published ports are discarded when using host network mode                           0.0s
 ✔ Container vulnerable-web                                                  Started                   0.4s
```

- [x] 4. Запустите скрипт из `venv` и проанализируйте то, что вывело на терминале и что вывело при конвертировании

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install openpyxl odfpy

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab06$ python3 -m venv venv
ris@DESKTOP-HS8SF48:~/course_labs/labs/lab06$ source venv/bin/activate
(venv) ris@DESKTOP-HS8SF48:~/course_labs/labs/lab06$ pip install openpyxl odfpy
Collecting openpyxl
  Downloading openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 250.9/250.9 KB 1.3 MB/s eta 0:00:00
Collecting odfpy
  Downloading odfpy-1.4.1.tar.gz (717 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 717.0/717.0 KB 6.2 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Collecting et-xmlfile
  Downloading et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
Collecting defusedxml
  Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Using legacy 'setup.py install' for odfpy, since package 'wheel' is not installed.
Installing collected packages: et-xmlfile, defusedxml, openpyxl, odfpy
  Running setup.py install for odfpy ... done
Successfully installed defusedxml-0.7.1 et-xmlfile-2.0.0 odfpy-1.4.1 openpyxl-3.1.5

$ ./audit.sh

(venv) ris@DESKTOP-HS8SF48:~/course_labs/labs/lab06$ ./audit.sh
Starting Docker CIS & Image Security Audit
==========================================
Detected platform: Linux
Using docker-bench-security image: docker/docker-bench-security:latest
Reports will be saved to: ./audit_reports/

Running Trivy scan for docker/docker-bench-security:latest...
2026-01-12T21:43:44+03:00       INFO    Need to update DB
2026-01-12T21:43:44+03:00       INFO    Downloading DB...       repository="ghcr.io/aquasecurity/trivy-db:2"
80.14 MiB / 80.14 MiB [---------------------------------------------------------] 100.00% 21.02 MiB p/s 4.0s
2026-01-12T21:43:53+03:00       INFO    Vulnerability scanning is enabled
2026-01-12T21:43:53+03:00       INFO    Secret scanning is enabled
2026-01-12T21:43:53+03:00       INFO    If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2026-01-12T21:43:53+03:00       INFO    Please see also https://aquasecurity.github.io/trivy/v0.52/docs/scanner/secret/#recommendation for faster secret detection
2026-01-12T21:43:53+03:00       INFO    Detected OS     family="alpine" version="3.8.2"
2026-01-12T21:43:53+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.8" repository="3.8" pkg_num=25
2026-01-12T21:43:53+03:00       INFO    Number of language-specific files       num=0
2026-01-12T21:43:53+03:00       WARN    This OS version is no longer supported by the distribution      family="alpine" version="3.8.2"
2026-01-12T21:43:53+03:00       WARN    The vulnerability detection may be insufficient because security updates are not provided
Saved to: ./audit_reports/json/docker-bench-security-trivy.json

Scanning lab images for vulnerabilities...

=== Trivy scan for nginx:alpine ===
2026-01-12T21:43:54+03:00       INFO    Vulnerability scanning is enabled
2026-01-12T21:43:54+03:00       INFO    Secret scanning is enabled
2026-01-12T21:43:54+03:00       INFO    If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2026-01-12T21:43:54+03:00       INFO    Please see also https://aquasecurity.github.io/trivy/v0.52/docs/scanner/secret/#recommendation for faster secret detection
2026-01-12T21:43:55+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2026-01-12T21:43:55+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2026-01-12T21:43:55+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=72
2026-01-12T21:43:55+03:00       INFO    Number of language-specific files       num=0
Saved to: ./audit_reports/json/nginx-alpine-trivy.json

=== Trivy scan for python:3.11-alpine ===
2026-01-12T21:43:56+03:00       INFO    Vulnerability scanning is enabled
2026-01-12T21:43:56+03:00       INFO    Secret scanning is enabled
2026-01-12T21:43:56+03:00       INFO    If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2026-01-12T21:43:56+03:00       INFO    Please see also https://aquasecurity.github.io/trivy/v0.52/docs/scanner/secret/#recommendation for faster secret detection
2026-01-12T21:43:56+03:00       INFO    [python] License acquired from METADATA classifiers may be subject to additional terms      name="pip" version="24.0"
2026-01-12T21:43:56+03:00       INFO    [python] License acquired from METADATA classifiers may be subject to additional terms      name="autocommand" version="2.2.2"
2026-01-12T21:43:56+03:00       INFO    [python] License acquired from METADATA classifiers may be subject to additional terms      name="typeguard" version="4.3.0"
2026-01-12T21:43:56+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2026-01-12T21:43:56+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2026-01-12T21:43:56+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=38
2026-01-12T21:43:56+03:00       INFO    Number of language-specific files       num=1
2026-01-12T21:43:56+03:00       INFO    [python-pkg] Detecting vulnerabilities...
Saved to: ./audit_reports/json/python-3.11-alpine-trivy.json

=== Trivy scan for postgres:16-alpine ===
2026-01-12T21:43:57+03:00       INFO    Vulnerability scanning is enabled
2026-01-12T21:43:57+03:00       INFO    Secret scanning is enabled
2026-01-12T21:43:57+03:00       INFO    If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2026-01-12T21:43:57+03:00       INFO    Please see also https://aquasecurity.github.io/trivy/v0.52/docs/scanner/secret/#recommendation for faster secret detection
2026-01-12T21:44:01+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2026-01-12T21:44:01+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2026-01-12T21:44:01+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=45
2026-01-12T21:44:01+03:00       INFO    Number of language-specific files       num=1
2026-01-12T21:44:01+03:00       INFO    [gobinary] Detecting vulnerabilities...
Saved to: ./audit_reports/json/postgres-16-alpine-trivy.json

Linux host detected – configuring mounts for CIS Docker Benchmark coverage

Mounting /usr/lib/systemd
Mounting /var/log
Running Docker Bench Security container (CIS host audit)

docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "/usr/bin/dumb-init": stat /usr/bin/dumb-init: no such file or directory: unknown.

WARN: docker-bench-security image run failed (exit=127).
Falling back to running Docker Bench from GitHub repository (host script).

Cloning into '/tmp/tmp.LLogar7v9V/docker-bench-security'...
remote: Enumerating objects: 33, done.
remote: Counting objects: 100% (33/33), done.
remote: Compressing objects: 100% (30/30), done.
remote: Total 33 (delta 0), reused 16 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (33/33), 350.40 KiB | 1.89 MiB/s, done.
# --------------------------------------------------------------------------------------------
# Docker Bench for Security v1.6.0
#
# Docker, Inc. (c) 2015-2026
#
# Checks for dozens of common best-practices around deploying Docker containers in production.
# Based on the CIS Docker Benchmark 1.6.0.
# --------------------------------------------------------------------------------------------

[WARN] Some tests might require root to run

Initializing 2026-01-12T21:44:06+03:00


Section A - Check results

[INFO] 1 - Host Configuration
[INFO] 1.1 - Linux Hosts Specific Configuration
WARNING: daemon is not using the default seccomp profile
[WARN] 1.1.1 - Ensure a separate partition for containers has been created (Automated)
[INFO] 1.1.2 - Ensure only trusted users are allowed to control Docker daemon (Automated)
[INFO]       * Users: ris
[WARN] 1.1.3 - Ensure auditing is configured for the Docker daemon (Automated)
[WARN] 1.1.4 - Ensure auditing is configured for Docker files and directories -/run/containerd (Automated)
[WARN] 1.1.5 - Ensure auditing is configured for Docker files and directories - /var/lib/docker (Automated)
[INFO] 1.1.6 - Ensure auditing is configured for Docker files and directories - /etc/docker (Automated)
[INFO]        * Directory not found
[INFO] 1.1.7 - Ensure auditing is configured for Docker files and directories - docker.service (Automated)
[INFO]        * File not found
[INFO] 1.1.8 - Ensure auditing is configured for Docker files and directories - containerd.sock (Automated)
[INFO]        * File not found
[WARN] 1.1.9 - Ensure auditing is configured for Docker files and directories - docker.socket (Automated)
[INFO] 1.1.10 - Ensure auditing is configured for Docker files and directories - /etc/default/docker (Automated)
[INFO]        * File not found
[INFO] 1.1.11 - Ensure auditing is configured for Dockerfiles and directories - /etc/docker/daemon.json (Automated)
[INFO]        * File not found
[INFO] 1.1.12 - 1.1.12 Ensure auditing is configured for Dockerfiles and directories - /etc/containerd/config.toml (Automated)
[INFO]        * File not found
[INFO] 1.1.13 - Ensure auditing is configured for Docker files and directories - /etc/sysconfig/docker (Automated)
[INFO]        * File not found
[INFO] 1.1.14 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd (Automated)
[INFO]         * File not found
[INFO] 1.1.15 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim (Automated)
[INFO]         * File not found
[INFO] 1.1.16 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim-runc-v1 (Automated)
[INFO]         * File not found
[INFO] 1.1.17 - Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim-runc-v2 (Automated)
[INFO]         * File not found
[INFO] 1.1.18 - Ensure auditing is configured for Docker files and directories - /usr/bin/runc (Automated)
[INFO]         * File not found
[INFO] 1.2 - General Configuration
[NOTE] 1.2.1 - Ensure the container host has been Hardened (Manual)
[PASS] 1.2.2 - Ensure that the version of Docker is up to date (Manual)
[INFO]        * Using 27.3.1 which is current
[INFO]        * Check with your operating system vendor for support and security maintenance for Docker

[INFO] 2 - Docker daemon configuration
[NOTE] 2.1 - Run the Docker daemon as a non-root user, if possible (Manual)
[WARN] 2.2 - Ensure network traffic is restricted between containers on the default bridge (Scored)
[PASS] 2.3 - Ensure the logging level is set to 'info' (Scored)
[PASS] 2.4 - Ensure Docker is allowed to make changes to iptables (Scored)
[PASS] 2.5 - Ensure insecure registries are not used (Scored)
[PASS] 2.6 - Ensure aufs storage driver is not used (Scored)
[INFO] 2.7 - Ensure TLS authentication for Docker daemon is configured (Scored)
[INFO]      * Docker daemon not listening on TCP
[INFO] 2.8 - Ensure the default ulimit is configured appropriately (Manual)
[INFO]      * Default ulimit doesn't appear to be set
[WARN] 2.9 - Enable user namespace support (Scored)
[PASS] 2.10 - Ensure the default cgroup usage has been confirmed (Scored)
[PASS] 2.11 - Ensure base device size is not changed until needed (Scored)
[WARN] 2.12 - Ensure that authorization for Docker client commands is enabled (Scored)
[WARN] 2.13 - Ensure centralized and remote logging is configured (Scored)
[WARN] 2.14 - Ensure containers are restricted from acquiring new privileges (Scored)
[PASS] 2.15 - Ensure live restore is enabled (Scored) (Incompatible with swarm mode)
[WARN] 2.16 - Ensure Userland Proxy is Disabled (Scored)
[INFO] 2.17 - Ensure that a daemon-wide custom seccomp profile is applied if appropriate (Manual)
[INFO] Ensure that experimental features are not implemented in production (Scored) (Deprecated)

[INFO] 3 - Docker daemon configuration files
[INFO] 3.1 - Ensure that the docker.service file ownership is set to root:root (Automated)
[INFO]      * File not found
[INFO] 3.2 - Ensure that docker.service file permissions are appropriately set (Automated)
[INFO]      * File not found
[INFO] 3.3 - Ensure that docker.socket file ownership is set to root:root (Automated)
[INFO]      * File not found
[INFO] 3.4 - Ensure that docker.socket file permissions are set to 644 or more restrictive (Automated)
[INFO]      * File not found
[INFO] 3.5 - Ensure that the /etc/docker directory ownership is set to root:root (Automated)
[INFO]      * Directory not found
[INFO] 3.6 - Ensure that /etc/docker directory permissions are set to 755 or more restrictively (Automated)
[INFO]      * Directory not found
[INFO] 3.7 - Ensure that registry certificate file ownership is set to root:root (Automated)
[INFO]      * Directory not found
[INFO] 3.8 - Ensure that registry certificate file permissions are set to 444 or more restrictively (Automated)
[INFO]      * Directory not found
[INFO] 3.9 - Ensure that TLS CA certificate file ownership is set to root:root (Automated)
[INFO]      * No TLS CA certificate found
[INFO] 3.10 - Ensure that TLS CA certificate file permissions are set to 444 or more restrictively (Automated)
[INFO]       * No TLS CA certificate found
[INFO] 3.11 - Ensure that Docker server certificate file ownership is set to root:root (Automated)
[INFO]       * No TLS Server certificate found
[INFO] 3.12 - Ensure that the Docker server certificate file permissions are set to 444 or more restrictively (Automated)
[INFO]       * No TLS Server certificate found
[INFO] 3.13 - Ensure that the Docker server certificate key file ownership is set to root:root (Automated)
[INFO]       * No TLS Key found
[INFO] 3.14 - Ensure that the Docker server certificate key file permissions are set to 400 (Automated)
[INFO]       * No TLS Key found
[PASS] 3.15 - Ensure that the Docker socket file ownership is set to root:docker (Automated)
[PASS] 3.16 - Ensure that the Docker socket file permissions are set to 660 or more restrictively (Automated)
[INFO] 3.17 - Ensure that the daemon.json file ownership is set to root:root (Automated)
[INFO]       * File not found
[INFO] 3.18 - Ensure that daemon.json file permissions are set to 644 or more restrictive (Automated)
[INFO]       * File not found
[INFO] 3.19 - Ensure that the /etc/default/docker file ownership is set to root:root (Automated)
[INFO]       * File not found
[INFO] 3.20 - Ensure that the /etc/default/docker file permissions are set to 644 or more restrictively (Automated)
[INFO]       * File not found
[INFO] 3.21 - Ensure that the /etc/sysconfig/docker file permissions are set to 644 or more restrictively (Automated)
[INFO]       * File not found
[INFO] 3.22 - Ensure that the /etc/sysconfig/docker file ownership is set to root:root (Automated)
[INFO]       * File not found
[INFO] 3.23 - Ensure that the Containerd socket file ownership is set to root:root (Automated)
[INFO]       * File not found
[INFO] 3.24 - Ensure that the Containerd socket file permissions are set to 660 or more restrictively (Automated)
[INFO]       * File not found

[INFO] 4 - Container Images and Build File
[WARN] 4.1 - Ensure that a user for the container has been created (Automated)
[WARN]      * Running as root: insecure-db
[WARN]      * Running as root: openmp_stack_worker.1.bdhi2j5bnj8no4grx9quebu4q
[WARN]      * Running as root: openmp_stack_worker.2.psmuemlu38kt8brcxcq1k5yr2
[WARN]      * Running as root: openmp_stack_worker.4.odmnw93v7636383ycthfxmbyj
[WARN]      * Running as root: openmp_stack_worker.5.o0a2nu31i5arkjrs3v65udg0u
[WARN]      * Running as root: openmp_stack_master.1.j4otsiuy1kq0upq33ijueydxu
[WARN]      * Running as root: openmp_stack_worker.3.jxv5xxq3omg4qnv79woali6k3
[WARN]      * Running as root: registry.1.6m4tzbprnz727um2203dw3abb
[NOTE] 4.2 - Ensure that containers use only trusted base images (Manual)
[NOTE] 4.3 - Ensure that unnecessary packages are not installed in the container (Manual)
[NOTE] 4.4 - Ensure images are scanned and rebuilt to include security patches (Manual)
[WARN] 4.5 - Ensure Content trust for Docker is Enabled (Automated)
[WARN] 4.6 - Ensure that HEALTHCHECK instructions have been added to container images (Automated)
[WARN]      * No Healthcheck found: [lab05-client:latest]
[WARN]      * No Healthcheck found: [lab05-server:latest]
[WARN]      * No Healthcheck found: [hellow-appsec-world:latest ris4png/hellow-appsec-world:latest]
[WARN]      * No Healthcheck found: [hellow-appsec-world:latest ris4png/hellow-appsec-world:latest]
[WARN]      * No Healthcheck found: [nginx:latest]
[WARN]      * No Healthcheck found: [nginx:alpine]
[WARN]      * No Healthcheck found: [127.0.0.1:5000/mpi:latest]
[WARN]      * No Healthcheck found: [python:3.11-alpine]
[WARN]      * No Healthcheck found: [postgres:16-alpine]
[WARN]      * No Healthcheck found: [alpine:latest]
[WARN]      * No Healthcheck found: [geminishkvdev/hello-appsec-world:latest]
[WARN]      * No Healthcheck found: [ubuntu:latest]
[WARN]      * No Healthcheck found: [registry:2@sha256:a3d8aaa63ed8681a604f1dea0aa03f100d5895b6a58ace528858a7b332415373]
[INFO] 4.7 - Ensure update instructions are not used alone in the Dockerfile (Manual)
[INFO]      * Update instruction found: [lab05-client:latest]
[INFO]      * Update instruction found: [lab05-server:latest]
[INFO]      * Update instruction found: [hellow-appsec-world:latest ris4png/hellow-appsec-world:latest]
[INFO]      * Update instruction found: [hellow-appsec-world:latest ris4png/hellow-appsec-world:latest]
[INFO]      * Update instruction found: [geminishkvdev/hello-appsec-world:latest]
[NOTE] 4.8 - Ensure setuid and setgid permissions are removed (Manual)
[INFO] 4.9 - Ensure that COPY is used instead of ADD in Dockerfiles (Manual)
[INFO]      * ADD in image history: [127.0.0.1:5000/mpi:latest]
[INFO]      * ADD in image history: [ubuntu:latest]
[NOTE] 4.10 - Ensure secrets are not stored in Dockerfiles (Manual)
[NOTE] 4.11 - Ensure only verified packages are installed (Manual)
[NOTE] 4.12 - Ensure all signed artifacts are validated (Manual)

[INFO] 5 - Container Runtime
[WARN] 5.1 - Ensure swarm mode is not Enabled, if not needed (Automated)
[WARN] 5.2 - Ensure that, if applicable, an AppArmor Profile is enabled (Automated)
[WARN]      * No AppArmorProfile Found: vulnerable-web
[WARN]      * No AppArmorProfile Found: insecure-db
[WARN]      * No AppArmorProfile Found: openmp_stack_worker.1.bdhi2j5bnj8no4grx9quebu4q
[WARN]      * No AppArmorProfile Found: openmp_stack_worker.2.psmuemlu38kt8brcxcq1k5yr2
[WARN]      * No AppArmorProfile Found: openmp_stack_worker.4.odmnw93v7636383ycthfxmbyj
[WARN]      * No AppArmorProfile Found: openmp_stack_worker.5.o0a2nu31i5arkjrs3v65udg0u
[WARN]      * No AppArmorProfile Found: openmp_stack_master.1.j4otsiuy1kq0upq33ijueydxu
[WARN]      * No AppArmorProfile Found: openmp_stack_worker.3.jxv5xxq3omg4qnv79woali6k3
[WARN]      * No AppArmorProfile Found: registry.1.6m4tzbprnz727um2203dw3abb
[WARN] 5.3 - Ensure that, if applicable, SELinux security options are set (Automated)
[WARN]      * No SecurityOptions Found: insecure-db
[WARN]      * No SecurityOptions Found: openmp_stack_worker.1.bdhi2j5bnj8no4grx9quebu4q
[WARN]      * No SecurityOptions Found: openmp_stack_worker.2.psmuemlu38kt8brcxcq1k5yr2
[WARN]      * No SecurityOptions Found: openmp_stack_worker.4.odmnw93v7636383ycthfxmbyj
[WARN]      * No SecurityOptions Found: openmp_stack_worker.5.o0a2nu31i5arkjrs3v65udg0u
[WARN]      * No SecurityOptions Found: openmp_stack_master.1.j4otsiuy1kq0upq33ijueydxu
[WARN]      * No SecurityOptions Found: openmp_stack_worker.3.jxv5xxq3omg4qnv79woali6k3
[WARN]      * No SecurityOptions Found: registry.1.6m4tzbprnz727um2203dw3abb
[WARN] 5.4 - Ensure that Linux kernel capabilities are restricted within containers (Automated)
[WARN]      * Capabilities added: CapAdd=[ALL] to vulnerable-web
[WARN] 5.5 - Ensure that privileged containers are not used (Automated)
[WARN]      * Container running in Privileged mode: vulnerable-web
[PASS] 5.6 - Ensure sensitive host system directories are not mounted on containers (Automated)
[PASS] 5.7 - Ensure sshd is not run within containers (Automated)
[PASS] 5.8 - Ensure privileged ports are not mapped within containers (Automated)
[WARN] 5.9 - Ensure that only needed ports are open on the container (Manual)
[WARN]      * Port in use: 5432 in insecure-db
[WARN] 5.10 - Ensure that the host's network namespace is not shared (Automated)
[WARN]      * Container running with networking mode 'host': vulnerable-web
[WARN] 5.11 - Ensure that the memory usage for containers is limited (Automated)
[WARN]       * Container running without memory restrictions: vulnerable-web
[WARN]       * Container running without memory restrictions: insecure-db
[WARN]       * Container running without memory restrictions: openmp_stack_worker.1.bdhi2j5bnj8no4grx9quebu4q
[WARN]       * Container running without memory restrictions: openmp_stack_worker.2.psmuemlu38kt8brcxcq1k5yr2
[WARN]       * Container running without memory restrictions: openmp_stack_worker.4.odmnw93v7636383ycthfxmbyj
[WARN]       * Container running without memory restrictions: openmp_stack_worker.5.o0a2nu31i5arkjrs3v65udg0u
[WARN]       * Container running without memory restrictions: openmp_stack_master.1.j4otsiuy1kq0upq33ijueydxu
[WARN]       * Container running without memory restrictions: openmp_stack_worker.3.jxv5xxq3omg4qnv79woali6k3
[WARN]       * Container running without memory restrictions: registry.1.6m4tzbprnz727um2203dw3abb
[WARN] 5.12 - Ensure that CPU priority is set appropriately on containers (Automated)
[WARN]       * Container running without CPU restrictions: vulnerable-web
[WARN]       * Container running without CPU restrictions: insecure-db
[WARN]       * Container running without CPU restrictions: openmp_stack_worker.1.bdhi2j5bnj8no4grx9quebu4q
[WARN]       * Container running without CPU restrictions: openmp_stack_worker.2.psmuemlu38kt8brcxcq1k5yr2
[WARN]       * Container running without CPU restrictions: openmp_stack_worker.4.odmnw93v7636383ycthfxmbyj
[WARN]       * Container running without CPU restrictions: openmp_stack_worker.5.o0a2nu31i5arkjrs3v65udg0u
[WARN]       * Container running without CPU restrictions: openmp_stack_master.1.j4otsiuy1kq0upq33ijueydxu
[WARN]       * Container running without CPU restrictions: openmp_stack_worker.3.jxv5xxq3omg4qnv79woali6k3
[WARN]       * Container running without CPU restrictions: registry.1.6m4tzbprnz727um2203dw3abb
[WARN] 5.13 - Ensure that the container's root filesystem is mounted as read only (Automated)
[WARN]       * Container running with root FS mounted R/W: vulnerable-web
[WARN]       * Container running with root FS mounted R/W: insecure-db
[WARN]       * Container running with root FS mounted R/W: openmp_stack_worker.1.bdhi2j5bnj8no4grx9quebu4q
[WARN]       * Container running with root FS mounted R/W: openmp_stack_worker.2.psmuemlu38kt8brcxcq1k5yr2
[WARN]       * Container running with root FS mounted R/W: openmp_stack_worker.4.odmnw93v7636383ycthfxmbyj
[WARN]       * Container running with root FS mounted R/W: openmp_stack_worker.5.o0a2nu31i5arkjrs3v65udg0u
[WARN]       * Container running with root FS mounted R/W: openmp_stack_master.1.j4otsiuy1kq0upq33ijueydxu
[WARN]       * Container running with root FS mounted R/W: openmp_stack_worker.3.jxv5xxq3omg4qnv79woali6k3
[WARN]       * Container running with root FS mounted R/W: registry.1.6m4tzbprnz727um2203dw3abb
[WARN] 5.14 - Ensure that incoming container traffic is bound to a specific host interface (Automated)
[WARN]       * Port being bound to wildcard IP: 0.0.0.0 in insecure-db
[PASS] 5.15 - Ensure that the 'on-failure' container restart policy is set to '5' (Automated)
[WARN] 5.16 - Ensure that the host's process namespace is not shared (Automated)
[WARN]       * Host PID namespace being shared with: vulnerable-web
[PASS] 5.17 - Ensure that the host's IPC namespace is not shared (Automated)
[PASS] 5.18 - Ensure that host devices are not directly exposed to containers (Manual)
[INFO] 5.19 - Ensure that the default ulimit is overwritten at runtime if needed (Manual)
[INFO]       * Container no default ulimit override: vulnerable-web
[INFO]       * Container no default ulimit override: insecure-db
[INFO]       * Container no default ulimit override: openmp_stack_worker.1.bdhi2j5bnj8no4grx9quebu4q
[INFO]       * Container no default ulimit override: openmp_stack_worker.2.psmuemlu38kt8brcxcq1k5yr2
[INFO]       * Container no default ulimit override: openmp_stack_worker.4.odmnw93v7636383ycthfxmbyj
[INFO]       * Container no default ulimit override: openmp_stack_worker.5.o0a2nu31i5arkjrs3v65udg0u
[INFO]       * Container no default ulimit override: openmp_stack_master.1.j4otsiuy1kq0upq33ijueydxu
[INFO]       * Container no default ulimit override: openmp_stack_worker.3.jxv5xxq3omg4qnv79woali6k3
[INFO]       * Container no default ulimit override: registry.1.6m4tzbprnz727um2203dw3abb
[PASS] 5.20 - Ensure mount propagation mode is not set to shared (Automated)
[PASS] 5.21 - Ensure that the host's UTS namespace is not shared (Automated)
[WARN] 5.22 - Ensure the default seccomp profile is not Disabled (Automated)
[WARN]       * Default seccomp profile disabled: vulnerable-web
[NOTE] 5.23 - Ensure that docker exec commands are not used with the privileged option (Automated)
[NOTE] 5.24 - Ensure that docker exec commands are not used with the user=root option (Manual)
[PASS] 5.25 - Ensure that cgroup usage is confirmed (Automated)
[WARN] 5.26 - Ensure that the container is restricted from acquiring additional privileges (Automated)
[WARN]       * Privileges not restricted: insecure-db
[WARN]       * Privileges not restricted: openmp_stack_worker.1.bdhi2j5bnj8no4grx9quebu4q
[WARN]       * Privileges not restricted: openmp_stack_worker.2.psmuemlu38kt8brcxcq1k5yr2
[WARN]       * Privileges not restricted: openmp_stack_worker.4.odmnw93v7636383ycthfxmbyj
[WARN]       * Privileges not restricted: openmp_stack_worker.5.o0a2nu31i5arkjrs3v65udg0u
[WARN]       * Privileges not restricted: openmp_stack_master.1.j4otsiuy1kq0upq33ijueydxu
[WARN]       * Privileges not restricted: openmp_stack_worker.3.jxv5xxq3omg4qnv79woali6k3
[WARN]       * Privileges not restricted: registry.1.6m4tzbprnz727um2203dw3abb
[WARN] 5.27 - Ensure that container health is checked at runtime (Automated)
[WARN]       * Health check not set: vulnerable-web
[WARN]       * Health check not set: insecure-db
[WARN]       * Health check not set: openmp_stack_worker.1.bdhi2j5bnj8no4grx9quebu4q
[WARN]       * Health check not set: openmp_stack_worker.2.psmuemlu38kt8brcxcq1k5yr2
[WARN]       * Health check not set: openmp_stack_worker.4.odmnw93v7636383ycthfxmbyj
[WARN]       * Health check not set: openmp_stack_worker.5.o0a2nu31i5arkjrs3v65udg0u
[WARN]       * Health check not set: openmp_stack_master.1.j4otsiuy1kq0upq33ijueydxu
[WARN]       * Health check not set: openmp_stack_worker.3.jxv5xxq3omg4qnv79woali6k3
[WARN]       * Health check not set: registry.1.6m4tzbprnz727um2203dw3abb
[INFO] 5.28 - Ensure that Docker commands always make use of the latest version of their image (Manual)
[WARN] 5.29 - Ensure that the PIDs cgroup limit is used (Automated)
[WARN]       * PIDs limit not set: vulnerable-web
[WARN]       * PIDs limit not set: insecure-db
[WARN]       * PIDs limit not set: openmp_stack_worker.1.bdhi2j5bnj8no4grx9quebu4q
[WARN]       * PIDs limit not set: openmp_stack_worker.2.psmuemlu38kt8brcxcq1k5yr2
[WARN]       * PIDs limit not set: openmp_stack_worker.4.odmnw93v7636383ycthfxmbyj
[WARN]       * PIDs limit not set: openmp_stack_worker.5.o0a2nu31i5arkjrs3v65udg0u
[WARN]       * PIDs limit not set: openmp_stack_master.1.j4otsiuy1kq0upq33ijueydxu
[WARN]       * PIDs limit not set: openmp_stack_worker.3.jxv5xxq3omg4qnv79woali6k3
[WARN]       * PIDs limit not set: registry.1.6m4tzbprnz727um2203dw3abb
[PASS] 5.30 - Ensure that Docker's default bridge 'docker0' is not used (Manual)
[PASS] 5.31 - Ensure that the host's user namespaces are not shared (Automated)
[WARN] 5.32 - Ensure that the Docker socket is not mounted inside any containers (Automated)
[WARN]       * Docker socket shared: vulnerable-web

[INFO] 6 - Docker Security Operations
[INFO] 6.1 - Ensure that image sprawl is avoided (Manual)
[INFO]      * There are currently: 13 images
[INFO] 6.2 - Ensure that container sprawl is avoided (Manual)
[INFO]      * There are currently a total of 41 containers, with only 9 of them currently running

[INFO] 7 - Docker Swarm Configuration
[PASS] 7.1 - Ensure that the minimum number of manager nodes have been created in a swarm (Automated)
[PASS] 7.2 - Ensure that swarm services are bound to a specific host interface (Automated)
[WARN] 7.3 - Ensure that all Docker swarm overlay networks are encrypted (Automated)
[WARN]      * Unencrypted overlay network: ingress (swarm)
[WARN]      * Unencrypted overlay network: openmp_stack_default (swarm)
[INFO] 7.4 - Ensure that Docker's secret management commands are used for managing secrets in a swarm cluster (Manual)
[WARN] 7.5 - Ensure that swarm manager is run in auto-lock mode (Automated)
[NOTE] 7.6 - Ensure that the swarm manager auto-lock key is rotated periodically (Manual)
[INFO] 7.7 - Ensure that node certificates are rotated as appropriate (Manual)
[INFO] 7.8 - Ensure that CA certificates are rotated as appropriate (Manual)
[INFO] 7.9 - Ensure that management plane traffic is separated from data plane traffic (Manual)


Section C - Score

[INFO] Checks: 117
[INFO] Score: -13


CIS audit output saved to: ./audit_reports/text/docker-bench-security-cis.txt

Converting Trivy JSON reports to XLSX/ODT formats...
✓ Saved to XLSX: ./audit_reports/xlsx/postgres-16-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/postgres-16-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/nginx-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/nginx-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/docker-bench-security-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/docker-bench-security-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/python-3.11-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/python-3.11-alpine-trivy.odt

==========================================
Audit complete!
Reports directory structure:
   ./audit_reports/
   ├── json/          (Trivy JSON outputs)
   ├── text/          (CIS audit text outputs)
   ├── xlsx/          (Excel spreadsheets)
   └── odt/           (OpenDocument Text files)

For CIS Docker Benchmark details, see:
https://www.cisecurity.org/benchmark/docker

$ deactivate # или $ deactivate 2>/dev/null || true
```
 
- [x] 5. Проведите анализ уязвимостей, опишите их причину возникновения

По результатам CIS Docker Benchmark (docker-bench-security) выявлены следующие ключевые проблемы:

1) Privileged контейнер
CIS: `5.5 - Container running in Privileged mode: vulnerable-web`  
Причина: в `vulnerable-app.yml` задано `privileged: true` для `vulnerable-web` (и также для `debug-shell`).

2) Linux capabilities не ограничены (cap_add: ALL)
CIS: `5.4 - Capabilities added: CapAdd=[ALL] to vulnerable-web`  
Причина: `cap_add: - ALL` в `vulnerable-app.yml`.

3) Сетевое пространство имён хоста разделяется с контейнером (host networking)
CIS: `5.10 - Container running with networking mode 'host': vulnerable-web`  
Причина: `network_mode: host` в `vulnerable-app.yml`.

4) PID namespace хоста разделяется с контейнером (host pid)
CIS: `5.16 - Host PID namespace being shared with: vulnerable-web`  
Причина: `pid: host` в `vulnerable-app.yml`.

5) Docker socket смонтирован внутрь контейнера
CIS: `5.32 - Docker socket shared: vulnerable-web`  
Причина: `/var/run/docker.sock:/var/run/docker.sock` в `vulnerable-app.yml`.

6) Корень хоста смонтирован как RW 
Причина: `- /:/hostroot:rw` в `vulnerable-app.yml`.

7) Seccomp/AppArmor не применяются (unconfined/disabled)  
CIS фиксирует проблемы seccomp/AppArmor (в частности, `Default seccomp profile disabled: vulnerable-web`).  
Причина: `seccomp:unconfined` и `apparmor:unconfined` в `vulnerable-app.yml`.

8) Порт БД открыт наружу и привязан к 0.0.0.0  
CIS:  
- `5.9 - Port in use: 5432 in insecure-db`  
- `5.14 - Port being bound to wildcard IP: 0.0.0.0 in insecure-db`  
Причина: в `docker-compose.yml` указан проброс `5432:5432` без ограничения интерфейса.

9) Нет лимитов ресурсов (CPU/RAM/PIDs)
CIS WARN: `5.11` (memory), `5.12` (CPU), `5.29` (PIDs).  
Причина: в compose-файлах не указаны ограничения ресурсов.

10) Root FS контейнеров в режиме R/W и нет HEALTHCHECK  
CIS WARN: `5.13 root FS mounted R/W`, `5.27 health check not set`, также `4.6 No Healthcheck found`.  
Причина: в сервисах/образах не заданы `read_only: true` и `healthcheck`.


- [x] 6. Опишите влияния уязвимостей, их сценарий атаки


Доступ внутрь `vulnerable-web` и захват Docker на хосте через `docker.sock`
- Условие: атакующий получает выполнение команд в `vulnerable-web` (эксплойт уязвимого приложения/доступные debug-инструменты).
- Факторы усиления: `docker.sock` смонтирован, `privileged: true`, `cap_add: ALL`, профили защиты отключены.
- Развитие атаки:
  1) выполнить docker-команды из контейнера, управляя Docker daemon хоста;
  2) запустить дополнительный контейнер с маунтом хостовой ФС;
  3) украсть конфиги/ключи/данные и/или закрепиться.
- Итог: утечка данных и компрометация окружения WSL/хоста.

Прямой доступ к ФС хоста через `/hostroot:rw`
- Условие: атакующий внутри контейнера.
- Вектор: `/:/hostroot:rw` позволяет читать/менять файлы хоста.
- Итог: кража секретов (ssh-ключи, токены), подмена конфигов, внедрение “закладок”.

Компрометация БД через открытый порт 5432
- Условие: атакующий имеет доступ к сети хоста.
- Вектор: порт Postgres открыт наружу и привязан к `0.0.0.0`, а учётные данные легко угадываются/находятся в compose.
- Итог: чтение/удаление/подмена данных приложения.

Supply-chain риск из-за уязвимостей в образах
- В `docker/docker-bench-security:latest` присутствуют CRITICAL CVE (`libseccomp`, `musl`).
- Итог: риск эксплуатации уязвимостей в среде, где этот образ используется (особенно при расширенных правах/доступах).

- [x] 7. Оцените риски ИБ и предложите меры для их снижения: 
> - Следует разобрать `.yaml` описав, что в них считается не безопасным и почему
> - Опишите сценарии реализации рисков CR, DL
> - Предложили исправленные `.yaml`

7.1 Оценка рисков

- **Критический CR-риск**: `docker.sock` + `privileged` + `cap_add: ALL` + `/:/hostroot:rw` + `seccomp/apparmor unconfined`  
  => компрометация контейнера практически равна компрометации хоста.

- **Высокий CR-риск**: открытый Postgres на `0.0.0.0` + слабые/известные секреты в env.

- **Высокий DL-риск**: отсутствие лимитов ресурсов и healthcheck (возможны простои и каскадные падения).

- **Supply-chain риск**: CRITICAL CVE в образе docker-bench-security.

---

7.2 Предложения по снижению рисков

Для `vulnerable-app.yml` (снижение CR критического уровня)
1) Удалить `privileged: true`.
2) Добавить `cap_drop: [ALL]`.
3) Убрать `network_mode: host` и `pid: host`.
4) Убрать маунты `/var/run/docker.sock` и `/:/hostroot:rw`.
5) Не использовать `seccomp:unconfined` и `apparmor:unconfined`.
6) Убрать “удалённый вход” в debug-shell (SSH root + пароль), оставить только локальный `docker exec` при необходимости.

Для `docker-compose.yml`
1) Ограничить проброс Postgres: `127.0.0.1:5432:5432` или вовсе убрать ports.
2) Вынести секреты в `.env`/secrets (не хранить в репозитории).
3) Добавить `healthcheck` для db/app/web.
4) Добавить ограничения ресурсов (CPU/RAM/PIDs), включить `no-new-privileges`, `read_only` (где возможно).

- [x] 8. Сделайте анализ уязвимостей из сгенерированных файлов .odt, .xslx и опишите их в отчете. Файлы конвертируются в эти директории

```bash
"├── json/          (Trivy JSON outputs)"
"├── text/          (CIS audit text outputs)"
"├── xlsx/          (Excel spreadsheets)"
"└── odt/           (OpenDocument Text files)"
```

Образ docker/docker-bench-security:latest

Образ построен на базе Alpine Linux версии 3.8.2, которая на момент анализа является устаревшей и не поддерживается разработчиками дистрибутива. Это означает отсутствие регулярных обновлений безопасности и повышенный риск наличия неисправленных уязвимостей.

В данном образе были выявлены уязвимости критического уровня:

- **CVE-2019-9893 (CRITICAL)** — уязвимость в библиотеке `libseccomp`, связанная с некорректной фильтрацией системных вызовов, что потенциально может позволить обход ограничений песочницы.
- **CVE-2019-14697 (CRITICAL)** — уязвимость в стандартной библиотеке `musl libc`, связанная с ошибками обработки памяти и возможной эскалацией привилегий или отказом в обслуживании.

Наличие критических уязвимостей в инструменте безопасности указывает на риск компрометации цепочки поставки и необходимость регулярного обновления даже вспомогательных инструментов.

---

Образ postgres:16-alpine

В образе обнаружены уязвимости высокого и среднего уровня в бинарнике `gosu`, который используется для запуска процессов от имени непривилегированного пользователя.

Выявлены следующие значимые уязвимости:

- **CVE-2025-58183 (HIGH)** — уязвимость в модуле `archive/tar`, допускающая неограниченное выделение памяти при обработке специально сформированных архивов, что может привести к отказу в обслуживании.
- **CVE-2025-61729 (HIGH)** — уязвимость в библиотеке `crypto/x509`, позволяющая спровоцировать чрезмерное потребление ресурсов при обработке некорректных сертификатов.

Дополнительно выявлен ряд уязвимостей среднего уровня в компонентах `net/http`, `crypto/tls`, `encoding/asn1`, `encoding/pem`, `net/url`, `net/mail`, связанных в основном с обработкой некорректных входных данных и риском отказа в обслуживании.

Основной класс угроз для данного образа — атаки на доступность сервиса (DoS) и потенциальные ошибки обработки сетевых и криптографических данных.

---

Образ python:3.11-alpine

В образе выявлена уязвимость:

- **CVE-2025-8869 (MEDIUM)** — уязвимость в пакете `pip`, связанная с некорректной обработкой символических ссылок при извлечении архивов, что может привести к перезаписи или чтению файлов вне ожидаемого каталога.

Данная уязвимость может быть использована при установке пакетов из недоверенных источников и представляет риск нарушения целостности файловой системы контейнера.

- [x] 9. Подготовьте отчет `gist`.
- [x] 10. Почистите кеш от `venv` и остановите уязвимостей приложение, почистите контейнера

```bash
$ rm -rf venv
$ docker-compose -f demo-vulnerable-app.yml down

(venv) ris@DESKTOP-HS8SF48:~/course_labs/labs/lab06$ docker compose -f docker-compose.yml -f vulnerable-app.yml down
WARN[0000] /home/ris/course_labs/labs/lab06/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
WARN[0000] /home/ris/course_labs/labs/lab06/vulnerable-app.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
[+] Running 5/5
 ✔ Container vulnerable-web  Removed                                                                   0.3s
 ✔ Container debug-shell     Removed                                                                   0.2s
 ✔ Container vulnerable-app  Removed                                                                   0.1s
 ✔ Container insecure-db     Removed                                                                   0.6s
 ✔ Network lab06_default     Removed  
 
$ docker system prune -f

(venv) ris@DESKTOP-HS8SF48:~/course_labs/labs/lab06$ docker system prune -f
Deleted Containers:
44d07287c9404a4fe53c1ef5dcb2446d37f7f576446ab6741b502e36d4c2009c
0d33fd545efc12563d020ed5f78a9e1a5ae54caf45de0c9b798dca193d2669e0
660033fab6486c9e320f48caa39c6ccb9b2e6ef212a2dc241531407d3987b1e6
dedf0e4e834d7dafc0a2024ab10e856bdcbf4d87bc6175923a88c1e1782e674c
7f909e609fe7587faa150c90e9dba66f1de72a3e3326008e13bf7aad37429bd3
d77216df43f7f690df8cc25ba814e7920cf8d5af41942a04170263bea1c90505
c2e9a9e68bc5461c00f52143be1eb380958a3ed036500ca90d7d6cd9ba4cb113
19fcccfe982106da5c30d4f206abb1e377378986c1f2c3642c0beeb6b3237f17
ecdd09aba505cd577aadf0924870b4bd2df283edcb5880d3da5005585d3c8eac
f01e0054716707a27da8ea30f7ae02012ea8a115edaac52e7569dd3a8d18fcd7
9243549a34c8d69bcbcda72f1e5bbf8c9f6e54224550f18a65c89fc2ed3e2182
b4a9975292aa9deb461d5596f52d8f6e202259ce41c9895d628adfa94dc21c5e
48bd98daf529940b5f797cebfc51ee40591f8e26e2a7be773f392e0ba290cfb2
8ba420767545104e009347c6cb842bf03d9b1585adff89b46321199b9b5ed8c8
af36be61fcd71674f6cb2ab46101131d992e7a8d93051c77a5c0f536a60387d2
9c2c24545808cfd455e35eb62b8986d23e79c14325f06eb049fd182cbe942c72
0b158fc88abb5a39553575180148af11ba9ef51a11ffa77631c17d86f25dc192
9da6fbec913ada7c10c2c64332f77629aa7cd1c29e1a2ca70c5bd5012f6cbcaf
de9754901bff299495388a92296c5887d5f3f0963f89977d13f27cc1a1f56e7a
de170528ad2af1b8fba313f35e2b588ceb98839f433308560664b6bc4dccc308
647c1122d7c25f99085496ba3593babe870bbedf860402e3efd377201aa8bfcd
8720e74038eee75761b472bd965d98e3e113915b697c0805eb769273bec11155
333e40786732841c4a88644e3b649b34306f1b70da9cc9a0520193bade13fbd0
3cacb12f9272d344b9b5b934bf80adff0b01ec3db5cbc5a7f7c7d0c69a2be737
faadae4b28f91a543624856645f198f6f45d048ad1b91d47aa0cab17b309449c
5b7a331a785b85c901fb050b4f7a4fb02e3319817085a39e204cbe562c0e08e2
d42ada671fb3953d7c38dacc358918b6c95f677694199f5157bf64b40655b9e4
3a533a91628f2f8ccfe42c1f980446a858051662e5555119cb8c2602ffa92c58
6f49029ece63beba4e5defc1372cf024ec274de75972c2b92a0cb505a5c66425
dc57dfc4a773e168e2de7aa7b7b0e3d3683d5987107189ae198a466b5b317994

Deleted Networks:
lab05_app_net

Deleted build cache objects:
r7rhrhjeh4awf7r6h23supgdi
5fjqnfinbi84i8onub9samnnb
vdtq7rhdogx0h8o47th771s7h
dub7aw2c3eufe2dgibpqavsgf
hiu3olcxdjsh2fv9qz0me5tov
ytzb47bzppucu05e7126i25df
0a5vg3xx3cv6al80ad0q1amzz
dt2ehf2p2cfru894ms9d27yon
dsdt54tga650fi8febb7jsxnd
y8h5v2luiblrvgn232i70kn4v
fke24662veaufxklbeqmpcf6i
gy14l035zps9xfljso8d9yp6o
vm5qaotjlfzyztwwwvyvvtx6h
qsrqq7tk39am2r10xbrc020o1
ix0a1eoqiqbjsxwtpikd27ldw
l0vgf0kn9biotpr1ba8hkk3rp
ysy624bgjxl6fhnqx4q26aj4s
tszyaivbljuffwqe78n71twdk
o5mubgq01h9vaunnrbzp3t97n
dfreq4deu5n1o1l8zo7ioglug
1pfmi2oz82a4qhzvqd0uqygkn
iwk3fy3o63zru88v0hw5derfi
ng4x8a38zude8431or4ciz34o
oa5lh8b09530cg4vp4w4g2o6e
k0mcvhka3ctyvrked19yfcyli
yq65c7fp8jrkve0yyii9qchia
zsqklqw8id87y7g6v1ghidztl
zcg84ri44knjp4h8atl3p8uxb
q9skjin0aloz5ed28wg1jn2zb
uezxjk572smbksgzocp8qln94
ly9ze5fvzofm08rjgqx7rbuim
kej7ca6og28ncqd8yl577zmek
9frwbh756dfqy1tny4clvsst9
rhfd74tiacw6tgqync9e3fz6m
r2oangu8tgy02glx4g1xrh9sz
5jbsepy75yzzf57ovku4ygy2j
rp1rr80nuaxqszxdpmt031ld4
puvm7vywqgzw00b2hbt15u6vh
q1hvybdfudp43mik8ohkv3ma5
8opa9ugb59qmgauc0x1frq8m6
v1rpmwrxoj76c20cvdpb3ebq3

Total reclaimed space: 400.6MB
```
 
***

## Troobleshooting

- Права для исполнения скрипта

```bash
$ chmod +x xxx.sh # разрешение прав при permission denied
```

- На macOS/AArch64 docker-bench-security может не запускаться из‑за ограничений Docker Desktop и это работает для Linux‑VM. На Mac используем Trivy‑скан и разбор конфигурации compose‑файлов.

***

## Links

- [Docker](https://docs.docker.com/)
- [Docker Engine security](https://docs.docker.com/engine/security/)
- [Docker Bench for Security](https://github.com/docker/docker-bench-security)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)
- [Trivy: Container Security Scanner](https://aquasecurity.github.io/trivy/)
- [Markdown](https://stackedit.io)
- [Gist](https://gist.github.com)
- [GitHub Docs](https://docs.github.com/en)
- [GitHub CLI](https://cli.github.com)
