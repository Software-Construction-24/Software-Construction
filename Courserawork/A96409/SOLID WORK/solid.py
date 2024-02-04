# (SRP )
class ReportGenerator:
    def generate_report(self, employee):
        if employee.role == "Manager":
            print(f"Manager Report: {employee.name}")
        elif employee.role == "Developer":
            print(f"Developer Report: {employee.name}")
# (Open closed Principle)
class BonusCalculator:
    def calculate_bonus(self, employee):
        return employee.calculate_bonus()
# {LSP}
class Employee:
    def calculate_bonus(self):
        pass

class Manager(Employee):
    def calculate_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")
# (ISP Refactored)
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Worker(Workable, Eatable):
    pass
