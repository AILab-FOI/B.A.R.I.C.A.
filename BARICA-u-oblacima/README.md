B.A.R.I.C.A. kontroler
======================

Inicijalna implementacija kontrolera, back-end API-ja i dva front-end
API-ja (REST i WebSocket). Ovo je samo okvir, nedostaje većina 
funkcionalnosti!

Preduvjeti
----------
Python 3, moduli Flask, Flask-Login, SimpleWebSocketServer, tqdm i pyxf
te SWI Prolog za pokretanje primjera baze znanja.

'''
sudo pip3 install flask flask-login SimpleWebSocketServer tqdm
sudo pip3 install  git+https://github.com/AILab-FOI/pyxf
sudo apt install swi-prolog
'''

Pokretanje
----------
Pokrenuti 

'''
./controller
'''

Zatim u pregledniku isprobati adresu za REST API:

'''
http://localhost:5000/ask/%7B%20%22module%22:%22DummyTestingModule%22,%20%22method%22:%22eval%22,%20%22args%22:[%20%223%20*%209%22%20]%20%7D
'''

Odnosno za WS API

'''
http://localhost:5000/wsapi-test
'''

Primjer modula
--------------

U direktoriju *modules* nalazi se primjer modula (ključna je datoteka
interface.json u kojoj je specifikacija modula i kako se pokreće).
Svaki modul može imati jednu ili više metoda navedenih u toj datoteci
koje se onda preko front-end API-ja mogu pozivati.

U načelu, modul može biti implementiran u bilo kojoj tehnologiji bitno
da radi na konzoli i vraća odgovarajući JSON format.

Za sada je implementirana samo veza upit-odgovor (kad klijent pošalje
upit, poslužitelj vraća odgovor), no postoji i mogućnost push veze
(poslužitelj šalje poruke). Taj dio još treba razraditi da se omogući
stream podataka (npr. putem nekakvog pipe-a na strani modula koji
se proslijeđuje klijentu, odnosno stream-a na strani klijenta koji
se proslijeđuje modulu). 


