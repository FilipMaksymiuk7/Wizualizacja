import math
import string
#zad1
wynik = math.exp(10)
print(wynik)

wynik2 = (math.log(5+math.sin(8)**2))**(1/6)
wynik3 = pow(math.log(5 + pow(math.sin(8),2)),(1/6))
print(wynik2)
print(wynik3)

wynik4 = math.floor(3.55)
wynik5= math.ceil(4.80)
print(wynik4)
print(wynik5)
#zad2
imie = 'FILIP'
nazwisko = 'MAKSYMIUK'
razem = imie.capitalize() +" "+ nazwisko.capitalize()
print(razem)

#zad3

piosenka = 'la la la spiewam lalala'
print("ile razy slowo la:",piosenka.count('la'))
#zad4
ostatnia = len(imie)-1
print(imie[1],imie[ostatnia])


#zad6

aa,bb,cc = 'taki',2.05,0xFF
print('string:{0:s}, float:{1:f}, szesnastkowy: {2:d}'.format(aa,bb,cc))
zmienna='string:{0:s}, float:{1:f}, szesnastkowy: {2:d}'
#zad5

print(zmienna.split(","))
#text = "ty,ja,my"
#print(text.split(","))

#zad7
lista = ['tenis','siatkowka','pilka reczna']
print(lista)
lista.reverse()
print(lista)
lista.extend(['pilka nozna','koszykowka'])
print(lista)

#zad8
slownik = {'pt':'piatek','pn':'poniedzialek','wt':'wtorek'}
#print(slownik)
#print(slownik.keys())
#print(slownik.values())
print(slownik.items())

#zad9
slownikgry={'Riot Games':'LOL','Valve':'CS GO','Blizzard':'WOW'}
print(slownikgry)
print(len(slownikgry))
#zad10
usertext = input("Podaj losowy text: ")
ilea = usertext.count('a')
print(ilea)

#zad11
print("podaj 3 liczby calkowite: ")
a= int(input("pierwsza: "))
b= int(input("druga: "))
c= int(input("trzecia: "))
if a>=b and a>=c:
    print("Najwieksza liczba z podanych to: ",a)
elif b>=a and b>=c:
    print("Najwieksza liczba z podanych to: ", b)
elif c>=a and c>=b:
    print("Najwieksza liczba z podanych to: ", c)
else:
    print("wystapil blad")

#zad12
listasquare = [2,3,5.5,8.0,1.5,1]
nowa = []
for x in listasquare:
    x = x**2
    nowa.append(x)
listasquare = nowa
print(listasquare)


#zad13
i=0
parzyste = []
while(i<10):
    a = int(input("podaj liczbe"))
    if a%2==0:
        parzyste.append(a)
    i+=1
print(parzyste)

