class Robot:

    count = 0

    def __init__(self,name):
        self.name=name
        Robot.count+=1
        print(f"Created robot {name}")

    def sayHi(self):
        print(f"Hi my name is {self.name}")

    def die(self):
        Robot.count-=1
        print(f"{self.name} eliminated")

    @classmethod
    def howMany(cls):
        print(f"There are {cls.count} robots in my universe")

robot1=Robot("R2D2")
robot2=Robot("RoBoy")
Robot.howMany()
robot2.die()
Robot.howMany()
