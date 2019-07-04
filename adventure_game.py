#  import time for delayed message printing and import random to randomly
#  select a villain
import time
import random


def print_pause(message):
    print(message)
    time.sleep(3)


def intro(villain):
    print_pause("\nFriends of yours invite you out for a day of fun rafting."
                " \n")
    print_pause("Buses take you and your friends from the rafting company "
                "office to \nthe spot on the river where the trip begins.\n")
    print_pause("Right before rafting begins, the guides share some "
                "unwelcomed news. \n")
    print_pause("The party that rafted right before us didn't make it back.\n")
    print_pause("It turns out this river crosses through territory that\n"
                f"{villain} act like savages in.\n")
    print_pause(f"'The {villain} are likely to attack again', the guides said."
                "\n")
    print_pause("The bus that dropped everyone off has already left.\n")
    print_pause("We have to try our luck and raft to where the buses will "
                "pick us up, \nthe guides said.\n")
    print_pause("Your friends are terrified and they are trying to arm "
                "themselves.\n")
    print_pause("They ask you to check your backpack for any supply that "
                "could be used \nas a weapon.\n")
    print_pause("Do you check your backpack or do you want"
                " to begin rafting?\n")


def go_rafting(items, villain):
    response = input("Enter 1 if you want to check your backpack.  \n"
                     "Enter 2 if you want to begin rafting and get the trip "
                     "over with.\n")
    if response == '1':
        check_supplies(items, villain)
    elif response == '2':
        begin_journey(items, villain)
    else:
        print_pause("Please enter 1 or 2.")
        go_rafting(items, villain)


def check_supplies(items, villain):
    print_pause("You check your backpack.")
    if "Ginsu knife" in items:
        print_pause("The Ginsu knife is the only weapon like thing I had in \n"
                    "here and I already have it, time to raft. \n")
        print_pause("Your friends ask you to double check your bags, just to"
                    " make sure you \nare not overlooking anything.\n")
        go_rafting(items, villain)
    else:
        print_pause("The Ginsu steak knife.  Even Crocodile Dundy would "
                    "respect this one.\nI can use this if needed.\n")
        print_pause("Your friends ask you to double check your bags, just to"
                    " make sure you \nare not overlooking anything.")
        items.append("Ginsu knife")
        go_rafting(items, villain)


def begin_journey(items, villain):
    print_pause("The rapids are very calm at the start.\n")
    print_pause("For a moment, everyone is one with nature.\n")
    print_pause("The river began making a right turn and suddenly "
                "the rafts fall down\na 10ft waterfall!\n")
    print_pause("The fall tosses everyone from the raft.\n")
    print_pause("Luckily, people all made it to land safely.\n")
    print_pause("'And we are close to the bus pick up spot, too!' "
                "the guides said.\n")
    print_pause("Just as everyone begins to regroup, one of the rafting guides"
                " says \nthat he sees something coming our way...\n")
    print_pause(f"It's the {villain}!  And they are coming to kill!\n")
    print_pause(f"The {villain} have attacked you and your friends.\n")
    print_pause("Friends to turn you and ask, 'Should we fight or run?'\n")
    print_pause("Do you want to fight or run?\n")


def fight_or_run(items, villain):
    response = input("Enter 1 if you want to fight.\n"
                     "Enter 2 if you want to run.\n")
    if response == '1':
        fight(items, villain)
    elif response == '2':
        run(items, villain)
    else:
        print_pause("Please enter 1 or 2.")
        fight_or_run(items, villain)


def fight(items, villain):
    print_pause("'Everyone stand your ground' you say.\n")
    print_pause(f"These {villain} do not scare me.\n")
    if "Ginsu knife" in items:
        print_pause("You raise the Ginsu knife into the air.  \n")
        print_pause("The sunlight reflects off of the wet steel and "
                    f"blinds one of the {villain}, \nmaking him fall.\n")
        print_pause(f"The {villain} leader tells the {villain} to take no"
                    " prisoners.\n")
        print_pause("Effortlessly, the Ginsu knife slices and dices, without"
                    " dulling one bit!\n")
        print_pause(f"As the {villain} leader sees the {villain} losing the "
                    "battle, he orders them to\nretreat.\n")
        print_pause(f"Congratulations, you beat the {villain} and kept your"
                    " friends safe.\nYou have won the game.")
        play_again()
    else:
        print_pause("As the enemy charges, you fear not.\n")
        print_pause("You curl your bicepts and say, 'As long as I have ole "
                    "thunder and lightning,\nnothing can beat me.'\n")
        print_pause(f"The {villain} attack without fear. Try as they might, "
                    "your friends cannot\ndefend themselves.\n")
        print_pause(f"One of the {villain} clubs you with a bat.  As you fall "
                    "to the" f" ground, you \nlook up and see the {villain} "
                    "kill your friends.\n")
        print_pause("Game Over.  You lose.")
        play_again()


def run(items, villain):
    print_pause("Everybody, run!")
    print_pause(f"The {villain} are fast and are right on your tail.")
    if "Ginsu knife" in items:
        print_pause("I have this Ginsu knife, maybe we can take them on?")
        fight_or_run(items, villain)
    else:
        print_pause("'I'm not sure how much longer we can run for', "
                    "you say.\n")
        fight_or_run(items, villain)


def play_again():
    response = input("\nDo you want to play again? \n"
                     "Press 1 to play again. \n"
                     "Press 2 to quit.\n")
    if response == '1':
        play_game()
    elif response == '2':
        exit()
    else:
        print_pause("Please enter 1 or 2.")
        play_again()


def play_game():
    items = []
    villain = random.choice(["bandits", "lunatics", "thugs"])
    intro(villain)
    go_rafting(items, villain)
    fight_or_run(items, villain)


play_game()
