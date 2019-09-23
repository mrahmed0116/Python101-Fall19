# Python 101 week 3 challenges - 9/18/19
# Python 3

# 1.) Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((8, 2, 3, -1, 7)))


# 2.) Write a Python program that accepts a string and calculate the number of digits and letters.
# - Sample Data : Python 3.2
#    - Expected Output:
#    - Letters 6
#    - Digits 2

def count_alpha_num():
    s= input("Input a string: ")
    d = 0
    l = 0
    for char in s:
        if char.isdigit():
            d=d+1
        elif char.isalpha():
            l=l+1
        else:
            pass
    print("Letters", l)
    print("Digits", d)
count_alpha_num()


# 3.) Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14

Circle1 = Circle(8) # circle object with radius 8
print(Circle1.area())
print(Circle1.perimeter())

Circle2 = Circle(5) # circle object with radius 5
print(Circle2.area())
print(Circle2.perimeter())

