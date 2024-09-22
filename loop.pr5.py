# Q1 PRINT ELEMENTS OF FOLLOWING LIST USING A LOOP:

#[1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

for value in nums:
    print(value)
    
# Q2 SEARCH FOR X IN THIS TUPLE USING LOOP:

nums =  [1,4,9,16,25,36,49,64,81,100, 81]  
x = 81 
idx = 0 #idx is given to track 
for el in nums:
    if el == x:
        print("Found at", idx)
        break #break if we want to stop once we find x (81)
    idx += 1    
    

