class Intern:
        
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return(self.Name)
    
    class Coffee:
        def __str__(self):
            return("This is the worst coffee you ever tasted.")
    
    def make_coffee(self):
        return(self.Coffee())
    
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    
def test():
    anonymous = Intern()
    mark = Intern("Mark")
    print(anonymous)
    print(mark)
    print(mark.make_coffee())
    try:
        anonymous.work()
    except Exception as ex:
        print(ex)

test()