for j in range(3):
    i = input()

    answer = 0

    arrNum = i.split(' ')
    arrNum = [int (i) for i in arrNum]
    for number in arrNum:
        answer = answer + number

    if answer == 3 : 
        print("A")
    elif answer == 2 : 
        print("B")
    elif answer == 1 : 
        print("C")
    elif answer == 0 : 
        print("D")
    elif answer == 4 : 
        print("E")