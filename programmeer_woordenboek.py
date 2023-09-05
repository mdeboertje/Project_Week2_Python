class Collectie:
    collectie = {
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
    def __init__(self, collectie=None):
        self.collectie = collectie if collectie is not None else self.collectie

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
    def addTerm(self):
        term = (input("Geef hier de term: "))
        omschrijving = (str(input("Geef hier de omschrijving van de term: ")))

        self.collectie[term] = omschrijving
        self.keuzeMenu()

    #
    def keuzeMenu(self):
        choice = input(
            "Welke keuze wilt u maken?\n"
            "Keuzen uit \n"
            "1. Zoeken \n"
            "2. Alles weergeven \n"
            "3. Toevoegen \n"
            "4. Verwijderen \n"
            "5. Sluiten \n")
        match choice:
            case "Zoeken" | "1":
                self.searchTerm()
            case "Alles weergeven" | "2":
                self.returnAll()
            case "Toevoegen" | "3":
                self.addTerm()
            case "Verwijderen" | "4":
                self.removeTerm()
            case "Sluiten" | "5":
                print("Tot ziens!")
            case _:
                print("Ongeldige keuze. Probeer opnieuw")
                self.keuzeMenu()


def main():
    collectie = Collectie()
    collectie.keuzeMenu()


if __name__ == '__main__':
    main()
