import math
import string
#zad 1
#
# try:
#     a = input('Podaj 1 liczbe')
#     b = input('Podaj 2 liczbe')
#     a = int(a)
#     b = int(b)
#     wynik = a ** 2 + a * b + b ** 2
#     wynik2 = str(wynik)
#     with open('zadanie1.txt', 'w+') as plik:
#         for x in wynik2:
#             plik.write(x)
# #with open('zadanie1.txt', 'w') as plik:
# #        plik.write(f'{wynik}\n')
# except Exception as e:
#     print(f'Wystąpił błąd: {e}')
#






#zad 2
# def listy(lista1,lista2):
#     nowa = []
#     for x in range(len(lista1)):
#         nowa.append(lista1[x]+lista2[x])
#     print(nowa)
#
# lista1 = [2,3,-1,5]
# lista2 = [1,1,1,10]
# listy(lista1,lista2)



#zad3
with open('zadanie1.txt','r',encoding='UTF-8') as plik:
    plik.seek(100)
    znaki = plik.read(35)

print(znaki)
ilosc_duzych_liter = 0
duze_litery = ''

for znak in znaki:
    if znak.isupper():
        ilosc_duzych_liter += 1
        duze_litery += znak

if ilosc_duzych_liter == 0:
    print('W wybranym fragmencie tekstu nie ma żadnych dużych liter.')
else:
    print(f'Duże litery w wybranym fragmencie tekstu ({ilosc_duzych_liter}): {duze_litery}')

#caly tekst
# with open('zadanie1.txt','r',encoding='utf8') as plik:
#     for x in plik:
#
#         tekst = plik.read()
#
# print(tekst)

#zad4
# lista = [1,2,3,4]
# a = 2
# nowa = [x for x in lista if a<x]
# print(nowa)


#zad 5
# matematyczne =(math.exp(3)+math.cos(39)**2)**(1/5) + (2/7)**3 + math.pi
# print(str(round(matematyczne, 2)))



#Egzamin B
#zad1

# with open('tekst.txt','r',encoding='utf-8') as plik:
#     plik.seek(71)
#     znaki2 = plik.read(40)
#
# print(znaki2)
# ilosc_litery_A = znaki2.count('A')
# if ilosc_litery_A ==0:
#     print('Nie ma litery A')
# else:
#     print(f'Litera A wystepuje {ilosc_litery_A} razy')


#zad2
# lista = [2,3,4.0,5.34,3,3.3,3.33]
#
#
# nowa = [x for x in lista if isinstance(x, float)]
# print(lista)
# print(nowa)


#zad3

# def funkcja(lista):
#     for x in range(len(lista)):
#         zmienna =lista[0]+lista[x]
#         lista.append(zmienna)
#     return lista
#     print(lista)
# lista = [1,3.5,4,-1,2,0,3.33]
# print(funkcja(lista))



#zad4

# wynik = math.sin(56)**2 + ((4**2)/25 + math.log(85, 3))**(1/4)
# print(wynik)
# wynik = round(wynik,2)
# print(wynik)

#zad5
# Napisz skrypt, który od
# użytkownika z konsoli pobiera dwie
# liczby całkowite n. Program ma za z
# adanie zrobić sumę liczb od 1 do n,
# łącznie z n. Dokonaj zapisu wyniku do
# pliku o nazwie zadanie5.txt. W skrypcie
# dokonaj sprawdzenia błędów związanych z
# wczytywanymi wartościami, do tego celu
# użyj składni try-except.

try:
    suma =0
    n = int(input('Podaj liczbe calkowita'))
    for x in range(1,n+1):
        suma += x
    print(suma)
    with open('zadanie5.txt','w+',encoding='utf8') as plik:
        plik.write(str(suma))
except Exception as e:
    print("Nie poprawne dane wejsciowe")












#dla list o roznej dlugosci
# def sum_lists(lista1, lista2):
#     nowa = []
#     max_len = max(len(lista1), len(lista2))
#     for i in range(max_len):
#         elem1 = lista1[i] if i < len(lista1) else 0
#         elem2 = lista2[i] if i < len(lista2) else 0
#         nowa.append(elem1 + elem2)
#     return nowa
#
# lista1 = [2, 3, -1, 5]
# lista2 = [1, 1, 1, 10]
# wynik = sum_lists(lista1, lista2)
# print(wynik)
#




