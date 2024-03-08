# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:32:05 2024

@author: ASAF
"""



# %% Değişkenler
integer1 = 33
string1 = " aalss"

# %% Sınıflar (Classes)
# Bir çalışan sınıfı tanımlanıyor.
class Employe():
    pass

# Bir çalışan nesnesi oluşturuluyor.
employee1 = Employe()

# %% Öznitelikler (Attributes)
# Bir futbolcu sınıfı tanımlanıyor.
class Footballer:
    football_club = "Barcelona"
    age = 30

# Bir futbolcu nesnesi oluşturuluyor.
f1 = Footballer()

# Nesne özniteliklerine erişiliyor ve değiştiriliyor.
print(f1.football_club)  # Varsayılan kulüp değeri
f1.football_club = "Real Madrid"
print(f1.football_club)  # Değiştirilen kulüp değeri

# %% Metodlar (Methods)
# Kare sınıfı tanımlanıyor.
class Square:
    edge = 5
    area = 0

    # Alan hesaplama metodu
    def area1(self):
        self.area = self.edge * self.edge
        print("Alan:", self.area)

# Kare nesnesi oluşturuluyor.
s1 = Square()

# Kare özniteliğine ve metodu çağrılıyor.
print(s1.edge)  # Kenar uzunluğu
s1.area1()      # Alan hesaplama metodu çağrılıyor

# Kare özniteliği değiştiriliyor ve alan tekrar hesaplanıyor.
s1.edge = 9
s1.area1()

# %% Metodlar ve Fonksiyonlar (Methods vs Functions)
# Çalışan sınıfı tanımlanıyor.
class Emp:
    age = 25
    salary = 2000

    # Yaş-maaş oranı hesaplama metodu
    def agesalaryratio(self):
        a = self.salary / self.age
        print("Metod:", a)

# Çalışan nesnesi oluşturuluyor ve metodu çağrılıyor.
e1 = Emp()
e1.agesalaryratio()

# Fonksiyon: Yaş-maaş oranı hesaplanıyor.
def agesalaryratio(salary, age):
    a = salary / age
    print("Fonksiyon:", a)

# Fonksiyon çağrılıyor.
agesalaryratio(3000, 30)

# Kare alanı hesaplama fonksiyonu
def findarea(a, b):  # a = pi, b = çap
    area = a * b**2
    print(area)
    return area

# Fonksiyon çağrılıyor ve sonuçlar toplanıyor.
pi = 3.147
r = 7
result1 = findarea(pi, r)
result2 = findarea(pi, 13)
print(result1 + result2)

# %% Yapıcı (Constructor)
# Hayvan sınıfı tanımlanıyor.
class Animal:
    def __init__(self, a, b):  # name, age = a, b
        self.name = a
        self.age = b

    # Yaş bilgisini döndüren metot
    def getAge(self):
        return self.age

    # İsim bilgisini yazdıran metot
    def getName(self):
        print(self.name)

# Hayvan nesneleri oluşturuluyor.
a1 = Animal("Köpek", 2)
a2 = Animal("Kedi", 4)
a3 = Animal("Kuş", 1)
