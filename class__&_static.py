import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # creating a class method, as it effect the functionality of the lass

    # as it create the object by birth year
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, datetime.date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


# main file
emp1 = Person("Zain", 22)
emp2 = Person.from_birth_year("xyz", 2005)

print("Age of Employee# 1 [{0}] is {1}".format(emp1.name, emp1.age))
print("As age accordingly to second object is: {}".format(emp2.age))

# printing the result using the objects and directly by using class itself
# print(Person.is_adult(22))
dummy = Person.is_adult(22)
if dummy:
    print("Person Age is greater then 18")
else:
    print("person is not adult now ")





