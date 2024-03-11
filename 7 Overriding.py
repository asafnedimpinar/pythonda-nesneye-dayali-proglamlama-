# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:53:37 2024

@author: ASAF
"""
# bu kod ıkı fonksıyon bırden aynı metodu cagırınca hangısıne gıdecegını gostermek ıcın yazılmıstır
class Animal:
    """
    Animal sınıfı, temel olarak bir hayvanı temsil eder.
    """
    def tostring(self):
        """
        Hayvanın dize temsilini oluşturan metod.
        """
        print("animal")
     
class Monkey(Animal):
    """
    Monkey sınıfı, Animal sınıfından türetilmiş bir alt sınıftır ve bir maymunu temsil eder.
    """
    def tostring(self):
        """
        Maymunun dize temsilini oluşturan metod.
        """
        print("monkey")
        

a1 = Animal()  # Hayvan nesnesi oluşturulur
a1.tostring()  # tostring metodu çağrılarak "animal" yazdırılır

m1 = Monkey()  # Maymun nesnesi oluşturulur
m1.tostring()  # tostring metodu çağrılarak "monkey" yazdırılır