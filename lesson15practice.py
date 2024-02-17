class vehicle:
    def __init__(self,engine):
        self.engine = engine

    
    def start_engine(self):
        return (f"{self.engine} has started")


class Car(vehicle):
    pass




car = Car("engine")
print(car.start_engine())