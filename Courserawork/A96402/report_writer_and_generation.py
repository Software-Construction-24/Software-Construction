class ManagerReportWriter(ReportGenerator):
    def generate_report(self, manager):
        return f"Manager Report: {manager.name}\n{manager.manage_team()}"

class DeveloperReportWriter(ReportGenerator):
    def generate_report(self, developer):
        return f"Developer Report: {developer.name}\n{developer.code_review()}"
