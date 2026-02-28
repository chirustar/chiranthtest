class Flight:
    def __init__(self,flight_no,source,destination,base_fare):
        self.flight_no=flight_no
        self.source=source
        self.destination=destination
        self.base_fare=base_fare
        
    def flight_info(self):
        print(f"The flight number is {self.flight_no} from source {self.source} to destination {self.destination}")
        
        
    def calculate_fare(self,passenger_count,discount_percent):
        total_fare=self.base_fare*passenger_count
        if discount_percent>=0:
            discount_amount=total_fare*(discount_percent/100)
            total_fare -=discount_amount
            return total_fare
        
    def update_route(self,source=None, destination=None):
            self.source=source  
            self.destination=destination
        
Flight1=Flight("A121", "Bengluru", "Delhi", 20000)

fare1=Flight1.calculate_fare(2,5)
print("Total fare with discount",fare1)

fare2=Flight1.calculate_fare(4,9)
print("Total fare without discount",fare2)

Flight1.update_route(destination= "Delhi")
print(f"updated route:{Flight1.source} to {Flight1.destination}")

Flight1.update_route(source="Bengaluru", destination="Delhi")
print(f"updated route:{Flight1.source} to {Flight1.destination}")


        
            
            