#Python program som lar brukeren lage månedlige kalendere
import datetime

#Konstanter
DAGER = ('Søndag', 'Mandag', 'Tirsdag', 'Onsdag',
'Torsdag', 'Fredag', 'Lørdag')
MÅNEDER = ('Januar', 'Februar', 'Mars', 'April', 'Mai', 'Juni',
'Juli', 'August', 'September', 'Oktober', 'November', 'Desember')

print('✪✪✪✪LAG EN KALENDER✪✪✪✪')

#loopen ber om et årstall fra brukeren
while True:
    print('Oppgi året for kalenderen:')
    respons = input('> ')

    if respons.isdecimal() and int(respons) > 0:
        årstall = int(respons)
        break

    print('Oppgi et gyldig årstall, feks 2022.')

while True:
    print('Oppgi en desimal for måneden du ønsker, 1-12.')
    respons = input('> ')

    if not respons.isdecimal():
        print('Vennligst oppgi et gyldig tall, Feks. 2 for Februar')

    måned = int(respons)
    if 1 <= måned <= 12:
        break

    print('Vennligst oppgi et nummer fra 1 til 12.')


def lagKalenderFor(årstall, måned):
    kalenderTekst = ''

    #legg til måneden og årstallet i toppen av kalenderen
    kalenderTekst += (' ' * 34) + MÅNEDER[måned - 1] + ' ' + str(årstall) + '\n'

    #legger til ukedagene til kalenderen
    kalenderTekst +=  '...Søndag.....Mandag....Tirsdag....Onsdag....Torsdag....Fredag.....Lørdag..\n'

    #De horisontale linjene som skiller ukene:
    ukeSkillelinje = ('+----------' * 7) + '+\n'

    #Blanke rader har ti mellomrom mellom vertikale dags-skillelinjene
    blankRad = ('|          ' * 7) + '|\n'

    #Henter den første datoen i måneden ved å bruke datetime modulen
    nåværendeDato = datetime.date(årstall, måned, 1)

    #skru tilbake nåværendeDato til vi når søndag
    #Søndag returneres som 6
    while nåværendeDato.weekday() != 6:
        nåværendeDato -= datetime.timedelta(days=1)

    while True:
        #looper over hver uke i måneden
        kalenderTekst += ukeSkillelinje

        #datoRad er raden med dato som merkelapp....
        datoRad = ''
        for i in range(7):
            dato = str(nåværendeDato.day).rjust(2)
            datoRad += '|' + dato + (' ' * 8)
            nåværendeDato += datetime.timedelta(days=1) #inkrementerer til neste dags
        datoRad += '|\n' # Vertikal linje etter lørdag.

        #legger til day number og 3 blanke rader til kalenderen
        kalenderTekst += datoRad
        for i in range(3):
            kalenderTekst += blankRad

        #Sjekker om måneden er fullført
        if nåværendeDato.month != måned:
            break

    kalenderTekst += ukeSkillelinje
    return kalenderTekst

kalenderTekst = lagKalenderFor(årstall, måned)
print(kalenderTekst)


while True:
    print('Ønsker du å lagre kalenderen som en tekstil? Oppgi (J)a eller (N)ei')

    respons = input('- ')

    if respons.upper() == 'J':
        #lagrer kalenderen som en tekstil
        kalenderFilnavn = 'calendar_{}_{}.txt'.format(årstall, måned)
        with open(kalenderFilnavn, 'w') as filObj:
            filObj.write(kalenderTekst)
        print('Fil largret som ' + kalenderFilnavn)

    if respons.upper() == 'N':
        print('Kalenderen lagres ikke')
        break

    print('Vennligst oppgi J eller N for om du ønsker å lagre kalenderen')

































