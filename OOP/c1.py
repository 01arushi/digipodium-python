class Cat:
    breed = None 
    gender = None
    fur_color= None 
    age= None
    height =None
    weight = None
    is_tamed=None

    def eat(self, food='catfood'):
        print(f'🐈 is eating {food}')

    def play(self):
        print('🐈 is playing')

    def sleep(self)        :
        print('🐈 is sleeping')

billu = Cat()  # constructor calling
# print(billu, type(billu)) 
tom = Cat()   
pusy = Cat()
billu.breed ='persian'
billu.weight=2
billu.age=2
billu.fur_color='white' 
billu.height=1
billu.is_tamed=True
billu.gender='M'

tom.breed ='street cat'
tom.weight=1.5
tom.age=100
tom.fur_color='grey' 
tom.height=1.1
tom.is_tamed=True
tom.gender='M'

pusy.breed ='wild cat'
pusy.weight=2.5
pusy.age=6
pusy.fur_color='black' 
pusy.height=3
pusy.is_tamed=False
pusy.gender='F'

print('Billu Details')
print('breed:',billu.breed)
print('gender:',billu.gender)
print('age:',billu.age)
print('weight:',billu.weight)
print('height:',billu.height)
print('color:',billu.fur_color)
print('pet:','yes' if billu.is_tamed else 'no')
billu.eat()
billu.sleep()
billu.play()

print('Tom Details')
print('breed:',tom.breed)
print('gender:',tom.gender)
print('age:',tom.age)
print('weight:',tom.weight)
print('height:',tom.height)
print('color:',tom.fur_color)
print('pet:','yes' if tom.is_tamed else 'no')
tom.sleep()
tom.play()
tom.sleep()

print('pusy Details')
print('breed:',pusy.breed)
print('gender:',pusy.gender)
print('age:',pusy.age)
print('weight:',pusy.weight)
print('height:',pusy.height)
print('color:',pusy.fur_color)
print('pet:','yes' if pusy.is_tamed else 'no')
pusy.eat('mouse')
pusy.eat('bird')
pusy.sleep()
pusy.eat('bird')



 
