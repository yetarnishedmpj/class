import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def __repr__(self):
        return f"Employee({self.empcode}, {self.empname}, {self.doj}, {self.salary})"

emp = Employee(101, 'John Doe', '2020-01-01', 50000)

with open('employee.pkl', 'wb') as f:
    pickle.dump(emp, f)

with open('employee.pkl', 'rb') as f:
    loaded_emp = pickle.load(f)
    print("Deserialized Employee:", loaded_emp)
