# %%
empty_set = set()
print(empty_set)
print(type(empty_set))

# %%
techs = {'python', 'java', 'sql', 'c++'}
print(type(techs))
print(len(techs))

# %%
'python' in techs
# %%
'html' in techs

# %%
techs.add('sas')
print(techs)

# %%
techs.remove('sql')
print(techs)

# %%
techs.clear()

# %%
print(techs)

# %%
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}

# %%
C.issubset(A)

# %%
A.issuperset(C)

# %%
B.issubset(C)

# %%
A.union(B)

# %%
A.intersection(B)

# %%
A.symmetric_difference(B)

# %%
D = A.copy()
# %%
print(D)
# %%
