ismlar = [ 'Name1','Name2','Name3']
print('Salom', ismlar[0],'\nHush kelibsan',ismlar[2],'\nAhvollaring yaxshimi', ismlar[2])

#1

sonlar = [ ]
musbat = sonlar
musbat.append(2)
musbat.append(-2)
musbat.append(3.5)
musbat.append(2/5)

print(musbat)

#2

sonlar = [ ]
musbat = sonlar
musbat.append(2)
musbat.append(-2)
musbat.append(3.5)
musbat.append(2/5)
yigindi=musbat[1]+musbat[2]
ayirma=musbat[1]-musbat[2]
bolinma=musbat[1]/musbat[2]
kopaytma=musbat[1]*musbat[2]
print(yigindi,ayirma,bolinma,kopaytma)

#3

sonlar = [ ]
musbat = sonlar
musbat.append(2)
musbat.append(-2)
musbat.append(3.5)
musbat.append(2/5)
# yigindi=musbat[1]+musbat[2]
# ayirma=musbat[1]-musbat[2]
# bolinma=musbat[1]/musbat[2]
# kopaytma=musbat[1]*musbat[2]
# print(yigindi,ayirma,bolinma,kopaytma)
musbat.sort()
print(musbat)
musbat.reverse()
print(musbat)

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

friends =[] 
friends.append("Ali")
friends.append("Vali")
friends.append("Lola")
friends.append("Soli")
friends.append("Guli")
friends.append("Nurullo")
mehmonlar=[]
mehmonlar.append(friends.pop(0))
print(mehmonlar)


