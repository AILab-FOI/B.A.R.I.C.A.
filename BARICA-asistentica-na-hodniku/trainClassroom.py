
from chatterbot.trainers import ListTrainer

def trainClassroom( bot ):
	chatbot = ListTrainer( bot )
	
	# reove these two lines for version 1.0.0 of chatterbot
	bot.set_trainer( ListTrainer ) #1
	chatbot = bot #2

	chatbot.train([
		'dvorana 9',
		'd9'
	])

	chatbot.train([
		'dvoranu 9',
		'd9'
	])

	chatbot.train([
		'b9',
		'd9'
	])

	chatbot.train([
		'9',
		'd9'
	])

	chatbot.train([
		'info',
		'info'
	])

	chatbot.train([
		'infokop',
		'info'
	])

	chatbot.train([
		'info klub',
		'info'
	])

	chatbot.train([
		'kafić',
		'info'
	])

	chatbot.train([
		'knjižnica',
		'knjiznica'
	])

	chatbot.train([
		'boje knjižnica',
		'knjiznica'
	])

	chatbot.train([
		'koji knjižnica',
		'knjiznica'
	])

	chatbot.train([
		'dvorana 10',
		'd10'
	])

	chatbot.train([
		'dvoranu 10',
		'd10'
	])

	chatbot.train([
		'10',
		'd10'
	])

	chatbot.train([
		'dvorana 10',
		'd10'
	])

	chatbot.train([
		'referada',
		'referada'
	])

	chatbot.train([
		'laboratorij 5',
		'lab5'
	])

	chatbot.train([
		'love pet',
		'lab5'
	])

	chatbot.train([
		'25',
		'lab5'
	])

	chatbot.train([
		'laptop',
		'lab5'
	])

	chatbot.train([
		'pet',
		'lab5'
	])

	chatbot.train([
		'dvorana 5',
		'lab5'
	])

	chatbot.train([
		'dvoranu 5',
		'lab5'
	])

	chatbot.train([
		'skriptarnica',
		'skriptarnica'
	])

	chatbot.train([
		'fotokopirnica',
		'foto'
	])

	chatbot.train([
		'fotokopiranje',
		'foto'
	])

	chatbot.train([
		'fotokopira ona',
		'foto'
	])

	chatbot.train([
		'dvorana 6',
		'd6'
	])

	chatbot.train([
		'dvoranu 6',
		'd6'
	])

	chatbot.train([
		'b6',
		'd6'
	])

	chatbot.train([
		'šest',
		'd6'
	])

	chatbot.train([
		'dvorana 7',
		'd7'
	])

	chatbot.train([
		'dvoranu 7',
		'd7'
	])

	chatbot.train([
		'b7',
		'd7'
	])

	chatbot.train([
		'd7',
		'd7'
	])

	chatbot.train([
		'sedam',
		'd7'
	])

	chatbot.train([
		'laboratorij 12',
		'lab12'
	])

	chatbot.train([
		'laboratory 12',
		'lab12'
	])

	chatbot.train([
		'lav 12',
		'lab12'
	])

	chatbot.train([
		'lab 12',
		'lab12'
	])

	chatbot.train([
		'12',
		'lab12'
	])

	chatbot.train([
		'laboratorij 13',
		'lab13'
	])

	chatbot.train([
		'laboratorija 13',
		'lab13'
	])

	chatbot.train([
		'lap 13',
		'lab13'
	])

	chatbot.train([
		'lav 13',
		'lab13'
	])

	chatbot.train([
		'lab 13',
		'lab13'
	])

	chatbot.train([
		'13',
		'lab13'
	])

	chatbot.train([
		'dvorana 13',
		'lab13'
	])

	chatbot.train([
		'dvoranu 13',
		'lab13'
	])

	chatbot.train([
		'laboratorij 14',
		'lab14'
	])

	chatbot.train([
		'laboratorija 14',
		'lab14'
	])

	chatbot.train([
		'love 14',
		'lab14'
	])

	chatbot.train([
		'Labin 14',
		'lab14'
	])

	chatbot.train([
		'lab 14',
		'lab14'
	])

	chatbot.train([
		'14',
		'lab14'
	])

	chatbot.train([
		'dvorana 14',
		'lab14'
	])

	chatbot.train([
		'dvoranu 14',
		'lab14'
	])

	chatbot.train([
		'laboratorij 15',
		'lab15'
	])

	chatbot.train([
		'laboratorija 15',
		'lab15'
	])

	chatbot.train([
		'lab 15',
		'lab15'
	])

	chatbot.train([
		'love 15',
		'lab15'
	])

	chatbot.train([
		'Club 15',
		'lab15'
	])

	chatbot.train([
		'15',
		'lab15'
	])

	chatbot.train([
		'dvorana 15',
		'lab15'
	])

	chatbot.train([
		'dvoranu 15',
		'lab15'
	])

	chatbot.train([
		'dekanat',
		'dekanat'
	])

	chatbot.train([
		'centar za podršku studentima i razvoj karijere',
		'CPSRK'
	])

	chatbot.train([
		'centar za podršku studentima i razvoj karijera',
		'CPSRK'
	])

	chatbot.train([
		'centar za podršku',
		'CPSRK'
	])

	chatbot.train([
		'računovodstvo',
		'racunovodstvo'
	])

	chatbot.train([
		'dvorana 4',
		'd4'
	])

	chatbot.train([
		'dvoranu 4',
		'd4'
	])

	chatbot.train([
		'd4',
		'd4'
	])

	chatbot.train([
		'četiri',
		'd4'
	])

	chatbot.train([
		'dvorana 11',
		'd11'
	])

	chatbot.train([
		'Brana 11',
		'd11'
	])

	chatbot.train([
		'dvoranu 11',
		'd11'
	])

	chatbot.train([
		'd11',
		'd11'
	])

	chatbot.train([
		'11',
		'd11'
	])

	chatbot.train([
		'dvorana 1',
		'd1'
	])

	chatbot.train([
		'dvoranu 1',
		'd1'
	])

	chatbot.train([
		'N1',
		'd1'
	])

	chatbot.train([
		'jedan',
		'd1'
	])

	chatbot.train([
		'dvorana 2',
		'd2'
	])

	chatbot.train([
		'dvorana dva',
		'd2'
	])

	chatbot.train([
		'D2',
		'd2'
	])

	chatbot.train([
		'dva',
		'd2'
	])

	chatbot.train([
		'dvorana 8',
		'd8'
	])

	chatbot.train([
		'dvoranu 8',
		'd8'
	])

	chatbot.train([
		'te 8',
		'd8'
	])

	chatbot.train([
		'd8',
		'd8'
	])

	chatbot.train([
		'osam',
		'd8'
	])

	chatbot.train([
		'dvorana 3',
		'd3'
	])

	chatbot.train([
		'dvoranu 3',
		'd3'
	])

	chatbot.train([
		'D3',
		'd3'
	])

	chatbot.train([
		'tri',
		'd3'
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
	



	
