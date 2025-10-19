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
        'Nabroji fizikalna svojstva tvari.',
        '01'
    ])

    chatbot.train([
        'Koja su fizikalna svojstva tvari.',
        '01'
    ])

    chatbot.train([
        'Navedi fizikalna svojstva tvari.',
        '01'
    ])

    chatbot.train([
        'U kojim agregacijskim stanjima mogu biti tvari?',
        '02'
    ])
    chatbot.train([
        'Navedi agregacijska stanja tvari?',
        '02'
    ])
    chatbot.train([
        'Koje su vrste agregacijskih stanja tvari?',
        '02'
    ])

    chatbot.train([
        'Što je taljenje?',
        '03'
    ])
    chatbot.train([
        'Što je to taljenje?',
        '03'
    ])
    chatbot.train([
        'Objasni taljenje?',
        '03'
    ])
    chatbot.train([
        'Pojasni taljenje?',
        '03'
    ])

    chatbot.train([
        'Što je isparavanje?',
        '04'
    ])
    chatbot.train([
        'Što je to isparavanje?',
        '04'
    ])
    chatbot.train([
        'Objasni isparavanje?',
        '04'
    ])
    chatbot.train([
        'Pojasni isparavanje?',
        '04'
    ])

    chatbot.train([
        'Što je kondenzacija?',
        '05'
    ])

    chatbot.train([
        'Što je to kondenzacija?',
        '05'
    ])

    chatbot.train([
        'Objasni kondenzaciju?',
        '05'
    ])

    chatbot.train([
        'Pojasni kondenzaciju?',
        '05'
    ])

    chatbot.train([
        'Što je očvrščivanje?',
        '06'
    ])

    chatbot.train([
        'Što je to očvrščivanje?',
        '06'
    ])

    chatbot.train([
        'Objasni očvrščivanje?',
        '06'
    ])

    chatbot.train([
        'Pojasni očvrščivanje?',
        '06'
    ])

    chatbot.train([
        'Što je sublimacija?',
        '07'
    ])

    chatbot.train([
        'Što je to sublimacija?',
        '07'
    ])

    chatbot.train([
        'Objasni sublimaciju?',
        '07'
    ])

    chatbot.train([
        'Pojasni sublimacija?',
        '07'
    ])

    chatbot.train([
        'Kako se nazivaju tvari koje provode električnu struju?',
        '08'
    ])

    chatbot.train([
        'Kako se nazivaju tvari koje provode struju?',
        '08'
    ])

    chatbot.train([
        'Kako se zovu tvari koje provode električnu struju?',
        '08'
    ])

    chatbot.train([
        'Kako se zovu tvari koje provode struju?',
        '08'
    ])

    chatbot.train([
        'Kakve mogu biti tvari s obzirom na kemijska svojstva?',
        '09'
    ])
    chatbot.train([
        'Kakve su tvari s obzirom na kemijska svojstva?',
        '09'
    ])
    chatbot.train([
        'Kakve mogu biti tvari obzirom na kemijska svojstva?',
        '09'
    ])
    chatbot.train([
        'Kakve tvari postoje s obzirom na kemijska svojstva?',
        '09'
    ])

    chatbot.train([
        'Kako smo razvrstali tvari?',
        '10'
    ])

    chatbot.train([
        'Razvrstaj tvari',
        '10'
    ])

    chatbot.train([
        'Na koje smo vrste razvrstali tvari?',
        '10'
    ])

    chatbot.train([
        'Na što smo razvrstali tvari?',
        '10'
    ])

    chatbot.train([
        'Koja je razlika između čistih tvari i smjesa?',
        '11'
    ])
    chatbot.train([
        'Po čemu se razlikuju čiste tvari i smjese?',
        '11'
    ])
    chatbot.train([
        'Navedi razlike između čistih tvari i smjesa?',
        '11'
    ])
    chatbot.train([
        'Koja je razlika između smjesa i čistih tvari?',
        '11'
    ])

    chatbot.train([
        'Kako smo razvrstali čiste tvari?',
        '12'
    ])
    chatbot.train([
        'Razvrstaj čiste tvari',
        '12'
    ])
    chatbot.train([
        'Na koje smo vrste razvrstali čiste tvari?',
        '12'
    ])
    chatbot.train([
        'Na što smo razvrstali čiste tvari?',
        '12'
    ])

    chatbot.train([
        'Koja je razlika između elementarnih tvari i kemijskih spojeva?',
        '13'
    ])
    chatbot.train([
        'Navedi razlike između elementarnih tvari i kemijskih spojeva?',
        '13'
    ])
    chatbot.train([
        'Po čemu se razlikuju elementarne tvari i kemijski spojevi?',
        '13'
    ])
    chatbot.train([
        'Koja je razlika između kemijskih spojeva i elementarnih tvari?',
        '13'
    ])

    chatbot.train([
        'Što su reagensi?',
        '14'
    ])
    chatbot.train([
        'Što su to reagensi?',
        '14'
    ])
    chatbot.train([
        'Objasni reagense?',
        '14'
    ])
    chatbot.train([
        'Pojasni reagense?',
        '14'
    ])

    chatbot.train([
        'Koji je reagens za dokazivanje vode?',
        '15'
    ])

    chatbot.train([
        'Koji se reagens koristi za dokazivanje vode?',
        '15'
    ])

    chatbot.train([
        'Što koristimo za dokazivanje vode?',
        '15'
    ])

    chatbot.train([
        'Kakve su heterogene smjese?',
        '16'
    ])

    chatbot.train([
        'Kakve su to heterogene smjese?',
        '16'
    ])

    chatbot.train([
        'Što su heterogene smjese?',
        '16'
    ])

    chatbot.train([
        'Objasni heterogene smjese?',
        '16'
    ])
    chatbot.train([
        'Pojasni heterogene smjese?',
        '16'
    ])

    chatbot.train([
        'Kakve su homogene smjese?',
        '17'
    ])
    chatbot.train([
        'Kakve su to homogene smjese?',
        '17'
    ])
    chatbot.train([
        'Što su homogene smjese?',
        '17'
    ])
    chatbot.train([
        'Objasni homogene smjese?',
        '17'
    ])
    chatbot.train([
        'Pojasni homogene smjese?',
        '17'
    ])

    chatbot.train([
        'Što su legure ili slitine?',
        '18'
    ])
    chatbot.train([
        'Što su slitine?',
        '18'
    ])
    chatbot.train([
        'Što su legure?',
        '18'
    ])
    chatbot.train([
        'Što su to legure ili slitine?',
        '18'
    ])
    chatbot.train([
        'Što su to slitine?',
        '18'
    ])
    chatbot.train([
        'Što su to legure?',
        '18'
    ])

    chatbot.train([
        'Što su otopine?',
        '19'
    ])
    chatbot.train([
        'Što su to otopine?',
        '19'
    ])
    chatbot.train([
        'Objasni otopine?',
        '19'
    ])
    chatbot.train([
        'Pojasni otopine?',
        '19'
    ])

    chatbot.train([
        'Koje vrste otopina razlikujemo?',
        '20'
    ])
    chatbot.train([
        'Koje vrste otopina postoje?',
        '20'
    ])
    chatbot.train([
        'Koje su vrste otopina?',
        '20'
    ])
    chatbot.train([
        'Navedi vrste otopina?',
        '20'
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

