class cars:
    wheels=4

    def __init__(self):
        self.mil=10
        self.comp="BMW"

c1=cars()
c2=cars()

c1.mil=5
print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)
