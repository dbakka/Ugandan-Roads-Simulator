import os, time, random



roads = {
    'Yusuf Lule Rd': {
        'potholes': 7,
        'signposts': 2,
        'accidents': 3,
    },
    'Kabaka Anjagala Rd': {
        'potholes': 0,
        'signposts': 4,
        'accidents': 3,
    },
}

while True:
    print("🌟Ugandan Roads Simulator🌟")
    print()
    print("Welcome to the best roads simulator. Which of the following roads do you choose? ")
    print()
    for key in roads:
        print(key)
        print()
    card_choice = input("Choose your card? 1 - Yusuf lule / 2 - Kabaka Anjagala > \n")
    print()
    comp_choice = random.choice(list(roads.keys()))
    print("Computer has picked", comp_choice)
    print()
    print("""Which stat would you like to compete in?
         potholes
         signposts
         accidents
         """)
    stat_choice = input("> \n").lower()
    
    print(f"{card_choice}: {roads[card_choice][stat_choice]}")
    print()
    print(f"{comp_choice}: {roads[comp_choice][stat_choice]}")
    print()

    if roads[card_choice][stat_choice] > roads[comp_choice][stat_choice]:
        print(card_choice, "wins")
    elif roads[card_choice][stat_choice] < roads[comp_choice][stat_choice]:
        print(comp_choice, "wins")
    else:
        print("It's a Draw!")
        print()

    time.sleep(5)
    os.system("clear")


