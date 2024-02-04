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
