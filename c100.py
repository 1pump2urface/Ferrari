class Car(object):
    def __init__(self, model , color , company , speed , fuel) :
        self.model = model
        self.color = color
        self.company = company
        self.speed = speed
        self.fuel = fuel

    def start(self):
        print("started") 

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("increasing speed") 



ferrari = Car("la ferrari", "red","ferrari", 320, 10) 
ferrari.start()

ferrari.accelerate()
        