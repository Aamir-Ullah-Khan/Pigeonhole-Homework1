# Pigeonhole Principle
# If there are more pigeons than pigeonholes, then there must be at least one pigeonhole with at least two pigeons in it.
# Theorem –
# I) If “A” is the average number of pigeons per hole, where A is not an integer then
# 1) At least one pigeon hole contains ceil[A] (smallest integer greater than or equal to A) pigeons
# 2) Remaining pigeon holes contains at most floor[A] (largest integer less than or equal to A) pigeons
# II) We can say as, if n + 1 objects are put into n boxes, then at least one box contains two or more objects.
# The abstract formulation of the principle: Let X and Y be finite sets and let f: X –> Y be a function.
# 1) If X has more elements than Y, then f is not one-to-one.
# 2) If X and Y have the same number of elements and f is onto, then f is one-to-one.
# 3) If X and Y have the same number of elements and f is one-to-one, then f is onto.
# Pigeonhole principle is one of the simplest but most useful ideas in mathematics. We will see more applications
# that proof of this theorem.

# Example: Suppose there are "n" number of people in a room. Two or more people will have same birthday.
# Solution: If number of people in room is greater than number of days in an year, then at-least two people will have
# same birthday. e.g.
# Number of people in room = n= 500
# Number of days in an year = d = 365 (normal year) or 366 (leap year)
# Number of people having same birthday = bd = n/d = 1.37
# Hence according to Pigeonhole principle ceiling for current case will be 2 i.e. two people will have same birthday.


# Starting Code
print("This program shows number of people having same birthday in a room by taking input from user\n")
option = str('y')
while option == 'y':
    print("Enter number of people in the room")
    people = int(input())
    if people < 0:
        print("Invalid Entry: Choose again")
    elif :
        #exit(1)
        print("Enter number of days in a year i.e: leap or not")
        days = int(input())
    if days < 0:
        print("Invalid Entry: Choose again")
        exit(1)
    if people <= days:
        print("Pigeon rule does not apply")
        print("People may or may not have same birthday")
    elif people > days:
        print("Pigeon rule applies")
        result1 = people % days
        result = float(people // days)
        if result1 == 0:
            print(" Minimum number of people having same birthday:\n", result)
        else:
            print("Minimum number of people having same birthday:\n ", result + 1)
    else:
        print("Invalid Input: Please select again")
    print("If you want to continue enter y or else any other character")
    option = input()
input("")
