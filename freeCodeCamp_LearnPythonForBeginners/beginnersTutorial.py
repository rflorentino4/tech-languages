#Name: Romina Florentino
#Reference: Learn Python - Full Course for Beginners [Tutorial] by freeCodeCamp.org on YouTube
#Date: 02/11/2025 - TBH

#-----------------------------------------------
#variables and data types
characterName = "John"      #string
characterAge = 35           #integer
isMale = True               #boolean (true or false)


#string concatenation -meaning, adding strings together
print("There once was a man named " + characterName + ",")         


#type conversion - converting integer to string, **ONLY AFFECTS THE LINE IT IS ON IF USED LIKE THIS**
print("He was " + str(characterAge) + " years old.")


#working with strings
#print("\n")     #escape characters - \n creates a new line
#print("\t")     #\t creates a tab/indent


#print regular string
phrase = "Giraffe Academy"      


#string concatenation -> adding variables to strings
print(f"\n{phrase} is cool. -adding variable to a string\n")         


#LOWER AND UPPER CASE METHOD
print(phrase.lower() + "-convert to lower\n")               #lowercase conversion
print(phrase.upper() + "-convert to upper\n")               #uppercase conversion


#isupper() method
print(phrase.isupper())              #returns true or false depending on if the string is uppercase -> here, it is FALSE
print("False because it is not uppercase\n")


#accessing characters in a string, here it will print the first letter of the name
pam = "Pamela"
print(pam[0])           #this will grab the P
print(pam[1])           #this will grab the a


#INDEX METHOD
#index will let us know where a specific character is located
print(pam.index("e"))       #this will print the index # of the letter e in Pamela -> this is called passing a parameter (e being the parameter) ----> e is in index position 3 which is what the terminal prints out

#if you enter a character that is NOT in the string, it will give you an error message


#REPLACE METHOD
#this will print "Tall Kings" because it is replacing the word "Short" with "Tall"
sassy = "Short Kings"
print(sassy.replace("Short", "Tall"))     

#PEMDAS APPLIES in Python + arithmetic operations like + and - and * are done left to right -called operators I think


#MODULUS OPERATOR - returns the remainder of a division
print(10 % 3)       #3 goes into 10 3 times with a remainder of 1, so 1 will print in the terminal


#ABSOLUTE VALUE FUNCTION - will always make the number positive
num = -5
print(abs(num))  


#POW FUNCTION - pass two parameters, the first is the base (# of choosing) and the second is the exponent
print(pow(3, 2))     #3 to the power of 2 = 3x3 = 9


#MAX AND MIN FUNCTIONS
print(max(4, 6))     #returns the larger number, so 6 will print back to us
#vs
print(min(4, 6))     #returns the smaller number, so 4 will print back to us


#ROUND FUNCTION
print(round(3.2))     #will round DOWN and print 3
print(round(3.8))     #will round UP and print 4


from math import *       #importing the math module - gives us access to more math functions --46 minutes into the video


#FLOOR FUNCTION
#rounds DOWN to the nearest whole number
print(floor(3.7))      #will print 3    


#CEIL FUNCTION
#rounds UP to the nearest whole number
print(ceil(3.7))       #will print 4


#SQUARE ROOT FUNCTION
#sqrt gives you the square root of a number (whatever you put in the parentheses)
print(sqrt(36))       #will print 6.0


#Getting input from a user
#input() function
userName = input("Enter your name: ")          #this will ask the user to enter their name


#CAPITALIZE METHOD --capitalizes the first character, and makes the rest lowercase which is beautiful
name = userName.capitalize()                  #this will capitalize the first letter of the name, even if they enter "MINA," it will print "Mina"
print("Hello " + name)


#basic calculator
num1 = input("Enter a number: ")          #input() always returns a string
num2 = input("Enter another number: ")

print(num1 + num2)         #this will concatenate the two numbers together as strings. for example: 5 and 6 as "56" AKA THE WRONG ANSWER

#to convert the strings to integers, we use int() function
print(int(num1) + int(num2))        #this will add the two numbers together and print 11 instead of the concatenated "56"


#BUILDING A BETTER CALCULATOR
#we want to convert the inputs to floats so that we can do decimal points as well
#num1 = float(input("Enter a number: "))
#num2 = float(input("Enter another number: "))

#now we can use +, -, /, and * without worrying about what type of number they are

print(num1 + num2)

#-----------------------------------------------------------------
#leaving @ 57:39 / 4:26:52 - Building a Better Calculator >
#-----------------------------------------------------------------

#INDEX VALUES -> basic list, hardcoded
friends = ["Kevin", "Karen", "Jim"]
print(friends) #prints all the elements within the list

luckyNumbers = [4,8,15,16]

#add list items to another list
friends.extend(luckyNumbers)
print(friends)

#append method
friends.append("Creed") #add Creed to the END of a list

#insert method
friends.insert(1, "Karen")