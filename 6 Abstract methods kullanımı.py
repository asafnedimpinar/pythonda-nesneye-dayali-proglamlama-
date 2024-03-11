# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:24:43 2024

@author: ASAF
"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Animal (Hayvan) sınıfı, soyut bir sınıftır ve temel olarak hayvanların davranışlarını tanımlar.
    """
    @abstractmethod
    def walk(self): 
        """
        Yürüme davranışını soyut metot olarak tanımlar.
        """
        pass

    @abstractmethod
    def run(self): 
        """
        Koşma davranışını soyut metot olarak tanımlar.
        """
        pass

class Bird(Animal):
    """
    Bird (Kuş) sınıfı, Animal sınıfından türetilmiş bir alt sınıftır ve kuşların davranışlarını tanımlar.
    """
    def __init__(self):
        """
        Kuş sınıfının yapıcı metodu. 
        """
        print("bird")

    def walk(self):
        """
        Yürüme metodu. Kuşun yürüme davranışını tanımlar.
        """
        print("walk")

    def run(self):
        """
        Koşma metodu. Kuşun koşma davranışını tanımlar.
        """
        pass

b1 = Bird()




