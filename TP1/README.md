# TP1 : Maîtrise réseau du poste

Pour ce TP, on va utiliser **uniquement votre poste** (pas de VM, rien, quedal, quetchi).

Le but du TP : se remettre dans le bain tranquillement en manipulant pas mal de concepts qu'on a vu l'an dernier.

C'est un premier TP *chill*, qui vous(ré)apprend à maîtriser votre poste en ce qui concerne le réseau. Faites le seul ou avec votre mate préféré bien sûr, mais jouez le jeu, faites vos propres recherches.

La "difficulté" va crescendo au fil du TP, mais la solution tombe très vite avec une ptite recherche Google si vos connaissances de l'an dernier deviennent floues.

- [TP1 : Maîtrise réseau du poste](#tp1--maîtrise-réseau-du-poste)
- [I. Basics](#i-basics)
- [II. Go further](#ii-go-further)
- [III. Le requin](#iii-le-requin)

# I. Basics

> Tout est à faire en ligne de commande, sauf si précision contraire.

☀️ **Carte réseau WiFi**
```
PS C:\Users\lukas> ipconfig -all

Carte réseau sans fil Wi-Fi :

   Adresse physique . . . . . . . . . . . : 7C-21-4A-E4-8A-27
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.76.190(préféré)
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0
   Masque de sous réseau notation CIDR : /20 
```

☀️ **Déso pas déso**
```
10.33.64.0
10.33.79.255
4096
```

☀️ **Hostname**
```
PS C:\Users\lukas> hostname
DESKTOP-URQ404I
```

☀️ **Passerelle du réseau**
```
PS C:\Users\lukas> ipconfig -all

Carte réseau sans fil Wi-Fi :

   Passerelle par défaut. . . . . . . . . : 10.33.79.254
```
☀️ **Serveur DHCP et DNS**

```
PS C:\Users\lukas> arp -a | findstr 10.33.79.254
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
```

☀️ **Table de routage**
```
PS C:\Users\lukas> route print | findstr 10.33.79.254
          0.0.0.0          0.0.0.0     10.33.79.254     10.33.76.190     30

PS C:\Users\lukas> ipconfig -all
          Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
```

# II. Go further

> Toujours tout en ligne de commande.

---

☀️ **Hosts ?**

- faites en sorte que pour votre PC, le nom `b2.hello.vous` corresponde à l'IP `1.1.1.1`
- prouvez avec un `ping b2.hello.vous` que ça ping bien `1.1.1.1`
```
PS C:\Users\lukas> cat C:\Windows\System32\drivers\etc\hosts | findstr 1.1.1.1
1.1.1.1 b2.hello.vous

PS C:\Users\lukas> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=14 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 10ms, Maximum = 14ms, Moyenne = 11ms
```
> Vous pouvez éditer en GUI, et juste me montrer le contenu du fichier depuis le terminal pour le compte-rendu.

---

☀️ **Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**
```
PS C:\Users\lukas> netstat -n

Connexions actives

  Proto  Adresse locale         Adresse distante       État
  TCP    10.33.76.190:50113     142.250.75.228:443    ESTABLISHED

Port serveur : 443

Port Local : 50113
```

☀️ **Requêtes DNS**

Déterminer...

- à quelle adresse IP correspond le nom de domaine `www.ynov.com`

```
PS C:\Users\lukas> nslookup www.ynov.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    www.ynov.com
Addresses:  2606:4700:20::681a:be9
          2606:4700:20::ac43:4ae2
          2606:4700:20::681a:ae9
          104.26.10.233
          104.26.11.233
          172.67.74.226
```

> Ca s'appelle faire un "lookup DNS".

```
PS C:\Users\lukas> nslookup 174.43.238.89
Serveur :   dns.google
Address:  8.8.8.8

Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```

> Ca s'appelle faire un "reverse lookup DNS".

---

☀️ **Hop hop hop**

```
PS C:\Users\lukas> tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [104.26.10.233]
avec un maximum de 30 sauts :

  1     3 ms     1 ms     1 ms  10.33.79.254
  2     3 ms     2 ms     2 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     3 ms     2 ms     2 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     3 ms     3 ms     2 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    11 ms    11 ms    10 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  6    10 ms    10 ms     9 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  7    10 ms     9 ms    10 ms  141.101.67.48
  8    12 ms    12 ms    14 ms  141.101.67.54
  9    10 ms    10 ms     9 ms  104.26.10.233
```

☀️ **IP publique**

```
PS C:\Users\lukas> curl ifconfig.me

Content           : 195.7.117.146
```

☀️ **Scan réseau**

Déterminer...

- combien il y a de machines dans le LAN auquel vous êtes connectés

> Allez-y mollo, on va vite flood le réseau sinon. :)

# III. Le requin

☀️ **Capture ARP**

[Lien vers capture ARP](./captures/arp.pcap)

☀️ **Capture DNS**

[Lien vers capture DNS](./captures/dns.pcap)

☀️ **Capture TCP**

[Lien vers capture TCP](./captures/tcp.pcap)
