hidden = [2,4,1,3,1,3,2,4]
active_game = True

status = ["closed","closed","closed","closed","closed","closed","closed","closed"]
found = 0
while active_game:
    #read first position
    first_position = int(input("dose thn proti thesi 0-8:"))
    while (first_position < 0 or first_position >= len(hidden)) or status == "open":
        print("Error!")
        first_position = int(input("Give first position (0-(N-1)) and closed: "))

    #read second position
    second_position = int(input("dose thn proti thesi 0-8:"))
    while (second_position < 0 or second_position >= len(hidden)) or status[second_position] == "open" \
                                                                or second_position == first_position:
        print("Error!")
        second_position = int(input("Give first position (0-(N-1)) and closed: "))

    #change state : both temp_open
    status[first_position] = "temp_open"
    status[second_position] = "temp_open"

    #check if same then open, else closed
    print("")
    for position in range(len(hidden)):
        if status[position] == "closed":
            print("-", end="")
        elif status[position] == "open":
            print(hidden[position], end="")
        else:
            print(hidden[position], end="")
    print("")

        #check if same then open , else closed
    if hidden[first_position] == hidden[second_position]:
        status[first_position] == "open"
        status[second_position] == "open"
        print("Success")
        found +=2
        if found == len(hidden):
            print("bravo")
            active_game = False
    else:
        status[first_position] == "closed"
        status[second_position] == "closed"
        print("Failure")



    
         



