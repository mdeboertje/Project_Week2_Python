import json


class Collectie:
    DEFAULT_COLLECTIE = {
        "Functie": "",
        "Algoritme": "",
        "IDE": "",
        "Loop": "",
        "Dictionary": "pietje bell",
        "List": "",
        "Conditie": "",
        "Recursie": ""
    }

    # Initializes the collection
    def __init__(self):
        self.load_collection()
    def load_collection(self):
        try:
            with open("collectie.json", "r") as file:
                self.collectie = json.load(file)
        except FileNotFoundError:
            self.collectie = self.DEFAULT_COLLECTIE

    def save_collection(self):
        with open("collectie.json", "w") as file:
            json.dump(self.collectie, file, indent=4)

    # Searches for the output of the input and compares them to what is stored within the collection
    def searchTerm(self):
        term = input("Welke term zoekt u? ")
        omschrijving = self.collectie.get(term)
        if omschrijving is not None:
            print(f"Term: {term}, Omschrijving: {omschrijving}")
            self.keuzeMenu()
        else:
            print("Term niet gevonden")

    # Removes the provided term in the collection
    def removeTerm(self):
        print("Termen en Omschrijvingen:")
        for term, omschrijving in self.collectie.items():
            print(f"Term: {term}, Omschrijving: {omschrijving}")
        term = input("Welke term wilt u verwijderen")
        if term in self.collectie:
            del self.collectie[term]
            print(f"Term {term} is verwijdert.")

    # Returns the collection in a format
    def returnAll(self):
        print("Termen en Omschrijvingen:")
        for term, omschrijving in self.collectie.items():
            print(f"Term: {term}, Omschrijving: {omschrijving}")

    # Adds a new collection
    def add_term(self):
        term = input("Geef hier de term: ")
        omschrijving = input("Geef hier de omschrijving van de term: ")

        self.collectie[term] = omschrijving
        self.save_collection()
        print(f"Term '{term}' is toegevoegd met omschrijving '{omschrijving}'")

    #
    def menu(self):
        while True:
            choice = input(
                "Welke keuze wilt u maken?\n"
                "1. Zoeken\n"
                "2. Alles weergeven\n"
                "3. Toevoegen\n"
                "4. Verwijderen\n"
                "5. Sluiten\n"
                "Uw keuze: "
            )
            if choice == "1":
                self.searchTerm()
            elif choice == "2":
                self.returnAll()
            elif choice == "3":
                self.add_term()
            elif choice == "4":
                self.removeTerm()
            elif choice == "5":
                print("Tot ziens!")
                break
            else:
                print("Ongeldige keuze. Probeer opnieuw.")



def main():
    collectie = Collectie()
    collectie.menu()


if __name__ == '__main__':
    main()
