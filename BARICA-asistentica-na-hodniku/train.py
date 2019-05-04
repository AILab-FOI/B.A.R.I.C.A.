
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
		'Reci mi nešto općenito o FOI-u',
		'foi'
	])

	chatbot.train([
		'Reci mi nešto o FOI-u',
		'foi'
	])


	chatbot.train([
		'FOI',
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
		'Gdje je dvorana',
		'dvorana'
	])

	chatbot.train([
		'Dvorana',
		'dvorana'
	])


	chatbot.train([
		'Trebam naći profesora',
		'profesor'
	])

	chatbot.train([
		'Trebam naći jednog profesora',
		'profesor'
	])

	chatbot.train([
		'Trebam profesora',
		'profesor'
	])

	chatbot.train([
		'Profesor',
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
		'Raspored',
		'raspored'
	])

