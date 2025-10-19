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

    # Question: Što je fizika?
    chatbot.train([
        'Što je fizika?',
        '01'
    ])
    chatbot.train([
        'Možeš li objasniti što je fizika?',
        '01'
    ])
    chatbot.train([
        'Kako bi definirao fiziku?',
        '01'
    ])

    # Question: Kako glasi zakon o očuvanju mase?
    chatbot.train([
        'Kako glasi zakon o očuvanju mase?',
        '02'
    ])
    chatbot.train([
        'Možeš li mi reći zakon o očuvanju mase?',
        '02'
    ])
    chatbot.train([
        'Koji je zakon o očuvanju mase?',
        '02'
    ])

    # Question: Koja je osnovna mjerna jedinica mase?
    chatbot.train([
        'Koja je osnovna mjerna jedinica mase?',
        '03'
    ])
    chatbot.train([
        'Koja je temeljna mjerna jedinica za masu?',
        '03'
    ])
    chatbot.train([
        'Koja je mjerna jedinica za masu?',
        '03'
    ])

    # Question: Što je gustoća?
    chatbot.train([
        'Što je gustoća?',
        '04'
    ])
    chatbot.train([
        'Možeš li objasniti što je gustoća?',
        '04'
    ])
    chatbot.train([
        'Kako bi definirao gustoću?',
        '04'
    ])

    # Question: Koja je formula za gustoću?
    chatbot.train([
        'Koja je formula za gustoću?',
        '05'
    ])
    chatbot.train([
        'Možeš li mi reći formulu za gustoću?',
        '05'
    ])
    chatbot.train([
        'Kako se izračunava gustoća?',
        '05'
    ])

    # Question: Što je sila?
    chatbot.train([
        'Što je sila?',
        '06'
    ])
    chatbot.train([
        'Možeš li objasniti što je sila?',
        '06'
    ])
    chatbot.train([
        'Kako bi definirao silu?',
        '06'
    ])

    # Question: Što je vektor?
    chatbot.train([
        'Što je vektor?',
        '07'
    ])
    chatbot.train([
        'Možeš li objasniti što je vektor?',
        '07'
    ])
    chatbot.train([
        'Kako bi definirao vektor?',
        '07'
    ])

    # Question: Kakva su to elastična tijela?
    chatbot.train([
        'Kakva su to elastična tijela?',
        '08'
    ])
    chatbot.train([
        'Možeš li objasniti što su elastična tijela?',
        '08'
    ])
    chatbot.train([
        'Kako bi definirao elastična tijela?',
        '08'
    ])

    # Question: Kako glasi Hookeov zakon?
    chatbot.train([
        'Kako glasi Hookeov zakon?',
        '09'
    ])
    chatbot.train([
        'Možeš li mi reći Hookeov zakon?',
        '09'
    ])
    chatbot.train([
        'Koji je Hookeov zakon?',
        '09'
    ])

    # Question: Što je tlak?
    chatbot.train([
        'Što je tlak?',
        '10'
    ])
    chatbot.train([
        'Možeš li objasniti što je tlak?',
        '10'
    ])
    chatbot.train([
        'Kako bi definirao tlak?',
        '10'
    ])

    # Question: Što je rad?
    chatbot.train([
        'Što je rad?',
        '11'
    ])
    chatbot.train([
        'Možeš li objasniti što je rad?',
        '11'
    ])
    chatbot.train([
        'Kako bi definirao rad?',
        '11'
    ])

    # Question: Što je energija?
    chatbot.train([
        'Što je energija?',
        '12'
    ])
    chatbot.train([
        'Možeš li objasniti što je energija?',
        '12'
    ])
    chatbot.train([
        'Kako bi definirao energiju?',
        '12'
    ])

    # Question: Koja je osnovna mjerna jedinica za energiju?
    chatbot.train([
        'Koja je osnovna mjerna jedinica za energiju?',
        '13'
    ])
    chatbot.train([
        'Koja je temeljna mjerna jedinica za energiju?',
        '13'
    ])
    chatbot.train([
        'Koja je mjerna jedinica za energiju?',
        '13'
    ])

    # Question: Što je toplina?
    chatbot.train([
        'Što je toplina?',
        '14'
    ])
    chatbot.train([
        'Možeš li objasniti što je toplina?',
        '14'
    ])
    chatbot.train([
        'Kako bi definirao toplinu?',
        '14'
    ])

    # Question: Čime mjerimo temperaturu?
    chatbot.train([
        'Čime mjerimo temperaturu?',
        '15'
    ])
    chatbot.train([
        'Koja je mjerna jedinica za temperaturu?',
        '15'
    ])
    chatbot.train([
        'Kako mjerimo temperaturu?',
        '15'
    ])

    # Question: Što je optička leća?
    chatbot.train([
        'Što je optička leća?',
        '16'
    ])
    chatbot.train([
        'Možeš li objasniti što je optička leća?',
        '16'
    ])
    chatbot.train([
        'Kako bi definirao optičku leću?',
        '16'
    ])

    # Question: Koja je akceleracija djelovanja sile teže?
    chatbot.train([
        'Koja je akceleracija djelovanja sile teže?',
        '17'
    ])
    # Question: Koja je akceleracija djelovanja sile teže?
    chatbot.train([
        'Koja je akceleracija djelovanja sile teže?',
        '17'
    ])
    chatbot.train([
        'Kolika je akceleracija djelovanja sile teže?',
        '17'
    ])
    chatbot.train([
        'Možeš li mi reći akceleraciju djelovanja sile teže?',
        '17'
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
        'Doktor Slavica?',
        'izvoli'
    ])

    chatbot.train([
        'Slavica, jesi li tu?',
        'izvoli'
    ])

    chatbot.train([
        'Doktore, si tu?',
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




