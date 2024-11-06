#countries and their capital
cc = {
    "Sweden": "Stockholm",
    "Germany": "Berlin",
    "Norway": "Oslo",
    "Italy": "Rome",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Spain": "Madrid",
    "Belgium": "Brussels",
    "France": "Paris",
    "Austria": "Vienna",
}

#Loop
for country, capital in cc.items():
    # Ask the user for the capital
    mark= input(f"What is the capital of {country}? ").strip()
    
    # Check if the mark is correct (ignoring case)
    if mark.lower() == capital.lower():
        print("True! The answer is", capital + ".")
    else:
        print("False. The capital of", country, "is", capital + ".")

