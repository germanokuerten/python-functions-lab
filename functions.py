################################
## Python Functions - Lab
################################

## Challenges

# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# For example:

# sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_to (n):
    return sum(range(n+1))

print(sum_to(6))
print(sum_to(10))


################################

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

# For example:

# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(*args):
    nums_list = list(*args)
    print(max(nums_list))
    
largest([1, 2, 3, 4, 0])
largest([10, 4, 2, 231, 91, 54])


################################

# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# Example 1

# def occurances1(str1, str2):
#     count = 0
#     for word in str1:
#         for character in word:
#             if character == str2:
#                 count += 1
#     print(count)

# Example 2

# def occurrences2(str1, str2):
#     count = start = 0
#     while True:
#         start = str1.find(str2, start) + 1
#         if start > 0:
#             count+=1
#         else:
#             print(count)

# Example using the count() method.

def occurances(str1, str2):
    count = str1.count(str2)
    print(count)

# For example:

# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0

occurances('fleep floop', 'e')  
occurances('fleep floop', 'p')  
occurances('fleep floop', 'ee')  
occurances('fleep floop', 'fe')


################################

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

def product(*args):
    result = 1
    for x in args:
        result = result * x
    print(result)

# For example:

# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0

product(-1, 4)
product(2, 5, 5)
product(4, 0.5, 5)

