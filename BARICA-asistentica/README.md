B.A.R.I.C.A. - asistentica
==========================

BARICA-asistentica (engl. Beautiful ARtificial Intellgence Chat Agent)
je umjetna inteligencija za pripomoć pri prezentaciji. Sastoji se od
sljedećih komponenti:
1. Chatbot - neuronska mreža koja odlučuje o odgovoru na upit 
prirodnim jezikom;
2. Backend - inteligentni sustav koji upravlja ostalim komponentama
(prezentacijom, neuronskom mrežom, speech to text servisom, video
sučeljem);
3. Frontend - prezentacija, video sučelje i kontroler.

Izvedba
-------
Chatbot je implementiran u Python 3 programskom jeziku uz modul
chatterbot te se sastoji od niza potencijalnih naredbi koje osoba
može dati Barici te naredbi koje valja izvršiti za svaku naredbu.

Backend je također implementiran u Python 3 programskom jeziku
te se sastoji od WebSocket servera koji razgovara s frontend-om
konačnog automata koji u ovisnosti o kontekstu i konverzacijskoj
situaciji pokreće odgovarajuće komande. Backend također upravlja
prezentacijom kroz pyautogui (automatizacija grafičkog sučelja) 
odnosno slanjem komandi frontendu da primjerice pokrene određenu
sekvencu govora.

Frontend se sastoji od nekoliko komponenti. Prezentacija koja je
kreirana uz Hovercraft.js koji iz ReStructuredText-a generira
vizualno atraktivnu prezentaciju (za sada prezentacija za VIDI
Awards, no uskoro slijedi uopćavanje), zatim videa kreiranog uz
pomoć alata CrazyTalk koji sadrži sve govorne sekvence koje Barica
podržava, te na kraju kontrolera implementiranog u JavaScript-u
koji kroz WebSocket komunicira s backendom i izvršava odgovarajuće
komande (npr. pokretanje odgovarajuće sekvence govora).

Instalacij i pokretanje
-----------------------
Da bi se pokrenulo Baricu - asistenticu potrebno je instalirati
Voicenotebook kao dodatak u Google Chrome (https://voicenotebook.com/)
te podesiti speech language na hrvatski i uključiti opciju transfer
to clipboard. Zatim pokrenuti start recording.

Instalirati sve potrebne module za pokretanje backenda (pyperclip, 
SimpleWebSocketServer, pyautogui, chatterbot). Zatim, u pozadini 
pokrenuti backend (talk.py) pri čemu pri prvom pokretanju treba 
pokrenuti s opcijom --train kako bi se istrenirala mreža. 

```
python3 talk.py --train
python3 talk.py
```

Treba napraviti build prezentacije uz hovercraft npr u build 
direktorij:

```
hovercraft prezentacija.rst build
```

Na kraju otvoriti novi tab na Google Chrome pregledniku i otvoriti
lokaciju putanja/do/build/index.html. Tipka F11 će prezentaciju
staviti na full screen.

Napomene uz licencu
-------------------
Slika Barice je preuzeta pod fair use sa sljedeće adrese:
https://pixabay.com/en/woman-robot-artificial-intelligence-3124083/


