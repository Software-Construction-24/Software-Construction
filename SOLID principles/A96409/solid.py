#Sarah Nsereko A96409
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

# Interface Segregation Principle (ISP) for workable class 
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Worker(Workable, Eatable):
    pass

# Dependency Inversion Principle (DIP) for switchable class
class Switchable:
    def turn_on(self):
        pass

class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.turn_on()

if __name__ == "__main__":
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    # SRP refactor
    report_generator = ReportGenerator()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

       # OCP refactor
    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)
    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

      # LSP refactor
    manager.manage_team()
    developer.code_review()