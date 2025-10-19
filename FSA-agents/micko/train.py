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
        'Kada započinje i završava ljeto?',
        '01'
    ])

    chatbot.train([
        'Kada počinje ljeto?',
        '01'
    ])

    chatbot.train([
        'Kada završava ljeto?',
        '01'
    ])

    chatbot.train([
        'Od kad do kad traje ljeto?',
        '01'
    ])

    chatbot.train([
        'Koji su ljetni mjeseci?',
        '02'
    ])

    chatbot.train([
        'Koje mjeseci čine ljeto?',
        '02'
    ])

    chatbot.train([
        'U kojim mjesecima je ljeto?',
        '02'
    ])

    chatbot.train([
        'Kakvo je vrijeme ljeti?',
        '03'
    ])

    chatbot.train([
        'Kakve su vremenske prilike ljeti?',
        '03'
    ])

    chatbot.train([
        'Kakvo vrijeme imamo ljeti?',
        '03'
    ])

    chatbot.train([
        'Trajanje dana i noći na početku ljeta?',
        '04'
    ])

    chatbot.train([
        'Koliko traju dan i noć na početku ljeta?',
        '04'
    ])

    chatbot.train([
        'Što se događa s danom i noći na početku ljeta?',
        '04'
    ])

    chatbot.train([
        'Kavi su dani i noći na početku ljeta?',
        '04'
    ])

    chatbot.train([
        'Što se događa s trajanjem dana i noći tijekom ljeta?',
        '05'
    ])

    chatbot.train([
        'Kako se mijenja trajanje dana i noći tijekom ljeta?',
        '05'
    ])

    chatbot.train([
        'Što ne bismo smjeli napraviti za vrijeme grmljavine ako smo vani?',
        '06'
    ])

    chatbot.train([
        'Gdje se ne bi trebali skloniti tijekom grmljavine?',
        '06'
    ])

    chatbot.train([
        'Što ne smijemo raditi tijekom grmljavine?',
        '06'
    ])

    chatbot.train([
        'Zašto ljeti ne smijemo paliti vatru u prirodi?',
        '07'
    ])

    chatbot.train([
        'Zašto je opasno paliti vatru u prirodi ljeti?',
        '07'
    ])

    chatbot.train([
        'Zašto nije dobro paliti vatru u prirodi po ljeti?',
        '07'
    ])

    chatbot.train([
        'Što rade ljeti životinje koje imaju mladunce?',
        '08'
    ])

    chatbot.train([
        'Kako se životinje brinu o svojim mladuncima ljeti?',
        '08'
    ])

    chatbot.train([
        'Što rade životinje koje imaju mladunce ljeti?',
        '08'
    ])

    chatbot.train([
        'Što rade ptice selice ljeti?',
        '09'
    ])

    chatbot.train([
        'Kako se ponašaju ptice selice ljeti?',
        '09'
    ])

    chatbot.train([
        'Što ljeti rade ptice selice?',
        '09'
    ])

    chatbot.train([
        'Koji plodovi dozrijevaju ljeti u voćnjaku?',
        '10'
    ])

    chatbot.train([
        'Koje voće dozrijeva ljeti?',
        '10'
    ])

    chatbot.train([
        'Koje je voće ljeti zrelo?',
        '10'
    ])

    chatbot.train([
        'Koji povrtni plodovi dozrijevaju ljeti u vrtu?',
        '11'
    ])

    chatbot.train([
        'Koje povrće dozrijeva tijekom ljeta?',
        '11'
    ])

    chatbot.train([
        'Koje povrće je zrelo na ljeto?',
        '11'
    ])

    chatbot.train([
        'Što radimo s viškom voća i povrća?',
        '12'
    ])

    chatbot.train([
        'Kako se može iskoristiti višak voća i povrća?',
        '12'
    ])

    chatbot.train([
        'Zašto bor i maslina mogu rasti na ljetnoj suši?',
        '13'
    ])

    chatbot.train([
        'Kako bor i maslina preživljavaju ljetnu sušu?',
        '13'
    ])

    chatbot.train([
        'Zašto tijekom ljeta odijevamo laganiju odjeću?',
        '14'
    ])

    chatbot.train([
        'Opiši odjeću koju nosiš ljeti',
        '14'
    ])

    chatbot.train([
        'Kakvu odjeću treba nositi tijekom ljeta?',
        '14'
    ])

    chatbot.train([
        'Kakve aktivnosti mogu raditi na otvorenom tijekom ljeta?',
        '15'
    ])

    chatbot.train([
        'Što se može raditi vani ljeti?',
        '15'
    ])

    chatbot.train([
        'Koje su ljetne aktivnosti na otvorenom?',
        '15'
    ])

    chatbot.train([
        'Objasni zašto ljeti trebamo posebno zaštititi kožu kremom?',
        '16'
    ])

    chatbot.train([
        'Zašto moramo koristiti zaštitnu kremu za sunčanje tijekom ljeta?',
        '16'
    ])

    chatbot.train([
        'Zašto tijekom ljeta ne idem u školu?',
        '17'
    ])

    chatbot.train([
        'Zašto su škole zatvorene tijekom ljeta?',
        '17'
    ])

    chatbot.train([
        'Zašto nema škole tijekom ljeta?',
        '17'
    ])

    chatbot.train([
        'Tko su turisti?',
        '18'
    ])

    chatbot.train([
        'Kako bi definirao turiste?',
        '18'
    ])

    chatbot.train([
        'Kako bi opisao turiste?',
        '18'
    ])
    
    chatbot.train([
        'Koje bi znamenitosti turisti mogli posjetiti u našem gradu tijekom ljeta?',
        '19'
    ])
    
    chatbot.train([
        'Koje bi atrakcije turisti mogli posjetiti u našem gradu tijekom ljeta?',
        '19'
    ])

    chatbot.train([
        'Koja su mjesta koja bi turisti mogli posjetiti u našem gradu ljeti?',
        '19'
    ])

    chatbot.train([
        'Kako biljka privlači kukce na travnjacima ljeti?',
        '20'
    ])

    chatbot.train([
        'Ljeti se na travnjacima uočavamo mnoštvo kukaca. Čime biljka privlači kukce?',
        '20'
    ])

    chatbot.train([
        'Čime biljke privlače kukce ljeti?',
        '20'
    ])

    chatbot.train([
        'Koji je najpoznatiji pčelinji proizvod i kako ga možemo koristiti?',
        '21'
    ])

    chatbot.train([
        'Pčele oblijeću cvjetove. Koji je najpoznatiji njihov proizvod i za što ga možemo koristiti?',
        '21'
    ])

    chatbot.train([
        'Što je najpoznatije što pčele proizvode i kako to koristimo?',
        '21'
    ])

    chatbot.train([
        'Kakvo vrijeme pčele nagovješćuju ako ostaju u svojim košnicama?',
        '22'
    ])

    chatbot.train([
        'Što pčele nagovješćuju ako ostaju u košnicama?',
        '22'
    ])

    chatbot.train([
        'Što znači kad pčele ostaju u košnicama?',
        '22'
    ])
    
    chatbot.train([
        'Zašto na plaži ne koristimo pjenu za kupanje?',
        '23'
    ])
    
    chatbot.train([
        'Zašto ne koristimo sapun za kupanje na plaži?',
        '23'
    ])

    chatbot.train([
        'Zašto ne bismo trebali koristiti pjenu za kupanje dok smo na plaži?',
        '23'
    ])

    chatbot.train([
        'Zašto nije dobro ići na plažu kad na zvoniku otkuca podne? ',
        '24'
    ])

    chatbot.train([
        'Zašto bi trebali izbjegavati plažu kada je podne?',
        '24'
    ])

    chatbot.train([
        'Zašto nije preporučljivo biti na plaži kada otkuca podne?',
        '24'
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
        'Micko?',
        'izvoli'
    ])

    chatbot.train([
        'Micko, jesi li tu?',
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


