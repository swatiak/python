#Syntax
#for <variable> in xrange(<an integer expression >)
#  <statement-1>
#  <statement-n>


#while <condition>
#       <statement>
checking_acc = 5678143
num = int("Enter the account number\t")
while checking_acc != num:
    num = int("Enter the right account number\t")
print ("\n********")
print ("Your account number is", num)