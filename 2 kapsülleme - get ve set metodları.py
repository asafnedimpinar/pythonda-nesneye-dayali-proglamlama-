# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:42:28 2024

@author: ASAF
"""
# kapsulleme 
class BankAccount1(object):
    """
    Banka hesabı sınıfı, müşteri adı, bakiyesi ve soyadı ile banka hesabı nesneleri oluşturur.
    
    Attributes:
        name (str): Müşteri adı.
        money (float): Hesap bakiyesi.
        surname (str): Müşteri soyadı.
    """
    def __init__(self, name, money, surname):
        """
        BankAccount sınıfının yapıcı (constructor) metodu. 
        
        Args:
            name (str): Müşteri adı.
            money (float): Hesap bakiyesi.
            surname (str): Müşteri soyadı.
        """
        self.name = name
        self.money = money
        self.surname = surname
        
# Banka hesabı nesneleri oluşturuluyor.
p1 = BankAccount1("hasan", 3000, "kara")
p2 = BankAccount1("ahmet", 2000, "yıldız")

# Hesap bakiyeleri birbirine ekleniyor ve birinci müşterinin bakiyesi sıfırlanıyor.
p2.money = p2.money + p1.money 
p1.money = 0




#%% 


class BankAccount2(object):
    """
    Banka hesabı sınıfı, müşteri adı, bakiyesi ve soyadı ile banka hesabı nesneleri oluşturur.
    
    Attributes:
        name2 (str): Müşteri adı.
        __money2 (float): Hesap bakiyesi (gizli).
        surname2 (str): Müşteri soyadı.
    """
    def __init__(self, name2, money2, surname2):
        """
        BankAccount2 sınıfının yapıcı (constructor) metodu. 
        
        Args:
            name2 (str): Müşteri adı.
            money2 (float): Hesap bakiyesi.
            surname2 (str): Müşteri soyadı.
        """
        self.name2 = name2
        self.__money2 = money2  # Bakiye, özel (private) bir değişken olarak tanımlanır.
        self.surname2 = surname2
        
    def getMoney2(self):      
        """Mevcut bakiyeyi döndüren metod."""
        return self.__money2
        
    def setMoney2(self, amount):       
        """Yeni bakiye atayan metod."""
        self.__money2 = amount
       
# Banka hesabı nesneleri oluşturuluyor.
p3 = BankAccount2("yusuf", 3200, "pınar")
p4 = BankAccount2("hazal", 4500, "dere")

# Bakiye bilgisi get ve set metotları aracılığıyla erişilir ve değiştirilir.
print("get methods :", p3.getMoney2())
p3.setMoney2(12000)
print("after set methods :", p3.getMoney2())



