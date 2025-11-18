import random
import json
import os

#color mapping
COLOR_MEANING = {
    "red": "Confidence, passion",
    "blue": "Calmness, trust",
    "green": "Balance, freshness",
    "black": "Power, elegance",
    "yellow": "Optimism, energy",
    "white": "Purity, simplicity"
}

#mood-color mapping
MOOD_MAP = {
    "happy": "yellow",
    "calm": "blue",
    "confident": "red",
    "energetic": "yellow",
    "stressed": "green"
}

#event-color mapping
EVENT_MAP = {
    "interview": "black",
    "date": "red",
    "party": "white",
    "casual outing": "green"
}

#outfit suggestion
OUTFITS = {
    "red": [
        "a bold red shirt with black jeans",
        "a red jacket with a white t-shirt"
    ],
    "blue": [
        "a blue shirt with grey trousers",
        "a navy-blue blazer with a white tee"
    ],
    "green": [
        "an olive green jacket with denim jeans",
        "a green shirt with beige pants"
    ],
    "black": [
        "a black formal shirt with trousers",
        "an all-black outfit with a watch"
    ],
    "yellow": [
        "a bright yellow t-shirt with light jeans",
        "a mustard yellow hoodie with joggers"
    ],
    "white": [
        "a white shirt with blue jeans",
        "an all-white casual outfit"
    ]
}

# Optional seasonal hints
SEASON_HINTS = {
    "summer": "(choose light fabrics for summer)",
    "winter": "(layer up for winter)",
    "spring": "(add light pastel layers)",
    "autumn": "(earthy tones work well in autumn)"
}

# Optional style tips
STYLE_TIPS = [
    "Balance bright colors with neutral accessories.",
    "Wear what fits well—comfort is style.",
    "Layering makes any outfit look better."
]

#history saving
HISTORY_FILE = "history.json"

def save_history(entry):
    data = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                data = json.load(f)
        except:
            data = []

    data.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)



def main():
    print("===== Color Psychology Outfit Recommender =====")
    
    # Ask user -- mood or event
    print("\nChoose an input type:")
    print("1) Mood")
    print("2) Event")
    
    choice = input("Enter 1 or 2: ")

# input of mood
    if choice == "1":
        mood = input("Enter your mood (happy, calm, confident, energetic, stressed): ").lower()
        if mood in MOOD_MAP:
            color = MOOD_MAP[mood]
            phrase = f"You’re feeling {mood}."
        else:
            print("Unknown mood. Try again.")
            return
#input for event
    elif choice == "2":
        event = input("Enter the event (interview, date, party, casual outing): ").lower()
        if event in EVENT_MAP:
            color = EVENT_MAP[event]
            phrase = f"You have a {event}."
        else:
            print("Unknown event. Try again.")
            return

    else:
        print("Invalid selection.")
        return

    #gender
    gender = input("\nDo you want gender-specific suggestions? (male/female/neutral): ").lower()
    if gender not in ["male", "female", "neutral"]:
        gender = "neutral"

    #season
    season = input("Enter season (summer/winter/spring/autumn) or press Enter to skip: ").lower()
    season_hint = SEASON_HINTS.get(season, "")

    #number of suggestions
    try:
        n = int(input("How many outfit suggestions do you want? (1–3): "))
        n = max(1, min(3, n))
    except:
        n = 1

    # Pick outfit suggestions
    suggestions = random.sample(OUTFITS[color], k=n)

#outfit
    print("\n-----------------------------------------------")
    print(phrase)
    print(f"Recommended color: {color.capitalize()}")
    print(f"Psychology: {COLOR_MEANING[color]}\n")

    for i, outfit in enumerate(suggestions, 1):
        print(f"Suggestion {i}: Try {outfit} {season_hint}")

    print("\nStyle Tip:", random.choice(STYLE_TIPS))
    print("-----------------------------------------------\n")

    # Save history
    save_history({
        "input_type": "mood" if choice == "1" else "event",
        "color": color,
        "suggestions": suggestions
    })

    print("Your recommendation has been saved (optional feature).")


if __name__ == "__main__":
    main()
