
from ScrapInformation import scrapProfessorsForTrain, scrapAllGroups


d = {'Izvoli': {
    'izvoli': 'Izvoli?'},
     'FOI': {
         'foi': 'Fakultet organizacije i informatike jedna je od sastavnica Sveučilišta u Zagrebu. FOI je visokoobrazovna ustanova u interdisciplinarnom području informatike, organizacije i poslovanja. Studijski programi utemeljeni su na modernim svjetskim modelima, načelima Bolonjske deklaracije i ECTS bodovnom sustavu.'},
     'Dvorana': {
         'dvorana': 'Koja dvorana?'},
     'Profesor': {
         'profesor': 'Koji profesor?'},
     'Raspored': {
         'raspored': 'Za koju vrstu studija trebaš raspored?'},
    'Dvorane': {
    'd9': 'Dvorana devet se nalazi u podrumu, u istočnom krilu zgrade',
    'info': 'Info Klub kafić se nalazi u podrumu, u istočnom krilu zgrade',
    'knjiznica': 'Knjižnica se nalazi u podrumu, u južnom krilu zgrade',
    'd10': 'Dvorana deset se nalazi u prizemlju, u istočnom krilu zgrade',
    'referada': 'Referada se nalazi u prizemlju, u istočnom krilu zgrade',
    'lab5': 'Laboratorij pet se nalazi u prizemlju, u istočnom krilu zgrade',
    'skriptarnica': 'Skriptarnica se nalazi u prizemlju, u istočnom krilu zgrade',
    'foto': 'Fotokopiraona se nalazi u prizemlju, kod samog  ulaza u zgradu',
    'd6': 'Dvorana šest se nalazi u prizemlju, u južnom krilu zgrade',
    'd7': 'Dvorana sedam se nalazi u prizemlju, u južnom krilu zgrade',
    'lab12': 'Laboratorij dvanaest se nalazi u prizemlju, u južnom krilu zgrade',
    'lab13': 'Laboratorij trinaest se nalazi u prizemlju, u južnom krilu zgrade',
    'lab14': 'Laboratorij četrnaest se nalazi u prizemlju, u južnom krilu zgrade',
    'lab15': 'Laboratorij petnaest se nalazi u prizemlju, u južnom krilu zgrade',
    'dekanat': 'Dekanat se nalazi na prvom katu, na kraju istočnog krila zgrade',
    'CPSRK': 'Centar za podršku studentima i razvoj karijera se nalazi na prvom katu, u istočnom krilu zgrade',
    'racunovodstvo': 'Računovodstvo se nalazi na prvom katu, u istočnom krilu zgrade',
    'd4': 'Dvorana četiri se nalazi na prvom katu, između južnog i istočnog krila, u kutu',
    'd11': 'Dvorana jedanaest se nalazi na prvom katu, u južnom krilu zgrade',
    'd1': 'Dvorana jedan se nalazi na drugom katu, na kraju istočnog krila zgrade',
    'd2': 'Dvorana dva se nalazi na drugom katu, u istočnom krilu zgrade',
    'd8': 'Dvorana osam se nalazi na drugom katu, između južnog i istočnog krila, u kutu',
    'd3': 'Dvorana tri se nalazi na drugom katu, u južnom krilu zgrade'},
     'Vrsta_studija': {
             '2824': 'Za koju godinu studija trebaš raspored?',
             '2825': 'Za koju godinu studija trebaš raspored?',
             '44700': 'Za koju godinu studija trebaš raspored?',
             '2831': 'Za koju godinu studija trebaš raspored?',
             '2832': 'Za koju godinu studija trebaš raspored?',
             '2826': 'Za koju godinu studija trebaš raspored?',
             '99118': 'Za koju godinu studija trebaš raspored?',
             '2827': 'Za koju godinu studija trebaš raspored?',
             '99119': 'Za koju godinu studija trebaš raspored?',
             '2828': 'Za koju godinu studija trebaš raspored?',
             '99120': 'Za koju godinu studija trebaš raspored?',
             '2829': 'Za koju godinu studija trebaš raspored?',
             '99121': 'Za koju godinu studija trebaš raspored?',
             '2834': 'Za koju godinu studija trebaš raspored?',
             '198034': 'Za koju godinu studija trebaš raspored?',
             '2835': 'Za koju godinu studija trebaš raspored?',
             '2836': 'Za koju godinu studija trebaš raspored?',
             '33958': 'Za koju godinu studija trebaš raspored?',
             '52162': 'Za koju godinu studija trebaš raspored?',
             },
     'Godina_studija': {
             '1': 'Za koju grupu trebaš raspored?',
             '2': 'Za koju grupu trebaš raspored?',
             '3': 'Za koju grupu trebaš raspored?',
             }}



        
def dictionary():
        global d
        professors = scrapProfessorsForTrain()
        prof = {}
        for name, user_name in professors.items():
                prof[user_name] = 'Izvoli podatke za ' + name
                d['Profesori'] = prof
                
                
        groups = scrapAllGroups()
        gr = {}
        for group in groups:
                gr[group] = 'Izvoli raspored'
                d['Grupa'] = gr
        return d

