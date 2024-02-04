class ManagerBonusCalculator(BonusCalculator):
    def calculate_bonus(self, manager):
        return 1000 + manager.manage_team_performance()  # Implement performance logic

class DeveloperBonusCalculator(BonusCalculator):
    def calculate_bonus(self, developer):
        return 500 + developer.code_quality_rating()  # Implement rating logic
