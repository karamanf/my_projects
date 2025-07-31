#keni lista
new_list = []

# euros listas
n = int(input("dose to n: "))
while n<3 or n>20:
    n = int(input("dose enan arithmo apo to (3-20) "))

#metritis kai epanalipsi gia na mpoun oi akeraioi apo thn eisodo tou xristi
cnt = 0
for i in range(0,n):
    user_input = int(input("dose ton " + str(cnt+1) +"o arithmo: "))
    new_list.append(user_input)
    cnt +=1

# auksousa seira kai ektiposi ths listas 
new_list.sort()
print(new_list)
