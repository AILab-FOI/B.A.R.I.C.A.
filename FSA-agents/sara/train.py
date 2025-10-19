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
        'Kada je proglašena Opća deklaracija o ljudskim pravima i tko ju je proglasio?',
        '01'
    ])
    chatbot.train([
        'Tko je proglasio opću deklaraciju o ljudskim pravima?',
        '01'
    ])
    chatbot.train([
        'Kada je proglašena Opća deklaracija o ljudskim pravima?',
        '01'
    ])
    chatbot.train([
        'Tko je proglasio opću deklaraciju o ljudskim pravima i kada?',
        '01'
    ])

    chatbot.train([
        'Što propisuje zakon?',
        '02'
    ])
    chatbot.train([
        'Što je to zakon?',
        '02'
    ])
    chatbot.train([
        'Objasni zakon',
        '02'
    ])
    chatbot.train([
        'Čemu služi zakon?',
        '02'
    ])

    chatbot.train([
        'Što je demokracija?',
        '03'
    ])
    chatbot.train([
        'Objasni demokraciju',
        '03'
    ])
    chatbot.train([
        'Pojasni demokraciju',
        '03'
    ])
    chatbot.train([
        'Što je to demokracija?',
        '03'
    ])

    chatbot.train([
        'Što je monarhija?',
        '04'
    ])
    chatbot.train([
        'Što je to monarhija?',
        '04'
    ])
    chatbot.train([
        'Objasni monarhiju',
        '04'
    ])
    chatbot.train([
        'Pojasni monarhiju',
        '04'
    ])

    chatbot.train([
        'Koga predstavlja Hrvatski sabor i što je njegova uloga?',
        '05'
    ])
    chatbot.train([
        'Koga predstavlja Hrvatski sabor?',
        '05'
    ])
    chatbot.train([
        'Koja je uloga Hrvatskog sabora?',
        '05'
    ])
    chatbot.train([
        'Koja je uloga Hrvatskog sabora i koga on predstavlja?',
        '05'
    ])

    chatbot.train([
        'Što je volontiranje?',
        '06'
    ])
    chatbot.train([
        'Što je to volontiranje?',
        '06'
    ])
    chatbot.train([
        'Pojasni volontiranje?',
        '06'
    ])
    chatbot.train([
        'Objasni volontiranje?',
        '06'
    ])

    chatbot.train([
        'Što su mediji?',
        '07'
    ])
    chatbot.train([
        'Što su to mediji?',
        '07'
    ])
    chatbot.train([
        'Pojasni medije',
        '07'
    ])
    chatbot.train([
        'Objasni medije',
        '07'
    ])

    chatbot.train([
        'Što je medijska pismenost?',
        '08'
    ])
    chatbot.train([
        'Što je to medijska pismenost?',
        '08'
    ])
    chatbot.train([
        'Pojasni medijsku pismenost?',
        '08'
    ])
    chatbot.train([
        'Objasni medijsku pismenost?',
        '08'
    ])

    chatbot.train([
        'Što je migracija?',
        '09'
    ])
    chatbot.train([
        'Što je to migracija?',
        '09'
    ])
    chatbot.train([
        'Pojasni migraciju',
        '09'
    ])
    chatbot.train([
        'Objasni migraciju',
        '09'
    ])

    chatbot.train([
        'Navedi tri razloga zbog kojih ljudi migriraju.',
        '10'
    ])
    chatbot.train([
        'Navedi razloge zbog kojih ljudi migriraju.',
        '10'
    ])
    chatbot.train([
        'Koji su razlozi zbog kojih ljudi migriraju.',
        '10'
    ])
    chatbot.train([
        'Zašto ljudi migriraju?',
        '10'
    ])

    chatbot.train([
        'Definiraj pojam međukulturalnost.',
        '11'
    ])
    chatbot.train([
        'Što je međukulturalnost.',
        '11'
    ])
    chatbot.train([
        'Što je to međukulturalnost.',
        '11'
    ])
    chatbot.train([
        'Objasni međukulturalnost.',
        '11'
    ])
    chatbot.train([
        'Pojasni međukulturalnost.',
        '11'
    ])

    chatbot.train([
        'Koja je religija najzastupljenija u Hrvatskoj?',
        '12'
    ])
    chatbot.train([
        'Koja je najčešća religija u Hrvatskoj?',
        '12'
    ])
    chatbot.train([
        'Koja je vjera najzastupljenija u Hrvatskoj?',
        '12'
    ])
    chatbot.train([
        'Koja je vjeroispovjest najzastupljenija u Hrvatskoj?',
        '12'
    ])
    chatbot.train([
        'Koja je vjera najčešća u Hrvatskoj?',
        '12'
    ])
    chatbot.train([
        'Koja je vjeroispovjest najčešća u Hrvatskoj?',
        '12'
    ])

    chatbot.train([
        'Kada se obilježava Dan sjećanja na žrtve holokausta?',
        '13'
    ])
    chatbot.train([
        'Kada je Dan sjećanja na žrtve holokausta?',
        '13'
    ])
    chatbot.train([
        'Na koji datum je Dan sjećanja na žrtve holokausta?',
        '13'
    ])

    chatbot.train([
        'Kako jednim imenom nazivamo običaje, vjerovanja, način odijevanja, pripremu jela u određenom kraju?',
        '14'
    ])
    chatbot.train([
        'Kako nazivamo običaje, vjerovanja, način odijevanja, pripremu jela u određenom kraju?',
        '14'
    ])
    chatbot.train([
        'Kako jednim imenom nazivamo običaje kraju?',
        '14'
    ])
    chatbot.train([
        'Kako jednim imenom nazivamo vjerovanja u određenom kraju?',
        '14'
    ])
    chatbot.train([
        'Kako jednim imenom nazivamo način odijevanja u određenom kraju?',
        '14'
    ])
    chatbot.train([
        'Kako jednim imenom nazivamo pripremu jela u određenom kraju?',
        '14'
    ])
    chatbot.train([
        'Kako nazivamo vjerovanja, način odijevanja, običaje, pripremu jela u određenom kraju?',
        '14'
    ])
    chatbot.train([
        'Kako nazivamo način odijevanja, običaje, pripremu jela, vjerovanja u određenom kraju?',
        '14'
    ])
    chatbot.train([
        'Kako nazivamo vjerovanja, običaje, pripremu jela u određenom kraju?',
        '14'
    ])

    chatbot.train([
        'Što je poduzetništvo?',
        '15'
    ])
    chatbot.train([
        'Što je to poduzetništvo?',
        '15'
    ])
    chatbot.train([
        'Objasni poduzetništvo',
        '15'
    ])
    chatbot.train([
        'Pojasni poduzetništvo',
        '15'
    ])

    chatbot.train([
        'Koji je glavni cilj društvenog ili socijalnog poduzetništva?',
        '16'
    ])

    chatbot.train([
        'Koji je glavni cilj društvenog poduzetništva?',
        '16'
    ])

    chatbot.train([
        'Koji je glavni cilj socijalnog poduzetništva?',
        '16'
    ])

    chatbot.train([
        'Koji je cilj društvenog ili socijalnog poduzetništva?',
        '16'
    ])

    chatbot.train([
        'Koji je cilj društvenog poduzetništva?',
        '16'
    ])
    chatbot.train([
        'Koji je cilj socijalnog poduzetništva?',
        '16'
    ])

    chatbot.train([
        'Objasni pojmove bruto i neto plaća.',
        '17'
    ])
    chatbot.train([
        'Što su to bruto i neto plaća?',
        '17'
    ])
    chatbot.train([
        'Pojasni bruto i neto plaću.',
        '17'
    ])
    chatbot.train([
        'Što je bruto, a što neto plaća?',
        '17'
    ])

    chatbot.train([
        'Što je održivi razvoj?',
        '18'
    ])
    chatbot.train([
        'Što je to održivi razvoj?',
        '18'
    ])
    chatbot.train([
        'Pojasni održivi razvoj?',
        '18'
    ])
    chatbot.train([
        'Objasni održivi razvoj?',
        '18'
    ])

    chatbot.train([
        'Kako nazivamo ponovnu upotrebu nekog proizvoda?',
        '19'
    ])
    chatbot.train([
        'Kako se zove ponovna upotreba nekog proizvoda?',
        '19'
    ])
    chatbot.train([
        'Kako nazivamo ponovnu upotrebu proizvoda?',
        '19'
    ])
    chatbot.train([
        'Kako se zove ponovna upotreba proizvoda?',
        '19'
    ])

    chatbot.train([
        'Što je adolescencija?',
        '20'
    ])
    chatbot.train([
        'Što je to adolescencija?',
        '20'
    ])
    chatbot.train([
        'Objasni adolescenciju',
        '20'
    ])
    chatbot.train([
        'Pojasni adolescenciju',
        '20'
    ])

    chatbot.train([
        'Čime održavamo fizičko zdravlje?',
        '21'
    ])
    chatbot.train([
        'Kako održavamo fizičko zdravlje?',
        '21'
    ])
    chatbot.train([
        'Što je važno za fizičko zdravlje?',
        '21'
    ])
    chatbot.train([
        'Kako biti fizički zdrav?',
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

