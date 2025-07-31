list3d = [[1,2,3,7],
          [4,5,6,3],
          [7,8,9,5]
          ]

list3d.insert(0,[0,0,0,0])

for row in list3d:
    row.append(1)
    print("[", end="")
    for i, elem in enumerate(row): 
        print(elem, end="")
        if i != len(row) - 1:
            print(",", end="")
    print("]")
