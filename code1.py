
# Hello World
print("Hello world")

# Printing shapes
print(" /___/|")
print("  / |")
print(" /  |")
print("/___|")

# Variables and Data Types
character_name = "Tom"
character_age = "55"


print("There was once a man named " + character_name + ",")
print("He was " + character_age + "years old.")
print("He really liked the name " + character_name + ",")
print("But didn't like being "  + character_age + ".")

#String Manipulation
print ("Giraffe\nAcademy") # New line \n

phrase = "Shoe Academy"
print(phrase + " is cool")
print (phrase.upper().isupper())
print(len(phrase))
print (phrase[0])
print (phrase.index("c"))
print (phrase.replace("Shoe", "Sock"))


# Numbers

from math import *

print(2.0912)
print(3 / 4.5)
print (10 % 3 )

my_num = 5
print (str(my_num) + " my favorite number")
print (abs(my_num))
print(pow(3,my_num))
print (min(4,6))
print (round(3.8))

print(floor(3.7)) #Floor
print(ceil(3.7)) #Ceiling
print(sqrt(81)) #Sqrt


# Getting Imput from Users

age = input("Enter your age: ")
print("You are " + str(age) + " years old.")


#Building a Basic Calculator

num1 = input("Enter a number :")
num2 = input("Enter another number :")
result = float(num1) + float(num2)

print(result)


# Mad Libs Game

color = input("Enter a color ")
plural_noun = input("Enter a noun ")
price = input("Enter an amount ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("Salmon is " + price)



# Lists and Functions

friends = ["Kevin", "Kared", "Jim", "Oscar", "Toby", "Jim"]
lucky_numbers = [4, 8, 15, 16, 23, 42]
print(friends[:5])
friends[1] = "Micheal"
#friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(3, "Kelly")
print(friends)
friends.remove("Kelly")
print (friends)

friends.pop()
print (friends.index("Oscar"))
print (friends.count("Jim"))

friends.sort()
print (friends)
lucky_numbers.sort()
print (lucky_numbers)
lucky_numbers.reverse()
print (lucky_numbers)

friends2 = friends.copy()
print (friends2)


# Tuples

coordinates = (4, 5)
coordinates2 = [(4, 5), (14, 45), (44, 50)]
print (coordinates[1])
print (coordinates2)


# Functions

def say_hi(name, age):
    print("Hello " + name + " You are " + str(age))

say_hi("Mike", 37)
print ("Top")
say_hi("Steve", 45)
print ("Bottom")


# Return Statements

def cube(num):
    return num*num*num

print(cube(89))




# If statements

is_Male = False
is_Tall = False

if is_Male and is_Tall:
    print ("You are Male or Tall or Both")

elif is_Male and not(is_Tall):
    print("You are Male but not Tall")

elif is_Tall and not(is_Male):
    print("You are Tall but not Male")

else:
    print ("You are not Male or Tall")



# If Statements and Comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print (max_num(8,14,5))


# Building a Better Calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operator: ")


if op == "+":
    print (num1 + num2)
elif op == "-":
    print (num1 - num2)
elif op == "*":
    print (num1 * num2)
elif op == "/":
    print (num1 / num2)
else:
    print ("Invalid Operation")


# Dictionaries

monthConversations = {

    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print (monthConversations.get("dec"))


# While Loop

i = 2
while i <= 10:
    print(i)
    i += 1

print("Done with the Loop")


# Building a Guessing Game

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print ("Out of Guesses, You Lose")
else:
    print("You Win!")

print("You win!")


# For Loop

#for letter in "Giraffe Academy":
#    print(letter)


friends = ["Jim", "Karen", "Kevin"]
len(friends)
for friend in friends:
    print (friend)

for index in range(len(friends)):
    print(friends[index])
    friends[2]

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")



# Exponent Function

print (2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print (raise_to_power(3,4))


# 2D Lists and Nested Loops

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print (number_grid[2][2])

for row in number_grid:
    for col in row:
        print (col)


# Build a Translator


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print (translate(input("Enter a phrase ")))


# Try Except

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print (err)
except ValueError:
    print("Invalid Point")


# Reading Files
# r, w, a

employee_file = open("employees.txt", "r")

# print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()



# Writing to Files

employee_file = open("employees.txt", "a")

# Creating a New File

employee_file = open("employees1.txt", "a")

employee_file.write("\nToby - HR")
employee_file.write("\nKelly - Customer Service")

employee_file.close()


# Creating a HTML File

employee_file = open("index.html", "w")

employee_file.write("<p>This is HTML</p>")

employee_file.close()


# Modules and Pip

import useful_tools

print (useful_tools.roll_dice(10))

import docx


# Classes and Objects

from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Dwight", "Business", 3.8, True)

print (student2.gpa)


# Building A Multiple Choice Quiz

from Question import Question

question_prompts = [

    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n"
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n"
    "What color are strawberries?\n(a) Red\n(b) Yellow\n(c) Blue\n\n"

]

questions = [

    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),

]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")


run_test(questions)



# Object Functions

from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Dwight", "Business", 3.8, True)

print (student2.on_honor_roll())


# Inheritance

from Chef import Chef
from ChineseChef import ChineseChef


myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()


# Python Interpreter
