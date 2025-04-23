wheather= int(input("Enter the number for the current wheather condition(1. raining/ 2. sunny/ 3. cold/ 4. humid): "))

if wheather==1:
    print("It is raining.")
elif wheather==2:
    print("It is sunny.")
elif wheather==3:
    print("It is cold.")
elif wheather ==4:
    print("It is humid")
else:
    print("Invalid Input")

# Check Numbers

print("Checking if the number is greater than 100 or not.")
number= int(input("Enter a number: "))

if number>100:
    print(number, " is greater than 100.")
elif number<100:
    print(number," is smaller than 100.")
else:
    print("Provided Number is 100.")