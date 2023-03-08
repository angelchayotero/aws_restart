

print("Cuenta hasta diez")

for i in range(51):
    print(i)
    
    if i % 3 == 0 and  i % 5: 
        print("FizzBuzz")
    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)
    