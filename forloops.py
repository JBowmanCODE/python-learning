#Asks the user to enter a number
#Uses a loop to print every number from 1 up to that number
#But if the number is divisible by 3, print "Fizz" instead

number = int(input("Enter a number: "))

for i in range(1, number + 1):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)