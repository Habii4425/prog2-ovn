min = int(input('Skriv antal minuter:  '))

pris = float(input('Skriv in pris per minut:  '))
summa = min*pris
dis = 0.90
if summa > 300:
    summa = summa*dis

print(f'Pris: {summa:.2f} kr')