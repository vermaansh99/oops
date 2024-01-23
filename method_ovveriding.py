class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def speak(self):
        print("I can speak")



class Admin(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def speak(self):
        print("Hello I am an admin and I can also type.")


p = Person("Sumit",27)

a = Admin("Ansh",24)


p.speak()
a.speak()


    

