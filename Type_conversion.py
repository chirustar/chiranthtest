flight_no="AI203"
base_fare="4500.75"
tax_percent="5"
seat_numbers="12A,12B,14C,15D"
is_international="TRUE"

base_fare=float('4500.75')
tax_percent=float('5')
final_fare=base_fare+(base_fare*tax_percent/100)
print(final_fare)

seat_list=seat_numbers.split(",")
print(f"given the seat list :{seat_list}")

set_seat=set(seat_list)
print(f"provide us the seat number in set format:{set_seat}")

is_international = True if is_international.lower()=="" else False
print("Flight internation", is_international)

flight_summary = {
    "flight_no":flight_no,
    "final_fare":int(final_fare),
    "seat_numbers":tuple(seat_list)
}
print(flight_summary)



