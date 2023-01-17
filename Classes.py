# using inheritance to pass value to a another class as well via one class

class Person(object):
    # as init in Oython is known as constructor like CPP
    def __init__(self, name, enrol_id):
        self.name=name
        self.enrol_id=enrol_id

    def display(self):
        print(self.name)
        print(self.enrol_id)

# child class that use parent properties
class Employee(Person):
    # It is ( INHERITANCE )inheriting the property of Person as we use Aggregation in CPP
    def __init__(self, name, enrol_id, salary, post ):
        self.salary=salary
        self.post=post
        Person.__init__(self, name, enrol_id )
    def display(self):
        print("Employee class is used here...")
    def detail(self):
        print("Name of Employee is {} ".format(self.name))
        print("Enrollment ID of Employee is {} pkr".format(self.enrol_id))
        print("Salary of Employee is {}".format(self.salary))
        print("Designation of Employee is {}".format(self.post))

# main portion
x=Employee("Zain", 181018, 35000, "Software Engineer")
# as we declare an object of class Employee
x.detail()
x.display()

#Now using polymorphism here
y=Person("ZZZ", 180998)
y.display()





