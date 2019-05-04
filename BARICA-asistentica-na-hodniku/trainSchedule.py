
from chatterbot.trainers import ListTrainer

from ScrapInformation import scrapAllGroups
groups = scrapAllGroups()

def trainSchedule( bot ):
    chatbot = ListTrainer( bot )
    
    # reove these two lines for version 1.0.0 of chatterbot
    bot.set_trainer( ListTrainer ) #1
    chatbot = bot #2

    chatbot.train([
        'informacijski poslovni sustavi 1.1 preddiplomski',
        '2824'
    ])

    chatbot.train([
        'ekonomika poduzetništva 1.0 preddiplomski',
        '2825'
    ])

    chatbot.train([
        'ekonomika poduzetništva 1.1 preddiplomskii',
        '44700'
    ])

    chatbot.train([
        'diplomski studij informatike 1.2 diplomski',
        '2831'
    ])

    chatbot.train([
        'diplomski studij ekonomika poduzetništva 1.0 diplomski',
        '2832'
    ])

    chatbot.train([
        'pitu varaždin 1.1 stručni',
        '2826'
    ])

    chatbot.train([
        'pitu varaždin 1.2 stručni',
        '99118'
    ])

    chatbot.train([
        'pitu križevci 1.1 stručni',
        '2827'
    ])

    chatbot.train([
        'pitu križevci 1.2 stručni',
        '99119'
    ])

    chatbot.train([
        'pitu sisak 1.1 stručni',
        '2828'
    ])

    chatbot.train([
        'pitu sisak 1.2 stručni',
        '99120'
    ])

    chatbot.train([
        'pitu zabok 1.1 stručni',
        '2829'
    ])

    chatbot.train([
        'pitu zabok 1.2 stručni',
        '99121'
    ])

    chatbot.train([
        'upravljanje sigurnošću i revizijom informacijskih sustava 1.0 specijalistički',
        '2834'
    ])

    chatbot.train([
        'upravljanje sigurnošću i revizijom informacijskih sustava 2.0 specijalistički',
        '198034'
    ])

    chatbot.train([
        'inženjerstvo i reinženjerstvo organizacija informacijskog doba 1.0 specijalistički',
        '2835'
    ])

    chatbot.train([
        'menadžment poslovnih sustava 1.0 specijalistički',
        '2836'
    ])

    chatbot.train([
        'poslijediplomski doktorski studij 1.1 doktorski',
        '33958'
    ])

    chatbot.train([
        'pedagoško psihološko didaktičko metodičko obrazovanje 1.0 specijalistički',
        '52162'
    ])

    chatbot.train([
        'prva',
        '1'
    ])

    chatbot.train([
        'prvu',
        '1'
    ])

    chatbot.train([
        'druga',
        '2'
    ])

    chatbot.train([
        'drugu',
        '2'
    ])

    chatbot.train([
        'treća',
        '3'
    ])

    chatbot.train([
        'treći',
        '3'
    ])

    chatbot.train([
        'treću',
        '3'
    ])

    for g in groups:
                
                chatbot.train([
                        g,
                        g
                ])
                
                b_name = g.replace('G', 'b')
                
                chatbot.train([
                        b_name,
                        g
                ])

    chatbot.train([
		'Barice',
		'izvoli'
	])

    chatbot.train([
            'Marice',
            'izvoli'
    ])


    chatbot.train([
            'Zorice',
            'izvoli'
    ])


    chatbot.train([
            'Starice',
            'izvoli'
    ])


    chatbot.train([
            'Varice',
            'izvoli?'
    ])
                

    

    

    
