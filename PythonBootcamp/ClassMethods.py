class Employees:
    no_of_leaves = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def display_details(self):
        print(f"{self.name} salary is {self.salary} and job role is {self.role}. No of leaves is {self.no_of_leaves}")

    @classmethod
    def change_leaves(cls, leaves):
        print("Changing no of leaves...")
        cls.no_of_leaves = leaves

    # Class Methods as alternative constructor
    @classmethod
    def from_str(cls, string):
        name, salary, job = string.split('-')
        return cls(name, int(salary), job)

    @staticmethod
    def is_jobless(salary):
        print(salary < 1)


john = Employees("John", 2000, "Instructor")
john.display_details()
john.change_leaves(12)
john.display_details()

rahul = Employees.from_str("Rahul-3000-Engineer")
rahul.display_details()

karan = Employees.from_str("Karan-0-Student")
karan.display_details()
karan.is_jobless(karan.salary)
