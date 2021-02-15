num1 = int(input("Type Number 1: "))
num2 = int(input("Type Number 2: "))
 
print("Prime Numbers Between",num1,"And",num2,":")
 
for num in range(num1,num2 + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
 
