# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 21:44:05 2022

@author: user
"""
#Exercise 1: finding the maximum of three numbers
def max_of_two(x,y):
    if x>y:
        return x
    return y

print(max_of_two(2,3))

def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))

print(max_of_three(3,4,6))

#Exercise2: Summing the numbers in a list

def sum_of_list(example_list):
    sum = 0
    i=0
    while i < len(example_list):
        x=example_list[i]
        sum = sum+x
        i+=1
    print(sum)
sum_of_list([1,2,3,4,5])    



#Exercise4: Reversing a string 
def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index >0:
        rstr1 += str1[index-1]
        index = index-1
    return rstr1  
print(string_reverse('1234abcd'))

#Exercise 5: Counting the number of lower and uppercase in a word
def string_test(s):
    d = {'UPPER_CASE': 0, 'LOWER_CASE': 0}
    for c in s:
        if c.isupper():
            d['UPPER_CASE']+=1
        elif c.islower():
            d['LOWER_CASE']+=1
        else:
            pass
        
    print("Original String", s)
    print("The number of uppercase letter is:", d['UPPER_CASE'])
    print('The number of lowercase letters is:', d['LOWER_CASE'] )        

string_test('The quick Brown Fox')

#Exercise 8: Getting Unique elements from a list:
def unique_list(sample_list):
        sample_list = set(sample_list)
        sample_list = list(sample_list)
        return sample_list
print(unique_list([1,2,3,3,3,3,4,5])) 

def unique_list2(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list2([1,2,3,3,3,3,4,5])) 

#Exercise 9: How to check if a number is a prime number
def test_prime(n):
    if n == 1:
        return False
    elif n==2:
        return False
    else:
        for x in range(2,n):
            if (n % x == 0):
                return False
        return True 
test_prime(15)
# Exercise 10: List all the prime factors of a number 

# Exercise 11: Print all the even numbers in a list 
def even_number(l):
    List = []
    for n in l:
        if n % 2 == 0:
            List.append(n)
    return List
print(even_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Exercise 11: Check if a number is a perfect number 
def perfect_number(n):
    sum = 0
    for i in range(1,n):
        if n % i ==0:
            sum = sum + i
    print(sum)
    if n == sum:
        print('The number is a perfect number')
    else:
        print('The number is not a perfect number')

perfect_number(6)

# Exercise 12: Check whether a string is palindrome 
def is_palindrome(string):
    rev_string = string_reverse(string)
    if string == rev_string:
        print('String is Palindrome')
    else: 
        print('String is not PaLindrome')
is_palindrome('civic')

#Exercise 13: Print lines of a Pascal's triangle 

#Exercise 14: Check if a sentence is a panagram
import string,sys 
def is_pangram(str1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
print ( is_pangram('The quick brown fox jumps over the lazy dog')) 

#Exercise 15: Sorting out inputs seperated using hyphen
#items = [n for n in input().split('-')]
#items.sort()
#print('-'.join(items))

items = ['apple','zip','banana']
items.sort()
print(items)
print('-'.join(items))

#Exercise 16: Writing a list of square numbers
x= [i**2 for i in range(31)]
print(x)

# Make a chain of function decorators in python
def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello())

# Using decorators
def inc(x):
    return x+1
def dec(x):
    return x-1

def operate(func,x):
    result = func(x)
    return result

print(operate(inc,3))
print(operate(dec,3))