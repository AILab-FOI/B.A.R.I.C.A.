
from chatterbot.trainers import ListTrainer

def train( bot ):
	chatbot = ListTrainer( bot )
	
	# reove these two lines for version 1.0.0 of chatterbot
	bot.set_trainer( ListTrainer ) #1
	chatbot = bot #2

	chatbot.train([
		'Barice',
		'Da?'
	])

	chatbot.train([
		'Marice',
		'Da?'
	])


	chatbot.train([
		'Zorice',
		'Da?'
	])


	chatbot.train([
		'Starice',
		'Da?'
	])


	chatbot.train([
		'Varice',
		'Da?'
	])

	chatbot.train([
		'Slajd',
		'slide'
	])

	chatbot.train([
		'Sljedeći slajd',
		'slide'
	])

	chatbot.train([
		'Sljedeći slajd molim',
		'slide'
	])

	chatbot.train([
		'Sljedeći slajd molim te',
		'slide'
	])

	chatbot.train([
		'Promijeni slajd',
		'slide'
	])

	chatbot.train([
		'Promijeni slajd molim te',
		'slide'
	])

	chatbot.train([
		'Promijeni slajd molim',
		'slide'
	])

	chatbot.train([
		'Može dalje',
		'slide'
	])

	chatbot.train([
		'Idemo dalje',
		'slide'
	])

	chatbot.train([
		'Je li umjetna inteligencija dobra ili zla?',
		'govor'
	])

	chatbot.train([
		'Je li umjetna inteligencija dobra?',
		'govor'
	])

	chatbot.train([
		'Je li umjetna inteligencija zla?',
		'govor'
	])

	chatbot.train([
		'Kakva je umjetna inteligencija, dobra ili zla?',
		'govor'
	])

	chatbot.train([
		'Kakva je umjetna inteligencija?',
		'govor'
	])

	chatbot.train([
		'Animiraj',
		'animiraj'
	])

	chatbot.train([
		'Pokreni animaciju',
		'animiraj'
	])

	chatbot.train([
		'Pokreni animaciju molim te',
		'animiraj'
	])

	chatbot.train([
		'Prikaži animaciju',
		'animiraj'
	])

	chatbot.train([
		'Hvala',
		'nema_na_cemu'
	])

	chatbot.train([
		'Hvala ti',
		'nema_na_cemu'
	])

	chatbot.train([
		'Hvala ti Barice',
		'nema_na_cemu'
	])

	chatbot.train([
		'Zahvaljujem',
		'nema_na_cemu'
	])

	chatbot.train([
		'Lijepo od tebe',
		'nema_na_cemu'
	])

	chatbot.train([
		'Predstavi se',
		'predstavljanje'
	])

	chatbot.train([
		'Tko si ti',
		'predstavljanje'
	])

	chatbot.train([
		'Što si ti',
		'predstavljanje'
	])

	chatbot.train([
		'Što se radi u A I labu?',
		'cool_projekti'
	])

	chatbot.train([
		'Što radimo u A I labu?',
		'cool_projekti'
	])

	chatbot.train([
		'Što ima u A I labu?',
		'cool_projekti'
	])

	chatbot.train([
		'Što mi radimo u A I labu?',
		'cool_projekti'
	])

	chatbot.train([
		'Što preporučuješ studentima?',
		'ucite'
	])

	chatbot.train([
		'Što bi preporučila studentima?',
		'ucite'
	])

	chatbot.train([
		'Što bi studenti trebali raditi?',
		'ucite'
	])
