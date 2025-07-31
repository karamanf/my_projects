lista = []

for i in range(10):
    user_input = int(input("Give a number metaksi 10 kai 20: "))
    while user_input <10 or user_input>20:
        user_input = int(input("Give a number metaksi 10 kai 20:"))
    lista.append(user_input)


my_tuple = tuple(lista)
print(my_tuple)

list_squares = []
for i in range(10):
    list_squares.append(lista[i]**2)

list_squares.sort()

my_tuple2 = tuple(list_squares)
print(my_tuple2)
    






    
    
