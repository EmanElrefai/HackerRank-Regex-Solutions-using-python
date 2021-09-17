import re

for _ in range(int(input(""))):
    phone_number=re.split("-|\s",input(""))
    print("CountryCode="+phone_number[0]+",LocalAreaCode="+phone_number[1]+",Number="+phone_number[2])
    
