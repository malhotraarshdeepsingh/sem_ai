# Assignments for Learn Python Course

# CHAPTER 1 : HELLO WORLD

# 1.1 : WAP to print your name three times.

name = "Arshdeep Singh Malhotra"
print(name)
print(name)
print(name)


# -------------------------------------------------------------------------------------------------------------------------------------
# CHAPTER 2 : ADD NUMBERS AND CONCATENATE STRINGS 

# 2.1 : WAP to add three numbers and print the result.

num1 = 5
num2 = 10
num3 = 15

result = num1 + num2 + num3
print(f"The sum of {num1}, {num2}, and {num3} is: {result}")


# 2.2 : WAP to concatinate three strings and print the result.

str1 = "Hello"
str2 = "World"
str3 = "Python"

result = str1 + str2 + str3
print(f"{str1} + {str2} + {str3} = {result}")


# -------------------------------------------------------------------------------------------------------------------------------------
# CHAPTER 4 : LOOPS

# 4.1 : WAP to print the table of 7, 9.

def print_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

print_table(7)
print_table(9)


# 4.2 : WAP to print the table of n where n is taken from user input.

n = int(input("Enter a number: "))
print_table(n)


# 4.3 : WAP to add all the numbers from 1 to n where n is taken from user input.

n = int(input("Enter a number: "))
sum = sum(range(1, n + 1))
print(f"The sum of numbers from 1 to {n} is {sum}")


# -------------------------------------------------------------------------------------------------------------------------------------
# CHAPTER 5 : CONDITIONAL STATEMENTS

# 5.1 : WAP to find max among three numbers given by user input.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

max_num = max(num1, num2, num3)
print(f"The maximum number among {num1}, {num2}, and {num3} is: {max_num}")


# 5.2 : WAP to add all the numbers which are divisible by 7 and 9 from 1 to n where n is taken from user input.

n = int(input("Enter a number: "))
sum_divisible = sum(i for i in range(1, n + 1) if i % 7 == 0 or i % 9 == 0)
print(f"The sum of numbers from 1 to {n} that are divisible by 7 or 9 is: {sum_divisible}")


# 5.3 : WAP to add all prime numbers from 1 to n where n is taken from user input.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
sum_primes = sum(i for i in range(1, n + 1) if is_prime(i))
print(f"The sum of prime numbers from 1 to {n} is: {sum_primes}")


# -------------------------------------------------------------------------------------------------------------------------------------
# CHAPTER 6 : FUNCTIONS

# 6.1 : WAP using function that add all the numbers from 1 to n where n is taken from user input.

def sum_numbers(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s

n = int(input("Enter a number: "))
print(f"The sum of numbers from 1 to {n} is: {sum_numbers(n)}")


# 6.2 : WAP using function that add all prime numbers from 1 to n where n is taken from user input.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_prime_numbers(n):
    return sum(i for i in range(1, n + 1) if is_prime(i))

n = int(input("Enter a number: "))
print(f"The sum of prime numbers from 1 to {n} is: {sum_prime_numbers(n)}")


# -------------------------------------------------------------------------------------------------------------------------------------