import unicodedata


def email_gen(name):
    normal = []

    normal1 = unicodedata.normalize('NFKD', name[0]).encode('ASCII', 'ignore')
    normal2 = unicodedata.normalize('NFKD', name[1]).encode('ASCII', 'ignore')

    email = str.lower(normal1.decode("utf-8")) + "." + str.lower(
        normal2.decode("utf-8")) + "@company.hu"
    return email


def pwd_gen(name):
    pwd = name + "123Start"
    return pwd


# name = ['Matuszka', 'Kristóf']
# print(name)
# print(email_gen(name))
# print(pwd_gen(name[0]))

names = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]

user = dict()
new_user = {'name': '', 'email': '', 'password': ''}

for i in range(0, len(names)):
    new_user['name'] = names[i]
    new_user['email'] = email_gen(names[i])
    new_user['password'] = pwd_gen(names[i][0])
    user[i] = new_user
print(user)

# from os import path

# # lekerdezzuk az aktualis mappat
# current_path = path.dirname(__file__)
# print(current_path)
# file_name = 'nevek.txt'

# with open(path.join(current_path, file_name), 'w') as f:
#     for item in user:
#         f.write(f'{item}\n')
