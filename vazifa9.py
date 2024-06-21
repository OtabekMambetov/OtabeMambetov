
#1

foydalanuvchi={
    'ism':ism,
    'familya':familya,
    'tug`ilgan_yil':tugilgan_yil,
    'tug`ilgan_joyi':tugilgan_joy
}
    if email:
        foydalanuvchi['email']:email
    if telefon:
        foydalanuvchi['telefon']:telefon
    return foydalanuvchi
ism = input("Ismingizni kiriting: ")
familya = input("Familiyangizni kiriting: ")
tugilgan_yil = input("Tug'ilgan yilingizni kiriting: ")
tugilgan_joy = input("Tug'ilgan joyingizni kiriting: ")
email = input("Email manzilingizni kiriting: ")
telefon = input("Telefon raqamingizni kiriting: ")
foydalanuvchi_malumotlari = foydalanuvchi_info(ism, familya, tugilgan_yil, tugilgan_joy, email, telefon)
print("Foydalanuvchi ma'lumotlari:")
print(foydalanuvchi_malumotlari)