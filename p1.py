    
class developer:
    print("this code is from developer section.")

class employee:
    company_name = "ITC"
    name="ram"
    print("this code is from employee section.")

class tester(developer,employee):
    n= "value"
    print(f"value is {n}")
    print("this code is from tester section")


r=tester()
print(f"company name is {r.company_name}\nemployee name is {r.name}")


