
from chatterbot.trainers import ListTrainer

from ScrapInformation import scrapProfessorsForTrain


def trainProfessor( bot ):
        professors = scrapProfessorsForTrain()
        chatbot = ListTrainer( bot )

        # reove these two lines for version 1.0.0 of chatterbot
        bot.set_trainer( ListTrainer ) #1
        chatbot = bot #2

        for name, user_name in professors.items():
                chatbot.train([
                name,
                user_name
                ])
                word_list = name.split()
                chatbot.train([
                word_list[-1],
                user_name
                ])                
                if 'nastavnici' or 'sluzbe' in user_name:
                        if name.split(' ', 1)[0].endswith('a'):
                                chatbot.train([
                                'profesorica ' + name,
                                user_name
                                ])
                        else:
                                chatbot.train([
                                'profesor ' + name,
                                user_name
                                ])
                        if name.split(' ', 1)[0].endswith('a'):
                                chatbot.train([
                                'asistentica ' + name,
                                user_name
                                ])
                        else:
                                chatbot.train([
                                'asistent ' + name,
                                user_name
                                ])
                        if name.split(' ', 1)[0].endswith('a'):
                                chatbot.train([
                                'nastavnica ' + name,
                                user_name
                                ])
                        else:
                                chatbot.train([
                                'nastavnik ' + name,
                                user_name
                                ])

                chatbot.train([
                'marcus hutchins',
                'mschatte#nastavnici'
                ])

                chatbot.train([
                'marcus sa tim',
                'mschatte#nastavnici'
                ])

                chatbot.train([
                'marcus',
                'mschatte#nastavnici'
                ])

                chatbot.train([
                'mišu reko',
                'mdzeko#nastavnici'
                ])

                chatbot.train([
                'miš u džepu',
                'mdzeko#nastavnici'
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

                chatbot.train([
		'Perice',
		'izvoli?'
                ])

                chatbot.train([
		'Da li ce',
		'izvoli?'
	        ])

                chatbot.train([
		'barbike',
		'izvoli?'
	        ])

                chatbot.train([
		'bakice',
		'izvoli?'
	        ])

                chatbot.train([
		'reče',
		'izvoli?'
	        ])

                chatbot.train([
		'reči',
		'izvoli?'
	        ])

                chatbot.train([
		'perike',
		'izvoli?'
	        ])

                chatbot.train([
		'meriće',
		'izvoli?'
	        ])

                chatbot.train([
		'majice',
		'izvoli?'
	        ])

                chatbot.train([
		'mače',
		'izvoli?'
	        ])

                chatbot.train([
		'priče',
		'izvoli?'
	        ])

                chatbot.train([
		'Verice',
		'izvoli?'
	        ])

                chatbot.train([
		'srce',
		'izvoli?'
	        ])

        





        
