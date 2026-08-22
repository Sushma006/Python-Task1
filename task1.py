# Task 1 - Python Programming Internship
# Maincrafts Technology
# 1. Sum of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
print("\n-----------------------")
# 2. Odd or Even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
print("\n-----------------------")
# 3. Factorial
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)
print("\n-----------------------")
# 4. Fibonacci Series
n = int(input("How many terms? "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("\n\n-----------------------")
# 5. Reverse String
text = input("Enter a string: ")
print("Reversed String:", text[::-1])
print("\n-----------------------")
# 6. Palindrome
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
print("\n-----------------------")
# 7. Leap Year
year = int(input("Enter Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is Leap Year")
else:
    print(year, "is Not Leap Year")
print("\n-----------------------")
# 8. Armstrong Number
num = int(input("Enter a number: "))
order = len(str(num))
total = 0
temp = num
while temp > 0:
    digit = temp % 10
    total += digit ** order
    temp //= 10
if total == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")
