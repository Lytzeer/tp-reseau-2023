# TP2 : Environnement virtuel

- [TP2 : Environnement virtuel](#tp2--environnement-virtuel)
- [I. Topologie réseau](#i-topologie-réseau)
  - [Topologie](#topologie)
  - [Tableau d'adressage](#tableau-dadressage)
  - [Hints](#hints)
  - [Marche à suivre recommandée](#marche-à-suivre-recommandée)
  - [Compte-rendu](#compte-rendu)
- [II. Interlude accès internet](#ii-interlude-accès-internet)
- [III. Services réseau](#iii-services-réseau)
  - [1. DHCP](#1-dhcp)
  - [2. Web web web](#2-web-web-web)

# I. Topologie réseau

## Compte-rendu

☀️ Sur **`node1.lan1.tp2`**

```shell
[lytzeer@node1-lan1-tp2 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:7a:71:f1 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe7a:71f1/64 scope link
       valid_lft forever preferred_lft forever

[lytzeer@node1-lan1-tp2 ~]$ ip r s
10.1.1.0/24 dev enp0s8 proto kernel scope link src 10.1.1.11 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s8 proto static metric 100

[lytzeer@node1-lan1-tp2 ~]$ ping 10.1.2.12
PING 10.1.2.12 (10.1.2.12) 56(84) bytes of data.
64 bytes from 10.1.2.12: icmp_seq=1 ttl=63 time=0.725 ms
64 bytes from 10.1.2.12: icmp_seq=2 ttl=63 time=0.757 ms
64 bytes from 10.1.2.12: icmp_seq=3 ttl=63 time=0.646 ms
64 bytes from 10.1.2.12: icmp_seq=4 ttl=63 time=0.419 ms
64 bytes from 10.1.2.12: icmp_seq=5 ttl=63 time=0.400 ms

--- 10.1.2.12 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4110ms
rtt min/avg/max/mdev = 0.400/0.589/0.757/0.151 ms

[lytzeer@node1-lan1-tp2 ~]$ traceroute 10.1.2.12
traceroute to 10.1.2.12 (10.1.2.12), 30 hops max, 60 byte packets
 1  10.1.1.254 (10.1.1.254)  0.516 ms  0.476 ms  0.469 ms
 2  10.1.2.12 (10.1.2.12)  0.462 ms !X  0.454 ms !X  0.883 ms !X
```

# II. Interlude accès internet

☀️ **Sur `router.tp2`**

```shell
[lytzeer@router-tp2 ~]$ ping 94.23.214.79
PING 94.23.214.79 (94.23.214.79) 56(84) bytes of data.
64 bytes from 94.23.214.79: icmp_seq=1 ttl=52 time=14.7 ms
64 bytes from 94.23.214.79: icmp_seq=2 ttl=52 time=14.2 ms
64 bytes from 94.23.214.79: icmp_seq=3 ttl=52 time=13.9 ms
64 bytes from 94.23.214.79: icmp_seq=4 ttl=52 time=16.4 ms
64 bytes from 94.23.214.79: icmp_seq=5 ttl=52 time=14.2 ms

--- 94.23.214.79 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 13.937/14.685/16.427/0.902 ms

[lytzeer@router-tp2 ~]$ ping cataas.com
PING cataas.com (94.23.214.79) 56(84) bytes of data.
64 bytes from ns304722.ip-94-23-214.eu (94.23.214.79): icmp_seq=1 ttl=52 time=13.5 ms
64 bytes from ns304722.ip-94-23-214.eu (94.23.214.79): icmp_seq=2 ttl=52 time=16.0 ms
64 bytes from ns304722.ip-94-23-214.eu (94.23.214.79): icmp_seq=3 ttl=52 time=14.1 ms
64 bytes from ns304722.ip-94-23-214.eu (94.23.214.79): icmp_seq=4 ttl=52 time=13.7 ms
64 bytes from ns304722.ip-94-23-214.eu (94.23.214.79): icmp_seq=5 ttl=52 time=14.1 ms

--- cataas.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4007ms
rtt min/avg/max/mdev = 13.457/14.279/15.983/0.888 ms
```

☀️ **Accès internet LAN1 et LAN2**

- dans le compte-rendu, mettez-moi que la conf des points précédents sur `node2.lan1.tp2`

```shell
[lytzeer@node1-lan1-tp2 ~]$ cat /etc/sysconfig/network-scripts/route-enp0s8
10.1.2.0/24 via 10.1.1.254 dev eth0
default via 10.1.1.254 dev eth0

[lytzeer@node1-lan1-tp2 ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
DEVICE=enp0s8

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.1.11
NETMASK=255.255.255.0

DNS1=1.1.1.1
```
- prouvez que `node2.lan1.tp2` a un accès internet :

```shell
[lytzeer@node2-lan1-tp2 ~]$ ping 94.23.214.79
PING 94.23.214.79 (94.23.214.79) 56(84) bytes of data.
64 bytes from 94.23.214.79: icmp_seq=1 ttl=51 time=17.3 ms
64 bytes from 94.23.214.79: icmp_seq=2 ttl=51 time=13.7 ms
64 bytes from 94.23.214.79: icmp_seq=3 ttl=51 time=13.9 ms
64 bytes from 94.23.214.79: icmp_seq=4 ttl=51 time=13.6 ms
64 bytes from 94.23.214.79: icmp_seq=5 ttl=51 time=13.7 ms

--- 94.23.214.79 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4008ms
rtt min/avg/max/mdev = 13.588/14.426/17.266/1.423 ms

[lytzeer@node2-lan1-tp2 ~]$ ping cataas.com
PING cataas.com (94.23.214.79) 56(84) bytes of data.
64 bytes from ns304722.ip-94-23-214.eu (94.23.214.79): icmp_seq=1 ttl=51 time=14.9 ms
64 bytes from ns304722.ip-94-23-214.eu (94.23.214.79): icmp_seq=2 ttl=51 time=14.4 ms
64 bytes from ns304722.ip-94-23-214.eu (94.23.214.79): icmp_seq=3 ttl=51 time=13.3 ms
64 bytes from ns304722.ip-94-23-214.eu (94.23.214.79): icmp_seq=4 ttl=51 time=13.6 ms
64 bytes from ns304722.ip-94-23-214.eu (94.23.214.79): icmp_seq=5 ttl=51 time=13.3 ms

--- cataas.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4005ms
rtt min/avg/max/mdev = 13.310/13.915/14.914/0.627 ms
```

# III. Services réseau

## 1. DHCP

☀️ **Sur `dhcp.lan1.tp2`**

```shell
[lytzeer@dhcp-lan1-tp2 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:8c:b7:e4 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.253/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe8c:b7e4/64 scope link
       valid_lft forever preferred_lft forever

[lytzeer@dhcp-lan1-tp2 ~]$ sudo dnf install -y dhcp-server

[lytzeer@dhcp-lan1-tp2 ~]$ sudo cat /etc/dhcp/dhcpd.conf
default-lease-time 900;
max-lease-time 10800;

authoritative;

subnet 10.1.1.0 netmask 255.255.255.0 {
range 10.1.1.100 10.1.1.200;
option routers 10.1.1.254;
option subnet-mask 255.255.255.0;
option domain-name-servers 1.1.1.1;
}

[lytzeer@dhcp-lan1-tp2 ~]$ sudo firewall-cmd --add-service=dhcp
success
[lytzeer@dhcp-lan1-tp2 ~]$ sudo firewall-cmd --reload
success

[lytzeer@dhcp-lan1-tp2 ~]$ sudo systemctl enable --now dhcpd
Created symlink /etc/systemd/system/multi-user.target.wants/dhcpd.service → /usr/lib/systemd/system/dhcpd.service.
[lytzeer@dhcp-lan1-tp2 ~]$ sudo systemctl status dhcpd | grep Status
     Status: "Dispatching packets..."
```

☀️ **Sur `node1.lan1.tp2`**

```shell
[lytzeer@node1-lan1-tp2 ~]$ sudo dhclient -v enp0s8
[sudo] password for lytzeer:
Internet Systems Consortium DHCP Client 4.4.2b1
Copyright 2004-2019 Internet Systems Consortium.
All rights reserved.
For info, please visit https://www.isc.org/software/dhcp/

Listening on LPF/enp0s8/08:00:27:7a:71:f1
Sending on   LPF/enp0s8/08:00:27:7a:71:f1
Sending on   Socket/fallback
DHCPDISCOVER on enp0s8 to 255.255.255.255 port 67 interval 5 (xid=0x80aefd2f)
DHCPOFFER of 10.1.1.101 from 10.1.1.253
DHCPREQUEST for 10.1.1.101 on enp0s8 to 255.255.255.255 port 67 (xid=0x80aefd2f)
DHCPACK of 10.1.1.101 from 10.1.1.253 (xid=0x80aefd2f)
bound to 10.1.1.101 -- renewal in 421 seconds

[lytzeer@node1-lan1-tp2 ~]$ ip r s
default via 10.1.1.254 dev enp0s8 proto dhcp src 10.1.1.101 metric 100

[lytzeer@node1-lan1-tp2 ~]$ ping 10.1.2.11
PING 10.1.2.11 (10.1.2.11) 56(84) bytes of data.
64 bytes from 10.1.2.11: icmp_seq=1 ttl=63 time=0.519 ms
64 bytes from 10.1.2.11: icmp_seq=2 ttl=63 time=0.455 ms
64 bytes from 10.1.2.11: icmp_seq=3 ttl=63 time=0.420 ms

--- 10.1.2.11 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2061ms
rtt min/avg/max/mdev = 0.420/0.464/0.519/0.041 ms
```

## 2. Web web web

☀️ **Sur `web.lan2.tp2`**

```shell
[lytzeer@web-lan2-tp2 ~]$ sudo dnf install nginx

[lytzeer@web-lan2-tp2 ~]$ sudo cat /etc/nginx/nginx.conf
server {
        listen       80;
        listen       [::]:80;
        server_name  _;
        root         /var/www/site_nul/;

[lytzeer@web-lan2-tp2 ~]$ sudo firewall-cmd --permanent --add-service=http
success
[lytzeer@web-lan2-tp2 ~]$ sudo firewall-cmd --reload
success

[lytzeer@node2-lan2-tp2 ~]$ sudo ss -ltunp | grep nginx
tcp   LISTEN 0      511          0.0.0.0:80        0.0.0.0:*    users:(("nginx",pid=1838,fd=6),("ngin",pid=1837,fd=6))
tcp   LISTEN 0      511             [::]:80           [::]:*    users:(("nginx",pid=1838,fd=7),("ngin",pid=1837,fd=7))

[lytzeer@node2-lan2-tp2 ~]$ sudo firewall-cmd --list-all | grep services
  services: cockpit dhcpv6-client http ssh
```

☀️ **Sur `node1.lan1.tp2`**

```shell

[lytzeer@node1-lan1-tp2 ~]$ curl site_nul.tp2
<!DOCTYPE html>
<html>
<head>
<title>Bojou</title>
</head>
<body>

<h1>Hello There</h1>
<p>Le site est magnifiquement magnifique</p>

</body>
</html>
```