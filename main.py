from commons import hcfactor
from evens import evenwords

print("---Main Menu---")
print("1. Provide 2 integer values in order to return the highest common factor of the numbers.")
print("2. Provide a string to find and print all even length words in that string.")
print("3. Exit the program")
inP=input("")

if(inP==1):
    in1=input("Please enter integer 1: ")
    in2=input("Please enter integer 2: ")
    print("The highest common factor from the 2 integers provided is: " + hc_factor(in1, in2))
    
elif(inP==2):
    str0=input("Please enter a string in which to find and print all the even length words: This is a example string. ")
    
    print("Even length words found in the string are: " + evenwords(str0))
    
else:
    exit()