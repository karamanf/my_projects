N = 7

for i in range(N):
    for j in range(N-i):
        print(" ", end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print("")