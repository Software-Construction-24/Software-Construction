# OCP: Introduce interfaces for report generation and bonus calculation

from abc import ABC, abstractmethod

class Reportable(ABC):
    @abstractmethod
    def generate_report(self):
        pass

class BonusCalculatable(ABC):
    @abstractmethod
    def calculate_bonus(self):
        pass

class ReportGenerator:
    def generate_report(self, reportable):
        report_content = reportable.generate_report()
        self.write_report(report_content)

    def write_report(self, content):
        print(content)

class Manager(Employee, Reportable, BonusCalculatable):
    def generate_report(self):
        return f"Manager Report: {self.name}"

    def calculate_bonus(self):
        return 1000

class Developer(Employee, Reportable, BonusCalculatable):
    def generate_report(self):
        return f"Developer Report: {self.name}"

    def calculate_bonus(self):
        return 500

if __name__ == "__main__":
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    report_generator = ReportGenerator()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)
