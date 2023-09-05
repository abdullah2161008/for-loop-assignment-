#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Basic Level:


# In[2]:


#1. Write a Python program to print the numbers from 1 to 10 using a `for` loop.


# In[3]:


for i in range(1,11):
    print(i)


# In[4]:


#2. Create a program that calculates the sum of all numbers in a list using a `for` loop.


# In[5]:


numbers=[1,2,3,4,5,6,7,8,9,10]
sum_of_numbers=0
for num in numbers:
    sum_of_numbers=sum_of_numbers+num
print(sum_of_numbers)


# In[6]:


#3. Write a program to print the characters of a string in reverse order using a `for` loop.


# In[7]:


string="Hello,World!"
reversed_string=""
for characters in reversed(string):
    reversed_string=reversed_string+characters
print(reversed_string)


# In[8]:


#4. Develop a program that finds the factorial of a given number using a `for` loop.


# In[61]:


n = int (input ("Enter a number: "))
factorial = 1
if n >= 1:
    for i in range (1, n+1):
        factorial=factorial *i
print("Factorial of the given number is: ", factorial)


# In[ ]:


#5. Create a program to print the multiplication table of a given number using a `for` loop.


# In[1]:


number=int(input("Enter the number for multiplication table:"))
for i in range(1,11):
    print(number,"x",i,"=",number*i)


# In[2]:


#6. Write a program that counts the number of even and odd numbers in a list using a `for` loop.


# In[12]:


numbers=[1,2,3,4,5,6,7,8,9,10]
even_count=0
odd_count=0
for num in numbers:
    if num%3==0:
        even_count+=1
    else:
        odd_count+=1
print(f"Even Count:{even_count}")
print(f"Odd Count:{odd_count}")
   


# In[13]:


#7. Develop a program that prints the squares of numbers from 1 to 5 using a `for` loop.


# In[21]:


for i in range(1,6):
    print(i**2)


# In[22]:


#8. Create a program to find the length of a string without using the `len()` function.


# In[27]:


string="my name is abdullah"
lenght=0
for i in string:
    lenght+=1
print(lenght)


# In[28]:


#9. Write a program that calculates the average of a list of numbers using a `for` loop.


# In[36]:


numbers=[10,20,30,40,50]
total_sum=0
count=0
for num in numbers:
    total_sum+=num
    count+=1
if count > 0:
    average = total_sum / count
else:
    average = 0
print("The average of the numbers is:", average)


# In[37]:


#10. Develop a program that prints the first `n` Fibonacci numbers using a `for` loop.


# In[38]:


def print_fibonacci(n):
    fib1 = 0
    fib2 = 1

    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print(fib1)
    elif n == 2:
        print(fib1)
        print(fib2)
    else:
        print(fib1)
        print(fib2)
        for _ in range(2, n):
            next_fib = fib1 + fib2
            print(next_fib)
            fib1, fib2 = fib2, next_fib
n = 10
print_fibonacci(n)


# In[1]:


#Intermediate Level:


# In[2]:


#11. Write a program to check if a given list contains any duplicates using a `for` loop.


# In[12]:


my_list = [1, 2, 3, 4, 5,2]

has_duplicates = False

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
            has_duplicates = True
            break
    if has_duplicates:
        break  

if has_duplicates:
    print("The list contains duplicates")
else:
    print("The list does not contain duplicates")


# In[11]:


#12. Create a program that prints the prime numbers in a given range using a `for` loop.


# In[27]:


for i in range(2, 101): 
    is_prime = True  
    for x in range(2, i):  
        if i % x == 0:
            is_prime = False  
            break  

    if is_prime:
        print(i)  


# In[28]:


#13. Develop a program that counts the number of vowels in a string using a `for` loop.


# In[32]:


str1="my name is abdullah khan"
vowels_count=0
st1=str1.lower()
vowels="aeiou"

for char in str1:
    if char in vowals:
        vowels_count +=1
print("string contains ",vowels_count,"vowels.")


# In[33]:


# 14. Write a program to find the maximum element in a 2D list using a nested `for` loop.


# In[34]:


matrix = [
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
]

max_element = matrix[0][0]

for row in matrix:
    for element in row:
        if element > max_element:
            max_element = element

print("The maximum element in the 2D list is:", max_element)


# In[35]:


#15. Create a program that removes all occurrences of a specific element from a list using a `for` loop.


# In[41]:


my_list = [1, 2, 3, 2, 4, 5, 2]

element_to_remove = 2

new_list = []

for item in my_list:
    if item != element_to_remove:
        new_list.append(item)

my_list = new_list

print("List after removing all occurrences of", element_to_remove, ":", my_list)


# In[ ]:


#16. Develop a program that generates a multiplication table for numbers from 1 to 5 using a nested `for` loop.


# In[42]:


start_num = 1
end_num = 5


for i in range(start_num, end_num + 1):
    print(f"Multiplication table for {i}:")

   
    for j in range(1, 11):  
        product = i * j
        print(f"{i} x {j} = {product}")

   
    print()


# In[43]:


#17. Write a program that converts a list of Fahrenheit temperatures to Celsius using a `for` loop.


# In[47]:


fahrenheit_temperatures = [32, 68, 100, 212, 50]
celsius_temperature=[]
for fahrenheit in fahrenheit_temperatures:
    celsius=(fahrenheit-32)*5/9
    celsius_temperature.append(celsius)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)
print("Celsius Temperatures:", celsius_temperature)


# In[48]:


#18. Create a program to print the common elements from two lists using a `for` loop.


# In[49]:


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = []

for element1 in list1:
    for element2 in list2:
        if element1 == element2:
            common_elements.append(element1)
            break  
print("Common elements in the two lists:", common_elements)


# In[50]:


#19. Develop a program that prints the pattern of right-angled triangles using a `for` loop. Use ‘*’ to draw the
#pattern


# In[53]:


for i in range(1,6):
  
   for j in range(i):
       print('*', end=' ')  
   print()


# In[54]:


#20. Write a program to find the greatest common divisor (GCD) of two numbers using a `for` loop.


# In[56]:


num1 = 23
num2 =43
min_num = min(num1, num2)
gcd = 1
for i in range(1, min_num + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print(f"The greatest common divisor (GCD) of {num1} and {num2} is {gcd}")


# In[58]:


#Advanced Level:


# In[13]:


#21. Create a program that calculates the sum of the digits of numbers in a list using a list comprehension.


# In[16]:


numbers = [123, 45, 6789, 12, 3]

digit_sums = []
for num in numbers:
    num_str = str(num)
    num_sum = 0
    for digit in num_str:
        num_sum += int(digit)
    
    digit_sums.append(num_sum)
print("Original numbers:",numbers)
print("Sum of digits for each number:", digit_sums)


# In[ ]:


#22. Write a program to find the prime factors of a given number using a `for` loop and list comprehension.


# In[19]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

prime_factors = [x for x in range(2, n + 1) if n % x == 0 and is_prime(x)]

print(f"Prime factors of {n} are:", prime_factors)


# In[20]:


#23. Develop a program that extracts unique elements from a list and stores them in a new list using a list
#comprehension.


# In[21]:


original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

unique_list = [x for x in original_list if original_list.count(x) == 1]

print("Original List:", original_list)
print("Unique Elements List:", unique_list)


# In[22]:


#24. Create a program that generates a list of all palindromic numbers up to a specified limit using a list
#comprehension.


# In[24]:


def is_palindrome(num):
    return str(num) == str(num)[::-1]

limit = 550  

palindromic_numbers = []

for num in range(1, limit + 1):
    if is_palindrome(num):
        palindromic_numbers.append(num)

print("Palindromic Numbers up to", limit, ":", palindromic_numbers)


# In[ ]:





# In[25]:


#25. Write a program to flatten a nested list using list comprehension.


# In[26]:


nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flattened_list = []

for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)

print("Flattened List:", flattened_list)


# In[ ]:


#26. Develop a program that computes the sum of even and odd numbers in a list separately using list
#comprehension.


# In[32]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)


# In[ ]:


#27. Create a program that generates a list of squares of odd numbers between 1 and 10 using list
#comprehension.


# In[28]:


odd_squares = []

for num in range(1, 11):
    if num % 2 != 0:
        odd_squares.append(num ** 2)

print("Squares of odd numbers:", odd_squares)


# In[ ]:


#28. Write a program that combines two lists into a dictionary using list comprehension.


# In[29]:


keys = ["a", "b", "c"]
values = [1, 2, 3]

result_dict = {}

for i in range(len(keys)):
    result_dict[keys[i]] = values[i]

print("Combined Dictionary:", result_dict)


# In[ ]:


#29. Develop a program that extracts the vowels from a string and stores them in a list using list comprehension.


# In[30]:


text = "Hello, World!"

vowels = []

for char in text:
    if char.lower() in "aeiou":
        vowels.append(char)

print("Vowels in the string:", vowels)


# In[ ]:


#30. Create a program that removes all non-numeric characters from a list of strings using list comprehension.


# In[31]:


strings = ["abc", "123", "xyz456", "789"]

numeric_chars = []

for string in strings:
    numeric_chars.extend([char for char in string if char.isnumeric()])

print("Numeric characters in the list:", numeric_chars)


# In[33]:


#Challenge Level:


# In[34]:


#31. Write a program to generate a list of prime numbers using the Sieve of Eratosthenes algorithm and list
#comprehension.


# In[44]:


def sieve_of_eratosthenes(n):
    # Create a boolean list "is_prime" and initialize all entries as True
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    # Mark non-prime numbers
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    # Use list comprehension to generate the list of prime numbers
    prime_numbers = [i for i in range(2, n + 1) if is_prime[i]]

    return prime_numbers

# Specify the limit for prime numbers
limit = int(input("Enter the limit for prime numbers: "))
prime_list = sieve_of_eratosthenes(limit)
print("Prime numbers up to", limit, "are:", prime_list)


# In[35]:


#32. Create a program that generates a list of all Pythagorean triplets up to a specified limit using list
#comprehension.


# In[45]:


def generate_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= limit:
                triplets.append((a, b, int(c)))
    return triplets

# Specify the limit for Pythagorean triplets
limit = int(input("Enter the limit for Pythagorean triplets: "))
triplets = generate_pythagorean_triplets(limit)
print("Pythagorean triplets up to", limit, "are:", triplets)


# In[36]:


#33. Develop a program that generates a list of all possible combinations of two lists using list comprehension.


# In[54]:


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

combinations = [(x, y) for x in list1 for y in list2]
print(combinations)


# In[37]:


#34. Write a program that calculates the mean, median, and mode of a list of numbers using list
#comprehension.


# In[53]:


import statistics

numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

mean = sum(numbers) / len(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)


# In[38]:


#35. Create a program that generates Pascal's triangle up to a specified number of rows using list
#comprehension.


# In[52]:


def generate_pascals_triangle(rows):
    triangle = [[1]]
    for i in range(1, rows):
        previous_row = triangle[-1]
        new_row = [1] + [previous_row[j] + previous_row[j + 1] for j in range(len(previous_row) - 1)] + [1]
        triangle.append(new_row)
    return triangle

rows = int(input("Enter the number of rows for Pascal's triangle: "))
pascals_triangle = generate_pascals_triangle(rows)
for row in pascals_triangle:
    print(row)


# In[39]:


#36. Develop a program that calculates the sum of the digits of a factorial of numbers from 1 to 5 using list
#comprehension.


# In[50]:


import math

factorial_sums = [sum(int(digit) for digit in str(math.factorial(n))) for n in range(1, 6)]
print("Sum of digits of factorials from 1 to 5:", factorial_sums)


# In[40]:


#37. Write a program that finds the longest word in a sentence using list comprehension.


# In[49]:


sentence = "This is a sample sentence with some long words."

words = sentence.split()
longest_word = max(words, key=lambda word: len(word))
print("Longest word in the sentence:", longest_word)


# In[41]:


#38. Create a program that filters a list of strings to include only those with more than three vowels using list
#comprehension.


# In[48]:


words = ["apple", "banana", "cherry", "elephant", "frog"]

filtered_words = [word for word in words if sum(1 for letter in word if letter in "AEIOUaeiou") > 3]
print("Words with more than three vowels:", filtered_words)


# In[42]:


#39. Develop a program that calculates the sum of the digits of numbers from 1 to 1000 using list
#comprehension.


# In[47]:


digit_sums = [sum(int(digit) for digit in str(n)) for n in range(1, 1001)]
print("Sum of digits of numbers from 1 to 1000:", digit_sums)


# In[43]:


#40. Write a program that generates a list of prime palindromic numbers using list comprehension.


# In[46]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

prime_palindromes = [num for num in range(1, 1000) if is_prime(num) and is_palindrome(num)]
print("Prime palindromic numbers:", prime_palindromes)


# In[ ]:




