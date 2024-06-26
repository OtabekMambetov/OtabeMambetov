class User:
    def __init__(self, ism, foydalanuvchi_ismi, email, yosh, manzil):
        self.ism = ism
        self.foydalanuvchi_ismi = foydalanuvchi_ismi
        self.email = email
        self.yosh = yosh
        self.manzil = manzil

    def get_info(self):
        return (f"Foydalanuvchi: {self.foydalanuvchi_ismi}, ismi: {self.ism}, "
                f"email: {self.email}, yosh: {self.yosh}, manzil: {self.manzil}")


user1 = User("Alijon Valiyev", "alijon1994", "alijon1994@gmail.com", 30, "Toshkent, O'zbekiston")
user2 = User("Otabek Hasanov", "otabek1990", "otabek1990@mail.com", 34, "Xorazm, O'zbekiston")

print(user1.get_info())
print(user2.get_info())