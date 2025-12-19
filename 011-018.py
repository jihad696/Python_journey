'''
the assignment
"Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt

notice : i change varaible names 

'''

#assignment1
Name = "Gehad"
Age = "23"
Country = "Egypt"
print("Hello \'" + Name + "\', How You Doing \\ \"\"\" Your Age Is \""+ Age +"\"\" + And Your Country Is: " + Country)

#assignment2
print("Hello \'" + Name + "\', How You Doing \\ \n \""" Your Age Is \""+ Age +"\"\" + \n And Your Country Is: " + Country)


#assignment3
namee = "Elzero"

# Second Letter Is "l"
print(namee[1])

# Third Letter Is "z"
print(namee[3])

# Last Letter Is "o"
print(namee[-1])


#assignment4

name = 'Elzero'

# Needed Output
# "lze"
print(name[1:4])
# "Ezr"
print(name[0:5:2])

# "rzE"
print(name[-2::-2])  #Moves backward through the string, skipping one character at a time (every second character in reverse).


#5
myname = "#@#@Gehad#@#@"

print(myname.strip("@,#"))


#6

num = "9"
num1 = "15"
num2= "130"
num3 = "950"
num4 = "1500"

print(num.zfill(4) +"\n" + num1.zfill(4) +"\n" + num2.zfill(4)+"\n" + num3.zfill(4) +"\n" + num4.zfill(4))

#7

name_name = "Gehad"
last_name = "Baleegh Saad Ali"

print(name_name.rjust(20,"@"))
print(last_name.rjust(20,"@"))

#8

name_one = "geHadD"
name_two = "HellYea"

print(name_one.swapcase())
print(name_two.swapcase())

#9

msg = "I Love Python And Although Love Elzero Web School love"

print(msg.count("Love"))

#10

name9 = "Elzero"

# Needed Output
print(name9.index("z"))


#11

msg = "I <3 Python And Although <3 Elzero Web School"

# I Love Python And Although <3 Elzero Web School

print(msg.replace("<3", "Love"))


#12

name8 = "Gehad"
age8 = 23
country8 = "Egypt"


# Needed Output Using f""

print(f"My name is {name8} and i am {age8} and  i am from {country8} ,Asyut ")


