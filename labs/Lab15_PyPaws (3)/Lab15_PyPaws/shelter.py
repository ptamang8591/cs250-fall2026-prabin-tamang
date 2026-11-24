"""
shelter.py  -  STEP 3 and STEP 5

Functions that work with FILES: loading pets, saving a report,
and keeping a log of adoptions.
Look for the lines that start with  # TODO  and complete them.
"""

import random                       # a built-in library
from datetime import datetime       # import ONE thing from a library
from pathlib import Path

from pet import Pet                 # import from OUR OWN file, pet.py

# These paths always point to the "data" folder next to this file,
# no matter which folder your IDE runs the program from.
DATA_FOLDER = Path(__file__).parent / "data"
PETS_FILE = DATA_FOLDER / "pets.csv"
REPORT_FILE = DATA_FOLDER / "shelter_report.txt"
ADOPTION_LOG = DATA_FOLDER / "adoptions.txt"


# -------------------------------------------------------------------
# STEP 3: reading a file + handling exceptions
# -------------------------------------------------------------------
def load_pets(filename):
    """Read pets from a CSV file and return a list of Pet objects.

    Each line looks like:   Mochi,cat,3,40,75
                            name,species,age,hunger,happiness
    Some lines in pets.csv are BROKEN on purpose. Skip them without crashing.
    """
    pets = []

    # TODO 3b: This crashes if the file does not exist!
    #          Put the whole "with open(...)" block inside  try:
    #          and add  except FileNotFoundError:  that prints a friendly
    #          message such as:   ! Could not find the file: <filename>
    #          (Select the lines and press Tab to indent them all at once.)

    try:
        with open(filename, "r", encoding="utf-8") as file:
            file.readline()                     # skip the header line
            for line in file:
                line = line.strip()
                if line == "":
                    continue                    # skip empty lines

                # TODO 3a: These 3 lines CRASH on a broken line like "Ghost,dog,three,50,50".
                #          Put them inside  try:  and add  except ValueError:
                #          In the except block print:   ! Skipping bad line: <line>
                try:
                    name, species, age, hunger, happiness = line.split(",")
                    pet = Pet(name, species, int(age), int(hunger), int(happiness))
                    pets.append(pet)
                except ValueError:
                    print(f"  ! Skipping bad line: {line}")
    except FileNotFoundError:
        print(f"  ! Could not find the file: {filename}")

    return pets


# -------------------------------------------------------------------
# STEP 5: writing and appending to files
# -------------------------------------------------------------------
def save_report(pets, filename):
    """Write a report of every pet to a text file (WRITE mode, "w")."""
    today = datetime.now().strftime("%Y-%m-%d")     # e.g. "2026-12-01"

    # TODO 5a:
    #   1. Open filename in WRITE mode ("w") using   with open(...) as file:
    #   2. Write a title line:   PyPaws Shelter Report - <today>
    #   3. Loop over pets and write  str(pet)  for each one.
    #   Remember: file.write() does NOT add a new line. Add "\n" yourself!
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"PyPaws Shelter Report - {today}\n")
        for pet in pets:
            file.write(f"{str(pet)}\n")


def log_adoption(pet, adopter, filename):
    """Add ONE line to the adoption log (APPEND mode, "a")."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")  # e.g. "2026-12-01 14:05"

    # TODO 5b:
    #   Open filename in APPEND mode ("a") and write ONE line like:
    #   2026-12-01 14:05 | Mochi the cat was adopted by Sam
    #   (Append mode adds to the end of the file instead of erasing it.)
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{now} | {pet.name} the {pet.species} was adopted by {adopter}\n")


# -------------------------------------------------------------------
# Already done for you: a random surprise! (uses the random library)
# -------------------------------------------------------------------
def random_event(pets):
    """Something surprising happens to one random pet in the shelter."""
    available = [p for p in pets if not p.adopted]      # list comprehension
    if not available:
        return "The shelter is quiet... every pet has a home!"

    pet = random.choice(available)
    event = random.randint(1, 4)

    if event == 1:
        pet.feed(30)
        return f"{pet.name} found a secret snack stash under the couch! (hunger -30)"
    elif event == 2:
        pet.play(15)
        return f"A volunteer took {pet.name} to the park! (happiness +30)"
    elif event == 3:
        pet.happiness = max(0, pet.happiness - 20)
        return f"{pet.name} got scared by the vacuum cleaner... (happiness -20)"
    else:
        pet.hunger = min(100, pet.hunger + 25)
        return f"{pet.name} did zoomies for an hour and is now STARVING! (hunger +25)"