#1
def tugilgan_yil():
    ism = input("Ismingiz nima? ")
    yosh = int(input("Yoshingiz nechida? "))
    hozirgi_yil = 2024
    tugilgan_yil = hozirgi_yil - yosh
    print(f"{ism}, siz {tugilgan_yil}-yilda tug'ilgansiz.")
    
#2

def kvadrati_va_kubi():
    son = int(input("Iltimos, biror son kiriting: "))
    kvadrati = son** 2
    kubi = son ** 3
    print(f"{son} ning kvadrati {kvadrati}, kubi esa {kubi}.")
#3
def juft_yoki_toq():
    son = int(input("Iltimos, biror son kiriting: "))
    if number % 2 == 0:
        print(f"{son} juft son.")
    else:
        print(f"{son} toq son.")
    #4
def son(x=None, y=2):
    if x is None:
        x = int(input("Birinchi sonni kiriting: "))
    y = int(input("Ikkinchi sonni kiriting: ")) if y == 2 else y
    if x > y:
        print(f"Katta son: {x}")
    elif y > x:
        print(f"Katta son: {y}")
    else:
        print("Sonlar teng.")
#5
def toplam():
    son = int(input("Iltimos, biror son kiriting: "))
    for i in range(2, 11):
        if son % i == 0:
            print(f"{son} {i} ga qoldiqsiz bo'linadi.")
        else:
            print(f"{son} {i} ga qoldiqsiz bo'linmaydi.")


