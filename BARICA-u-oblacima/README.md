B.A.R.I.C.A. kontroler
======================

Inicijalna implementacija kontrolera, back-end API-ja i tri front-end
API-ja (REST, WebSocket i Slack-bot). Ovo je samo okvir, nedostaje
većina funkcionalnosti!

Preduvjeti
----------
Python 3, moduli Flask, Flask-Login, SimpleWebSocketServer, tqdm,
slackclient i pyxf te SWI Prolog za pokretanje primjera baze znanja.

```
sudo pip3 install flask flask-login SimpleWebSocketServer tqdm slackclient
sudo pip3 install  git+https://github.com/AILab-FOI/pyxf
sudo apt install swi-prolog
```

Pokretanje
----------
Pokrenuti 

```
./controller.py --ip localhost
```

Po potrebi je moguće podesiti IP adresu i port na kojem se pokreće poslužitelj:

```
$ ./controler.py --help
usage: controler.py [-h] [--ip [IP]] [--port [PORT]]

optional arguments:
  -h, --help     show this help message and exit
  --ip [IP]      Specify the IP address of the server.
  --port [PORT]  Specify the port of the server.
```

Zatim u pregledniku isprobati adresu za REST API:

```
http://localhost:5000/ask/%7B%20%22module%22:%22DummyTestingModule%22,%20%22method%22:%22eval%22,%20%22args%22:[%20%223%20*%209%22%20]%20%7D
```

Odnosno za WS API

```
http://localhost:5000/wsapi-test
```

Za Slack-bot API potrebno je više koraka opisanih [ovdje](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html).
Najvažniji korak (osim instalacije aplikacije na Slack workspace-u) je
postavljanje *SLACK_BOT_TOKEN* varijable okružja:

```
export SLACK_BOT_TOKEN='vaš token'
```

Primjer modula
--------------

U direktoriju *modules* nalaze se primjeri modula (ključna je datoteka
interface.json u kojoj je specifikacija modula i kako se pokreće).
Svaki modul može imati jednu ili više metoda navedenih u toj datoteci
koje se onda preko front-end API-ja mogu pozivati.

U načelu, modul može biti implementiran u bilo kojoj tehnologiji bitno
da radi na konzoli i vraća odgovarajući JSON format.

Za sada je implementirana veza upit-odgovor (kad klijent pošalje
upit, poslužitelj vraća odgovor), no postoji i mogućnost push veze
(poslužitelj šalje poruke).

Također, omogućen je stream podataka putem net cat poslužitelja
(putem pipe-a na strani modula koji se proslijeđuje klijentu, odnosno
stream-a na strani klijenta koji se proslijeđuje modulu).

Za primjere klijenata pogledati u [dokumentaciju BARICE-u-oblacima](https://github.com/AILab-FOI/B.A.R.I.C.A./tree/master/BARICA-u-oblacima/doc).


