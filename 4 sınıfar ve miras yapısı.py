# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 17:45:48 2024

@author: ASAF
"""

class Animal:
    """
    Hayvan sınıfı, hayvan nesneleri oluşturur.
    """
    def __init__(self):
        """
        Hayvan sınıfının yapıcı (constructor) metodu. 
        
        Args:
            self: Sınıfın kendisi.
        """
        print("Animal is created")
        
    def tostring(self):
        """
        Hayvanın dize temsili.
        """
        print("animal")
        
    def walk(self):
        """
        Hayvanın yürüme yeteneği.
        """
        print("Animal can walk")
        
    
class Monkey(Animal):
    """
    Maymun sınıfı, hayvan sınıfından türetilir.
    """
    def __init__(self):
        """
        Maymun sınıfının yapıcı (constructor) metodu. 
        
        Args:
            self: Sınıfın kendisi.
        """
        super().__init__()
        print("Monkey is created")
        
    def tostring(self):
        """
        Maymunun dize temsili.
        """
        print("monkey")
        
    def climb(self):
        """
        Maymunun tırmanma yeteneği.
        """
        print("Monkey can climb")
        
        

class Bird(Animal):
    """
    Kuş sınıfı, hayvan sınıfından türetilir.
    """
    def __init__(self):
        """
        Kuş sınıfının yapıcı (constructor) metodu. 
        
        Args:
            self: Sınıfın kendisi.
        """
        super().__init__()
        print("Bird is created")
        
    def tostring(self):
        """
        Kuşun dize temsili.
        """
        print("Bird")
            
    def fly(self):
        """
        Kuşun uçma yeteneği.
        """
        print("Fly")
        
        
m1 = Monkey()   # Maymun nesnesi oluşturuluyor.
m1.walk()       # Maymunun yürüme yeteneği çağrılıyor.
print("------")

b1 = Bird()     # Kuş nesnesi oluşturuluyor.
b1.tostring()   # Kuşun dize temsili çağrılıyor.

