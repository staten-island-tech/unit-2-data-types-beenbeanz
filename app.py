"""values = [1,2.23,5,7,2,30,15]
print(values[7])
for i in values:
    print(i)"""

"""x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)"""

"""def getLength():   define function                          
    msg = input("input a sentence \n")      get user input
    print(len(msg))   print length of input
getLength()"""

"""verb1 = input("input a verb in present tense\n")
verb2 = input("input a second verb in past tense\n")
noun = input("input a noun\n")
number = input("input a number\n")
celebrity = input("input a celebrity's name\n")
animal = input("input an animal\n")

Madlib = f"One day, {celebrity} was {verb1} their {animal}. The {animal} had {number} friends of the same species, and they suddenly {verb2} at {celebrity}. However, {celebrity} had a {noun} in their bag, and attacked the animals. The {animal}s ran away from fright."
print(Madlib)"""

"""def oddOrEven():
    number = int(input("Enter a number\n")) % 2
    if (number == 0):
        print("That is an even number")
    elif (number == 1):
        print("That is an odd number")
oddOrEven()"""

"""def tip(bill):
    if bill == "bad":
        print("You get a 0% tip")
    elif bill == "okay":
        print("You get a 15% tip")
    elif bill == "good":
        print("You get a 20% tip")
    elif bill == "great":
        print("You get a 25% tip")
tip("bad")"""


def factors(num):
    factorsList = []
    for i in range(1, num + 1):
        if num % i == 0:
            factorsList.append(i)
print(factors(12))




