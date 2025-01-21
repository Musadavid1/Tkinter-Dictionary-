import tkinter
from tkinter import ttk

# Extended dictionary with multiple languages (Igala and English)
dictionaries = {
    "Igala": {
        "Love": "Tari",
        "Ijaw (self-identification)": "Izon",
        "Sun": "Ere",
        "Water": "Beni",
        "Peace": "Timine",
        "Life": "Bu",
        "House": "Bele",
        "Friend": "Ogbo",
        "Sea": "Abadi",
        "River": "Toru",
        "Fire": "Fie",
        "Earth": "Aru",
        "Moon": "Numa",
        "Forest": "Ogoni",
        "Place of rest": "Peremabiri",
        "Work": "Dubo",
        "Good": "Keme",
        "Path": "Seikiri",
        "Child": "Igoni",
        "Food": "Feni"
    },
    "French": {
        "House" : "Maison" ,
        "Car" : "Voiture" ,
        "Book" : "Livre",
        "Water" : "Eau" ,
        "Food" : "Nourriture",
        "Friend" : "Amie",
        "Love" : "Amour",
        "Sun" : "Soleil",
        "Moon" : "Lune",
        "Tree" : "Arbre",
        "sky" : "Ciel",
        "Flower" : "Fleur",
        "Mountain" : "Montagne",
        "River" : "Riviere",
        "City" : "Ville",
        "Dog" : "Chien",
        "Cat" : "Chat",
        "Music" : "Musique",
        "Family" : "Famille",
        "Dream" : "Reve",
    },

    "Ijaw": {
        "Love": "Tari",
        "Ijaw (self-identification)": "Izon",
        "Sun": "Ere",
        "Water": "Beni",
        "Peace": "Timine",
        "Life": "Bu",
        "House": "Bele",
        "Friend": "Ogbo",
        "Sea": "Abadi",
        "River": "Toru",
        "Fire": "Fie",
        "Earth": "Aru",
        "Moon": "Numa",
        "Forest": "Ogoni",
        "Place of rest": "Peremabiri",
        "Work": "Dubo",
        "Good": "Keme",
        "Path": "Seikiri",
        "Child": "Igoni",
        "Food": "Feni"

}


def search_word():
    word = entry.get()
    language = language_combobox.get()  # Get selected language
    result_label.config(text="")


    selected_dict = dictionaries.get(language)

    if selected_dict:
        # Search for the word in the selected language dictionary
        meaning = selected_dict.get(word)

        if meaning:
            result_label.config(text=f"Meaning of '{word}' in {language}: {meaning}")
        else:
            result_label.config(text=f"Word '{word}' not found in {language}!")
    else:
        result_label.config(text="Selected language not found!")


# Set up the Tkinter window
root = tkinter.Tk()
root.title("Multi-Language Dictionary")
root.geometry("600x600")

# Add a Label to show language selection
language_label = tkinter.Label(root, text="Select Language:", font=("Helvetica", 12))
language_label.pack(pady=5)

# Add a ComboBox to select language (Igala, English, etc.)
language_combobox = ttk.Combobox(root, values=["Igala", "English", "French"])
language_combobox.set("Igala")  # Set default language to Igala
language_combobox.pack(pady=10)

# Add an Entry widget for the user to type the word
entry = tkinter.Entry(root)
entry.pack(pady=10)

# Add a Button widget that triggers the search
search_button = tkinter.Button(root, text="Search", command=search_word)
search_button.pack(pady=10)

# Label to display the result of the search
result_label = tkinter.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
