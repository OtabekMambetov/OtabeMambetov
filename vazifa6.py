davlatlar_poytaxtlar = {
    "O'zbekiston": "Toshkent",
    "Qozog'iston": "Nur-Sulton",
    "Qirg'iziston": "Bishkek",
    "Tojikiston": "Dushanbe",
    "Turkmaniston": "Ashxobod",
    "Rossiya": "Moskva",
    "AQSh": "Vashington",
    "Xitoy": "Pekin",
    "Yaponiya": "Tokio",
    "Germaniya": "Berlin"
}


davlatlar = sorted(davlatlar_poytaxtlar.keys())
print("Davlatlar:")
for davlat in davlatlar:
    print(davlat)

# Poytaxtlarni alifbo ketma-ketligida chiqarish
poytaxtlar = sorted(davlatlar_poytaxtlar.values())
print("\nPoytaxtlar:")
for poytaxt in poytaxtlar:
    print(poytaxt)

# Foydalanuvchidan davlatni kiritishni so'rash va poytaxtni chiqarish
foydalanuvchi_davlati = input("\nDavlat nomini kiriting: ")
if foydalanuvchi_davlati in davlatlar_poytaxtlar:
    print(f"{foydalanuvchi_davlati}ning poytaxti {davlatlar_poytaxtlar[foydalanuvchi_davlati]}")
else:
    print("Bizda bunday ma'lumot yo'q")

# Restoran menusi
menu = {
    "Osh": 20000,
    "Shashlik": 15000,
    "Lag'mon": 18000,
    "Mastava": 12000,
    "Somsa": 8000,
    "Manti": 16000,
    "Qozon kabob": 22000,
    "Chuchvara": 14000,
    "Salat": 10000,
    "Non": 2000
}

# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rash
buyurtmalar = []
for i in range(3):
menu = {
"Osh": 20000,
"Shashlik": 15000,
"Lag'mon": 18000,
"Mastava": 12000,
"Somsa": 8000,
"Manti": 16000,
"Qozon kabob": 22000,
"Chuchvara": 14000,
"Salat": 10000,
"Non": 2000
}

# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rash
buyurtmalar = []
for i in range(3):
    buyurtma = input(f"{i+1}-taomni kiriting: ")
    buyurtmalar.append(buyurtma)
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtmalar.title()} {menu[buyurtma]} so`m")
else:
    print("Kechirasz bizda {buyurtma } yo`q ")