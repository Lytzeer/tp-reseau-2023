# I. Simple bs program

- [I. Simple bs program](#i-simple-bs-program)
  - [1. First steps](#1-first-steps)
  - [2. User friendly](#2-user-friendly)
  - [3. You say client I hear control](#3-you-say-client-i-hear-control)

## 1. First steps
```shell
[lytzeer@serveur ~]$ git clone https://github.com/Lytzeer/serveur-reseau.git
[lytzeer@serveur ~]$ cd serveur-reseau/
[lytzeer@serveur serveur-reseau]$ python bs_server_I1.py
Connected by ('10.1.4.3', 50502)
Données reçues du client : b'Meooooo !'
```
```shell
[lytzeer@client ~]$ git clone https://github.com/Lytzeer/client-reseau.git
[lytzeer@client ~]$ cd client-reseau/
[lytzeer@client client-reseau]$ python bs_client_I1.py
Le serveur a répondu b'Hi mate !'
```
```shell
[lytzeer@serveur ~]$ ss -altnp | grep 13337
LISTEN 0      1            0.0.0.0:13337      0.0.0.0:*    users:(("python",pid=1440,fd=3))
```
## 2. User friendly

🌞 **`bs_client_I2.py`**

> Vous aurez besoin du [**cours sur la gestion d'erreurs**](../../../../cours/dev/error_handling/README.md) pour cette partie.

- retour visuel
  - afficher un message de succès chez le client quand il se co au serveur
  - le message doit être : `Connecté avec succès au serveur <IP_SERVER> sur le port <PORT>`
  - vous utiliserez un `try` `except` pour savoir si la connexion est correctement effectuée
- le programme doit permettre à l'utilisateur d'envoyer la string qu'il veut au serveur
  - on peut récupérer un input utilisateur avec la fonction `input()` en Python
  - au lancement du programme, un prompt doit apparaître pour indiquer à l'utilisateur qu'il peut envoyer une string au serveur :
    - `Que veux-tu envoyer au serveur : `

🌞 **`bs_server_I2.py`**

- retour visuel
  - afficher un message de succès quand un client se co
  - le message doit être : `Un client vient de se co et son IP c'est <CLIENT_IP>.`
- réponse adaptative
  - si le message du client contient "meo" quelque part, répondre : `Meo à toi confrère.`
  - si le message du client contient "waf" quelque part, répondre : `ptdr t ki`
  - si le message du client ne contient PAS "meo", ni "waf", répondre :  `Mes respects humble humain.`

## 3. You say client I hear control

On va ajouter un peu de contrôle pour éviter que notre client fasse nawak à l'utilisation du programme.

🌞 **`bs_client_I3.py`**

- vérifier que...
  - le client saisit bien une string
    - utilisez la méthode native `type()` pour vérifier que c'est une string
  - que la string saisie par le client contient obligatoirement soit "waf" soit "meo"
    - utilisez [**une expression régulière**](https://www.programiz.com/python-programming/regex) (signalez-le moi s'il serait bon de faire un cours sur cette notion)
- sinon lever une erreur avec `raise`
  - choisissez avec pertinence l'erreur à lever dans les deux cas (s'il saisit autre chose qu'une string, ou si ça contient aucun des deux mots)
  - y'a une liste des exceptions natives (choisissez-en une donc) tout en bas du [cours sur la gestion d'erreur](../../../../cours/dev/error_handling/README.md)

> On poussera le contrôle plus loin plus tard.