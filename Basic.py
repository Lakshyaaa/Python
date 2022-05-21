#1      Calculate the multiplication and sum of two number
#Simple without def
"""
a = int(input('Enter first Number'))
b = int(input('Enter second Number'))

mul = a*b
sum = a+b

if mul>1000:
         print(sum)
else:
         print(mul)
"""  
         
#with def
"""
def multiple_or_sum(a, b):
                 
         if a*b<=1000:
                  return a*b
         else:
                  return a+b
         

a = int(input('Enter first Number = '))
b = int(input('Enter second Number = '))

result = multiple_or_sum(a, b)
print(result)
"""

#2      Print the function of Current Number and Previous Numbers
"""
a = int(input("Enter total Number ="))
Previous_Number = 0

for i in range(a):
         current_number = Previous_Number + i
         print("Current Number = ",i, "Previous Number = ",Previous_Number, "Sum = ", Previous_Number+i)
         
         Previous_Number = i
"""

#3      Print characters from a string that are present at an even index number

# using length of character
"""
str = input("Enter character = ")
print("Original =",str)

size = len(str)

print("even index character")

for i in range(0, size, 2):
         print(str[i])
"""
# Using List Slicing
"""
str = input("Enter character = ")
print("Original =",str)

size = list(str)
print(size)
 
for i in size[0::2]: # 2 means leave first two words like index[0 and 1]
         print(i)
"""

#4        Remove first n characters from a string (count = n)

"""
def remove_char(str,count):
         print("Original = ", str)
         size = str[count:]
         return size

str = input("Enter a String = ")
count = int(input("Enter count of a character you want to remove = "))

Result = remove_char(str, count)
print(Result)
"""
 
 #5      Check if the first and last number of a list is the same.
"""
def first_last_same(Value_List):
         print(Value_List)
         
         num1 = Value_List[0]
         num2 = Value_List[-1]
         
         if num1 == num2:
                  return True
         else:
                  return False


Result = []
Value_List = input("Enter the value = ")
Result = first_last_same(Value_List.split())
print(Result)
"""

#6       Display numbers divisible by 5 from a list.
"""
numlist = [10, 23, 11, 50]
print(numlist)
for num in numlist:
         if num%5==0:
                  print(num)

"""
#7       Return the count of a given substring from a string

"""
#using count method
str = input("Enter the Sentence = ")
str2 = input("Enter the string wanna find = ")
cunt = str.count(str2)
print(cunt)
"""

#using without string method
"""
def str_count(statement):
         print("Original Statement = ",statement)
         count = 0
         
         strng = input("word = ")
                  
         for i in range(len(statement)-1):
             count += statement[i: i+4] == strng
         return count

statement = input("Enter the statement = ")
count = str_count(statement)
print(count)
"""      
            
  
#8       Print following pattern
# 1
# 22
# 333
# 4444
# 55555
"""
number = int(input("Enter the range = "))
for num in range(number+1):
         for i in range(num):
                  print(num, end=" ") #print number
                  
         print("\n")
"""

#9  Check the Palindrome Number:
"""
def palindrome(number):
    print("Original Number = ", number)
    original_num = number
    
    #reverse
    reverse_number = 0
    while number > 0:                                            #number = 101
        reminder = number % 10                                   #reminder = 1 
        reverse_number = (reverse_number * 10) + reminder        #RN = 1
        number = number // 10                                    #number = 101 // 10 = 10        
    #check
    if original_num == reverse_number:
        print("Its palindrome")
    else:
        print("Its Not palindrome")
        
number = int(input("Enter the Number = "))
Result = palindrome(number)
"""
#10     Create a new list from a two list using the following condition
        #new list contain odd number from first list and even from second
"""
def merge_list(list1, list2):
    result_list = []
    
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
            
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
            
    return result_list                              
            
list1 = []
list1 = [int(item) for item in input("Enter the list1 items : ").split()]

list2 = []
list2 = [int(item) for item in input("Enter the list2 items : ").split()]

print("Value of merge list = ",  merge_list(list1, list2))
"""

#11      Write a program to extract each digit from an integer in the reverse order

"""
number = int(input("Enter the number = "))
print("Original Number = ", number)

while number > 0:           
    digit = number % 10     
    number = number // 10   
    
    print(digit, end=" ")
"""

#12   Calculate Income tax
"""
income = int(input("Enter the income = "))
tax_payable = 0
print("Given income = ", income)

if income <= 10000:
    tax_payable = 0
    
elif income <= 20000:
    x=income - 10000
    tax_payable = x*10/100
    
else:
    tax_payable = 0
    tax_payable = 10000 * 10 /100
    
    tax_payable += (income - 20000)*20/100
    
print(tax_payable)
"""

#13     Print Multiplication
"""
start = int(input("enter the start number = "))
end = int(input("enter the end number = "))
for i in range(start,end+1):
    for j in range(start, end+1):
        print(i*j, end=" ")
    print("\t\t")
"""

#14     Print downward:
# *****
# ****
# ***
# **
# *
"""
number = int(input("enter the count = "))

for row in range(number, 0, -1):  #range (number=5, stop till 0 row, step = -1)
    for col in range(0, row): #range (start =0, stop =row)
        print("*", end=" ")
    print(" ")
"""

#15     Write a Function called exponent(base,exp) that returns an int value of base raise to the power of exp.
"""
base = int(input("Enter the Base value = "))
exp = int(input("Enter the exponential value = "))

Result = base**exp

print(base, " raise to the power of ", exp, " = " ,Result)

"""