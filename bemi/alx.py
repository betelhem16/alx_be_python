import random

truths = ["What's your biggest fear?", "Who is your crush?", "What's your most embarrassing moment?"]
dares = ["Do 10 push-ups", "Dance for 30 seconds", "Sing your favorite song"]

while True:
    choice = input("Truth or Dare? (t/d, q to quit): ").lower()
    if choice == "q": break
    if choice == "t": print("Truth:", random.choice(truths))
    elif choice == "d": print("Dare:", random.choice(dares))
    else: print("Invalid choice!")
