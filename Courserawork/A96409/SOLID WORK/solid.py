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
# Dip refactor
class Switchable:
    def turn_on(self):
        pass

class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.turn_on()


# SRP part 2
class ManagerReportWriter:
    def write_report(self, manager):
        print(f"Manager Report: {manager.name}")

class DeveloperReportWriter:
    def write_report(self, developer):
        print(f"Developer Report: {developer.name}")

class ReportGenerator:
    def generate_report(self, employee, report_writer):
        report_writer.write_report(employee)

