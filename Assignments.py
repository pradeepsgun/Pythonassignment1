#Assignment 1
s = [1,2,3,[4,5,[6,7,8,[9,[10,[11]]]]]]
print (s[0],s[2],s[3][1],s[3][2][1],s[3][2][3][0],s[3][2][3][1][1][0])

#Assignment 2
dob = int(input("Enter your year of birth :"))
cyear = 2020
age = cyear - dob
print ("you are ",age,"years old")

#Assignment 3
name = input("Enter your name :")
yob = int(input("Enter your year of birth :"))
edu = input("Enter your education :")
accno = input("Enter your Account Number :")
cno = input("Enter your Contact Number :")
area = input("Enter your Area :")
age = cyear - yob

l1 = [age,accno,cno]
l2 = [name.upper(),edu.upper(),area.upper()]
print (l1)
print (l2)

#Assignment 4
text="""Not restricting Himself to theory,
He is making people experience the Omni concepts: Omnipresence, Omniscience and Omnipotence.
He is The Scientific Saint,
His Holiness Sri Sri Sri Guru ViswaSphoorthi –
The Omnipresent, The Omniscient and The Omnipotent."""
l= len(text)
print (l)
print (text)

#Assignment 5
l3 = []
l3.extend(["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10"])
print (len(l3))
l3 = l3[1:len(l3)-1]
print (len(l3))
#adding 3 float number
l3.insert(0,1.0)
l3.insert(0,2.0)
l3.insert(0,3.0)
print (l3)
print (len(l3))
#Inser 2 string values at the middle of list
l4 = int(len(l3)/2)
l3.insert(l4,"Pradeep")
l4 = int(len(l3)/2)
l3.insert(l4,"Reddy")
print (len(l3))
#Inserting Duplicate values
l3.insert(0,"a6")
l3.insert(len(l3),"a9")
print (l3)
#Remove the duplicate value
l3.remove("a6")
print (l3) # first value will be removed
