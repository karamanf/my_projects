friends = ["george","kostas","mitsos"]
party = ["koulis","sofia","kostas","xristos","giannis","mauros","entheos","pavlos","sefe"]

cnt = 0
for i in friends:
    if i in party:
        cnt +=1

print(cnt)
 
if cnt < 2:
    print("Den erxomai sto parti ")
else:
    print("erxomai sto parti")
