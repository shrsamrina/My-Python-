
# #WAP TO ENTER MARKS OF 3 STUDENT FROM USER AND STORE IN A DICT. START WITH AN EMPTY DICT & ADD ONE BY ONE. USE SUBJECT NAME AS KEY AND MAKRS AS VALUE.
 
# marks = {}

# x = int(input("Enter you math marks: "))
# marks.update({"math": x})

# x = int(input("Enter your science marks: "))
# marks.update({"science" : x})

# x = int(input("Enter your physics marks: "))
# marks.update({"physics": x})

# print(marks)
    
    
#FIGURE OUT A WAY TO STORE 9 & 9.0 AS SEPARATE VALUES IN THE SET. (TAKE HELP OF BUILT-IN DATA TYPES)

values =  { 9,9.0} #if we "9.0" or "9" the only we can run both the digit
#another way is this, by using tuple

values =  {
    ("float", 9.0),
    ("int", 9)
}
float = {"9.0"}
int = {"9"}


print(values)