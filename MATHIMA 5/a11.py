#pithagoreia triada
for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if i**2 + j**2 == k**2:
                print(str(i) + str(j) + str(k))