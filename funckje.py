import random
import math
#zad1
A = [1-x for x in range(1,11)]
print(A)
B=[4**x for x in range (0,8) ]
print(B)
C=[x for x in B if x%2==0]
print(C)

#zad2
lista1 =[random.randint(1,100) for x in range(10)]
nowa = [x for x in lista1 if x%2==0]
print(lista1)
print(nowa)
#
# lista12 =[]
# for x in range(10):
#     lista12.append(random.randint(0, 100))
# print(lista12)
#
# nowalista = [x for x in lista12 if x%2==0]
# print(nowalista)


#zad3

produkty = {'jajka':'sztuki','marchew':'sztuki','ziemniaki':'kg'}
nowa2 = [x for x in produkty.keys() if produkty[x]=='sztuki']
print(nowa2)

# diary = {'ziemniaki':'kg', 'jajka':'szt', 'banany':'kg'}
# nowalista3 = [j for j,i in diary.items() if i == 'szt']
# print(nowalista3)


#zad4
def trojkat(x,y,z):
    if x<=0 or y<=0 or z<=0:
        print('podane wartosci byly nieprawidlowe')
    elif(x**2 + y**2 == z**2 or z**2 + y**2 == x**2 or x**2 + z**2 == y**2):
        print('Jest to trojkat prostokatny')
    else:
        print('Nie jest to trojkat prostokatny')


trojkat(4,3,5)

#zad5

def trapez(a=1,b=1,h=1):
    if a<=0 or b<=0 or h<=0:
        print('Podane wartosci byly nieprawidlowe')
    elif a + b <= h or b + h <= a or a + h <= b:
        print('Nie można utworzyć trapezu z podanymi wartościami')
    else:
        print((a+b)*h/2)


trapez(2,1,2)

#zad6
def ciag(a=1,b=4,ile=10):
    iloczyn = a
    for x in range(ile-1):
        a *= b
        iloczyn *= a
    print(iloczyn)




#zad7
def ciag2(*tak):

    if tak==0 or tak ==1 or tak==2 or len(tak)>3:
        return 0
    else:
        a = tak[0]
        b = tak[1]
        c = tak[2]
        for x in range(c-1):
            a *= b

        return print(a)


ciag2(1,4,10)

#zad8
# def hard(**rzeczy):
#     for cos in rzeczy:
#         print('to jest')
#         print(cos)
#         print('co lubie')
#         print(rzeczy[cos])
#
#
# hard(slodycze='czekolada',rozrywka=['gry','filmy'])


# def zakupy(**rzeczy):
#     suma: float =0
#     produkty = []
#     for i in rzeczy:
#         suma +=rzeczy[i]
#         produkty.append(i)
#     return suma,len(produkty)
#
# print(zakupy(mleko=5,kasz=2,maslo=8))


# def oblicz_koszt(*zakupy):
#     ilosc = 0
#     suma = 0
#     for produkt in zakupy:
#         ilosc += produkt[1]
#         suma += produkt[1] * produkt[2]
#     return ilosc, suma


# zakupy = [
#     ['mleko', 2, 2.5],
#     ['chleb', 1, 3.0],
#     ['masło', 1, 5.0],
#     ['jajka', 12, 0.5]
# ]
#
# ilosc, suma = oblicz_koszt(*zakupy)
# print(f'Ilość produktów: {ilosc}, całkowity koszt: {suma} zł')
#


def zakupy(**rzeczy):
    a=len(rzeczy)
    b = sum(rzeczy.values())
    return a,b

rzeczy={'jajka':2.5,'maslo':3.2,'kajzerka':2}
ilosc,koszt = zakupy(**rzeczy)
print("ilosc produktow:",ilosc,"koszt:",koszt)

#zad9

def pierwiastek(a):
    try:
        math.sqrt(a)
    except ValueError:
        print("Liczba ujemna")
    else:
        print(math.sqrt(a))

pierwiastek(-6)


