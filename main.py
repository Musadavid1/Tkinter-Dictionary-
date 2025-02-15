import tkinter
from tkinter import ttk
# Extended dictionary with multiple languages (Igala and English)
dictionaries = {

    "Igala": {
        "Stomache" : "Efu",
        "Eye" : "Eju",
        "Water" : "Omi",
        "Mouth" : "Alu",
        "Head" : "Oji",
        "Nose" : "Imo",
        "Light" : "Una",
        "Sky" : "Iri",
        "Home" : "Iwe",
        "Bag" : "Ikpe",
        "Mother" : "Iya",
        "Father" : "Baba",
        "Son" : "Ono",
        "Road" : "Ona",
        "Food" : "Acho",
        "Hello" : "Onwu",
        "Good morning" : "Olududu",
        "Thank you" : "Kede",
        "How are you" : "Ile",
        "How was work" : "Ucholowa",

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


    "Tiv": {
        "person" : "or",
        "land" : "tar",
        "house"  : "yo",
        "heart" : "shima",
        "king" : "tor",
        "Road" : "Ken",
        "Stone" : "Gba",
        "People" : "Lor",
        "Go" : "Do",
        "Peace" : "Yange",
        "Thing" : "Kwagh",
        "Thank you" : "Kyoho",
        "Children" : "Mbatsav",
        "Food" : "Ortom",
        "God" : "Aondo",
        "Health" : "Vesen",
        "Life" : "Nyian",
        "Mountain" : "Gbenda",
        "Love" : "Msen",
        "Tiv people" : "Tiv"
    },

    "German" : {
        "hello":"hallo",
        "goodbye":"auf_wiedersehen",
        "thank_you":"danke",
        "water":"wasser",
        "bread":"brot",
        "house":"haus",
        "car":"auto",
        "bicycle":"fahrrad",
        "love":"liebe",
        "flower":"blume",
        "sun":"sonne",
        "moon":"mond",
        "star":"sterm",
        "bird":"vogel",
        "fish":"fisch",
        "book":"buch",
        "school":"schule",
        "garten":"garden",
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
language_combobox = ttk.Combobox(root, values=["Igala", "TivG", "French", "Ijaw", "German"])
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
