'''
NB-2023.03.21

Feladat: mutasd be a matematikai műveleteket, példákkal

'''
print("----------------------")
print('Matematikai műveletek')
print("----------------------")

a = int(input("Add meg az első számot: "))
b = int(input("Add meg a második számot: "))
print('----------------')
print(f'Összeadás: {a} + {b} = {a + b}')
print(f'Kivonás: {a} - {b} = {a-b}')
print(f'Szorzás: {a} x {b} = {a*b}')
print(f'Osztás: {a} : {b} = {a/b}')
print(f'Osztás egészre kerekítve: {a} : {b} = {a//b}')
print(f'Az osztás maradéka: {a} : {b} = {a%b}')          # pl 10:3 = 3 és marad 1. Ebben az esetben az 1-et fogja kiírni
print ('----------------')