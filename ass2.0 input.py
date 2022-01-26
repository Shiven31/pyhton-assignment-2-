print("Python ASSIGNMENT 2")

print("Name: Shiven Goyal")

print("SID:21104017")

# Question1 ():
print("Question 1")
input_string="Python is a case sensitive language"
print("given input=",input_string)
#Part A
print("Part A!")
print("Length os input string=",len(input_string))
#Part B
print("Part B!")
print("Reverse of string is","'"+input_string[-1: :-1]+"'")
#Part C
print("Part C!")
slicestr=input_string[slice(9,26)]
print(slicestr)
#Part D
print("Part D!")
newstring=input_string.replace("a case sensitive","object oriented")
print(newstring)
#Part E
print("Part E")
print("Index of substring 'a' is",input_string.index('a') )
#Part F
print("Part F!")
print(input_string.replace(" ",""))

   

# Question2 ():
print("Question 2")
name=input("Please enter your name: ")
sid=input("Enter SID: ")
dep=input("Enter department name: ")
cgpa=float(input("Enter CGPA: "))
print('''
''')
print('''Hey, %s Here!
     My SID is %s
    I am from %s department and my CGPA is %s'''%(name,sid,dep,cgpa))


# Question3 ():
print("Question 3")
a=56
print("value of 'a' =",a)
b=10
print("value of 'b' =",b)
#Part A
print("Part A!")
print("a&b: ",a&b)
print(" ")
#Part B
print("Part B!")
print("a|b: ",a|b)
print(" ")
#Part C
print("Part C!")
print("a^b: ",a^b)
print(" ")
#Part D
print("Part D!")
print("a<<2:",a<<2,"and", "b<<2: ",  b<<2)
print(" ")
#Part E
print("Part E!")
print("a>>2:",a>>2, "and b>>4",b>>4)



# Question 4 ():
print("Question 4")
N1= float(input("Enter 1st number:"))
N2= float(input("Enter 2nd number:"))
N3= float(input("Enter 3rd number:"))

if(N1>N2) and (N1>N3):
    largest=N1
elif (N2>N1) and (N2>N3):
    largest=N2
else :
    largest=N3
print("The largest number is",largest)


#  question 5()
print("Question 5")
#word=("name")
#print("given word =",word)
j=input("Intro: (preferred format: My name is 'name' ,What is your name?) ")
print("string taken =",j)
if 'name' in j:
    print("yes, chosen word is present.")
else:
    print("no, the chosen word is not present.")



#  Question 6 ()
print("Question 6")
L1=float(input("Enter 1st length = "))
L2=float(input("Enter 2nd length = "))
L3=float(input("Enter 3rd length = "))
sum1  = L1+L2
sum2 = L2+L3
sum3 = L3+L1 
if(sum1 >L3 or sum2>L1 or sum3>L2):
    print("yes triangle is possible")
else:
    print("no triangle is possible")



    












    
