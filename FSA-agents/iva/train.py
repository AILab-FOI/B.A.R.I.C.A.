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
        'Što je ravnina?',
        '01'
    ])

    chatbot.train([
        'Što je to ravnina?',
        '01'
    ])

    chatbot.train([
        'Definiraj ravninu!',
        '01'
    ])

    chatbot.train([
        'Što je točka?',
        '02'
    ])

    chatbot.train([
        'Što je to točka?',
        '02'
    ])

    chatbot.train([
        'Definiraj točku!',
        '02'
    ])

    chatbot.train([
        'Što je pravac?',
        '03'
    ])

    chatbot.train([
        'Što je to pravac?',
        '03'
    ])

    chatbot.train([
        'Definiraj pravac!',
        '03'
    ])

    chatbot.train([
        'Što je polupravac?',
        '04'
    ])

    chatbot.train([
        'Što je to polupravac?',
        '04'
    ])

    chatbot.train([
        'Definiraj polupravac!',
        '04'
    ])

    chatbot.train([
        'Što je dužina?',
        '05'
    ])

    chatbot.train([
        'Što je to dužina?',
        '05'
    ])

    chatbot.train([
        'Definiraj dužinu!',
        '05'
    ])


    chatbot.train([
        'Što je kut?',
        '06'
    ])

    chatbot.train([
        'Što je to kut?',
        '06'
    ])

    chatbot.train([
        'Definiraj kut!',
        '06'
    ])

    chatbot.train([
        'Nabroji vrste kutova.',
        '07'
    ])

    chatbot.train([
        'Koje su vrste kutova?',
        '07'
    ])

    chatbot.train([
        'Koje vrste kutova poznaješ?',
        '07'
    ])

    chatbot.train([
        'Što je trokut?',
        '08'
    ])

    chatbot.train([
        'Što je to trokut?',
        '08'
    ])

    chatbot.train([
        'Definiraj trokut!',
        '08'
    ])

    chatbot.train([
        'Što su vrhovi trokuta?',
        '09'
    ])

    chatbot.train([
        'Što su to vrhovi trokuta?',
        '09'
    ])

    chatbot.train([
        'Definiraj vrhove trokuta?',
        '09'
    ])

    chatbot.train([
        'Što su stranice trokuta?',
        '10'
    ])

    chatbot.train([
        'Što su to stranice trokuta?',
        '10'
    ])

    chatbot.train([
        'Definiraj stranice trokuta?',
        '10'
    ])

    chatbot.train([
        'Kako označavamo veličine kutova trokuta?',
        '11'
    ])

    chatbot.train([
        'Čime označavamo veličine kutova trokuta?',
        '11'
    ])

    chatbot.train([
        'Kako označavamo kutove trokuta?',
        '11'
    ])

    chatbot.train([
        'Koliki je zbroj veličina unutarnjih kutova u svakom trkoutu?',
        '12'
    ])

    chatbot.train([
        'Koliki je zbroj unutarnjih kutova trokuta?',
        '12'
    ])

    chatbot.train([
        'Koliki je zbroj veličina unutarnjih kutova trokuta?',
        '12'
    ])


    chatbot.train([
        'Koliki je zbroj unutarnjih kutova svakog trokuta?',
        '12'
    ])


    chatbot.train([
        'Koliki je zbroj veličina vanjskih kutova trokuta?',
        '13'
    ])

    chatbot.train([
        'Koliki je zbroj vanjskih kutova trokuta?',
        '13'
    ])

    chatbot.train([
        'Koliki je zbroj vanjskih kutova svakog trokuta?',
        '13'
    ])


    chatbot.train([
        'Koliki je zbroj veličina vanjskih kutova svakog trokuta?',
        '13'
    ])


    chatbot.train([
        'Kako se računa opseg trokuta?',
        '14'
    ])

    chatbot.train([
        'Kako računamo opseg trokuta?',
        '14'
    ])

    chatbot.train([
        'Kako izračunati opseg trokuta?',
        '14'
    ])

    chatbot.train([
        'Što je visina trokuta?',
        '15'
    ])

    chatbot.train([
        'Što je to visina trokuta?',
        '15'
    ])

    chatbot.train([
        'Definiraj visinu trokuta?',
        '15'
    ])

    chatbot.train([
        'Kako se računa površina trokuta?',
        '16'
    ])

    chatbot.train([
        'Kako računamo površinu trokuta?',
        '16'
    ])

    chatbot.train([
        'Kako izračunati površinu trokuta?',
        '16'
    ])


    chatbot.train([
        'Što nam govori svojstvo koje nazivamo nejednakost trokuta?',
        '17'
    ])

    chatbot.train([
        'Što je to nejednakost trokuta?',
        '17'
    ])

    chatbot.train([
        'Definiraj nejednakost trokuta!',
        '17'
    ])

    chatbot.train([
        'Definiraj svojstvo nejednakosti trokuta!',
        '17'
    ])


    chatbot.train([
        'Što znaš o odnosu duljina stranica i veličina kutova u trokutu?',
        '18'
    ])

    chatbot.train([
        'Koji je odnos duljina stranica i veličina kutova u trokutu?',
        '18'
    ])

    chatbot.train([
        'U kojem su odnosu duljina stranica i veličina kutova u trokutu?',
        '18'
    ])

    chatbot.train([
        'Što znaš o odnosu veličina kutova i duljina stranica u trokutu?',
        '18'
    ])

    chatbot.train([
        'Koji je odnos veličina kutova i duljina stranica u trokutu?',
        '18'
    ])

    chatbot.train([
        'U kojem su odnosu veličina kutova i duljina stranica u trokutu?',
        '18'
    ])

    
    chatbot.train([
        'Kako dijelimo trokute prema duljini stranica?',
        '19'
    ])
    
    chatbot.train([
        'Kakvi trokuti prema duljini stranica postoje?',
        '19'
    ])

    chatbot.train([
        'Koje su vrste trokuta prema duljini stranica?',
        '19'
    ])

    chatbot.train([
        'Kakav je to raznostranični trokut?',
        '20'
    ])

    chatbot.train([
        'Što je to raznostranični trokut?',
        '20'
    ])

    chatbot.train([
        'Definiraj raznostranični trokut!',
        '20'
    ])

    chatbot.train([
        'Kakav je to jednakokračni trokut?',
        '21'
    ])

    chatbot.train([
        'Što je to jednakokračni trokut?',
        '21'
    ])

    chatbot.train([
        'Definiraj jednakokračni trokut!',
        '21'
    ])

    chatbot.train([
        'Kakav je to jednakostranični trokut?',
        '22'
    ])

    chatbot.train([
        'Što je to jednakostranični trokut?',
        '22'
    ])

    chatbot.train([
        'Definiraj jednakostranični trokut?',
        '22'
    ])
    
    chatbot.train([
        'Kako dijelimo trokute prema veličini kutova?',
        '23'
    ])
    
    chatbot.train([
        'Koji trokuti prema veličini kutova postoje?',
        '23'
    ])

    chatbot.train([
        'Koje su vrste trokuta prema veličini kutova?',
        '23'
    ])

    chatbot.train([
        'Kakav je to šiljastokutni trokut?',
        '24'
    ])

    chatbot.train([
        'Što je to šiljastokutni trokut?',
        '24'
    ])

    chatbot.train([
        'Definiraj šiljastokutni trokut?',
        '24'
    ])

    chatbot.train([
        'Kakav je to pravokutni trokut?',
        '25'
    ])

    chatbot.train([
        'Što je to pravokutni trokut?',
        '25'
    ])

    chatbot.train([
        'Definiraj pravokutni trokut?',
        '25'
    ])

    chatbot.train([
        'Kakav je to tupokutni trokut?',
        '26'
    ])

    chatbot.train([
        'Što je to tupokutni trokut?',
        '26'
    ])

    chatbot.train([
        'Definiraj tupokutni trokut?',
        '26'
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
        'Iva?',
        'izvoli'
    ])

    chatbot.train([
        'Ivaa, jesi li tu?',
        'izvoli'
    ])

    chatbot.train([
        'Iva, si tu?',
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
        'dobro',
        'Dobro',
        'izvoli'
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
