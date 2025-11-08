# Program to find LCM of two numbers using for loop

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    greater = num1
else:
    greater = num2
  
for i in range(greater, (num1 * num2) + 1):
    if (i % num1 == 0) and (i % num2 == 0):
        lcm = i
        break

print("LCM of", num1, "and", num2, "is:", lcm)
