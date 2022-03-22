#Operators: comparison, assignment, bitwise, logical, membership, and identity

"""
Comparison Operators: Return True or False
ex. ==, <, >, <=, >=, !=, <>
!= and <> have the same meaning

Assignment Operators: 
ex. =, +=, -=, *=, /=, **=(exponent)
>>> x=2
>>> y=3
>>> x**=y
>>> x
8
>>> x*=y
>>> x
24
Bitwise Operators:
ex. |, &, ~(binary XOR), ^(complement), <<(moved left), >>

Logical Operator: And, Or, Not
>>> 1>4
False
>>> 1>4 and 4>3
False
>>> 1>4 or 4>3
True
>>> not(4>1)
False

Memborship Operator: In - returns True if the specified operand is found in the sequence
Not In - returns True if the specified operand is not found in the sequence
>>> str1="John"
>>> 'o' in str1
True
>>> 'k' in str1
False

Identity Operators: Is - returns True if two variables point to the same object and False, otherwise
Not Is - Returns False if two variables point to the same object and True, otherwise'

>>> x=10
>>> y=10
>>> id(x)
140597998438800
>>> id(y)
140597998438800
>>> x is y
True
>>> x=[1,2,3]
>>> y=[1,2,3]
>>> x is y
False
>>> print x==y
True
>>> id(x)
4388749392
>>> id(y)
4388831744

"""

x=24


