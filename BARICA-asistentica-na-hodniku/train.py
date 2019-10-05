
from chatterbot.trainers import ListTrainer

def train_barica( chatbot ):
	chatbot.train([
		'barice',
		'izvoli'
	])

	chatbot.train([
		'marice',
		'izvoli'
	])


	chatbot.train([
		'zorice',
		'izvoli'
	])


	chatbot.train([
		'starice',
		'izvoli'
	])


	chatbot.train([
		'varice',
		'izvoli?'
	])


	chatbot.train([
		'perice',
		'izvoli?'
	])


	chatbot.train([
		'da li ce',
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
		'verice',
		'izvoli?'
	])


	chatbot.train([
		'srce',
		'izvoli?'
	])


	chatbot.train([
		'marice marice',
		'izvoli?'
	])


	chatbot.train([
		'barice barice',
		'izvoli?'
	])


	chatbot.train([
		'marice marice alo',
		'izvoli?'
	])

	chatbot.train([
		'marice marice alo marice',
		'izvoli?'
	])

	chatbot.train([
		'pariz',
		'izvoli?'
	])

	chatbot.train([
		'pričaj',
		'izvoli?'
	])

	chatbot.train([
		'reci nešto',
		'izvoli?'
	])



def train( bot ):
	chatbot = ListTrainer( bot )
	
	# reove these two lines for version 1.0.0 of chatterbot
	bot.set_trainer( ListTrainer ) #1
	chatbot = bot #2

	train_barica( chatbot )

	chatbot.train([
		'reci mi nešto općenito o FOI-u',
		'foi'
	])

	chatbot.train([
		'reci mi nešto o FOI-u',
		'foi'
	])

	chatbot.train([
		'zanima me nešto o FOI-u',
		'foi'
	])


	chatbot.train([
		'FOI',
		'foi'
	])


	chatbot.train([
		'što ima na FOI',
		'foi'
	])


	chatbot.train([
		'koji je ovo fakultet',
		'foi'
	])


	chatbot.train([
		'reci mi nešto o fakultetu',
		'foi'
	])


	chatbot.train([
		'reci mi nešto općenito o fakultetu',
		'foi'
	])


	chatbot.train([
		'fakultet',
		'foi'
	])
        

	chatbot.train([
		'što ima na FOI',
		'foi'
	])

	chatbot.train([
		'zanima me nešto o fakultetu',
		'foi'
	])

	chatbot.train([
		'foi',
		'foi'
	])

	chatbot.train([
		'fuj',
		'foi'
	])

	chatbot.train([
		'foj',
		'foi'
	])


	chatbot.train([
		'trebam naći dvoranu',
		'dvorana'
	])

	chatbot.train([
		'trebam dvoranu',
		'dvorana'
	])

	chatbot.train([
		'zanimaju me dvorane',
		'dvorana'
	])

	chatbot.train([
		'zanima me dvorana',
		'dvorana'
	])

	chatbot.train([
		'reci mi nešto o dvoranama',
		'dvorana'
	])

	chatbot.train([
		'gdje je dvorana',
		'dvorana'
	])

	chatbot.train([
		'dvorana',
		'dvorana'
	])

	chatbot.train([
		'gorana',
		'dvorana'
	])

	chatbot.train([
		'zorana',
		'dvorana'
	])


	chatbot.train([
		'trebam naći profesora',
		'profesor'
	])
        
	chatbot.train([
		'trebam naći profesoricu',
		'profesor'
	])

	chatbot.train([
		'trebam naći jednog profesora',
		'profesor'
	])

	chatbot.train([
		'trebam naći jednu profesoricu',
		'profesor'
	])

	chatbot.train([
		'zanima me profesor',
		'profesor'
	])

	chatbot.train([
		'zanima me profesorica',
		'profesor'
	])

	chatbot.train([
		'zanima me jedan profesor',
		'profesor'
	])

	chatbot.train([
		'zanima me jedna profesorica',
		'profesor'
	])

	chatbot.train([
		'trebam profesora',
		'profesor'
	])

	chatbot.train([
		'trebam profesoricu',
		'profesor'
	])

	chatbot.train([
		'profesor',
		'profesor'
	])

	chatbot.train([
		'profesorica',
		'profesor'
	])



	chatbot.train([
		'trebam naći nastavnika',
		'profesor'
	])
        
	chatbot.train([
		'trebam naći nastavnicu',
		'profesor'
	])

	chatbot.train([
		'trebam naći jednog nastavnika',
		'profesor'
	])

	chatbot.train([
		'trebam naći jednu nastavnicu',
		'profesor'
	])

	chatbot.train([
		'zanima me nastavnik',
		'profesor'
	])

	chatbot.train([
		'zanima me nastavnica',
		'profesor'
	])

	chatbot.train([
		'zanima me jedan nastavnik',
		'profesor'
	])

	chatbot.train([
		'zanima me jedna nastavnica',
		'profesor'
	])

	chatbot.train([
		'trebam nastavnika',
		'profesor'
	])

	chatbot.train([
		'trebam nastavnicu',
		'profesor'
	])

	chatbot.train([
		'nastavnik',
		'profesor'
	])

	chatbot.train([
		'nastavnica',
		'profesor'
	])


	chatbot.train([
		'trebam naći asistenta',
		'profesor'
	])
        
	chatbot.train([
		'trebam naći asistenticu',
		'profesor'
	])

	chatbot.train([
		'trebam naći jednog asistenta',
		'profesor'
	])

	chatbot.train([
		'trebam naći jednu asistenticu',
		'profesor'
	])

	chatbot.train([
		'zanima me asistent',
		'profesor'
	])

	chatbot.train([
		'zanima me asistentica',
		'profesor'
	])

	chatbot.train([
		'zanima me jedan asistent',
		'profesor'
	])

	chatbot.train([
		'zanima me jedna asistentica',
		'profesor'
	])

	chatbot.train([
		'trebam asistenta',
		'profesor'
	])

	chatbot.train([
		'trebam asistenticu',
		'profesor'
	])

	chatbot.train([
		'asistent',
		'profesor'
	])

	chatbot.train([
		'asistentica',
		'profesor'
	])

	chatbot.train([
		'tko je profesor',
		'profesor'
	])

	chatbot.train([
		'tko je asistent',
		'profesor'
	])

	chatbot.train([
		'tko je nastavnik',
		'profesor'
	])

	chatbot.train([
		'trebam raspored',
		'raspored'
	])

	chatbot.train([
		'molim raspored',
		'raspored'
	])

	chatbot.train([
		'trebam svoj raspored',
		'raspored'
	])

	chatbot.train([
		'molim te raspored',
		'raspored'
	])

	chatbot.train([
		'zanima me raspored',
		'raspored'
	])

	chatbot.train([
		'zanima me moj raspored',
		'raspored'
	])

	chatbot.train([
		'raspored',
		'raspored'
	])

