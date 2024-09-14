from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS_TIPE = {'ArcticClimber':ArcticClimber,'SummitClimber':SummitClimber}
    VALID_PEAKS_TIPE = {'ArcticPeak':ArcticPeak,'SummitPeak':SummitPeak}
    VALID_GEAR = {'ArcticClimber':["Ice axe", "Crampons", "Insulated clothing", "Helmet"],
                  'SummitClimber':["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]}
    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self,climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS_TIPE:
            return f"{climber_type} doesn't exist in our register."
        is_name = [True for c in self.climbers if c.name == climber_name]
        # is_name = is_name[0]
        if is_name:
            return f"{climber_name} has been already registered."
        climber = self.VALID_CLIMBERS_TIPE[climber_type](climber_name)
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self,peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS_TIPE:
            return f"{peak_type} is an unknown type of peak."
        peak = self.VALID_PEAKS_TIPE[peak_type](peak_name,peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self,climber_name: str, peak_name: str, gear: List[str]):
        climber = [c for c in self.climbers if c.name == climber_name]
        climber = climber[0]
        valid_sumer_gear =  ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
        valid_winter_gear = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
        type_of_climber = 'ArcticClimber' if climber.initual_strenght == 200 else 'SummitClimber'
        missing_gear = self.VALID_GEAR[type_of_climber]

        organised_gear = sorted(gear)
        organised_right_gear = sorted(self.VALID_GEAR[type_of_climber])
        if organised_gear != organised_right_gear:
            climber.is_prepared = False

        # for i in range(0,len(self.VALID_GEAR[type_of_climber])-1):
        #     if self.VALID_GEAR[type_of_climber][i] in gear:
        #         missing_gear.remove(self.VALID_GEAR[type_of_climber][i])
        #         i -= 1
        #     else:
        #         climber.is_prepared = False

        if climber.is_prepared:
            return f"{climber_name} is prepared to climb {peak_name}."


        a = f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."
        return a

    def perform_climbing(self,climber_name: str, peak_name: str):
        climber = [c for c in self.climbers if c.name == climber_name]
        if len(climber) == 0:
            return f"Climber {climber_name} is not registered yet."
        climber = climber[0]
        peak = [p for p in self.peaks if p.name == peak_name]
        if len(peak) == 0:
            return f"Peak {peak_name} is not part of the wish list."
        peak = peak[0]
        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        if climber.is_prepared:
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."
        return f"{climber_name} will need to be better prepared next time."


    def get_statistics(self):

        ordered_climbers = sorted(self.climbers,key=lambda x: (-len(x.conquered_peaks),x.name))
        total_countered = 0
        for cl in ordered_climbers:
            total_countered+= len(cl.conquered_peaks)

        result = f'Total climbed peaks: {total_countered}\n**Climber\'s statistics:**\n'
        for c in ordered_climbers:
            result+= str(c)+'\n'
        return result
