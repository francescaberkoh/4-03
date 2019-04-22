'''
Created on Apr 22, 2019

@author: Francesca
'''

def print_address(street, city="", province="", pcode="", aprt=""):
    if aprt == "":
        print(str(street) + " " + str(city) + " " + str(province) + " " + str (pcode) +" ")
    else:
        print (str(street) + " " + str(city) + " " + str(province) + " " + str (pcode) +" " + str(aprt))
    


street_address= input("Enter your Street Address:" )
city_name = input("Enter your city name:")
province_name = input("Enter your province name:")
postal_code = input("Enter your postal code:")
apartment_choice = input("Do you want your apartment number? (yes/no):")
if apartment_choice == "yes":
    apartment_num = input("Enter you number:")
    print_address(street_address, city_name, province_name, postal_code, apartment_num)
if apartment_choice == "no":
    print_address(street_address, city= city_name, province= province_name, pcode= postal_code)
    
