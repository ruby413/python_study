i = input()

day = 0 
dayArr = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, i.split())
for j in range(x-1):
    day = day+dayArr[j]

print(week[(day+y) % 7])

