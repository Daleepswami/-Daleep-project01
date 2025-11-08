#Write a program to print all Prime numbers between give range
print("please Enter the renge of two number for finding prime number :-" )
num1=int(input("Enter number their start the range :-"))
num2=int(input("Enter number their end the range :-"))
for i in range(num1,num2):
    count=0
    for j in range(1,i+1):
       if i%j==0:
           count+=1
    if count==2:
        print(i)
         
