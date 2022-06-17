import random
import beverages

class CoffeeMachine:
    
    def __init__(self):
        self.check_counter = 0

    class EmptyCup(beverages.HotBeverage):
        name = "empty cup"
        price = 0.90
        def description(self):
            return("An empty cup?! Gimme my money back!")
    
    def repair(self):
        self.check_counter = 0
    
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__( "This coffee machine has to be repaired.")

    def serve(self, bevarage):
        if self.check_counter >= 10:
            raise self.BrokenMachineException()
        self.check_counter += 1
        if random.randrange(2) == 0:
            return self.EmptyCup()
        else:
            return bevarage

def work_machine(machine):
    bevs = [beverages.HotBeverage(), beverages.Tea(), beverages.Coffee(), beverages.Cappuccino(), beverages.Chocolate()]
    for i in range(15):
        try:
            print(machine.serve(bevs[random.randrange(5)]))
        except Exception as ex:
            print(ex)

def test():
    machine = CoffeeMachine()
    work_machine(machine)
    machine.repair()
    work_machine(machine)
    machine.repair()

test()


    
        
