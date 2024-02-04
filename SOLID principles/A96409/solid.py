# Single Responsibility Principle (SRP) fro Report generator class
class ReportGenerator:
    def generate_report(self, employee):
        if employee.role == "Manager":
            print(f"Manager Report: {employee.name}")
        elif employee.role == "Developer":
            print(f"Developer Report: {employee.name}")
# Open/Closed Principle (OCP) for Bonus Calculator class
class BonusCalculator:
    def calculate_bonus(self, employee):
        return employee.calculate_bonus_amount()
    
# Liskov Substitution Principle (LSP) for employee class
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def calculate_bonus(self):
        pass

class Manager(Employee):
    def calculate_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")

class Developer(Employee):
    def calculate_bonus(self):
        return 500

    def code_review(self):
        print(f"{self.name} is conducting a code review.")
