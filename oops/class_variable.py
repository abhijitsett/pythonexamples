class Employee:
    company = "ABC Corp"

    def __init__(self,name,designation):
        self.name = name
        self.designation = designation

    def info(self):
        print("Company name : {}".format(self.company))
        print("Employee name : {}".format(self.name))

    @staticmethod
    def salary(emp : "Employee")->int:
        if emp.designation == 'manager':
            sal = 100000
        else:
            sal = 50000
        return sal

    @classmethod
    def change_company(cls, new_company: str):
        cls.company = new_company

emp1 = Employee("Abhijit", "manager")
emp1.info()
sal = Employee.salary(emp1)
print("Employee salary : ",sal)

Employee.change_company("XYZ") 
emp1.info()
