list_protos = []

for i in range(2,101):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        list_protos.append(i)

primes = tuple(list_protos)
print(primes)