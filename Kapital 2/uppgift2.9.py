import math #när det gäller math kan man importera genom att skriva import math och detta funktioner läser in math funktioner såsom radian, pi osv

r = float(input('Skriv cirkelns radie:')) #R är förkortat för radian, du kan döpa den till vad du vill. 
omkrets = 2*math.pi*r #math funktion kan räkna själv tex. istället för att skriva 3.14 kan man enkelt skriva math.pi, här math.pi läser värdet på Pi. Detta är ett formul för att cirkels omkrets.
arean = math.pi*r*r #math.pi räknar pi och R är förkortning för radian. En formul på hur arean på en cirkels räknas.

print('Omkretsen är: ',omkrets,'Arean är: ',arean) 
