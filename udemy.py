import datetime, pymongo, humanize
from pymongo import MongoClient


def stringify(name = "Jonas", age = "Unknown"):
    print(name, "is walking for", age, "years")
    # Default Arguments


stringify(str(27), str(2))
stringify("Vishrut", 22)
stringify(True, None)
stringify(age="545", name="Nicholas Flamel")
# KeyWord Arguments


# Infinite Arguments
def infinit(*people):
    for person in people:
        print("This person is", person)


infinit("Jason", "Mike", "Ashley", "Vishrut", "Joanne")


def maths(n1, n2):
    return n1 + n2


m1 = maths(12, 3)
m2 = maths(23, 34)

print("Sum1:", m1, "Sum2:", m2)

# Date Time
current_date = datetime.datetime.now()
print(current_date)
old_date = datetime.datetime(1986, 4, 26, 1, 23, 45)
# client = MongoClient()
# db = client.mydb
# Users = db.Users
# uid = Users.insert_one({'username': 'ids_fotowale', 'dob': old_date, 'today': current_date})
print(old_date)
print(humanize.naturaltime(current_date - old_date))
