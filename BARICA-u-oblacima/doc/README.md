B.A.R.I.C.A. u oblacima - primjeri
==================================

B.A.R.I.C.A. u oblacima (ilitiga cloud back-end API) je dio Barice koji omogućuje
korištenje različitih mehanizama umjetne inteligencije u obliku modula. U nastavku je
nekoliko primjera:

Primjer upita
=============

U direktoriju *examples* nalazi se datoteka *example-query.json* koja sadrži primjer JSON
upita koji se može postaviti nad WebSocket ili REST API-jem. U direktoriju *html* je datoteka
*wsapi-test.html* koja koristi upravo takav upit s WebSocketom. Za REST API moguće je koristiti
sljedeću adresu:

```
http://barica-host:port/json-upit
```

Gdje je *barica-host* host na kojem je pokrenuta Barica (npr. localhost ili 127.0.0.1),
*port* odgovarajući port (npr. 5000), a *json-upit* upit kao što je naveden u gornjoj
datoteci.

Primjer toka podataka
=====================

U direktoriju *examples* nalaze se datoteke *num-generator.sh* i *reciever.py* koje
omogućuju slanje i primanje toka (engl. stream) podataka na oblak. Konkretno koristi
se *dummy_stream* modul koji za poslani niz brojeva vraća odgovarajući broj Fibonaccijeve
sekvence. Umjesto *num-generator.sh* može se koristiti i *num-generator.py* odnosno
bilo koji program u bilo kojem programskom jeziku koji će generirati sekvencu cijelih
brojeva ako se pozove na način:

```
./num-generator.sh [broj]
```

Gdje je [broj] broj brojeva koje treba generirati (svaki se ispisuje u novom redu).

Nakon što se pokrene B.A.R.I.C.A. controller.py, npr.

```
./controler.py --ip localhost
```

Potrebno je pokrenuti *reciever.py* uz Netcat server na sljedeći način:

```
nc -lp 1234 | ./reciever.py localhost 5000
```

Pod pretpostavkom da je controler pokrenut na localhost-u na portu 5000.

Skripta će ispisati nasumičnu sekvencu Fibonaccijevih brojeva.

Što se u svari događa? Skripta *reciever.py* šalje upit B.A.R.I.C.A.
poslužitelju da želi koristiti dummy_stream modul, tj. njegovu metodu
fibonacci_stream, te daje do znanja da osluškuje port 1234 na hostu
localhost (tu nam pomaže Netcat poslužitelj). B.A.R.I.C.A. odgovara
u redu, evo na portu XY sam ti otvorila svoj poslužitelj na koji
možeš slati svoj tok podataka (stream), a ja ću tvoje podatke
proslijediti metodi fibonacci_stream i reziltate u obliku toka
slati na tvoj polsužitej (locahost:1234). Skripta *reciever.py*
tada pokreće skriptu *num-generator.sh* (po defaultu će generirati
100 random brojeva u obliku toka podataka) te ih opet putem Netcat-a
šalje na B.A.R.I.C.A. poslužitelj na port XY koji joj je dodjeljen.
S druge strane čeka skripta *fib-generator.py* koja za svaki primljeni
broj generira odgovarajući Fibonaccijev broj koji se u obliku toka
opet putem Netcat poslužitelja šalje skripti *reciever.py*.

Uočite da su ovdje ulančane 3 skripte i dva Netcat poslužitelja. U
načelu, bez B.A.R.I.C.A. poslužitelja isti bismo efekt postigli da
pokrenemo sljedeće tri naredbe (svaku u svojem prozoru):

```
nc -lp 1234 | ./reciever.py
nc -lp 1234 | ./fib-generator.py fibonacci_stream | nc localhost 4321
./num-generator.sh 100 | nc localhost 4321
```

Pri čemu je redosljed bitan, uz pretpostavku da se iz *reciever.py*
ispusti dio koda koji se spaja na poslužitelj i pokreće drugu skriptu
(linije 35 - 48). Rezultati se ispisuju u prozoru gdje je pokrenuta
skripta *reciever.py*.

Uočite također da su skripte *reciever.py* i *fib-generator.py* tzv.
filtri, tj. čitaju podatke sa stdin i pišu rezultate na stdout.
Upravo nam je to omogućilo da putem cjevovoda (engl. pipe "|")
povežemo priču preko Netcat poslužitelja.
