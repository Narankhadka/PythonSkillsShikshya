from abc import ABC , abstractmethod

class demo(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        
    @abstractmethod  
    def method2(self):
        print("concreate method")


class ConcreateClass(demo):
    def method2(self):
        return super().method2()
    

obj=ConcreateClass()
# obj.method1()
obj.method2()