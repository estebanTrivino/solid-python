# Incorrecto

from abc import ABC, abstractmethod

class workerInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Human(workerInterface):

    def work(self):
        print("Trabajando")

    def ear(self):
        print("Comiendo")

class Robot(workerInterface):

    def work(self):
        print("Trabajando")

    def ear(self):
        # Los Robots no comen
        pass

human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
robot.eat()


# Correcto

from abc import ABC, abstractmethod

class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        pass
    

class EatInterface(ABC):

    @abstractmethod
    def eat(self):
        pass



class Human(WorkInterface, EatInterface):

    def work(self):
        print("Trabajando")

    def ear(self):
        print("Comiendo")

class Robot(workInterface):

    def work(self):
        print("Trabajando")


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()