from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self):
        if self.elevation > 2500:
            self.difficulty_level = "Extreme"
        elif self.elevation >= 1500 and self.elevation <= 2500:
            self.difficulty_level = "Advanced"
        return self.difficulty_level
