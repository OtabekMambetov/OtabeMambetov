
friends = ['Oybek','Shohrux', 'Dilmurod']
friends.sort()
print(friends)

#1

sonlar = ['12','-5', '15.2']
sonlar.sort()
print(sonlar)

#2

ages = [-5,12,15.2]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))

#3

ages = [-5,12,15.2]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))

#4

t_shaxslar=['Stiv Jobs']
z_shaxslar=['Pavel Durov']
t_shaxslar.sort()
z_shaxslar.sort()
print('Tarixiy shaxslar',t_shaxslar,'Zamonaviy shaxslar',z_shaxslar)

#5
friends =[''] 
friends.append("Ali")
friends.append("Vali")
friends.append("Lola")
friends.append("Soli")
friends.append("Guli")
friends.append("Nurullo")
print(friends)

#6

friends =[''] 
friends.append("Ali")
friends.append("Vali")
friends.append("Lola")
friends.append("Soli")
friends.append("Guli")
friends.append("Nurullo")
friends.remove("Soli")
print(friends)

#7

friends =[''] 
friends.append("Ali")
friends.append("Vali")
friends.append("Lola")
friends.append("Soli")
friends.append("Guli")
friends.append("Nurullo")
friends.append("Shohrux")
friends[1]="Oybek"
friends.remove("Soli")
print(friends)

#8

friends = ["Ali", "Vali", "Lola", "Soli", "Guli", "Nurullo"]
yangi_mehmonlar=[' ']


yangi_mehmonlar.append(friends.pop(0))

print(friends)

