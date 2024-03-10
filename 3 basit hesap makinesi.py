# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:32:38 2024

@author: ASAF
"""

class Calc(object):
    "Hesap makinesi sınıfı"
    def __init__(self, a, b):
        # İki değeri alarak sınıfı başlatır
        self.value1 = a
        self.value2 = b
    
    # Toplama işlemi metodu
    def add(self):
        return self.value1 + self.value2
    
    # Çarpma işlemi metodu
    def multiply(self):
        return self.value1 * self.value2 
    
    # Bölme işlemi metodu
    def divide(self):
        return self.value1 / self.value2

# Kullanıcıya işlem seçimi yaptırılır
print("choose add(1) , multiply(2), divide (3) ")
selection = input('selection 1 or 2 or 3 ')

# İki değer kullanıcıdan alınır
v1 = int(input("first value"))
v2 = int(input("second value"))

# Hesap makinesi sınıfı oluşturulur
c1 = Calc(v1, v2)

# Kullanıcının seçimine göre ilgili işlem yapılır ve sonuç yazdırılır
if selection == "1":
    add_result = c1.add()
    print("add : {} ".format(add_result))
    
elif selection == "2":
    multiply_result = c1.multiply()
    print("multiply {} ".format(multiply_result))
      
elif selection == "3":
    divide_result = c1.divide()
    print(" divide : {}".format(divide_result))
      
else:
    print("error  there is no proper selection") 








        