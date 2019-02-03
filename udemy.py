def stringify(name = "Jonas", age = "Unknown"):
    print(name, "is walking for", age, "years")
    # Default Arguments

stringify(27,2)
stringify("Vishrut", 22)
stringify(True, None)
stringify(age="545", name="Nicholas Flamel") #KeyWord Arguments

#Infinite Arguments
def infinit(*people):
    for person in people:
        print("This person is", person)

infinit("Jason", "Mike", "Ashley", "Vishrut", "Joanne")

def maths(n1, n2):
    return n1 + n2

m1 = maths(12, 3)
m2 = maths(23, 34)

print("Sum1:", m1, "Sum2:", m2)