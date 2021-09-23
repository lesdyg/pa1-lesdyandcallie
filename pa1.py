# Team Members: Lesdy Galvez
# Course: CS151,Dr.Rajeev
# Date: 09-22-2021
# Programming Assignment: 1
# Program Inputs : input(length, width, height)
# Program Outputs : output(What is total area of 4 walls and ceiling, how many gallons of paint and primer needed)

#ask user for dimensions (length,width and height)of a room in feet
room_length=input("Enter room_length(feet):")
room_width=input("Enter room_width(feet):")
room_height=input("Enter room_height(feet):")
print(room_length)
print(room_width)
print(room_height)

#compute total area of the 4 walls and ceiling
area_of_room= 2*(room_length + room_width) * 4
print(area_of_room)
ceiling_area= float(room_length)*(room_width)
print(ceiling_area)
total_area=float(area_of_room)+(ceiling_area)
print(total_area)

#amount of primer and paint needed

primer_needed=float(total_area)/200
print(primer_needed)

paint_needed=float(total_area)/350
print(paint_needed)

print("Thank you for using my code.")











