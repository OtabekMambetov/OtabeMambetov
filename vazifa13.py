#1
import json



data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

data_json = json.dumps(data)
print(data_json)
#2
import json

talaba = {"Ismi" : "Otabek", "Familiya" : "Mambetov", "Yil":2005, }

talaba_json = json.dumps(talaba)
print(talaba_json)
#3
import json

talaba1={ "name": "Tom", "lastname": "Price", "year": 4, "faculty": "Engineering"}
talaba2={ "name": "Nick", "lastname": "Thameson", "year": 3, "faculty": "Computer Science"}
talaba3={ "name": "John", "lastname": "Doe", "year": 2, "faculty": "ICT"}
talaba1_json=json.dumps(talaba1)
talaba2_json=json.dumps(talaba2)
talaba3_json=json.dumps(talaba3)
print(talaba1_json)
print(talaba2_json)
print(talaba3_json)