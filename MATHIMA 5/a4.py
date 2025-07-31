#euresi apo tous 10 ton megalitero arithmo ths listas me xrisi arithmon tou xristi
new_list = []
print("dose 10 arithmous")

max = 0
i=0
while i < 10:
    user_input = int(input("dose ton " + str(i+1) +"o arithmo: "))
    new_list.append(user_input)
    if new_list[i] > max:
        max = new_list[i]
    i+=1
   

print("maximum is "+ str(max))