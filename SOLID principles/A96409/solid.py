#Sarah Nsereko A96409 

from abc import ABC, abstractmethod

class Employee:
    def _init_(self, name, role):
        self.name = name
        self.role = role

class Report:
    def _init_(self, report_writer):
        self.report_writer = report_writer

    def generate_report(self, employee):
        self.report_writer.write_report(employee)

class ReportWriter(ABC):
    @abstractmethod
    def write_report(self, employee):
        pass

class ManagerReportWriter(ReportWriter):
    def write_report(self, manager):
        print(f"Manager Report: {manager.name}")

class DeveloperReportWriter(ReportWriter):
    def write_report(self, developer):
        print(f"Developer Report: {developer.name}")

class EmployeeBonusCalculator(ABC):
    @abstractmethod
    def calculate_bonus(self):
        pass

class ManagerBonusCalculator(EmployeeBonusCalculator):
    def calculate_bonus(self):
        return 1000

class DeveloperBonusCalculator(EmployeeBonusCalculator):
    def calculate_bonus(self):
        return 500

class Manager(Employee):
    def calculate_bonus(self):
        calculator = ManagerBonusCalculator()
        return calculator.calculate_bonus()

    def manage_team(self):
        print(f"{self.name} is managing the team.")

class Developer(Employee):
    def calculate_bonus(self):
        calculator = DeveloperBonusCalculator()
        return calculator.calculate_bonus()

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

if _name_ == "_main_":
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    report_writer = ManagerReportWriter()  # Choose appropriate report writer
    report_generator = Report(report_writer)
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

    bonus_calculator = BonusCalculator()
    manager_bonus = manager.calculate_bonus()
    developer_bonus = developer.calculate_bonus()

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    manager.manage_team()
    developer.code_review()
