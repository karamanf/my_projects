#paixnidi mantepsias
secret_num = 15
meg_plithos = 10


while True:
    print("exete " + str(meg_plithos) + " prospatheies sinolika")
    user_input = int(input("dose enan arithmo: "))
    meg_plithos -=1

    if meg_plithos == 0:
        print("Xasate! Telos prospatheion")
        break
    elif user_input > secret_num:
        print("o arithmos einai megaliteros apo ton krifo")
    elif user_input < secret_num:
        print("o arithmos einai mikroteros apo ton krifo")
    else:
        print("Vrikate ton arithmo!")
        break 
    
    
