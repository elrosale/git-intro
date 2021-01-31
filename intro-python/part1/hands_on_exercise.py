"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi

print(type(pi), (pi))


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)

if i < 50:
    print("i es menor a 50")
elif i > 50:
    print("i es mayor a 50")
print("valor de i es:", i)

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(["orange", "strawberry", "banana"])

print(picked_fruit)

if picked_fruit == "orange":
    print("Fruit color is orange")
elif picked_fruit == "strawberry":
    print("Fruit color is red")
elif picked_fruit == "banana":
    print("Fruit color is yellow")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

def times(num1, num2):
    result = num1 * num2
    return result


# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", times(12, 96))

print("48 x 17 =", times(48, 17))

print("196523 x 87323 =", times(196523, 87323))
