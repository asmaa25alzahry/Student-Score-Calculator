print ("student score calculator")
#student data
student_name = input ("please enter your name?: \n")
print ("welcome " + student_name)
#student score
Arabic = float (input ("enter your degree on arabic :"))
math = float (input("enter your degree on math :"))
programming = float (input("enter your degree on programming :"))
#score list
score = [Arabic,math,programming]
#score total 
total = float(score[0] + score [1] + score [2]) 
print ("total score is : "  +  str(total))
#average of total score
average = total / len(score)
print ("average is : "  +  str(average))

#result
print("name: ",student_name)
print ("score:" , score)
print ("total:",total)
print("average:",average)