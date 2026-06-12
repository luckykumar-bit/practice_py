class employee:
    # name= "lucky"
    language= "py"
    income= 330000
    
    def  getinfo(self):
     print(f"the language is {self.language}. the income is {self.income}")

    def greet(self):
     print("good morning") 
     
lucky = employee()
# lucky.name="lucky"
# lucky.language="js"
# print(lucky.income,lucky.language,lucky.name)   
lucky.greet()
lucky.getinfo()
 
    # here name is object attribute and salary and language are
    # class attribute as they directly belong to the class

# constructor
class employee:
    language= "py"
    income= 330000
    
    def __init__(self,name,language,income):
        # automatically called
        self.name=name
        self.language= language
        self.income=income
        print("creating an object")
    def  getinfo(self):
     print(f"the language is {self.language}. the income is {self.income}")

    def greet(self):
     print("good morning")
 
lucky=employee("lucky","js",44444444)
# lucky.greet()
lucky.getinfo()
print(lucky.name,lucky.language,lucky.income)