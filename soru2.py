
from random import randint
sayilar = []
while len(sayilar) < 6:
    sayi = randint(1,50)
    if sayi not in sayilar:  # Sayıların birbirinden farklı olması istendiği için sorguladım.
        sayilar.append(sayi) # Aynı sayı üretilmediğinde listeye eklendi
print(sayilar)