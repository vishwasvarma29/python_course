# my_programs.py

def happy_number():
    print("Program: Check if a Number is a Happy Number")
    print("""
def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1
    """)
    print("Test Case 1: is_happy_number(19) -> True")
    print("Test Case 2: is_happy_number(4) -> False")
    print("Explanation: A Happy Number repeatedly replaces itself with the sum of the squares of its digits until it reaches 1 (happy) or loops endlessly (unhappy).")


def string_permutations():
    print("Program: Generate All Permutations of a String")
    print("""
from itertools import permutations
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]
    """)
    print("Test Case 1: string_permutations('abc') -> ['abc','acb','bac','bca','cab','cba']")
    print("Test Case 2: string_permutations('ab') -> ['ab','ba']")
    print("Explanation: Uses itertools.permutations to generate all possible arrangements of the given string.")


def count_vowel_words():
    print("Program: Count Words Starting with a Vowel")
    print("""
def count_vowel_words(sentence):
    vowels = 'aeiouAEIOU'
    return sum(1 for word in sentence.split() if word[0] in vowels)
    """)
    print("Test Case 1: count_vowel_words('An elephant is outside') -> 4")
    print("Test Case 2: count_vowel_words('Python is fun') -> 1")
    print("Explanation: Splits the sentence into words and counts how many start with a vowel.")


def number_to_words():
    print("Program: Convert Number to Words")
    print("""
import inflect
p = inflect.engine()
def number_to_words(num):
    return p.number_to_words(num)
    """)
    print("Test Case 1: number_to_words(123) -> 'one hundred and twenty-three'")
    print("Test Case 2: number_to_words(1005) -> 'one thousand and five'")
    print("Explanation: Uses the inflect library to convert numbers to their English word representation.")


def pascal_triangle():
    print("Program: Print Pascal's Triangle")
    print("""
def pascal_triangle(n):
    for i in range(n):
        print(' ' * (n - i), end='')
        num = 1
        for j in range(i + 1):
            print(num, end=' ')
            num = num * (i - j) // (j + 1)
        print()
    """)
    print("Test Case 1: pascal_triangle(3) -> \n   1\n  1 1\n 1 2 1")
    print("Test Case 2: pascal_triangle(5) -> prints 5 rows of Pascal's Triangle")
    print("Explanation: Uses combination formula to generate Pascal's Triangle row by row.")


def smith_number():
    print("Program: Check if a Number is a Smith Number")
    print("""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors_sum(num):
    factors = []
    i = 2
    while num > 1:
        if num % i == 0:
            factors.append(i)
            num //= i
        else:
            i += 1
    return sum(sum(int(d) for d in str(f)) for f in factors)

def is_smith_number(num):
    if is_prime(num):
        return False
    return sum(int(d) for d in str(num)) == prime_factors_sum(num)
    """)
    print("Test Case 1: is_smith_number(666) -> True")
    print("Test Case 2: is_smith_number(27) -> False")
    print("Explanation: A Smith Number is composite and the sum of its digits equals the sum of the digits of its prime factors.")


def longest_word():
    print("Program: Find the Longest Word in a Sentence")
    print("""
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
    """)
    print("Test Case 1: longest_word('Python programming is amazing') -> 'programming'")
    print("Test Case 2: longest_word('AI will change everything') -> 'everything'")
    print("Explanation: Splits the sentence into words and returns the one with maximum length.")


def dice_roll_game():
    print("Program: Dice Roll Game")
    print("""
import random
def dice_roll_game():
    count = 0
    while True:
        count += 1
        roll = random.randint(1, 6)
        if roll == 6:
            return count
    """)
    print("Test Case 1: dice_roll_game() -> returns number of rolls until 6 appears")
    print("Test Case 2: dice_roll_game() -> different output each run")
    print("Explanation: Simulates rolling a dice until 6 appears, counting the attempts.")


def binary_search():
    print("Program: Binary Search")
    print("""
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    """)
    print("Test Case 1: binary_search([1,3,5,7,9], 5) -> 2")
    print("Test Case 2: binary_search([2,4,6,8], 10) -> -1")
    print("Explanation: Uses the divide-and-conquer method to search for a target in a sorted list.")


def trimorphic_number():
    print("Program: Check if a Number is a Trimorphic Number")
    print("""
def is_trimorphic(num):
    return str(num**3).endswith(str(num))
    """)
    print("Test Case 1: is_trimorphic(376) -> True")
    print("Test Case 2: is_trimorphic(7) -> False")
    print("Explanation: A Trimorphic Number's cube ends with the same digits as the number itself.")
