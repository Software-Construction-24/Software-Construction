# SRP: Separate report generation and writing logic

class ReportGenerator:
    def generate_report(self, employee):
        report_content = employee.generate_report()
        self.write_report(report_content)

    def write_report(self, content):
        print(content)

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def generate_report(self):
        raise NotImplementedError("Subclasses must implement this method")

class Manager(Employee):
    def generate_report(self):
        return f"Manager Report: {self.name}"

class Developer(Employee):
    def generate_report(self):
        return f"Developer Report: {self.name}"

if __name__ == "__main__":
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    report_generator = ReportGenerator()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)
