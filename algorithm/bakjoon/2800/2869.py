i = input()

arrNum = i.split(' ')
arrNum = [int (i) for i in arrNum]

a1 = arrNum[0]
a2 = arrNum[0] - arrNum[1]

answer = (arrNum[2] - arrNum[1] -1) // a2 + 1

print(answer)
