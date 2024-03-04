# %%
empty_tuple = tuple()
print(empty_tuple)

# %%
amazon = ('Amazon', 'tech', 'usa', 1)
google = ('Google', 'tech', 'usa', 2)

# %%
name_google = google[0]
print(name_google)

# %%
data = (amazon, google)
print(data)

# %%
a = ('Arkadiusz', 'Zawieja')
print(a)

# %%
imie, nazwisko, id_number = ('Arkadiusz', 'Zawieja', '001')

# %%
name, sector, country, rank = amazon

# %%
nested = 'Europa', 'Polska', ('Warszawa', 'Poznan', 'Wroclaw')
print(nested)


# %%
x = 10
y = 15
x, y = y, x
print(x, y)

# %%
fruits = ('apple', 'banana', 'cherry')

fruit1, fruit2, fruit3 = fruits

print('Tuple:', fruits)
print('Fruit 1:', fruit1)
print('Fruit 2:', fruit2)
print('Fruit 3:', fruit3)
