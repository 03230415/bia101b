#!task
# build on top of the code provided
# create a new behaviour in the class
#? behaviour name : 'introduction'

#! expected outcome:
# dog.introduce()

class introduction:
    def __init__(self,breed,age,color):
        print("hii")
        self.breed = breed
        self.age = age
        self.color = color
    def introduce(self):
        print('hii')
        print("i am a "+ self.breed + "dog")
        print('i am ' + str(self.age) + " years old")
    def say_age(self):
        words_to_say = 'i am ' + str(self.age) + " years old"
        print(words_to_say)
    def my_breed(self):
        i_am =  'i am ' + str(self.breed) + " dog"
        print(i_am)
dog = introduction('bhutanese', 20, 'black')
dog.say_age()
dog.my_breed()




