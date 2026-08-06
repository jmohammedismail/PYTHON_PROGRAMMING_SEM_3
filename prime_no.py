import math

n = int(input("Enter no.: "))

if n <= 1:
    print("Not a prime number")
else:
    a = int(math.sqrt(n))

    for i in range(1, a + 1):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
