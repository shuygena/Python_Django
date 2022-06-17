class HotBeverage:
    name = "hot beverage"
    price = 0.30

    def description(self):
        return("Just some hot water in a cup.")

    def __str__(self):
        return("""name : {}
price : {}
description : {}""".format(self.name, self.price, self.description()))
    
class Tea(HotBeverage):
    name = "tea"
    
class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40
    def description(self):
        return("A coffee, to stay awake.")

class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.5
    def description(self):
        return("Chocolate, sweet chocolate...")        
    
class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45
    def description(self):
        return("Un po’ di Italia nella sua tazza!")

def test():
    hb = HotBeverage()
    tea = Tea()
    coffee = Coffee()
    chocolate = Chocolate()
    cappuccino = Cappuccino()
    print(hb)
    print(tea)
    print(coffee)
    print(chocolate)
    print(cappuccino)

test()