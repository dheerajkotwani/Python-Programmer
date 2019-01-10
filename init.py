class Computer:
    def __init__(self,ram,cpu):
     print("in __init__")
     self.ram=ram
     self.cpu=cpu

    def config(self):
     print("Config is ",self.ram ,self.cpu)

com1=Computer('i5',16)
com2=Computer('i7',32)

com1.config()
com2.config()
