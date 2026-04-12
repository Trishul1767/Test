import os
import random

def load_cards():
    cards = {}
    if os.path.exists("cards.txt"):
        with open("cards.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    deck, term, definition = parts
                    
                    if deck not in cards:
                        cards[deck] = [] 
                    
                    cards[deck].append((term, definition)) 
    return cards

def save_cards(cards):
    with open("cards.txt", "w") as file:
        for deck, deck_cards in cards.items():
            for term, definition in deck_cards:
                file.write(f"{deck}|{term}|{definition}\n")

def add_card(cards):
    print("\n--- Add a Flashcard ---")
    deck = input("Enter deck name (e.g., Python Basics): ").strip()
    term = input("Enter the term: ").strip()
    defi = input("Enter the definition: ").strip()

    if deck not in cards:
        cards[deck] = []
        
    cards[deck].append((term, defi))
    save_cards(cards)
    print("Card added successfully!")

def start_quiz(cards):
    if not cards:
        print("No cards available. Please add some first.")
        return

    print("\nAvailable decks:", ", ".join(cards.keys()))
    deck = input("Which deck do you want to study? ").strip()

    if deck not in cards:
        print("Deck not found.")
        return

    deck_cards = cards[deck].copy()
    random.shuffle(deck_cards)
    score = 0

    print(f"\n--- Starting Quiz on {deck} ---")
    for term, defi in deck_cards:
        print(f"\nTerm: {term}")
        input("Press Enter to reveal the definition...")
        print(f"Definition: {defi}")
        
        ans = input("Did you get it right? (y/n): ").strip().lower()
        if ans == 'y':
            score += 1

    print(f"\nQuiz over! You scored {score} out of {len(deck_cards)}.")

cards = load_cards()

while True:
    print("\n=== STUDY BUDDY ===")
    print("1. Add a Flashcard")
    print("2. Start a Quiz")
    print("3. Exit")
    
    try:
        choice = int(input("Choose an option (1-3): "))
        if choice == 1:
            add_card(cards)
        elif choice == 2:
            start_quiz(cards)
        elif choice == 3:
            print("Good luck with your exams! Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            
    except ValueError:
        print("Error: Please enter a valid number.")