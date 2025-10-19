from chatterbot.trainers import ListTrainer

LOGIC_ADAPTER = [
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.66,
            'default_response': 'ponovi'
        }
    ]

def train(bot):
    bot.set_trainer(ListTrainer)
    chatbot = bot

    chatbot.train([
        'Kako se zovu riječi koje zamjenjuju druge riječi?',
        '01'
    ])
    chatbot.train([
        'Koje riječi zamjenjuju druge riječi?',
        '01'
    ])
    chatbot.train([
        'Koje su riječi koje zamjenjuju druge riječi?',
        '01'
    ])
    chatbot.train([
        'Kako se zovu riječi koje zamjenjuju riječi?',
        '01'
    ])


    chatbot.train([
        'Koje su osobne zamjenice?',
        '02'
    ])
    chatbot.train([
        'Nabroji osobne zamjenice?',
        '02'
    ])
    chatbot.train([
        'Koje osobne zamjenice postoje?',
        '02'
    ])
    chatbot.train([
        'Navedi osobne zamjenice?',
        '02'
    ])

    chatbot.train([
        'Kako se zovu zamjenice kojima zamjenjujemo govorne osobe?',
        '03'
    ])
    chatbot.train([
        'Koje zamjenice zamjenjuju govorne osobe?',
        '03'
    ])
    chatbot.train([
        'Kojim zamjenicama zamjenjujemo govorne osobe?',
        '03'
    ])
    chatbot.train([
        'Navedi koje su zamjenice kojima zamjenjujemo govorne osobe?',
        '03'
    ])


    chatbot.train([
        'Koje su zamjenice negovorne osobe?',
        '04'
    ])
    chatbot.train([
        'Koje zamjenice zamjenjuju negovorne osobe?',
        '04'
    ])
    chatbot.train([
        'Navedi zamjenice negovorne osobe?',
        '04'
    ])
    chatbot.train([
        'Nabroji zamjenice negovorne osobe?',
        '04'
    ])


    chatbot.train([
        'Kako se zove promjena oblika osobnih zamjenica?',
        '05'
    ])
    chatbot.train([
        'Kako se naziva promjena oblika osobnih zamjenica?',
        '05'
    ])
    chatbot.train([
        'Kako se zove promjena osobnih zamjenica?',
        '05'
    ])
    chatbot.train([
        'Kako se naziva promjena osobnih zamjenica?',
        '05'
    ])

    chatbot.train([
        'Kada zamjenicu vi pišemo velikim početnim slovom?',
        '06'
    ])
    chatbot.train([
        'Kada se zamjenica vi piše velikim početnim slovom?',
        '06'
    ])
    chatbot.train([
        'Kada zamjenicu vi pišemo velikim slovom?',
        '06'
    ])
    chatbot.train([
        'Kada se zamjenicu vi piše velikim slovom?',
        '06'
    ])

    chatbot.train([
        'Koje su posvojne zamjenice?',
        '07'
    ])
    chatbot.train([
        'Navedi posvojne zamjenice?',
        '07'
    ])
    chatbot.train([
        'Nabroji posvojne zamjenice?',
        '07'
    ])
    chatbot.train([
        'Koje posvojne zamjenice postoje?',
        '07'
    ])


    chatbot.train([
        'Što zamjenjuju posvojne zamjenice?',
        '08'
    ])
    chatbot.train([
        'Što mijenjaju posvojne zamjenice?',
        '08'
    ])
    chatbot.train([
        'Koju vrstu riječi zamjenjuju posvojne zamjenice?',
        '08'
    ])
    chatbot.train([
        'Koje riječi zamjenjuju posvojne zamjenice?',
        '08'
    ])

    chatbot.train([
        'Na koje pitanje odgovaraju posvojne zamjenice?',
        '09'
    ])
    chatbot.train([
        'Koje pitanje odgovaraju posvojne zamjenice?',
        '09'
    ])
    chatbot.train([
        'Na koje pitanje odgovaramo posvojnim zamjenicama?',
        '09'
    ])
    chatbot.train([
        'Na koje se pitanje odgovara posvojnim zamjenicama?',
        '09'
    ])


    chatbot.train([
        'Što izriču posvojne zamjenice?',
        '10'
    ])
    chatbot.train([
        'Što govore posvojne zamjenice?',
        '10'
    ])
    chatbot.train([
        'Što iskazuju posvojne zamjenice?',
        '10'
    ])
    chatbot.train([
        'Što kazuju posvojne zamjenice?',
        '10'
    ])


    chatbot.train([
        'U čemu se posvojne zamjenice slažu s imenicom uz koju stoje?',
        '11'
    ])
    chatbot.train([
        'Po čemu se posvojne zamjenice slažu s imenicom uz koju stoje?',
        '11'
    ])
    chatbot.train([
        'U čemu se posvojne zamjenice slažu s imenicom?',
        '11'
    ])
    chatbot.train([
        'U čemu se posvojne zamjenice slažu s rječju uz koju stoje?',
        '11'
    ])


    chatbot.train([
        'Kako pišemo posvojne zamjenice vaš, vaša, vaše pri obraćanju dvjema osobama ili skupini ljudi?',
        '12'
    ])
    chatbot.train([
        'Kako se pišu posvojne zamjenice vaš, vaša, vaše pri obraćanju dvjema osobama ili skupini ljudi?',
        '12'
    ])
    chatbot.train([
        'Kako pišemo posvojne zamjenice vaš, vaša, vaše pri obraćanju skupini ljudi?',
        '12'
    ])
    chatbot.train([
        'Kako pišemo posvojne zamjenice vaš, vaša, vaše pri obraćanju dvjema osobama?',
        '12'
    ])


    chatbot.train([
        'Kojoj skupini riječi pripadaju zamjenice?',
        '13'
    ])
    chatbot.train([
        'Kojoj skupini pripadaju zamjenice?',
        '13'
    ])
    chatbot.train([
        'U koju skupinu riječi spadaju zamjenice?',
        '13'
    ])
    chatbot.train([
        'U kojoj skupini riječi su zamjenice?',
        '13'
    ])


    chatbot.train([
        'Što izriče povratna zamjenica sebe?',
        '14'
    ])
    chatbot.train([
        'Što iskazuje povratna zamjenica sebe?',
        '14'
    ])
    chatbot.train([
        'Što govori povratna zamjenica sebe?',
        '14'
    ])
    chatbot.train([
        'Što kazuje povratna zamjenica sebe?',
        '14'
    ])


    chatbot.train([
        'Koji se oblici zamjenica mogu naći na početku rečenice?',
        '15'
    ])
    chatbot.train([
        'Koji oblici zamjenica mogu biti na početku rečenice?',
        '15'
    ])
    chatbot.train([
        'Koji oblici zamjenica su na početku rečenice?',
        '15'
    ])
    chatbot.train([
        'Koji su oblici zamjenica na početku rečenice?',
        '15'
    ])


    chatbot.train([
        'Ima li povratna zamjenica sebe oblike u nominativu i vokativu?',
        '16'
    ])
    chatbot.train([
        'Ima li povratna zamjenica sebe oblik u nominativu?',
        '16'
    ])
    chatbot.train([
        'Ima li povratna zamjenica sebe oblik u vokativu?',
        '16'
    ])
    chatbot.train([
        'Je li povratna zamjenica sebe ima oblike u nominativu i vokativu?',
        '16'
    ])


    chatbot.train([
        'Što izriče povratno-posvojna zamjenica svoj?',
        '17'
    ])
    chatbot.train([
        'Što govori povratno-posvojna zamjenica svoj?',
        '17'
    ])
    chatbot.train([
        'Što iskazuje povratno-posvojna zamjenica svoj?',
        '17'
    ])
    chatbot.train([
        'Što kazuje povratno-posvojna zamjenica svoj?',
        '17'
    ])


    chatbot.train([
        'Koje zamjenice zamjenjuje povratno-posvojna zamjenica svoj?',
        '18'
    ])
    chatbot.train([
        'Što zamjenjuje povratno-posvojna zamjenica svoj?',
        '18'
    ])
    chatbot.train([
        'Koje riječi zamjenjuje povratno-posvojna zamjenica svoj?',
        '18'
    ])
    chatbot.train([
        'Navedi zamjenice koje zamjenjuje povratno-posvojna zamjenica svoj?',
        '18'
    ])


    chatbot.train([
        'Kojim oblicima zamjenica dajemo prednost?',
        '19'
    ])
    chatbot.train([
        'Navedi oblike zamjenica kojima dajemo prednost?',
        '19'
    ])
    chatbot.train([
        'Kakvim oblicima zamjenica dajemo prednost?',
        '19'
    ])
    chatbot.train([
        'Kakovim oblicima zamjenica dajemo prednost?',
        '19'
    ])


    chatbot.train([
        'Koje su riječi pokazne zamjenice?',
        '20'
    ])
    chatbot.train([
        'Navedi pokazne zamjenice?',
        '20'
    ])
    chatbot.train([
        'Koje su pokazne zamjenice?',
        '20'
    ])
    chatbot.train([
        'Nabroji pokazne zamjenice?',
        '20'
    ])


    chatbot.train([
        'Na koja pitanja odgovaraju pokazne zamjenice?',
        '21'
    ])
    chatbot.train([
        'Navedi pitanja na koja odgovaraju pokazne zamjenice?',
        '21'
    ])
    chatbot.train([
        'Na kakva pitanja odgovaraju pokazne zamjenice?',
        '21'
    ])
    chatbot.train([
        'Koja su pitanja na koja odgovaraju pokazne zamjenice?',
        '21'
    ])


    chatbot.train([
        'Tko si?',
        'predstavljanje-kratko'
    ])

    chatbot.train([
        'Bok, tko si ti?',
        'predstavljanje-kratko'
    ])

    chatbot.train([
        'Bok',
        'predstavljanje-kratko'
    ])

    chatbot.train([
        'Dobar dan',
        'predstavljanje-kratko'
    ])

    chatbot.train([
        'Pozdrav',
        'predstavljanje-kratko'
    ])

    chatbot.train([
        'Dobro večer',
        'predstavljanje-kratko'
    ])

    chatbot.train([
        'Dobro jutro',
        'predstavljanje-kratko'
    ])

    chatbot.train([
        'Bok, kak se zoveš?',
        'predstavljanje-kratko'
    ])

    chatbot.train([
        'Kak se zoveš?',
        'predstavljanje-kratko'
    ])

    chatbot.train([
        'Kako se zoveš?',
        'predstavljanje-kratko'
    ])

    chatbot.train([
        'Milka men?',
        'izvoli'
    ])
    chatbot.train([
        'Mister brundo?',
        'izvoli'
    ])
    chatbot.train([
        'Nadot?',
        'izvoli'
    ])

    chatbot.train([
        'Mister brundo, jesi li tu?',
        'izvoli'
    ])
    chatbot.train([
        'Milka men, jesi li tu?',
        'izvoli'
    ])
    chatbot.train([
        'Nadot, jesi li tu?',
        'izvoli'
    ])


    chatbot.train([
        'Milka men, si tu?',
        'izvoli'
    ])
    chatbot.train([
        'Mister brundo, si tu?',
        'izvoli'
    ])
    chatbot.train([
        'Nadot, si tu?',
        'izvoli'
    ])

    chatbot.train([
        'Si tu?',
        'izvoli'
    ])

    chatbot.train([
        'Me čuješ?',
        'izvoli'
    ])

    chatbot.train([
        'Slušaš?',
        'izvoli'
    ])

    chatbot.train([
        'Tko te je napravio?',
        'predstavljanje-dugo'
    ])

    chatbot.train([
        'Tko te je stvorio?',
        'predstavljanje-dugo'
    ])

    chatbot.train([
        'Tko je tvoj tvorac?',
        'predstavljanje-dugo'
    ])

    chatbot.train([
        'Kako si?',
        'dobro'
    ])
    chatbot.train([
        'Kako ti je s nama?',
        'lijepo'
    ])
    chatbot.train([
        'Bravo',
        'hvala'
    ])

    chatbot.train([
        'Odlično',
        'hvala'
    ])

    chatbot.train([
        'Izvrsno',
        'hvala'
    ])

    chatbot.train([
        'Jako dobro',
        'hvala'
    ])

    chatbot.train([
        'Hvala',
        'hvala'
    ])

