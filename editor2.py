class pyCharm:

    def editor(self):
        print("For pyCharm")
        print("Compile")
        print("Run")

class MyEditor:

    def editor(self):
        print("For MyEditor")
        print("Spell Check")
        print("Errors")
        print("Compile")
        print("Run")

class Laptop:

    def code(self,ide):
        ide.editor()


ide=MyEditor()

lap1=Laptop()
lap1.code(ide)
