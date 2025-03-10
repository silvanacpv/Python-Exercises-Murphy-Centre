#Question Two – Loop Practice
#Fizz Buzz
#By:   Silvana Paredes
#Date: 19/02/2025


for i in range(1, 101):
    div_3 = i % 3
    div_5 = i % 5
    if div_3 == 0 and div_5 !=0:
        print(i, ": Fizz")
    elif div_3 != 0 and div_5 ==0:
        print(i, ": Buzz")
    elif div_3 == 0 and div_5 ==0:
        print(i, ": FizzBuzz")
    else:
        print(i)
