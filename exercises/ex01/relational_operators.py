"""This program compares two numbers with 4 different relational operators"""

__author__ = "730528210"

leftStr: str = input("What number would you like on the left-hand side?")
rightStr: str = input("What number would you like on the right-hand side?")
left: int = int(leftStr)
right: int = int(rightStr)

print("Left-hand side: " + leftStr)
print("Right-hand side: " + rightStr)
print(leftStr + " < " + rightStr + " is " + str(left < right))
print(leftStr + " >= " + rightStr + " is " + str(left >= right))
print(leftStr + " == " + rightStr + " is " + str(left == right))
print(leftStr + " != " + rightStr + " is " + str(left != right))
