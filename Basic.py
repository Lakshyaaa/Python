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