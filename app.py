import os
import shutil
from datetime import datetime
from os.path import isfile, join

niz = [f for f in os.listdir() if isfile(join(os.getcwd(), f))]
niz.sort()

for i in niz:
    if i == 'a.py' or i == 'b.py':
        continue
    podniz = i.split(' ')
    datum = datetime.strptime(podniz[0] + ' ' + podniz[1], '%Y.%m.%d %H-%M-%S')
    datum_za_ime = podniz[0]
    #print(datum_za_ime)
    niz_datum = datum_za_ime.split('.')
    ime = niz_datum[2] + '.' + niz_datum[1] + '.' + niz_datum[0] + ' '

    dan_u_nedelji = datum.isoweekday()

    vezbe = True
    nastavak = ''

    if dan_u_nedelji == 1:
        nastavak = 'Distribuirani sistemi' 
        ime += nastavak
        if datum.hour >=10 and datum.hour < 12:
            vezbe = True
        else:
            vezbe = False
    elif dan_u_nedelji == 2:
        nastavak = 'Softversko inzenjerstvo' 
        ime += nastavak
        if datum.hour >=10 and datum.hour < 12:
            vezbe = True
        else:
            vezbe = False
    elif dan_u_nedelji == 3:
        nastavak = 'Mikroracunarski sistemi' 
        ime += nastavak
        if datum.hour >=10 and datum.hour < 12:
            vezbe = False
        else:
            vezbe = True
    elif dan_u_nedelji == 4:
        nastavak = 'Informacioni sistemi' 
        ime += nastavak
        if datum.hour >=10 and datum.hour < 12:
            vezbe = True
        else:
            vezbe = False
    elif dan_u_nedelji == 5:
        nastavak = 'Projektovanje i analiza algoritama' 
        ime += nastavak
        if datum.hour >=10 and datum.hour < 12:
            vezbe = False
        else:
            vezbe = True

 
    if vezbe:
        ime += ' vezbe'
    else:
        ime += ' predavanja'

    podfajl_niz = os.listdir(os.getcwd()+'/'+nastavak)

    pom_niz = [f[4:] for f in podfajl_niz]
    if ime in pom_niz:
        continue

    if podfajl_niz:
        podfajl_niz.sort(reverse = True) 
        broj = int(podfajl_niz[0][1])
        broj = (broj + 1) % 10
        prefiks = int(podfajl_niz[0][0])
        if broj == 0:
            prefiks += 1
        ime = str(prefiks) + str(broj) + '. ' + ime
    else:
        ime = '01. ' + ime

    #os.rename(i, ime)
    shutil.copy(os.getcwd() + '/' + i, os.getcwd()+'/'+nastavak)
    os.rename('./'+nastavak+'/'+i, './'+nastavak+'/'+ime)











