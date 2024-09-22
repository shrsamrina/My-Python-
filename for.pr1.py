#WAP TO FIND SUM OF FIRST N NUMBERS.(USE 'WHILE')
n = 10

sum = 0
i = 1 

while i <= n:
    sum += i
    i += 1

    print("Total sum= ",sum)
    
print ("dead")


#WAP TO FIND THE FACTORIAL OF FIRST N NUMBER (USE 'FOR')

n = 5

factorial = 1
for i in range(1 , n+1): #n +1 means we will go till 5 (n=5)
    factorial *= i    
    print ("total factorial : ", factorial)




    
    