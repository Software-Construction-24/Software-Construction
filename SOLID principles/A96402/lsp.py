# LSP: Use interfaces for employee classes

from abc import ABC, abstractmethod

class Reportable(ABC):
    @abstractmethod
    def generate_report(self):
        pass

class BonusCalculatable(ABC):
    @abstractmethod
    def calculate_bonus(self):
        pass

class Employee(Reportable, BonusCalculatable, ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Manager(Employee):
    def generate_report(self):
        return f"Manager Report: {self.name}"

    def calculate_bonus(self):
        return 1000

class Developer(Employee):
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
