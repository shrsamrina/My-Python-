#simple way
a = 1
b = 3

sum = a + b
print(a+b)

print("break")

#now to redo the same thing without adding same code again and being redundant; def is used for 'defining'

a = 3
b = 10   

def cal_sum(a,b):   #cal_sum is just a variable i took
    sum = a + b
    print(sum)
    return sum #in functions we use 'return'. The return gives the result back.

cal_sum(a,b) #this is argument,Arguments allow the function to use different numbers each time

a = 10 
b = 20
cal_sum(a,b) #now we just have to initialize a & b and it will give different value each time.
 