""" https://adventofcode.com/2021/day/6 """

from typing import List
from math import floor

class FishAdministration:
    def __init__(self, fishes: List[int], days: int) -> None:
        self.references = {} # key = (fish, daysleft), value = babies to be had
        self.total = 0
        self.get_information(fishes, days)


    def get_information(self, fishes: List[int], days: int) -> None:
        for fish in fishes:
            self.total += self._get_pregnancies(fish, days)

        self.total += len(fishes)       

    def _get_pregnancies(self, fish: int, days: int) -> int:
        if days < fish:
            return 0

        if (fish, days) in self.references: # Check if this pattern has been seen before
            return self.references[(fish, days)]
        else: 
            # The current fish will have x babies to start with
            children = floor(days / 7)
            if days % 7 > fish:
                children += 1
            
            # Each child created ^, will also get babies 
            baby_days = days - (fish + 1) # First day for newborn
            grandchildren = 0
            for baby in range(0, children):
                if baby_days > baby * 7:
                    grandchildren += self._get_pregnancies(6, baby_days - baby * 7 - 2)

        total = children + grandchildren
        self.references[(fish, days)] = total # To save calculating in the future
        return total

def generate_correct_answer():
    with open("input.txt", "r") as f:
        fishes = f.read()
        fishes = [int(fish) for fish in fishes.strip().split(",")]

    print(FishAdministration(fishes, 80).total)
    print(FishAdministration(fishes, 256).total)

if __name__ == "__main__":
    generate_correct_answer()



# Keeping this to show the story following method of implementation :)
def first_assignment(fishes: List[int], days: int) -> int:
    for i in range(0, days):
        fishes = [fish - 1 for fish in fishes]
        newborns = fishes.count(-1)
        fishes = [6 if fish == -1 else fish for fish in fishes]
        fishes += [8] * newborns
    return(len(fishes))
