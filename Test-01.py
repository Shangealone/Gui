class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum number of cars the parking lot can hold
        self.parked_cars = []      # Stack for parked cars
        self.waiting_queue = []     # List for waiting cars

    def enter_car(self, car_number):
        if len(self.parked_cars) < self.capacity:
            self.parked_cars.append(car_number)
            print(f"Car {car_number} has entered the parking lot.")
        else:
            self.waiting_queue.append(car_number)
            print(f"Parking lot full. Car {car_number} is waiting.")

    def exit_car(self):
        if self.parked_cars:
            exited_car = self.parked_cars.pop()
            print(f"Car {exited_car} has exited the parking lot.")
            
            # Check if there's a waiting queue and fill the slot with the most recent waiting car
            if self.waiting_queue:
                next_car = self.waiting_queue.pop()  # Get the most recently added car from the waiting queue
                self.parked_cars.append(next_car)
                print(f"Car {next_car} has entered the parking lot from the waiting queue.")
        else:
            print("No cars are parked in the lot.")

    def display_status(self):
        print("\nCurrent Parking Lot Status:")
        print("Parked Cars (Stack):", self.parked_cars[::-1])  # Show stack from top to bottom
        print("Waiting Queue:", self.waiting_queue)
        print(f"Available Spaces: {self.capacity - len(self.parked_cars)}\n")

def main():
    parking_lot = ParkingLot(capacity=3)  # Create a parking lot with a capacity of 3

    while True:
        print("Parking Lot Management System")
        print("1. Add a Car")
        print("2. Remove a Car")
        print("3. Display Parking Status")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            car_number = input("Enter the car number to add: ")
            parking_lot.enter_car(car_number)
            # Display the current status after adding a car
            parking_lot.display_status()
        elif choice == '2':
            parking_lot.exit_car()
            # Display the current status after removing a car
            parking_lot.display_status()
        elif choice == '3':
            parking_lot.display_status()
        elif choice == '4':
            print("Exiting the Parking Lot Management System.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()