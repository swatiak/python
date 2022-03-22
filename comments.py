#This is a single line comment

""" For multi -line
comment use three
double quotes"""

print("Hello World!") 
print('Hello World!') #prints the same with single quotes

"""print ('Hey there, it's a dog') - Syntax Error: invalid syntax
misinterpreted single quote in it's
"""

print("Hey there, it's a dog")
#double quotes - error free

#Python Backslash
""" used for continuation of the print statement
stretch a single statement across multiple lines"""
print("Hello\
World")

print("Hello World 'Mr' Bond")

print('old world "but" still good')

#Escape Sequence
""" 
Insert- tab, newline, backspace, special characters
b- backspace
a- sound system bell
N- newline
T- horizontal tab
Space- the character
'- single quotation mark
"- double quotation mark

"""
print('\a')
print('\tHermit')
print("i know, they are 'great'")

print("Only way to join" + "two strings") #Only way to jointwo strings

print("Name", "Marks", "Age")
print("John Doe", 80.67, "27")
print("Bhaskar", 76.908, "27")
print("Mohit", 56.98, "25")  #NOT FORMATTED
"""
%d- represent an integer
%f- represent a float
%s- String
"""
print("Name Marks Age")
print("%s %14.2f %11d" % ("John Doe", 80.67, 27))
print("%s %12.2f %11d" % ("Bhaskar", 76.908, 27))
print("%s %3.2f %11d" % ("Mohit", 56.98, 25)) #FORMATTED

#Indentation
"""
Most unique characteristic
Makes Python code readable
Distinguishes each block of code from one another
"""
def fun(): #for loop starts with a colon
    pass #use tab or space
for each in "Australia":
    pass