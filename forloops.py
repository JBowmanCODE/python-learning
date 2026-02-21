# Ask the user to enter a number and convert it to an integer
number = int(input("Enter a number: "))

# Loop from 1 up to and including the number the user entered
for i in range(1, number + 1):
    
    # Check if the current number is divisible by 3 (no remainder)
    if i % 3 == 0:
        print("Fizz")  # Print Fizz instead of the number
    else:
        print(i)  # Otherwise just print the number