class Dog:
    def __init__(self,breed,age,color):
        self.breed = breed
        self.age = age
        self.color = color
    def say_age(self):
        words_to_say = 'i am ' + str(self.age) + " years old"
        print(words_to_say)
    def bark(self):
        print("woof! woof!")
    def sleep(self):
        print("zzz")
    def eat(self):
        print("nom nom nom!")
dog = Dog('bhutanses',20,'black')
petdog = Dog('pug',10,'white')
dog.sleep()
dog.eat()
dog.bark()

dog.say_age()
petdog.say_age()

