imie = 'Arek'
wiek = '29'
with open('plik.txt', 'w') as f:
    print('Hello', 'world!', sep='+', file=f)
    print(imie, wiek, file=f)
