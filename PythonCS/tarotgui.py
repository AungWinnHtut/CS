import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Define a list of tarot cards and their interpretations
tarot_cards = [
    ("The Fool", "New beginnings, spontaneity, unpredictability, a leap of faith"),
    ("The Magician", "Manifestation, resourcefulness, power, skill"),
    ("The High Priestess", "Intuition, subconscious knowledge, mystery, inner voice"),
    ("The Empress", "Fertility, nurturing, abundance, motherhood"),
    ("The Emperor", "Authority, leadership, structure, control"),
    ("The Hierophant", "Tradition, spirituality, religious guidance, teaching"),
    ("The Lovers", "Love, relationships, union, choices"),
    ("The Chariot", "Victory, determination, willpower, self-control"),
    ("Strength", "Strength, courage, patience, inner power"),
    ("The Hermit", "Solitude, introspection, inner guidance, isolation"),
    ("Wheel of Fortune", "Change, cycles, destiny, luck"),
    ("Justice", "Justice, fairness, balance, truth"),
    ("The Hanged Man", "Sacrifice, letting go, suspension, gaining a new perspective"),
    ("Death", "Transformation, change, endings, new beginnings"),
    ("Temperance", "Balance, harmony, moderation, blending opposites"),
    ("The Devil", "Addiction, materialism, bondage, temptation"),
    ("The Tower", "Sudden upheaval, chaos, revelation, awakening"),
    ("The Star", "Hope, inspiration, spiritual guidance, renewal"),
    ("The Moon", "Illusion, subconscious, intuition, confusion"),
    ("The Sun", "Success, joy, positivity, enlightenment"),
    ("Judgment", "Judgment, transformation, rebirth, accountability"),
    ("The World", "Completion, wholeness, fulfillment, travel"),
]

def draw_tarot_card():
    card = random.choice(tarot_cards)
    return card

def draw_card_button_clicked():
    card_name, card_interpretation = draw_tarot_card()
    card_display.config(text=card_name)
    interpretation_display.config(text=card_interpretation)

# Create a main window
root = tk.Tk()
root.title("Tarot Card Reading")

# Create card display labels
card_display = tk.Label(root, text="", font=("Arial", 20))
card_display.pack()

interpretation_display = tk.Label(root, text="", font=("Arial", 12))
interpretation_display.pack()

# Create "Draw Card" button
draw_card_button = tk.Button(root, text="Draw Card", command=draw_card_button_clicked)
draw_card_button.pack()

# Run the GUI application
root.mainloop()