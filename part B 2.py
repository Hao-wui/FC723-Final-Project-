import random
import string

import pprint
seats = [['1A', '2A', '3A', '4A', '...', '78A', '77A', '79A', '80A'],
         ['1B', '2B', '3B', '4B', '...', '78B', '77B', '79B', '80B'],
         ['1C', '2C', '3C', '4C', '...', '78C', '77C', '79C', '80C'],
         ['X', 'X', 'X', 'X', '...', 'X', 'X', 'X', 'X'],
         ['1D', '2D', '3D', '4D', '...', 'S', 'S', '79D', '80D'],
         ['1E', '2E', '3E', '4E', '...', 'S', 'S', '79E', '80E'],
         ['1F', '2F', '3F', '4F', '...', 'S', 'S', '79F', '80F']]
dic={}
bookings={}
for x1 in seats:
    row_label = x1[0][:-1]  # Extracting the row label from the first seat of each sublist
    for x2 in x1:
        dic[x2]="F"
        dic[row_label + x2[-1]] = "F"  # Adding corresponding keys with row label to the dictionary
    dic["X"]="Not selectable"
    dic["S"]="Not selectable"


def Produce_random_booking_reference():
    used_references = []#Generates a list to store serial numbers

    while True:
        reference = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))#Generate sequence number
        if reference not in used_references:#Check whether the serial number is duplicate
            used_references.append(reference)#If it does not repeat, it is added to the list,
            # otherwise it is regenerated until it does not repeat
            return reference

# 示例用法



def Check_availability_of_seat(c):
        if dic[c]=="F":#Different situations arise through different seat states
            print("This seat can be reserved")
        elif dic[c]=="R":
            print("This seat has been reserved,Please re-select")
        elif dic[c]=="Not selectable" or dic[c]=="Not selectable":
            print("This seat can not be reserved,Please re-select")
def Book_a_seat():
    # Different situations arise through different seat states
    pprint.pprint(seats)
    result=input("Please enter the seat to book")
    result2=dic[result]#Check seat availability
    if result2=="F":#Collect user information
        print("You can reserve,Please give details")#passport number, first name, last name, seat row and seat column to be maintained in a database table
        passport_number=input("please input passport number")
        first_name=input("please input first name")
        last_name=input("please input last name")
        seat_row=input("please input seat row")
        seat_column=input("please input seat column")
        booking_reference = Produce_random_booking_reference()
        bookings[booking_reference] = {
            'seat_number': result,
            'passport_number': passport_number,
            'first_name': first_name,
            'last_name': last_name
        }#The user's information is stored by serial number
        dic[result]="R"#Update seat status

        print("You have successfully reserve ,the booking reference is",booking_reference)
    elif result2=="R":
        print("This seat has been reserved, please reschedule")
    elif result2=="Not selectable":
        print("This seat can not be reserved,Please re-select")
def Free_a_seat():
    result=input("Please enter the seat number  you wish to refund")#Different situations arise through different seat states
    reference=(input("Please enter the reference number"))
    result2=dic[result]
    if result2=="R":
        print("You have successfully refund")
        del dic[reference]#Deleted stored user information
        dic[result]="F"#Update seat status
    else:
        print("Input error, please re-enter")
def Show_booking_state():#Using pprint makes viewing the seat situation more convenient and intuitive
    pprint.pprint(seats)
    for sublist in seats:
        for seat in sublist:
            if seat == "...":
                print(f"{seat}", end=',')
            elif seat == "S":
                print(f"{seat}:storage area", end=',')
            elif seat == "X":
                print(f"{seat}: isles", end=',')
            else:
                print(f"{seat}:{dic[seat]}", end=',')
        print()
def Exit_program():
    print("You are welcome to use again next time")

while True:#Allow users to choose according to the situation
    option = int(input("Please select number:""\n\t"
                   "1. Check availability of seat\n\t"
                   "2. Book a seat\n\t"
                   "3. Free a seat\n\t"
                   "4. Show booking state\n\t"
                   "5. Exit program\n\t"))
    if option==1:
        pprint.pprint(seats)
        c=input("Please select the seat you want")
        Check_availability_of_seat(c)
    elif option==2:
        Book_a_seat()
    elif option==3:
        Free_a_seat()
    elif option==4:
        Show_booking_state()
    elif option==5:
        Exit_program()
        break