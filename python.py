#defining variables
n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1
#using while loop
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
#printing result
print()
