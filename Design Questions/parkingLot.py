'''
Assign the Driver to first parking lot with enough capacity and has a reserved spot that corresponds to the driver's requested spot
-If car type is compact only need 1 spot, if the car type is large need to 2 adjacent spots 
'''
class ParkingLot:
    def __init__(self,parking_id, capacity, reserved_spots):
        self.parking_id = parking_id
        self.capacity = capacity
        self.reserved_spots = set(reserved_spots)
    
    def hasCapacity(self, carSize):
        available = self.capacity - len(self.reserved_spots)
        if carSize == "compact":
            return available >= 1
        if carSize == "large":
            return available >=2
    
    def has_requested_spot(self, carSize, requestedSpot):
        if carSize == "compact" and requestedSpot not in self.reserved_spots:
            return True
        if carSize == "large" and (requestedSpot not in self.reserved_spots and requestedSpot + 1 not in self.reserved_spots):
            return True 
        return False
    
    def reserveSpot(self, carSize, requestedSpot):
        self.reserved_spots.add(requestedSpot)
        if carSize == "large":
            self.reserved_spots.add(requestedSpot + 1)
        
class Driver:
    def __init__(self, driver_id, car_size, requested_spot):
        self.driver_id = driver_id
        self.car_size = car_size
        self.requested_spot = requested_spot

class ParkingManager():
    def find_parking_spot(parking_lots, driver):
        assigned_parking_lot = None

        for parking_lot in parking_lots:
            if parking_lot.hasCapacity(driver.car_size):
                if parking_lot.has_requested_spot(driver.car_size, driver.requested_spot):
                    reserve = parking_lot.reserveSpot(driver.car_size, driver.requested_spot)
                    assigned_parking_lot = parking_lot
                    return assigned_parking_lot
                
        return assigned_parking_lot


def main():
    parking_lots = [
    ParkingLot(1, 10, [1, 2, 3]),
    ParkingLot(2, 6, [5, 6]),
    ParkingLot(3, 8, [2, 4, 6])]

    drivers = [
        Driver(101, "compact", 2),
        Driver(102, "compact", 4),
        Driver(200, "large", 2),
        Driver(201, "large", 3),
    ]

    for driver in drivers:

        assigned_spot = ParkingManager.find_parking_spot(parking_lots, driver)
        
        if assigned_spot:
            print(f"You are assigned to parking lot: {assigned_spot.parking_id}")
        else:
            print("There are no available spots for you to park at. Sorry.")

if __name__ == "__main__":
    main()