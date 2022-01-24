class Car:
    def __init__(self, size, id):
        self.size = size
        self.id = id
    
    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return self.__str__()

class ParkingLane:
    def __init__(self, length):
        self.park_list = [None] * length

    def insert(self, car):
        start_index = 0

        for i in range(len(self.park_list)):
            if self.park_list[i] is not None:
                start_index = i+1
            
            if ((i + 1) - start_index) >= car.size:
                for i in range(start_index, i+1):
                    self.park_list[i] = car
                return True
        
        return False
    
    def remove(self, car):
        found = False

        for i in range(len(self.park_list)):
            if self.park_list[i] == car:
                found = True
                self.park_list[i] = None
        
        return found

    def __iter__(self):
        last_yield = None

        for i in range(len(self.park_list)):
            if self.park_list[i] == None:
                continue

            car = self.park_list[i]
            
            if last_yield == car:
                continue

            last_yield = car
            yield self.park_list[i]

if __name__ == "__main__":
    car1 = Car(size=2, id=1)
    car2 = Car(size=2, id=2)
    car3 = Car(size=3, id=3)
    car4 = Car(size=3, id=4)

    p = ParkingLane(10)
    p.insert(car1)
    p.insert(car2)
    p.insert(car3)
    p.remove(car2)
    p.insert(car4)

    print(p.park_list)

    for car in p:
        print(car)