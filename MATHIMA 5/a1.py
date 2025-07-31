active = True

while active:
    user_input =  int(input("press 1 gia eksodo \npress 2 gia tetragono \n "))
    if user_input == 1:
        print("quit")
        active = False
    elif user_input == 2:
        user_input = int(input("Dose enan arithmo: "))
        print(user_input*user_input)
    else:
        print("Wrong Input!")