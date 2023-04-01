


#zad1
plik = open('tekst.txt','w')
for x in range(0,31):
    a = x*2
    plik.writelines(str(a))
    plik.write("\n")

plik.close()
#zad2
plik = open('tekst.txt','r')

# ileznakow = plik.read(10)
# print(ileznakow)
# linia = plik.readline()
# print(linia)
wiersze = plik.readlines()
print(wiersze)
plik.close()

with open('tekst.txt','r') as plik:
    for linia in plik:
        print(linia,end="")


#zad3
tekst = 'tekst po literce'
with open('tekst.txt','w+') as plik:
     for x in tekst:
         plik.writelines(x)

# plik = open('tekst.txt','w')
# for x in tekst:
#     plik.writelines(str(x))
#     plik.write(",")

with open('tekst.txt','r') as plik:
    for b in plik:
        print(b,end="")

#zad4

class NaZakupy:
    def __init__(self,nazwa,ilosc,miara,cena):
        self.nazwa_produktu = nazwa
        self.ilosc = ilosc
        self.jednostka_miary = miara
        self.cena_jed = cena
    def wyswietl_produkt(self):
        print(f"nazwa produktu: {self.nazwa_produktu}")
        print(f"cena produktu: {self.cena_jed}")
    def ile_produktu(self):
        print(str(self.ilosc) + " " + self.jednostka_miary)
    def ile_kosztuje(self):
        print(self.ilosc * self.cena_jed)

klasa = NaZakupy('marchew',3,'szt',1.50)
print("...\n")

klasa.wyswietl_produkt()
klasa.ile_produktu()
klasa.ile_kosztuje()

print("przerwa\n")
# print(klasa.nazwa_produktu)
# print(klasa.ilosc)
# print(klasa.jednostka_miary)
# print(klasa.cena_jed)

#zad5

class ciagi:
    def __init__(self,wartosc_poczatowa,roznica,ile):
        self.a = wartosc_poczatowa
        self.r = roznica
        self.n = ile
    def pobierz_elementy(self):
        self.a = int(input("Podaj pierwszy wyraz ciągu: "))
        self.r = int(input("Podaj różnicę ciągu: "))
        self.n = int(input("Podaj długość ciągu: "))
        self.elementy = []
        for i in range(self.n):
            self.elementy.append(self.a + i*self.r)
        print(self.elementy)

    def pobierz_parametry(self):
        self.a = int(input("Podaj wyraz poczatkowy: "))
        self.r = int(input("Podaj roznice ciagu: "))
        self.n = int(input("Podaj ile wyrazow ciagu: "))

    def wyswietl_dane(self):
        pomocnicza = self.a
        for x in range(self.n):
            print(pomocnicza)
            pomocnicza += self.r

    # def wyswietl_elementy(self):
    #     duzo = 0
    #     a = self.ile
    #     while (a > 0):
    #         print(self.a)
    #         self.a += self.r
    #         a -= 1


    def policz_sume(self):
        pomocnicza = self.a
        suma2 = 0
        for x in range(self.n):
            suma2 = suma2+pomocnicza
            pomocnicza += self.r
        print(suma2)


    def policz_elementy(self):
        ile = 0
        while ile < self.n and self.a < self.a + (self.n - 1) * self.r:
            ile += 1
            self.a += self.r
        print("Liczba elementów: ", ile)

 # def policz_elementy(self):
 #        duzo = 0
 #        a= self.ile
 #        while(a>0):
 #            duzo += 1
 #            a-=1
 #        print(duzo)
#wyswietla,parametry,suma
klasa2 = ciagi(0,0,0)
klasa2.wyswietl_dane()
print("Parametry")
klasa2.pobierz_parametry()
print("wyswietl")
klasa2.wyswietl_dane()
print("suma")
klasa2.policz_sume()
print("wyswietl")
klasa2.wyswietl_dane()
print("ele piob")
klasa2.pobierz_elementy()
print("wyswietl")
klasa2.wyswietl_dane()
print("elementow")
klasa2.policz_elementy()
print("wyswietl")
klasa2.wyswietl_dane()

#zad6

class Robaczek:
    def __init__(self,x=0,y=0,krok=1):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self,ile_krokow):
         self.y += ile_krokow*self.krok
    def idz_w_dol(self,ile_krokow):
        self.y -= ile_krokow * self.krok
    def idz_w_prawo(self,ile_krokow):
        self.x += ile_krokow * self.krok
    def idz_w_lewo(self,ile_krokow):
        self.x -= ile_krokow * self.krok
    def pokaz_gdzie_jestes(self):
        pion = self.y
        poziom = self.x
        print("y=",self.y,'x=',self.x)

ty =Robaczek(0,0,2)
ty.idz_w_dol(3)
ty.idz_w_gore(2)
ty.idz_w_prawo(12)
ty.idz_w_lewo(6)
ty.pokaz_gdzie_jestes()
