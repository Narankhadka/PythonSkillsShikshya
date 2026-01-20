class Employee:
    empCount=0

    def __init__(self ,name,age):
        self.name=name
        self.age=age
        Employee.empCount+=1


        @classmethod
        def showcount(cls):
            print(cls.empCount)


        
        @classmethod
        def newEmployee(cls, name, age):
            return cls(name,age)
        



e1= Employee("Naran khadka",22)
e1= Employee("Raj khadka",23)
e1= Employee("John",29)
e1= Employee("sarthak",12)


