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
        'Koji su osnovni dijelovi krvi?',
        '01'
    ])
    chatbot.train([
        'Navedi osnovne dijelovi krvi?',
        '01'
    ])
    chatbot.train([
        'Nabroji osnovne dijelove krvi?',
        '01'
    ])

    chatbot.train([
        'Navedi vrste krvnih stanica.',
        '02'
    ])
    chatbot.train([
        'Koje su vrste krvnih stanica.',
        '02'
    ])
    chatbot.train([
        'Nabroji vrste krvnih stanica.',
        '02'
    ])

    chatbot.train([
        'Koju ulogu imaju eritrociti?',
        '03'
    ])
    chatbot.train([
        'Čemu služe eritrociti?',
        '03'
    ])
    chatbot.train([
        'Što su to eritrociti?',
        '03'
    ])

    chatbot.train([
        'Koju ulogu imaju leukociti?',
        '04'
    ])
    chatbot.train([
        'Čemu služe leukociti?',
        '04'
    ])
    chatbot.train([
        'Što su to leukociti?',
        '04'
    ])

    chatbot.train([
        'Koju ulogu imaju trombociti?',
        '05'
    ])
    chatbot.train([
        'Čemu služe trombociti?',
        '05'
    ])
    chatbot.train([
        'Što su to trombociti?',
        '05'
    ])

    chatbot.train([
        'Zašto je krv crvene boje?',
        '06'
    ])
    chatbot.train([
        'Zašto je krv crvena?',
        '06'
    ])
    chatbot.train([
        'Zbog čega je krv crvene boje?',
        '06'
    ])
    chatbot.train([
        'Zbog čega je krv crvena?',
        '06'
    ])

    chatbot.train([
        'Koju ulogu imaju srčani zalisci?',
        '07'
    ])
    chatbot.train([
        'Čemu služe srčani zalisci?',
        '07'
    ])
    chatbot.train([
        'Što su to srčani zalisci?',
        '07'
    ])

    chatbot.train([
        'Što je puls ili bilo?',
        '08'
    ])
    chatbot.train([
        'Što je to puls?',
        '08'
    ])
    chatbot.train([
        'Što je to bilo?',
        '08'
    ])
    chatbot.train([
        'Što je puls?',
        '08'
    ])
    chatbot.train([
        'Što je bilo?',
        '08'
    ])

    chatbot.train([
        'Što je aorta?',
        '09'
    ])
    chatbot.train([
        'Što je to aorta?',
        '09'
    ])
    chatbot.train([
        'Objasni aortu?',
        '09'
    ])

    chatbot.train([
        'Čime je bogata arterijska krv?',
        '10'
    ])
    chatbot.train([
        'Što sadrži arterijska krv?',
        '10'
    ])
    chatbot.train([
        'Čega ima puno u arterijskoj krvi?',
        '10'
    ])

    chatbot.train([
        'Kojim procesom kisik i hranjive tvari iz kapilara ulaze u stanicu?',
        '11'
    ])
    chatbot.train([
        'Kojim procesom kisik iz kapilara ulazi u stanicu?',
        '11'
    ])
    chatbot.train([
        'Kojim procesom hranjive tvari iz kapilara ulaze u stanicu?',
        '11'
    ])
    chatbot.train([
        'Kako kisik i hranjive tvari iz kapilara ulaze u stanicu?',
        '11'
    ])
    chatbot.train([
        'Kako kisik iz kapilara ulazi u stanicu?',
        '11'
    ])
    chatbot.train([
        'Kako hranjive tvari iz kapilara ulaze u stanicu?',
        '11'
    ])

    chatbot.train([
        'U koje dvije mjerne jedinice izražavamo vrijednost krvnog tlaka?',
        '12'
    ])
    chatbot.train([
        'Koje mjerne jedinice koristimo za vrijednost krvnog tlaka?',
        '12'
    ])
    chatbot.train([
        'U čemu izražavamo vrijednost krvnog tlaka?',
        '12'
    ])

    chatbot.train([
        'Koliko krvi ima u odrasla čovjeka?',
        '13'
    ])
    chatbot.train([
        'Koliko krvi ima odrasla osoba?',
        '13'
    ])
    chatbot.train([
        'Koliko krvi ima odrastao čovjek?',
        '13'
    ])

    chatbot.train([
        'Navedi četiri šupljine koje nalazimo u srcu čovjeka?',
        '14'
    ])
    chatbot.train([
        'Koje su četiri šupljine koje nalazimo u srcu čovjeka?',
        '14'
    ])
    chatbot.train([
        'Navedi šupljine u srcu čovjeka?',
        '14'
    ])
    chatbot.train([
        'Koje su šupljine u srcu čovjeka?',
        '14'
    ])
    chatbot.train([
        'Navedi četiri šupljine u srcu čovjeka?',
        '14'
    ])
    chatbot.train([
        'Koje su četiri šupljine u srcu čovjeka?',
        '14'
    ])

    chatbot.train([
        'Od kojih dijelova je građeno srce kod vodozemaca?',
        '15'
    ])
    chatbot.train([
        'Navedi dijelove srca vodozemaca?',
        '15'
    ])
    chatbot.train([
        'Od čega je građeno srce vodozemaca?',
        '15'
    ])
    chatbot.train([
        'Koji su dijelovi srca vodozemaca?',
        '15'
    ])

    chatbot.train([
        'Koji kralježnjaci imaju vensko srce?',
        '16'
    ])
    chatbot.train([
        'Navedi kralježnjake koji imaju vensko srce?',
        '16'
    ])
    chatbot.train([
        'Nabroji kralježnjake koji imaju vensko srce?',
        '16'
    ])
    chatbot.train([
        'Tko od kralježnjaka ima vensko srce?',
        '16'
    ])

    chatbot.train([
        'Što je kapilarnost kod biljaka?',
        '17'
    ])
    chatbot.train([
        'Objasni kapilarnost kod biljaka?',
        '17'
    ])
    chatbot.train([
        'Objasni kapilarnost biljaka?',
        '17'
    ])

    chatbot.train([
        'Koju ulogu ima korijenova dlačica?',
        '18'
    ])
    chatbot.train([
        'Čemu služi korijenova dlačica?',
        '18'
    ])
    chatbot.train([
        'Što je to korijenova dlačica?',
        '18'
    ])
    chatbot.train([
        'Što je to korijenova dlaka?',
        '18'
    ])
    chatbot.train([
        'Koju ulogu ima korijenova dlaka?',
        '18'
    ])
    chatbot.train([
        'Čemu služi korijenova dlaka?',
        '18'
    ])

    chatbot.train([
        'Kroz koje dijelove biljke putuje voda i mineralne tvari do lista?',
        '19'
    ])
    chatbot.train([
        'Kuda putuje voda i mineralne tvari do lista biljke?',
        '19'
    ])
    chatbot.train([
        'Kroz koje dijelove biljke putuje voda do lista?',
        '19'
    ])
    chatbot.train([
        'Kroz koje dijelove biljke putuju mineralne tvari do lista?',
        '19'
    ])
    chatbot.train([
        'Kuda putuje voda do lista biljke?',
        '19'
    ])
    chatbot.train([
        'Kuda putuju mineralne tvari do lista biljke?',
        '19'
    ])

    chatbot.train([
        'Zašto prilikom transfuzije krvi osoba treba primiti krv isključivo svoje krvne grupe?',
        '20'
    ])
    chatbot.train([
        'Zašto transfuzijom krvi trebamo primiti krv isključivo svoje krvne grupe?',
        '20'
    ])
    chatbot.train([
        'Zašto trebamo primiti krv isključivo svoje krvne grupe?',
        '20'
    ])
    chatbot.train([
        'Zašto kod transfuzije krvi treba primiti krv isključivo svoje krvne grupe?',
        '20'
    ])
    chatbot.train([
        'Zašto kod transfuzije krvi osoba treba primiti krv isključivo svoje krvne grupe?',
        '20'
    ])

    chatbot.train([
        'Zbog čega nastaje infarkt srca?',
        '21'
    ])
    chatbot.train([
        'Zašto nastaje infarkt srca?',
        '21'
    ])
    chatbot.train([
        'Kako nastaje infarkt srca?',
        '21'
    ])
    chatbot.train([
        'Objasni infarkt srca?',
        '21'
    ])
    chatbot.train([
        'Objasni kada nastaje infarkt srca?',
        '21'
    ])

    chatbot.train([
        'Što je anemija ili slabokrvnost?',
        '22'
    ])
    chatbot.train([
        'Što je anemija?',
        '22'
    ])
    chatbot.train([
        'Što je slabokrvnost?',
        '22'
    ])
    chatbot.train([
        'Što je to anemija ili slabokrvnost?',
        '22'
    ])
    chatbot.train([
        'Što je to anemija?',
        '22'
    ])
    chatbot.train([
        'Što je to slabokrvnost?',
        '22'
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

