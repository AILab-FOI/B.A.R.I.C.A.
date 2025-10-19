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
        'Koji su gradovi Varaždinske županije?',
        '01'
    ])

    chatbot.train([
        'Koje gradove imamo u Varaždinskoj županiji?',
        '01'
    ])

    chatbot.train([
        'Koji su gradovi u Varaždinskoj županiji?',
        '01'
    ])

    chatbot.train([
        'Koje gradove u Varaždinskoj županiji poznaješ?',
        '01'
    ])

    chatbot.train([
        'Kako su se u prošlosti nazivali simboli određenog zanata?',
        '02'
    ])

    chatbot.train([
        'Kako su se zvali simboli određenog zanata?',
        '02'
    ])

    chatbot.train([
        'Koji je naziv simbola određenog zanata?',
        '02'
    ])

    chatbot.train([
        'Što je gospodarstvo?',
        '03'
    ])

    chatbot.train([
        'Što je to gospodarstvo?',
        '03'
    ])

    chatbot.train([
        'Objasni mi što je to gospodarstvo?',
        '03'
    ])

    chatbot.train([
        'Koja su zaštićena mjesta u Varaždinskoj županiji?',
        '04'
    ])

    chatbot.train([
        'Koja su mjesta u Varaždinskoj županiji zaštićena?',
        '04'
    ])

    chatbot.train([
        'Ima li u Varaždinskoj županiji zaštićenih mjesta?',
        '04'
    ])

    chatbot.train([
        'Koja su mjesta zaštićena u Varaždinskoj županiji?',
        '04'
    ])

    chatbot.train([
        'Kada i gdje se Varaždin prvi puta spominje?',
        '05'
    ])

    chatbot.train([
        'Kada se Varaždin prvi puta spominje?',
        '05'
    ])

    chatbot.train([
        'Gdje se Varaždin prvi puta spominje i kada je to bilo?',
        '05'
    ])


    chatbot.train([
        'Kakva su ljeta u Varaždinskoj županiji?',
        '06'
    ])

    chatbot.train([
        'Kakvo je ljeto u Varaždinu?',
        '06'
    ])

    chatbot.train([
        'Kako je ljeti u Varaždinskoj županiji?',
        '06'
    ])

    chatbot.train([
        'Koje su rijeke u Varaždinskoj županiji?',
        '07'
    ])

    chatbot.train([
        'Koje rijeke imamo u Varaždinskoj županiji?',
        '07'
    ])

    chatbot.train([
        'Koje rijeke poznaješ u Varaždinskoj županiji?',
        '07'
    ])

    chatbot.train([
        'Što su termalne vode?',
        '08'
    ])

    chatbot.train([
        'Kakve su to termalne vode?',
        '08'
    ])

    chatbot.train([
        'Što znači termalna voda?',
        '08'
    ])

    chatbot.train([
        'Koja su jezera u Varaždinskoj županiji?',
        '09'
    ])

    chatbot.train([
        'Koja jezera imamo u Varaždinskoj županiji?',
        '09'
    ])

    chatbot.train([
        'Koja jezera poznaješ u Varaždinskoj županiji?',
        '09'
    ])

    chatbot.train([
        'Što je reljef?',
        '10'
    ])

    chatbot.train([
        'Što je to reljef?',
        '10'
    ])

    chatbot.train([
        'Što znači riječ reljef?',
        '10'
    ])

    chatbot.train([
        'Što je Varaždinsko polje?',
        '11'
    ])

    chatbot.train([
        'Što je to polje Varaždinsko?',
        '11'
    ])

    chatbot.train([
        'Gdje je Varaždinsko polje?',
        '11'
    ])

    chatbot.train([
        'Za što nam služe prometnice?',
        '12'
    ])

    chatbot.train([
        'Čemu služe prometnice?',
        '12'
    ])

    chatbot.train([
        'Zašto postoje prometnice?',
        '12'
    ])


    chatbot.train([
        'Koja je najjača grana gospodarstva u našoj županiji?',
        '13'
    ])

    chatbot.train([
        'Koja je najpoznatija gospodarska grana u Varaždinskoj županiji?',
        '13'
    ])

    chatbot.train([
        'Koja je najjača gospodarska grana u Varaždinskoj županiji?',
        '13'
    ])


    chatbot.train([
        'Gdje je smješten Varaždin?',
        '14'
    ])

    chatbot.train([
        'Gdje je Varaždin?',
        '14'
    ])

    chatbot.train([
        'Gdje se nalazi Varaždin?',
        '14'
    ])

    chatbot.train([
        'Što su radila Ilirska plemena u našem kraju?',
        '15'
    ])

    chatbot.train([
        'Što su u našem kraju radila Ilirska plemena?',
        '15'
    ])

    chatbot.train([
        'Što su u Varaždinskoj županiji radili Iliri?',
        '15'
    ])

    chatbot.train([
        'Što su radili Stari Rimljani?',
        '16'
    ])

    chatbot.train([
        'Što su u našem kraju radili stari Rimljani?',
        '16'
    ])

    chatbot.train([
        'Kako su se branili od Turaka?',
        '17'
    ])

    chatbot.train([
        'Kako su se ljudi iz našeg kraja branili od Turaka?',
        '17'
    ])

    chatbot.train([
        'Kako se je nekad branilo od Turaka?',
        '17'
    ])

    chatbot.train([
        'Za što je korištena rijeka Drava prilikom velike seobe naroda?',
        '18'
    ])

    chatbot.train([
        'Čemu je služila rijeka Drava u velikoj seobi naroda?',
        '18'
    ])

    chatbot.train([
        'Tijekom velike seobe naroda, čemu je služila rijeka Drava?',
        '18'
    ])
    
    chatbot.train([
        'Kada Varaždin prestaje biti glavni grad Hrvatske?',
        '19'
    ])
    
    chatbot.train([
        'Do kada je Varaždin bio glavni grad Hrvatske?',
        '19'
    ])

    chatbot.train([
        'Od kada Varaždin više nije bio glavni grad Hrvatske?',
        '19'
    ])

    chatbot.train([
        'Koje su znamenite ličnosti naše županije?',
        '20'
    ])

    chatbot.train([
        'Tko su znamenite ličnosti Varaždinske županije?',
        '20'
    ])

    chatbot.train([
        'Tko su poznati Varaždinci?',
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
        'Zamrljan?',
        'izvoli'
    ])

    chatbot.train([
        'Zamrljan, jesi li tu?',
        'izvoli'
    ])

    chatbot.train([
        'Micko, si tu?',
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




