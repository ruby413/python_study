i = input()

number = 1000 - int(i)

fiveH = number // 500
H = number % 500 // 100
fif = number % 500 % 100 // 50
ten = number % 500 % 100 % 50 // 10
five = number % 500 % 100 % 50 % 10 // 5
one = number % 500 % 100 % 50 % 10 % 5 

answer = fiveH + H + fif + ten + five + one

print(answer)