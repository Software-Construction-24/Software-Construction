class Report:
    def __init__(self, report_writer):
        self.report_writer = report_writer

    def generate_report(self, employee):
        if employee.role == "Manager":
            report = self.report_writer.generate_report(employee)
        elif employee.role == "Developer":
            report = self.report_writer.generate_report(employee)
        else:
            raise ValueError("Unsupported employee role")
        return report

