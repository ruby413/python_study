i = input()
for num in range(1,int(i)+1):
    print( (int(i)-num) * " " + num * "*" + (num-1) * "*")
for num in reversed(range(1,int(i))):
    print( (int(i)-num) * " " + num * "*" + (num-1) * "*")
