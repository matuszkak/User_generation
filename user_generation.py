import unicodedata
from os import path


# név alapján email generálást végez, 2-nél több elemű névre is működik
def email_gen(name):
    normal = ""
    email = ""
    szamlalo = 1

    for elem in name:
        elem = elem.lower()
        normal = unicodedata.normalize('NFKD', elem).encode('ASCII', 'ignore')
        if szamlalo < len(name):
            normal = normal.decode("utf-8") + "."

        else:
            normal = normal.decode("utf-8")
        email = email + normal
        szamlalo = szamlalo + 1
    email = email + "@company.hu"
    return email


# név alapján password-öt generál
def pwd_gen(name):
    pwd = name + "123Start"
    return pwd


# név lekérdezés sorba rendezéshez
def get_name(elem):
    return elem.get('name')


names = [['Kovács', 'Béla'], ['Kiss', 'Gyula', 'Kristóf'], ['Szabó', 'Ervin'],
         ['Kovács', 'Aladár']]
users = []
new_user = {'name': '', 'email': '', 'password': ''}

#betöltjük az adatot és legeneráljuk az email címet és a pwd-öt

for i in range(len(names)):
    new_user = {}
    new_user['name'] = names[i]
    new_user['email'] = email_gen(names[i])
    new_user['password'] = pwd_gen(names[i][0])
    users.append(new_user)

# ABC sorrendbe tesszük a user-eket név alapján

users.sort(key=get_name)

# print(users)

# lekerdezzuk az aktualis mappat
current_path = path.dirname(__file__)
print(current_path)
file_name = 'nevek.txt'

# kiírjuk fájlba a megadott struktúrában
with open(path.join(current_path, file_name), 'w') as f:
    for i in range(len(users)):
        f.write(
            f'{users[i]["name"][0]} {users[i]["name"][1]} {users[i]["email"]} {users[i]["password"]}\n'
        )
