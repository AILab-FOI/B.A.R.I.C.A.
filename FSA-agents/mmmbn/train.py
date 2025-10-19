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
        'Što je klima?',
        '01'
    ])
    chatbot.train([
        'Što je to klima?',
        '01'
    ])
    chatbot.train([
        'Objasni klimu?',
        '01'
    ])
    chatbot.train([
        'Pojasni pojam klima?',
        '01'
    ])

    chatbot.train([
        'Što je vrijeme?',
        '02'
    ])
    chatbot.train([
        'Što je to vrijeme?',
        '02'
    ])
    chatbot.train([
        'Objasni vrijeme?',
        '02'
    ])
    chatbot.train([
        'Pojasni pojam vrijeme?',
        '02'
    ])

    chatbot.train([
        'Što su klimatski čimbenici?',
        '03'
    ])
    chatbot.train([
        'Što su to klimatski čimbenici?',
        '03'
    ])
    chatbot.train([
        'Objasni klimatske čimbenike?',
        '03'
    ])
    chatbot.train([
        'Pojasni pojam klimatskih čimbenika?',
        '03'
    ])


    chatbot.train([
        'Što je klimatski dijagram?',
        '04'
    ])
    chatbot.train([
        'Što je to klimatski dijagram?',
        '04'
    ])
    chatbot.train([
        'Pojasni klimatski dijagram?',
        '04'
    ])
    chatbot.train([
        'Objasni pojam klimatskog dijagrama?',
        '04'
    ])


    chatbot.train([
        'Kako raspodjela kopna i mora utječe na klimu?',
        '05'
    ])
    chatbot.train([
        'Kako kopno i more utječu na klimu?',
        '05'
    ])
    chatbot.train([
        'Utječe li raspodjela kopna i mora na klimu?',
        '05'
    ])
    chatbot.train([
        'Jesu li kopno i more važni za klimu?',
        '05'
    ])


    chatbot.train([
        'Koji su uvjeti u kojima nastaje mraz?',
        '06'
    ])
    chatbot.train([
        'U kojim uvjetima nastaje mraz?',
        '06'
    ])
    chatbot.train([
        'Kada nastaje mraz?',
        '06'
    ])



    chatbot.train([
        'U kojim uvjetima nastaju frontalne padaline?',
        '07'
    ])
    chatbot.train([
        'Kada nastaju frontalne padaline?',
        '07'
    ])
    chatbot.train([
        'Zašto nastaju frontalne padaline?',
        '07'
    ])
    chatbot.train([
        'Koji su uvjeti u kojima nastaju frontalne padaline?',
        '07'
    ])

    chatbot.train([
        'Na koje klimatske razrede je Vladimir Koppen podijelio klimu?',
        '08'
    ])
    chatbot.train([
        'Koji su klimatski razredi na koje je Vladimir Koppen podijelio klimu?',
        '08'
    ])
    chatbot.train([
        'Kako je Vladimir Koppen podijelio klimu?',
        '08'
    ])
    chatbot.train([
        'Koji su klimatski razredi Vladimira Koppena?',
        '08'
    ])

    chatbot.train([
        'Koja su glavna obilježja sredozemne klime?',
        '09'
    ])
    chatbot.train([
        'Što obilježava sredozemnu klimu?',
        '09'
    ])
    chatbot.train([
        'Po čemu je posebna sredozemna klima?',
        '09'
    ])
    chatbot.train([
        'Kakva je to sredozemna klima?',
        '09'
    ])

    chatbot.train([
        'Što je savana?',
        '10'
    ])
    chatbot.train([
        'Što je to savana?',
        '10'
    ])
    chatbot.train([
        'Objasni savanu?',
        '10'
    ])
    chatbot.train([
        'Pojasni pojam savana?',
        '10'
    ])


    chatbot.train([
        'Što je tajga?',
        '11'
    ])
    chatbot.train([
        'Što je to tajga?',
        '11'
    ])
    chatbot.train([
        'Objasni pojam tajga?',
        '11'
    ])
    chatbot.train([
        'Pojasni tajgu?',
        '11'
    ])

    chatbot.train([
        'Što je tundra?',
        '12'
    ])
    chatbot.train([
        'Što je to tundra?',
        '12'
    ])
    chatbot.train([
        'Objasni tundru?',
        '12'
    ])
    chatbot.train([
        'Pojasni pojam tundra?',
        '12'
    ])


    chatbot.train([
        'Na kojim se geografskim širinama pruža područje pustinjske klime?',
        '13'
    ])
    chatbot.train([
        'Koje su geografske širine pustinjske klime?',
        '13'
    ])
    chatbot.train([
        'Na kojim je geografskim širinama pustinjska klima?',
        '13'
    ])
    chatbot.train([
        'Pustinjska klima je na kojim geografskim širinama?',
        '13'
    ])

    chatbot.train([
        'Koje je glavno obilježje klime vječnoga mraza?',
        '14'
    ])
    chatbot.train([
        'Po čemu je posebna klima vječnoga mraza?',
        '14'
    ])
    chatbot.train([
        'Što je to klima vječnoga mraza?',
        '14'
    ])
    chatbot.train([
        'Objasni klimu vječnoga mraza?',
        '14'
    ])



    chatbot.train([
        'Kojim klimatskim razredima pripadaju tipovi klime koje se mogu pronaći u Hrvatskoj?',
        '15'
    ])
    chatbot.train([
        'Koji se tipovi klime mogu pronaći u Hrvatskoj?',
        '15'
    ])
    chatbot.train([
        'Koji se klimatski razredi mogu pronaći u Hrvatskoj?',
        '15'
    ])
    chatbot.train([
        'Koji su tipovi klime u Hrvatskoj?',
        '15'
    ])


    chatbot.train([
        'Koja su glavna obilježja prašumske klime?',
        '16'
    ])
    chatbot.train([
        'Koakva je to prašumska klima?',
        '16'
    ])
    chatbot.train([
        'Po čemu je posebna prašumska klima?',
        '16'
    ])
    chatbot.train([
        'Što obilježava prašumsku klimu?',
        '16'
    ])


    chatbot.train([
        'Na kojem se prostoru pruža područje prašumske klime?',
        '17'
    ])
    chatbot.train([
        'Gdje je područje prašumske klime?',
        '17'
    ])
    chatbot.train([
        'Gdje se nalazi prašumska klima?',
        '17'
    ])
    chatbot.train([
        'Koje je područje prašumske klime?',
        '17'
    ])

    chatbot.train([
        'Koji je drugi naziv za sredozemnu klimu?',
        '18'
    ])
    chatbot.train([
        'Kako se još naziva sredozemna klima?',
        '18'
    ])
    chatbot.train([
        'Kako se drukčije zove sredozemna klima?',
        '18'
    ])
    chatbot.train([
        'Koje je drugo ime za sredozemnu klimu?',
        '18'
    ])


    chatbot.train([
        'Koji je tip klime tipičan za grad Varaždin?',
        '19'
    ])
    chatbot.train([
        'Kakva je kilma u Varaždinu?',
        '19'
    ])
    chatbot.train([
        'Koji je tip klime u Varaždinu?',
        '19'
    ])
    chatbot.train([
        'Kakva je klima u gradu Varaždinu?',
        '19'
    ])


    chatbot.train([
        'Koja je površinom najveća vruća pustinja na svijetu?',
        '20'
    ])
    chatbot.train([
        'Koja je najveća vruća pustinja na svijetu?',
        '20'
    ])
    chatbot.train([
        'Koja vruća pustinja ima najveću površinu?',
        '20'
    ])
    chatbot.train([
        'Koja je najveća vruća pustinja?',
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

