# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:48:50 2024

@author: ASAF
"""

class Website:
    """
    Website sınıfı, bir web sitesini temsil eder.
    """
    def __init__(self, name, surname):
        """
        Website sınıfının yapıcı (constructor) metodu. 
        
        Args:
            name (str): Web sitesinin adı.
            surname (str): Web sitesinin soyadı.
        """
        self.name = name
        self.surname = surname
        
        
    def login(self):
        """
        Giriş bilgisi metodu. Web sitesinin adı ve soyadını yazdırır.
        """
        print(self.name  + "  " + self.surname)
            
class Website1(Website):
    """
    Website1 sınıfı, Website sınıfından türetilir.
    """
    def __init__(self, name, surname, ids):
        """
        Website1 sınıfının yapıcı (constructor) metodu. 
        
        Args:
            name (str): Web sitesinin adı.
            surname (str): Web sitesinin soyadı.
            ids (str): Kullanıcı kimliği.
        """
        Website.__init__(self, name, surname)
        self.ids = ids
        
    def login(self):
        """
        Giriş metodu. Web sitesinin adı, soyadı ve kullanıcı kimliğini yazdırır.
        """
        print(self.name + "  " + self.surname + "  " + self.ids)
            
            
class Website2(Website):
    """
    Website2 sınıfı, Website sınıfından türetilir.
    """
    def __init__(self, name, surname, email):
        """
        Website2 sınıfının yapıcı (constructor) metodu. 
        
        Args:
            name (str): Web sitesinin adı.
            surname (str): Web sitesinin soyadı.
            email (str): Kullanıcının e-posta adresi.
        """
        Website.__init__(self, name, surname)
        self.email = email 
        
    def login(self):
        """
        Giriş metodu. Web sitesinin adı, soyadı ve e-posta adresini yazdırır.
        """
        print(self.name + "  "+ self.surname + "  " + self.email)
        
        
w0 = Website("name", "surname")       
w1 = Website1("name", "surname", "ids")        
w2 = Website2("name","surname", "email")










            
