
otam={}
otam['ism']='Islambek'
otam['familya']='Atabayev'
otam['yosh']='43'

print(f"Dadam {otam['ism'].title()} {otam['familya']} yoshi {otam['yosh']}da")


#1

python_lugat = {
    'integer': 'butun son',
    'float': 'o\'nli son',
    'string': 'matnli qatorda',
    'if': 'agar',
    'else': 'aks holda',
    'list': 'ro\'yxat',
    'tuple': 'o\'zgarmas ro\'yxat',
    'dictionary': 'lug\'at',
    'for': 'uchun',
    'while': 'davomida'
}


soz = input("Biror so'z kiriting: ")


if soz in python_lugat:
    print(f"{soz} so'zining tarjimasi: {python_lugat[soz]}")
else:
    print("Bunda so'z mavjud emas")

#4

python_lugat = {
    'integer': 'butun son',
    'float': 'o\'nli son',
    'string': 'matnli qatorda',
    'if': 'agar',
    'else': 'aks holda',
    'list': 'ro\'yxat',
    'tuple': 'o\'zgarmas ro\'yxat',
    'dictionary': 'lug\'at',
    'for': 'uchun',
    'while': 'davomida'
}

    print(python_lugat)


#3

python_lugat = {}
python_lugat['oyim']= 'osh'
python_lugat['dadam']='manti',
python_lugat['ozim']='beshbarmoq'
print(f"Oyimning sevimli taomi {python_lugat['oyim']}")
#2

guruh={
    'Otabek':'Redmi',
    'Maqsadbek':'Samsung',
    'Ramziddin':'Vivo',
    'Ali':'Realmi',
    'Vali':'Oppo',
    'Oybek':'I phone',
    'Shoxruh':'Tecno',
    'Dilmurod':'Realmi 10 C',
    'Umirbek':'Redmi 9A',
    'Azizbek':'Honor'


}
ism= input('Ismni kiriting')
if ism in guruh:
    print(f"{ism} ning telefoni {guruh[ism]}")
else:
    print("Bunda so'z mavjud emas")