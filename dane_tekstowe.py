# %%
text = 'Najlepszy rodzaj Burgera to bbq. Burgery bbq są świetne'
print(text)

# %%
dir(text)
help(str.isalpha)

# %%
text.capitalize()

# %%
text.title()

# %%
text.count('Burgera')

# %%
text.startswith('Naj') #Duża/mała litera ma znaczenie

# %%
'Burger'.startswith('bu')

# %%
text.endswith('tne')

# %%
'input.py'.endswith('.py')

# %%
text.find('to')

# %%
hashtags = 'sports#gym'
idx = hashtags.find('gym')
hashtags[:idx]
print(hashtags[:idx])

# %%
'Arek123!'.isalnum() #litery i cyfry tylko

# %%
'Arek123'.isdigit() #cyfry tylko

# %%
'arek'.islower()

# %%
'AREK'.isupper()

# %%
'#'.join(['eat', 'burgers', 'fatty'])

# %%
'eat#burgers#fatty'.replace('#', '!')
'column name'.replace(' ', '_')

# %%
'       burger      '.strip()
'       burger      '.rstrip()
'       burger      '.lstrip()

# %%
'1,2,3,4,5,6,7'.split(',')
' python java sas php c++'.split()

# %%
'Az'.zfill(4)
# %%
