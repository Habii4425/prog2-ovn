import math

r = float(input ('Skriv ett tall:  '))
V = 4 * math.pi * r * r * r / 3
A = 4 * math.pi * r * r

print (f'Talets volymen är: {V:4.2f}')
print (f'Talets arean är: {A:4.2f}')