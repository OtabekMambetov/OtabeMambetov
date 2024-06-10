countries = {
    "O'zbekiston": {
        "poytaxt": "Toshkent",
        "hudud": "448978 kv.km",
        "aholi": "33000000",
        "pul birligi": "so'm"
    },
    "Rossiya": {
        "poytaxt": "Moskva",
        "hudud": "17098246 kv.km",
        "aholi": "144000000",
        "pul birligi": "rubl"
    },
    "AQSH": {
        "poytaxt": "Vashington",
        "hudud": "9631418 kv.km",
        "aholi": "327000000",
        "pul birligi": "dollar"
    },
    "Malayziya": {
        "poytaxt": "Kuala-Lumpur",
        "hudud": "329750 kv.km",
        "aholi": "25000000",
        "pul birligi": "rinngit"
    }
}

friends_movies = {
    "Alin": ["Terminator", "Rambo", "Titanic"],
    "Vali": ["Tenet", "Inception", "Interstellar"],
    "Hasan": ["Abdullajon", "Bomba", "Shaytanat"],
    "Husan": ["Mahallada duv-duv gap", "John Wick"]
}

# Functions
def get_country_info(country_name):
    info = countries.get(country_name)
    if info:
        print(f"{country_name}ning poytaxti {info['poytaxt']}")
        print(f"Hududi: {info['hudud']}")
        print(f"Aholisi: {info['aholi']}")
        print(f"Pul birligi: {info['pul birligi']}")
    else:
        print("Bizda bu davlat haqida ma'lumot mavjud emas")

def get_favorite_movies(friend_name):
    movies = friends_movies.get(friend_name)
    if movies:
        print(f"{friend_name}ning sevimli kinolari:")
        for movie in movies:
            print(movie)
    else:
        print(f"{friend_name} haqida ma'lumot mavjud emas")

# Example usage
while True:
    print("\n1. Davlat haqida ma'lumot olish")
    print("2. Do'stning sevimli kinolari")
    print("3. Chiqish")
    choice = input("Tanlang: ")
    
    if choice == "1":
        country_name = input("Davlat nomini kiriting: ")
        get_country_info(country_name)
    elif choice == "2":
        friend_name = input("Do'stingizning ismini kiriting: ")
        get_favorite_movies(friend_name)
    elif choice == "3":
        break
    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring.")