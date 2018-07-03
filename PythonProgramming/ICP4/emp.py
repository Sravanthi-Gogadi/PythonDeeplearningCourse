# Define a class named Employer
class Employee(object):
    # declare a data member named employee_count
    employee_count = 30

# Define the constructor for the class and pass the required arguments
    def __init__(self, name, family, salary, department):
        self._n = name
        self._f = family
        self._s = salary
        self._d = department
# Provide the function definiton for average salary

    def avg_sal(self):
        average_sal = self._s / self.employee_count
        print("The average value of {} is {}".format(self._n,average_sal))
        print(self._f)

# Print the insurance details of individual member

    def insurance_details(self):
        for k, v in self._f.items():
            print("{} has insurance of ${}".format(k,v))

if __name__ == "__main__":
    # create an object e to call the class and pass the arguments
    e = Employee("sravs",{'wife':5000,'child':2000},7899,"Account")
    # call the function
    e.avg_sal()
    e.insurance_details()

