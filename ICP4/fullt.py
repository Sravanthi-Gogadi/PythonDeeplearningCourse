# import base class Employee using the concept of inheritance
from emp import Employee
# create a child class
class Fulltime(Employee):
    # define the default constructor for the class and pass the arguments
    def __init__(self,name,family,salary,department):
        Employee.__init__(self, name, family, salary, department)

    def working_hours(self,start,end):
        print("{} working hours today are {} a.m to {} p.m".format(self._n,start,end))

if __name__ == "__main__":
    # create a instance and pass the parameters to base class
    x=Employee("sravs",{'wife':5000,'child':2000},7899,"Account")
    x.avg_sal()
    x.insurance_details()
    # create an instance and pass the parameters to child class
    y= Fulltime("sandy",{'wife':5000,'child':2000},9999, "Management")
    y.avg_sal()
    # print the insurance details
    y.insurance_details()
    y. working_hours(8,4)

