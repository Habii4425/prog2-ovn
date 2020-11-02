svar = input('Antal sekunder:  ')
sek = int(svar)
print('inmatchning: ', sek)
vecka = sek // 604800
sek = sek % 604800
print('rest från veckor: ', sek)
dag = sek // 86400
sek = sek % 86400
print('rest från dagar:  ', sek)
tim = sek // 3600
sek = sek % 3600
print('rest från timmar:  ', sek)
min = sek // 60
sek = sek % 60
print('rest från minuter:  ', sek)

print ('Veckor:', vecka)
print ('Dagar: ', dag)
print ('Timmar: ', tim)
print ('Minuter: ', min)
print ('Sekunder: ', sek)