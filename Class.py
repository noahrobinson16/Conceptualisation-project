from datetime import datetime
from math import *


class Personne:
    def __init__(self, name: str, last_name: str, birth_year: int, birth_month: int, birth_day: int):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        birth_year = self.birth_year
        birth_month = self.birth_month
        birth_day = self.birth_day


        def determine_age(birth_year, birth_month, birth_day):
            # Define the birthdate
            birthdate = datetime(birth_year, birth_month, birth_day)

            # Get the current date
            current_date = datetime.now()

            # Calculate the difference in days
            difference = current_date - birthdate
            days_passed_since_birth = difference.days

            return days_passed_since_birth

        days_passed_since_birth = determine_age(birth_year, birth_month, birth_day)

        self.age = floor(days_passed_since_birth / 365)

    def __repr__(self):
        pass

    def __hash__(self):
        pass

    def __str__(self):
        return f"-------------------------------" \
               f"\nPrénom: {self.name}" \
               f"\nNom: {self.last_name}" \
               f"\nÂge: {self.age}" \
               f"\nDate de naissance: {self.birth_day}\\{self.birth_month}\\{self.birth_year}" \
               f"\n-------------------------------"

    def __eq__(self, other):
        pass
########################################################################################################################

noah_robinson = Personne("Noah", "Robinson", 2006, 3, 16)
flavie_pepin = Personne("Flavie", "Pepin", 2006, 8, 25)
emmanuelle_turgeon = Personne("Emmanuelle", "Turgeon", 1979, 3, 23)
pierre_robinson = Personne("Pierre", "Robinson", 1979, 9, 19)
sophie_lebel = Personne("Sophie", "Lebel", 2008, 4, 28)
fred_hamel = Personne("Fred", "Hamel", 2007, 9, 8)
print(noah_robinson)
print(flavie_pepin)
print(fred_hamel)
print(sophie_lebel)
print(emmanuelle_turgeon)
print(pierre_robinson)
