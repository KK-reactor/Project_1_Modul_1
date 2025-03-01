"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Karel Kopecký
email: karel876@email.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# 1) import modulu re - pro práci s regulárními výrazy
import re

# 2) Registrovaní uživatelé a jejich hesla
users = {"bob": "123", 
         "ann": "pass123", 
         "mike": "password123", 
         "liz": "pass123"}

# 3) Input od uživatele (jméno, heslo)
user_name = input("Enter your username:\n")
user_password = input("Enter your password:\n")

# 4) Odpověď programu na input od uživatele
answer_for_registered_users = f"""
Username: {user_name}
Password: {user_password}
{"-" * 40}
Welcome to the app, {user_name}
We have {len(TEXTS)} texts to be analyzed.
{"-" * 40}"""

answer_for_unregistered_users = f"""
Username: {user_name}
Password: {user_password}
Unregistered user, terminating the program.
{"-" * 43}"""

answer_for_invalid_input = f"""Invalid input.
Please choose a number between 1 and {len(TEXTS)}.
Terminating the program.
{"-" * 40}"""

# 5) Analýza textů
def text_analysis(text):
    """Analyzuje zadaný text a vrací seznam s výsledky.

    Args:
        text: Analyzovaný text.

    Returns:
        Slovník s výsledky analýzy.
    """

    # Odstranění interpunkce a čísel
    text_without_punctutation = re.sub(r'[^\w\s]', '', text)

    # Rozdělení textu na slova
    words = text_without_punctutation.split()

    # výpočty
    count_of_words = len(words)
    titlecase_words = sum(1 for word in words if word[0].isupper() and word[1:].islower())
    uppercase_words = len(re.findall(r'\b[A-Z]+\b', text))
    lowercase_words = len([word for word in words if word.islower()])
    numeric_strings = len(re.findall(r'\d+', text))
    sum_of_all_the_numbers = sum(int(number) for number in re.findall(r'\d+', text))

    # výsledky
    results = f"""There are {count_of_words} words in the selected text.
There are {titlecase_words} titlecase words.
There are {uppercase_words} uppercase words.
There are {lowercase_words} lowercase words.
There are {numeric_strings} numeric strings.
The sum of all the numbers {sum_of_all_the_numbers}"""

    return results


# 6) Analýza textů pro vytvoření grafu 
def word_frequency_graph(text):
    """Vytvoří graf četnosti slov podle délky pomocí hvězdiček, seřazený vzestupně.

    Args:
        text: Analyzovaný text.
    """
    # Odstranění interpunkce a čísel
    text_without_punctutation = re.sub(r'[^\w\s]', '', text)

    # Rozdělení textu na jednotlivá slova
    words = text_without_punctutation.split()

    # Vytvoření slovníku pro uchovávání hodnot: počet výskytu dle délky slova
    word_lengths = {}

    # Výpočet délky slov
    for word in words:
        word_length = len(word)
        word_lengths[word_length] = word_lengths.get(word_length, 0) + 1

    # Vzestupné seřazení výskytu: "x"-písmenných slov dle délky slova
    sorted_lengths = sorted(word_lengths.items())

    # Hlavička tabulky
    print(f"{'LEN':<3}|{'OCCURENCES':^14}|NR.")
    print("-" * 40)
    
    # Výpis výsledků
    for length, count in sorted_lengths:
        # Zarovnáno na levý okraj (délka slova), střed (počet: "*") a pravý okraj (počet slov)
        print(f"{length:>3}|{'*' * count:<20}|{count:<2}")


# 7) Výsledné analýzy
# List pro uložení výsledků analýz
results = []

# Pro každý text v listu "TEXTS" provedeme analýzu a uložíme výsledek do listu "results"
for text in TEXTS:
    results.append(text_analysis(text))

# 8) Cyklus programu 
if user_name in users and users[user_name] == user_password:
    print(answer_for_registered_users)
    while True:
        try:
            choice = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))
            print("-" * 40)
            if 1 <= choice <= len(TEXTS):
                print(results[choice - 1])  # Výběr analýzy pro odpovídající text
                print("-" * 40)
                word_frequency_graph(TEXTS[choice - 1])  # Zobrazení grafu pro vybraný text
                break
            else:
                print(answer_for_invalid_input)
                break
        except ValueError:
            print("-" * 40)
            print(answer_for_invalid_input)
            break
else:
    print(answer_for_unregistered_users)