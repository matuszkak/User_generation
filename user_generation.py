import unicodedata
from os import path
from collections import OrderedDict


# név alapján email generálást végzi
def email_gen(name):
    normal = []

    normal1 = unicodedata.normalize('NFKD', name[0]).encode('ASCII', 'ignore')
    normal2 = unicodedata.normalize('NFKD', name[1]).encode('ASCII', 'ignore')

    email = str.lower(normal1.decode("utf-8")) + "." + str.lower(
        normal2.decode("utf-8")) + "@company.hu"
    return email


# név alapján password-öt generál
def pwd_gen(name):
    pwd = name + "123Start"
    return pwd


names = [['Kovács', 'Béla'], ['Kiss', 'Gyula', 'Kristóf'], ['Szabó', 'Ervin']]

user = dict()

print(f'{names}\n')

new_user = {'name': '', 'email': '', 'password': ''}

#betöltjük az adatot és legeneráljuk az email címet és pwd-t

for i in range(len(names)):
    new_user = {'name': '', 'email': '', 'password': ''}
    new_user['name'] = names[i]
    new_user['email'] = email_gen(names[i])
    new_user['password'] = pwd_gen(names[i][0])
    user[i] = new_user

# print(user)

# ABC sorrendbe tesszük név alapján
ordered_user = dict(sorted(user.items(), key=lambda item: item[1]['name']))

print(ordered_user)

# lekerdezzuk az aktualis mappat
current_path = path.dirname(__file__)
print(current_path)
file_name = 'nevek.txt'

# kiírjuk fájlba megadott struktúrában
with open(path.join(current_path, file_name), 'w') as f:
    for i in range(len(ordered_user)):
        f.write(
            f'{ordered_user[i]["name"][0]} {ordered_user[i]["name"][1]} {ordered_user[i]["email"]} {ordered_user[i]["password"]}\n'
        )

# Bugs:
#1 több elemű névre is működjön!
#2 nem sorrendben írja a fájlba
