
#dict are mutable and can run for all types like int, str, float, bollean
#Here "Name" is key and "Sammy" is value
dict = {
    "Name" : "Sammy",
    "Height" : "5'7",
    "Learning" : "Coding",
    "Phase" : "1.2",
    "12" : "21"
    
}

print(dict["Name"])
print(dict["Phase"])


#now to change the value of a key , [IT DOESN'T ALLOW DUPLICATION. HENCE, THE NEW CODE OVERWRITES]
dict["Name"] = "Danny"
print(dict)