import random

print("Бабуля: Привет, внучок! Спрашивай, что хочешь.")

while True:
    user_input = input("Ты: ")

    if user_input.upper() == "ПОКА!":
        print("Бабуля: Ну ладно, пока! Приходи еще.")
        break

    if user_input.isupper() and user_input != "":
        year = random.randint(1930, 1950)
        print(f"Бабуля: НЕТ, НИ РАЗУ С {year} ГОДА!")
    else:
        print("Бабуля: АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")