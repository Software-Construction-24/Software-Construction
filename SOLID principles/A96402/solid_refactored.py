from abc import ABC, abstractmethod

# Interface for report generation
class Reportable(ABC):
    @abstractmethod
    def generate_report(self):
        pass

# Interface for bonus calculation
class BonusCalculatable(ABC):
    @abstractmethod
    def calculate_bonus(self):
        pass

# Class responsible for generating and writing reports
class ReportGenerator:
    def generate_report(self, reportable):
        # Generate the report content using the provided reportable object
        report_content = reportable.generate_report()
        # Write the report to the console
        self.write_report(report_content)

    def write_report(self, content):
        # Placeholder method for writing the report content (could be extended for different output mechanisms)
        print(content)

# Manager class implementing report generation and bonus calculation
class Manager(Reportable, BonusCalculatable):
    def __init__(self, name):
        self.name = name

    def generate_report(self):
        return f"Manager Report: {self.name}"

    def calculate_bonus(self):
        return 1000

# Developer class implementing report generation and bonus calculation
class Developer(Reportable, BonusCalculatable):
    def __init__(self, name):
        self.name = name

    def generate_report(self):
        return f"Developer Report: {self.name}"

    def calculate_bonus(self):
        return 500

if __name__ == "__main__":
    # Instantiate Manager and Developer objects
    manager = Manager("Alice")
    developer = Developer("Bob")

    # Instantiate the ReportGenerator
    report_generator = ReportGenerator()

    # Generate and write reports for Manager and Developer
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

    # Calculate and print bonuses for Manager and Developer
    manager_bonus = manager.calculate_bonus()
    developer_bonus = developer.calculate_bonus()

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")
