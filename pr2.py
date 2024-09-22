#WAP TO FIND THE GREATEST OF 4 NUMBERS ENTERED BY THE USER.

a = int(input("Enter your number :"))
b = int(input("Enter your number :"))
c = int(input("Enter your number :"))

if(a>=b and a >=c):
    print("First number is largest", a )
    
elif(b >=c):
    print("Second number is largest", b)
        
else:
     print("Third number is largest", c)
    