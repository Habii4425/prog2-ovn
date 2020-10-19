svar = input('Pris på varan?  ')
i = float(svar)
ink = i * 1.15
exk = i * 0.85
print(f'Totalt pris inklusiv moms {ink:4.2f}')
print(f'Totalt pris exklusiv moms {exk:4.2f}')