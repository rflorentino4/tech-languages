#Name: Romina Florentino
#Reference: Learn Python - Full Course for Beginners [Tutorial] by freeCodeCamp.org on YouTube
#Date: 02/11/2025 - TBH

#-----------------------------------------------
#variables and data types
characterName = "John"      #string
characterAge = 35           #integer
isMale = True               #boolean (true or false)

print("There once was a man named " + characterName + ",")      #string concatenation -meaning, adding strings together   

print("He was " + str(characterAge) + " years old.")            #type conversion - converting integer to string, **ONLY AFFECTS THE LINE IT IS ON IF USED LIKE THIS**

#-----------------------------------------------
#working with strings
print("\n")     #escape characters - \n creates a new line
print("\t")     #\t creates a tab/indent

phrase = "Giraffe Academy -print string\n"          #string
print(phrase + " is cool. -adding variable to a string\n")         #string concatenation -> adding variables to strings

print(phrase.lower() + "-convert to lower\n")               #lowercase conversion
print(phrase.upper() + "-convert to upper\n")               #uppercase conversion

print(phrase.isupper())              #returns true or false depending on if the string is uppercase -> here, it is FALSE

