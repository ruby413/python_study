a = input()
i = input()

answer = 0
realAnswer = 0
answerArr = []

arrNum = i.split(' ')
arrNum = [int (i) for i in arrNum]


arrNum.sort()

for number in arrNum:
    answer = answer + number
    answerArr.append(answer)

for number in answerArr:
    realAnswer = realAnswer + number

print(realAnswer)

