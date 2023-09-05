import tkinter as tk
from tkinter import simpledialog

class CollectieUI:
    def __init__(self, root):
        self.collectie = {
            "Functie": "",
            "Algoritme": "",
            "IDE": "",
            "Loop": "",
            "Dictionary": "pietje bell",
            "List": "",
            "Conditie": "",
            "Recursie": ""
        }

        self.root = root
        self.root.title("Termen en Omschrijvingen")
        self.root.geometry("400x400")

    def search_term(self):
        ant = self.entry.get()
        omschrijving = self.collectie.get(ant)
        self.display_result(f"Term: {ant}\n\nOmschrijving: {omschrijving if omschrijving else 'Term niet gevonden'}")

    def return_all(self):
        result = "Termen en Omschrijvingen:\n\n"
        for term, omschrijving in self.collectie.items():
            result += f"Term: {term}\nOmschrijving: {omschrijving}\n\n"
        self.display_result(result)

    def add_term(self):
        term = self.entry.get()
        omschrijving = simpledialog.askstring("Toevoegen", f"Geef hier de omschrijving van de term '{term}':")
        if omschrijving:
            self.collectie[term] = omschrijving
            self.display_result(f"Term '{term}' is toegevoegd met omschrijving '{omschrijving}'")

    def remove_term(self):
        term = self.entry.get()
        if term in self.collectie:
            del self.collectie[term]
            self.display_result(f"Term '{term}' is verwijderd.")
        else:
            self.display_result("Term niet gevonden.")

    def display_result(self, result_text):
        self.result_text.delete(1.0, tk.END)  # Clear previous content
        self.result_text.insert(tk.END, result_text)


def main():
    root = tk.Tk()
    app = CollectieUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
