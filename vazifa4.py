yangi_cars = ['toyota', 'mazda', 'hyundai]
for car in yangi_cars:
    if car.lower() == 'gm':
        print(car.upper())
else:
print(car.title())

yangi_cars = ['toyota', 'mazda', 'hyundai&#3
for i, car in enumerate(yangi_cars):
    if car.lower() != 'gm':
        yangi_cars[i] = car.capitalize()
    else:
        yangi_cars[i] = car.upper()
print(yangi_cars)

login = input("Iltimos, login ismingizni kiriting: ")

if login.lower() == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login.capitalize()}!")

# 1. Ikkita son tengligini tekshirish
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

if son1 == son2:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")

# 2. Son musbat yoki manfiyligini tekshirish
son = int(input("Istalgan sonni kiriting: "))

if son < 0:
    print("Manfiy son")
else:
    print("Musbat son")

# 3. Son musbat bo'lsa ildizini hisoblash
son = int(input("Sonni kiriting: "))

if son > 0:
    print("Sonning ildizi:", math.sqrt(son))
else:
    print("Musbat son kiriting")

# 4. Juft son kiritishni so'rash
son = int(input("Juft son kiriting: "))

if son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu son juft emas")

# 5. Yoshga qarab muzey chipta narxini aniqlash
yosh = int(input("Yoshingizni kiriting: "))

if yosh < 4 or yosh > 60:
    print("Chipta bepul")
elif yosh < 18:
    print("Chipta narxi 10000 so'm")
else:
    print("Chipta narxi 20000 so'm")

# 6. Ikkita sonni solishtirish
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

if son1 > son2:
    print(f"{son1} {son2} dan katta")
elif son1 < son2:
    print(f"{son1} {son2} dan kichik")
else:
    print("Sonlar teng")

# 7. Mahsulotlar ro'yxati va savatni solishtirish
mahsulotlar = ["non", "sut", "yog'", "un", "shakar", "tuz", "go'sht", "piyoz", "kartoshka", "sabzi"]
savat = []

print("Savatga kamida 5 ta mahsulot kiriting.")
for i in range(5):
    mahsulot = input(f"Savatga {i+1}-mahsulotni kiriting: ")
    savat.append(mahsulot)

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"{mahsulot} do'konimizda bor")
    else:
        print(f"{mahsulot} do'konimizda yo'q")

# 8. Sonning 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshirish
son = int(input("Biror butun son kiriting: "))

print(f"{son} quyidagi sonlarga qoldiqsiz bo'linadi:")
for i in range(2, 11):
    if son % i == 0:
        print(i)