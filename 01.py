print(2 + 2)
print(4 * 3)
print(10/2)
print(3+2*2)
print(10 // 3)
print(4 ** 3)
print(12 % 5)

a=20
b=20
c=a*b
print(c)
print(a-b+c)

print('Arek\nZawieja')
print("""Arek
Zawieja""")

print('\t\t\tpython')
print('C:path\\to\something\\new')
print(r'C:path\to\something\new')

tekst = 'I love Python. '
print(tekst * 3)
print('ha' * 8)
print('-+' * 20)
url= ('https://www.udemy.com/course/programowanie'
'-w-jezyku-python/learn/lecture/15714542#overview')
print(url)
name = 'python'
print(name, '3.12.2')

name = 'Arek'
age = '29'
print(name + ' ' + str(age))
print(name, age)
print('{} ma {} lat' .format(name, age))
print('{1} ma {0} lat' .format(name, age))
print(name, age, sep='|')
print('-+' * 20)
saldo = 40
saldo += 100
saldo -= 20

# %%
lokata = 1000
czynnik_akumulacyjny = 1 + 0.04
lokata_po_roku = lokata * czynnik_akumulacyjny
print('wartość lokaty po roku:', lokata_po_roku)

# %%
pixel = 155
pixel = pixel / 255
print(pixel)

# %%
base = 2
base **= 5
print(base)

# %%
x = 103
x %= 10
print(x)

# %%
name = 'Arek '
surname = 'Zawieja'
name += surname

print(name)

r = 4
pi = 3.14
circumference = 2 * pi * r
print(f'Obwód okręgu wynosi {circumference}cm.')

input('')