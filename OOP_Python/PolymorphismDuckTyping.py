class Duck:
    def sound(self):
        return "Quack ,quack !"
    


class AnotherBird:
    def sound(self):
        return "I am similar to Duck"
    


def makeSound(duck):
    print(duck.sound())


#creating instances 
duck =Duck()
anotherbird=AnotherBird()

makeSound(duck)
makeSound(anotherbird)
    