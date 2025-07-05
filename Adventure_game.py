import time
import random
# 6 function definitions


# Before the game starts, the score must be initialized to zero
def initialize_score():
    score = 0
    print(f"Score is now {score}")
    return score


# going to den function
def going_to_den(destination, score):
    while True:
        den = input("Go to den of monsters?[y/n] ").lower()
        if den == "y":
            score = score + 1
            print("-"*60)
            print(f"Your score is now {score}")
            print("-"*60)
            if destination == "house":
                print("You go super fast and reach the den of monsters")
                print("-"*60)
                time.sleep(3)
                print("And there you find a monster")
                print("-"*60)
                return score
            elif destination == "road":
                print("You go endlessly until you reach the den of monsters")
                print("-"*60)
                time.sleep(3)
                print("And there you find a monster")
                print("-"*60)
                return score
        elif den == "n":
            print("-"*60)
            print("You are stuck in this magical world forever")
            print("-"*60)
            time.sleep(3)
            print(f"Your score is {score}")
            print("-"*60)
            time.sleep(3)
            print("GAME OVER!!!")
            print("-"*60)
            return False
        else:
            print("-"*60)
            print("Not an answer!!!")
            print("-"*60)


# attacking the monster in the den function
def attack_mode(score):
    while True:
        attack = input("Cast a spell (press 2) , run away (press 1) or \
surrender (press 0)? ")
        if attack == "2":
            print("-"*60)
            print("Excellent!! the monster is struck dead")
            print("-"*60)
            time.sleep(2)
            score = score + 2
            print(f"Score is now {score}")
            return score
        elif attack == "1":
            print("-"*60)
            print("OK, the monster is still alive but you managed to escape.")
            print("Good work")
            print("-"*60)
            time.sleep(2)
            score = score + 1
            print(f"Score is now {score}")
            return score
        elif attack == "0":
            score = score + 0
            print("-"*60)
            print(f"Your score now is {score}")
            print("-"*60)
            time.sleep(2)
            print("You lose!!")
            print("-"*60)
            time.sleep(2)
            print("Because the monster ATE you!!!")
            print("-"*60)
            return False
        else:
            print("-"*60)
            print("Not an attack mode!!")
            print("-"*60)


# upgrading the wand function
def appreciate_help(score, appreciate):
    while True:
        if appreciate == "y":
            score = score + 1
            print("-"*60)
            print(f"Way to go! Score is now {score}")
            print("-"*60)
            break
        elif appreciate == "n":
            score = score + 0
            print("-"*60)
            print(f"Score is now {score}")
            print("-"*60)
            break
    return score


# React to either dragon, werewolf or devil
def react_to_monster(score, accept):
    while True:
        reaction = input("Cast a spell using the larger wand (press 2) or \
surrender (press 1)? ").lower()
        print("-"*60)
        if reaction == "2":
            if accept == "y":
                print(f"Wow this is awesome!! You have killed the {monster} an\
d saved all the {creature}s")
                print("-"*60)
                time.sleep(2)
                score = score + 5
                print(f"Score is now {score}")
                print("-"*60)
                time.sleep(2)
                print(f"All {creature}s jump and hug you and you return to \
the black forest")
                print("-"*60)
                time.sleep(2)
                print("You are victorious !!!!")
                print("-"*60)
                return score
            elif accept == "n":
                print(f"Oh no the {monster} eats you  ", end="")
                print("because you didn't ", end="")
                print(f"accept the {creature} help and ", end="")
                print("didn't take the larger wand")
                print("-"*60)
                time.sleep(2)
                score = score - 3
                print(f"Score is now {score}")
                print("-"*60)
                time.sleep(2)
                print("You have lost !!")
                print("-"*60)
                return score
        elif reaction == "1":
            print(f"Oh no the {monster} eats you")
            print("-"*60)
            time.sleep(2)
            score = score - 3
            print(f"Score is now {score}")
            print("-"*60)
            time.sleep(2)
            print("You have lost !!")
            print("-"*60)
            return score
        else:
            print("Not a reply !!!")
            print("-"*60)


# play again function
def play_again():
    while True:
        play_again = input("Play again?[y/n] ").lower()
        if play_again == "y":
            return True
        elif play_again == "n":
            print("-"*60)
            print("OK bye bye")
            print("-"*60)
            time.sleep(2)
            return False
        else:
            print("Not a reply!!!")
            print("-"*60)


while True:
    # Game's name
    print("-"*60)
    print("Adventure Game Project")
    print("By student: Yaseen Saeed")
    print("-" * 60)
    # Randomness of color of wand
    wand = ["yellow", "blue", "green", "red"]
    color_of_wand = random.choice(wand)
    # Randomness of creatures
    creatures = ["unicorn", "troll", "elf"]
    creature = random.choice(creatures)
    # randomness of monsters
    monsters = ["dragon", "werewolf", "devil"]
    monster = random.choice(monsters)
    # Randomness of knowledge about monster
    sources = ["Rumors", "Posters around you", "Road signs"]
    source = random.choice(sources)
    # describe what is happening
    print("You are wandering in the black forest, Germany")
    print("-"*60)
    time.sleep(3)
    print("You sit under a tree and fall asleep")
    print("ZzZzZzzzzz")
    print("-" * 60)
    time.sleep(3)
    print(f"You wake up to find yourself in a magical world with {creature}s \
going here and there")
    print("-"*60)
    time.sleep(3)
    print(f"{source} say that a {monster} eats {creature}s")
    print("-"*60)
    time.sleep(3)
    print(f"On your left is a house, on your right is a road and in your hand \
is a small, {color_of_wand} wand")
    print("-"*60)
    time.sleep(3)
    # Set score
    set_score = initialize_score
    score_0 = set_score()
    print("-"*60)
    # Giving player choices
    while True:
        way = input("Go to road or knock on the door of the house:(road/house\
) ").lower()
        if way == "road":
            print("-"*60)
            print(f"Score is now {score_0}")
            print("-"*60)
            time.sleep(3)
            print(f"You walk endlessly until you find an old wizard who wants \
he {monster} to die")
            print("-"*60)
            time.sleep(3)
            print(f"He gives you a spear and tells you to go to the \
den of monsters and you will find help there by an old {creature}")
            print("-"*60)
            time.sleep(3)
            print(f"Because the only way to get out and \
go back to the black forest is to help the {creature}s get rid \
of {monster}")
            print("-"*60)
            time.sleep(3)
            # going to the den of monsters
            function_1 = going_to_den
            score_1 = function_1(way, score_0)
            if score_1 is False:
                break
            # Attack mode on the monster
            function_2 = attack_mode
            score_2 = function_2(score_1)
            if score_2 is False:
                break
            # Exit den & upgrade your wand
            print("-"*60)
            print(f"You now exited the den of monsters and \
find an old {creature}")
            print("-"*60)
            time.sleep(2)
            print("He gives you a bigger, stronger wand")
            print("-"*60)
            time.sleep(2)
            # appreciate help
            while True:
                accept = input("Do you accept his help?[y/n] ").lower()
                if accept == "y" or accept == "n":
                    break
                else:
                    print("-"*60)
                    print("Not a reply !!!")
                    print("-"*60)
            function_3 = appreciate_help
            score_3 = function_3(score_2, accept)
            time.sleep(2)
            # meeting either dragon, werewolf or devil
            print("Then you go really slow until you find ...")
            print("-"*60)
            time.sleep(2)
            print(f"the {monster} all {creature}s spoke about !!!!")
            print("-"*60)
            # How do you react to the dragon, werewolf or devil??
            function_4 = react_to_monster
            score_4 = react_to_monster(score_3, accept)
            time.sleep(2)
            break
        elif way == "house":
            print("-"*60)
            print(f"Score is now {score_0}")
            print("-"*60)
            time.sleep(3)
            print(f"{creature}s open for you and tell you everything \
about the {monster} and give you a spear and tell you to go to \
the den of monsters")
            print("-"*60)
            time.sleep(3)
            print(f"Plus, they give a super-fast vehicle whose speed is \
1000 miles/hour !!!")
            print("-"*60)
            time.sleep(3)
            # going to the den of monsters
            function_1 = going_to_den
            score_1 = function_1(way, score_0)
            # play again option
            if score_1 is False:
                break
            # Attack mode on the monster
            function_2 = attack_mode
            score_2 = function_2(score_1)
            # Play again
            if score_2 is False:
                break
            print("-"*60)
            time.sleep(2)
            # Exit den & upgrade your wand
            print(f"You now exited the den of monsters and find an old \
{creature}")
            print("-"*60)
            time.sleep(2)
            print("He gives you a bigger, stronger wand")
            print("-"*60)
            time.sleep(2)
            # appreciate help
            while True:
                accept = input("Do you accept his help?[y/n] ").lower()
                if accept == "y" or accept == "n":
                    break
                else:
                    print("-"*60)
                    print("Not a reply !!!")
                    print("-"*60)
            function_3 = appreciate_help
            score_3 = function_3(score_2, accept)
            time.sleep(2)
            # meeting either the dragon, werewolf or devil
            print("Then you go super fast until you find ...")
            print("-"*60)
            time.sleep(2)
            print(f"the {monster} all {creature}s spoke about !!!!")
            print("-"*60)
            time.sleep(2)
            # How do you react to the dragon, werewolf or devil??
            function_4 = react_to_monster
            score_4 = react_to_monster(score_3, accept)
            time.sleep(2)
            break
        else:
            print("-"*60)
            print("Not a destination please type again !!")
            print("-"*60)
    # Play again option
    replay = play_again
    replay_1 = replay()
    if replay_1 is False:
        break
