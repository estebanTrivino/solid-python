# Incorrecto

class Bird:
    def fly(self):
        return "Flying"

class Chicken(Bird): 
    def fly(self): 
        raise Exception("Los pollos no vuelan")
    
#bird = Bird()
#bird.fly()
#chicken = Chicken()
#chicken.fly()

# Correcto

class Bird:
    def move(self):
        return "Moving"
    
class Chicken(Bird):
    def move(self):
        return "Walk"
    
bird = Bird()
print(bird.move())
chicken = Chicken()
print(chicken.move())

bird = Chicken()
print(bird.move())
chicken = Bird()
print(chicken.move())