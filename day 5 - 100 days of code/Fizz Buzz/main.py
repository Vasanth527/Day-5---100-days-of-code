fizz = 3
buzz = 5
for numbers in range (1 , 101) :
    if numbers % fizz == 0 and numbers % buzz == 0 :
        print("fizzbuzz")
    elif numbers % fizz == 0:
        print("fizz")
    elif numbers % buzz == 0:
        print("buzz")
    else:
        print(numbers)                