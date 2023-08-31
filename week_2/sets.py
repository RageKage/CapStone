cats = {"leopard", "tiger", "lion", "cheetah", "jaguar"}

print(cats) # {'tiger', 'cheetah', 'jaguar', 'leopard', 'lion'}

for cat in cats:
    print(cat)
    
cats.add('panther') # {'cheetah', 'panther', 'jaguar', 'leopard', 'lion', 'tiger'}

cats.remove("tiger") # {'cheetah', 'panther', 'jaguar', 'leopard', 'lion'}

print(cats)
# tiger
# cheetah
# leopard
# lion


cats.add('jaguar') # {'cheetah', 'panther', 'jaguar', 'leopard', 'lion'}, no duplicates


print(cats)