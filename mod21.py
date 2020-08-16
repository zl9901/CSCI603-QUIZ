for x in range(0,101):


    if ((x % 7 == 0 )& (x % 3==0)):
        print("FizzBuzz")
    elif(x%3==0 ):
        print("Fizz")
    elif (x % 7 == 0):
        print("Buzz")
    else:
        print(x)
