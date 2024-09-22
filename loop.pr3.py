#print the elements of the following list using a loop:
 #[ 1,4,9,16,25,36,49,64,81,100]
 
nums = [1,4,9,16,25,36,49,64,81,100] 

idx = 0
while idx< len(nums):
    print(nums[idx])
    idx +=1
    
#same for different example

phones = ["samsung", "iphone", "motorola", "oppo", "vivo"]

idx = 0 #if we do 'idx = 2' it will run from motorola
while idx <len(phones):
    print(phones[idx])
    idx += 1

#PR4 [ FOR TUPLE WE USE {}]

#SEARCH FOR A NUMBER X IN THIS TUPPLE USING LOOP: [1,4,9,16,25,36,49,64,81,100 ]

nums= [1,4,9,16,25,36,49,64,81,100, 49 ]

k = 0

x = 49
while k < len(nums):
    if(nums[k] == x):
        print("We found X at", k)
    else:
        print("Finding....")
    k += 1
    
    
    
