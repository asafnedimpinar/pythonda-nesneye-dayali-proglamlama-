"""
Created on Sun Mar 10 14:16:01 2024

@author: ASAF
"""

# cok sekıllılık 
# aynı metodu bırden fazla kez kullandıgımız durumlar ıcın

class Employee:
    """
    Employee sınıfı, çalışanları temsil eder.
    """
    def raisee(self):         
        """
        Çalışanın maaş artışını hesaplayan metod.
        """
        raise_rate = 0.1
        result = 100 + 100 * raise_rate 
        print("employee:", result)
         
class Ceng(Employee):
    """
    Ceng sınıfı, Employee sınıfından türetilmiş bir alt sınıftır ve bilgisayar mühendislerini temsil eder.
    """
    def raisee(self):
        """
        Bilgisayar mühendisinin maaş artışını hesaplayan metod.
        """
        raise_rate = 0.2
        result = 100 + 100 * raise_rate 
        print("ceng:", result)
        
class Eee(Employee):
    """
    Eee sınıfı, Employee sınıfından türetilmiş bir alt sınıftır ve elektrik-elektronik mühendislerini temsil eder.
    """
    def raisee(self):
        """
        Elektrik-elektronik mühendisinin maaş artışını hesaplayan metod.
        """
        raise_rate = 0.3
        result = 100 + 100 * raise_rate 
        print("eee:", result) 

# Nesne oluşturma
e1 = Employee()
ce = Ceng()
ee = Eee()

# Çalışanlar listesi
employee_list = [ce, ee]

# Her bir çalışanın maaş artışını hesaplama ve yazdırma
for employee in employee_list:
    employee.raisee()
        
     
        
     
        
     
        
     
        
