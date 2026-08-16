class family:
    def __init__(self, eyecolour, height_cm):
        self.eyecolour = eyecolour
        self.height_cm = height_cm
    def show_triats(self):
        print("Eye colour: ", self.eyecolour)
        print("Height in cm: ", self.height_cm)
class kid (family):
    def __init__(self,name,age,eyecolour,height_cm):
        family.__init__(self,eyecolour,height_cm)
        self.name = name
        self.age = age
        super().show_triats()
    def favourite_hobby(self, hobby):
        print("My favourite hobby is playing ", hobby)
    def show_triats(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        super().show_triats()
Child = kid("Steve", 17, "blue",190)
Child.favourite_hobby("football")
Child.show_triats()
print("Is kid a subclass of family? ", issubclass(kid, family))
