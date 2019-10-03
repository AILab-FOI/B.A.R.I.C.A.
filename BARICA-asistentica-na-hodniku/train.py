
from chatterbot.trainers import ListTrainer

def train( bot ):
	chatbot = ListTrainer( bot )
	
	# reove these two lines for version 1.0.0 of chatterbot
	bot.set_trainer( ListTrainer ) #1
	chatbot = bot #2

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

	chatbot.train([
		'Reci mi nešto općenito o FOI-u',
		'foi'
	])

	chatbot.train([
		'Reci mi nešto o FOI-u',
		'foi'
	])

	chatbot.train([
		'Zanima me nešto o FOI-u',
		'foi'
	])


	chatbot.train([
		'FOI',
		'foi'
	])


	chatbot.train([
		'Što ima na FOI',
		'foi'
	])


	chatbot.train([
		'Koji je ovo fakultet',
		'foi'
	])


	chatbot.train([
		'Reci mi nešto o fakultetu',
		'foi'
	])


	chatbot.train([
		'Reci mi nešto općenito o fakultetu',
		'foi'
	])


	chatbot.train([
		'Fakultet',
		'foi'
	])
        

	chatbot.train([
		'Što ima na FOI',
		'foi'
	])

	chatbot.train([
		'Zanima me nešto o fakultetu',
		'foi'
	])


	chatbot.train([
		'Trebam naći dvoranu',
		'dvorana'
	])

	chatbot.train([
		'Trebam dvoranu',
		'dvorana'
	])

	chatbot.train([
		'Zanimaju me dvorane',
		'dvorana'
	])

	chatbot.train([
		'Zanima me dvorana',
		'dvorana'
	])

	chatbot.train([
		'Reci mi nešto o dvoranama',
		'dvorana'
	])

	chatbot.train([
		'Gdje je dvorana',
		'dvorana'
	])

	chatbot.train([
		'Dvorana',
		'dvorana'
	])

	chatbot.train([
		'Gorana',
		'dvorana'
	])

	chatbot.train([
		'Zorana',
		'dvorana'
	])


	chatbot.train([
		'Trebam naći profesora',
		'profesor'
	])
        
	chatbot.train([
		'Trebam naći profesoricu',
		'profesor'
	])

	chatbot.train([
		'Trebam naći jednog profesora',
		'profesor'
	])

	chatbot.train([
		'Trebam naći jednu profesoricu',
		'profesor'
	])

	chatbot.train([
		'Zanima me profesor',
		'profesor'
	])

	chatbot.train([
		'Zanima me profesorica',
		'profesor'
	])

	chatbot.train([
		'Zanima me jedan profesor',
		'profesor'
	])

	chatbot.train([
		'Zanima me jedna profesorica',
		'profesor'
	])

	chatbot.train([
		'Trebam profesora',
		'profesor'
	])

	chatbot.train([
		'Trebam profesoricu',
		'profesor'
	])

	chatbot.train([
		'Profesor',
		'profesor'
	])

	chatbot.train([
		'Profesorica',
		'profesor'
	])



	chatbot.train([
		'Trebam naći nastavnika',
		'profesor'
	])
        
	chatbot.train([
		'Trebam naći nastavnicu',
		'profesor'
	])

	chatbot.train([
		'Trebam naći jednog nastavnika',
		'profesor'
	])

	chatbot.train([
		'Trebam naći jednu nastavnicu',
		'profesor'
	])

	chatbot.train([
		'Zanima me nastavnik',
		'profesor'
	])

	chatbot.train([
		'Zanima me nastavnica',
		'profesor'
	])

	chatbot.train([
		'Zanima me jedan nastavnik',
		'profesor'
	])

	chatbot.train([
		'Zanima me jedna nastavnica',
		'profesor'
	])

	chatbot.train([
		'Trebam nastavnika',
		'profesor'
	])

	chatbot.train([
		'Trebam nastavnicu',
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
		'Trebam naći asistenta',
		'profesor'
	])
        
	chatbot.train([
		'Trebam naći asistenticu',
		'profesor'
	])

	chatbot.train([
		'Trebam naći jednog asistenta',
		'profesor'
	])

	chatbot.train([
		'Trebam naći jednu asistenticu',
		'profesor'
	])

	chatbot.train([
		'Zanima me asistent',
		'profesor'
	])

	chatbot.train([
		'Zanima me asistentica',
		'profesor'
	])

	chatbot.train([
		'Zanima me jedan asistent',
		'profesor'
	])

	chatbot.train([
		'Zanima me jedna asistentica',
		'profesor'
	])

	chatbot.train([
		'Trebam asistenta',
		'profesor'
	])

	chatbot.train([
		'Trebam asistenticu',
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
		'Trebam raspored',
		'raspored'
	])

	chatbot.train([
		'Molim raspored',
		'raspored'
	])

	chatbot.train([
		'Trebam svoj raspored',
		'raspored'
	])

	chatbot.train([
		'Molim te raspored',
		'raspored'
	])

	chatbot.train([
		'Zanima me raspored',
		'raspored'
	])

	chatbot.train([
		'Zanima me moj raspored',
		'raspored'
	])

	chatbot.train([
		'Raspored',
		'raspored'
	])

