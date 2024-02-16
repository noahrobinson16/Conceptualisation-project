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
        self.days_passed_since_birth = days_passed_since_birth


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
               f"\nNombre de jour passé en vie: {self.days_passed_since_birth}" \
               f"\n-------------------------------"

    def __eq__(self, other):
        pass


class Job:
    def __init__(self, prénom:str, nom:str, company: str, heure_ouverture: int, heure_fermeture: int,
                 temps_plein: bool, jour_embauche: int, mois_embauche: int, année_embauche: int):
        self.company = company
        self.heure_ouverture = heure_ouverture
        self.heure_fermeture = heure_fermeture
        self.temps_plein = temps_plein
        self.jour_embauche = jour_embauche
        self.mois_embauche = mois_embauche
        self.année_embauche = année_embauche
        self.prénom = prénom
        self.nom = nom
        année_embauche = self.année_embauche
        mois_embauche = self.mois_embauche
        jour_embauche = self.jour_embauche

        def determine_day_since_acceptation_to_the_workplace(année_embauche, mois_embauche, jour_embauche):
            # Define the birthdate
            date_de_début_au_travail = datetime(année_embauche, mois_embauche, jour_embauche)

            # Get the current date
            current_date = datetime.now()

            # Calculate the difference in days
            difference = current_date - date_de_début_au_travail
            days_passed_since_acceptation_at_the_job = difference.days

            return days_passed_since_acceptation_at_the_job

        days_passed_since_acceptation_at_the_job = determine_day_since_acceptation_to_the_workplace(année_embauche,
                                                                                                    mois_embauche,
                                                                                                    jour_embauche)
        self.jour_depuis_début_emploi = days_passed_since_acceptation_at_the_job



    def __str__(self):
        return (f"-------------------------------"
                f"\nNom complet de l'employé: {self.prénom} {self.nom}"
                f"\nEmployeur: {self.company}"
                f"\nHeures d'ouverture: {self.heure_ouverture}:00 à {self.heure_fermeture}:00"
                f"\nTemps plein: {self.temps_plein}"
                f"\nNombre de jour à l'emploi: {self.jour_depuis_début_emploi}"
                f"\n-------------------------------")



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
job_noah_robinson = Job("Noah", "Robinson", "McDonald's", 5, 24, False, 4, 5, 2021)
print(job_noah_robinson)
