class Vehicle :
    def __init__(self,name,ms,mile):
        self.name = name
        self.ms = ms
        self.mile = mile

class Bus(Vehicle):
    pass
bus = Bus("Prade to Gangayal",2000,18)
print("Vehicle Name : ",bus.name,"Speed :",bus.ms,"Mileage : ",bus.mile)