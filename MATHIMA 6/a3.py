n = int(input("dose enan thetiko arithmo: "))

list_protos = []


if n == 0 or n == 1:
    print("den einai protos arithmos")
else:
    for i in range(2,n):
        if n % i == 0:
            print("den einai protos")
            break
    else:
        print("its prime")

    
