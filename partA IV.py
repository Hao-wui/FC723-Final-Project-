# Menu functionalities:
#
# Check availability of seat
# Book a seat
# Free a seat
# Show booking state
# Exit program
import pprint
seats = [['1A', '2A', '3A', '4A', '...', '78A', '77A', '79A', '80A'],
         ['1B', '2B', '3B', '4B', '...', '78B', '77B', '79B', '80B'],
         ['1C', '2C', '3C', '4C', '...', '78C', '77C', '79C', '80C'],
         ['X', 'X', 'X', 'X', '...', 'X', 'X', 'X', 'X'],
         ['1D', '2D', '3D', '4D', '...', 'S', 'S', '79D', '80D'],
         ['1E', '2E', '3E', '4E', '...', 'S', 'S', '79E', '80E'],
         ['1F', '2F', '3F', '4F', '...', 'S', 'S', '79F', '80F']]
dic={}
for x1 in seats:
    row_label = x1[0][:-1]  # Extracting the row label from the first seat of each sublist
    for x2 in x1:
        dic[x2]="F"
        dic[row_label + x2[-1]] = "F"  # Adding corresponding keys with row label to the dictionary
    dic["X"]="Not selectable"
    dic["S"]="Not selectable"

def Check_availability_of_seat(c):
        if dic[c]=="F":#Different situations arise through different seat states
            print("This seat can be reserved")
        elif dic[c]=="R":
            print("This seat has been reserved,Please re-select")
        elif dic[c]=="Not selectable" or dic[c]=="Not selectable":
            print("This seat can not be reserved,Please re-select")

def Book_a_seat():
    pprint.pprint(seats)#Different situations arise through different seat states
    result=input("Please enter the seat to book")
    result2=dic[result]
    if result2=="F":
        print("You have successfully book")
        dic[result]="R"
    elif result2=="R":
        print("This seat has been reserved, please reschedule")
    elif result2=="Not selectable":
        print("This seat can not be reserved,Please re-select")
def Free_a_seat():
    result=input("Please enter the seat you wish to refund")##Different situations arise through different seat states
    result2=dic[result]
    if result2=="R":
        print("You have successfully refund")
        dic[result]="F"
    else:
        print("Input error, please re-enter")
def Show_booking_state():
    pprint.pprint(seats)#Using pprint makes viewing the seat situation more convenient and intuitive
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




