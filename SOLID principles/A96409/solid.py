# Single Responsibility Principle (SRP) fro Report generator class
class ReportGenerator:
    def generate_report(self, employee):
        if employee.role == "Manager":
            print(f"Manager Report: {employee.name}")
        elif employee.role == "Developer":
            print(f"Developer Report: {employee.name}")
