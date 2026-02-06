num=int(input("enter a number to play fizzbuzz: "))
for _ in range(1,num+1):
    if(_%3==0 and _%5==0):
        print("fizzbuzz")
    elif(_%3==0):
        print("fizz")
    elif(_%5==0):
        print("buzz")
    else:
        print(_)