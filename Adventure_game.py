# Import statments
import time
import random


# Function for printing a message and pausing for a requested time
def print_pause(message, pause_time=1.8):

    print(message)
    time.sleep(pause_time)


# Function for valdiating user's input
def valid_input(prompt_type):

    validated_input = None

    # If the input is the choices that the player makes in the game
    if prompt_type == "options":
        while validated_input not in ["1", "2"]:
            validated_input = input("(Please enter 1 or 2)")

    # If the input is about wether the player plays again or quits
    if prompt_type == "play again":
        while validated_input not in [True, False]:
            validated_input = input("Would you like to play again?"
                                    "(y/n)").lower()
            if validated_input in ["y", "yes"]:
                validated_input = True
            if validated_input in ["n", "no"]:
                validated_input = False

    # Returning the player's validated input
    return validated_input


# Class for the first option
# (meeting_girl is the only class (option to play) now)
class meeting_girl:

    # __init__ function and the used variables
    def __init__(self):

        self.place = random.choice(["park", "garden", "farm"])
        self.clothes_color = random.choice(["blue", "black", "white"])
        self.input = None
        self.total_score = 5
        self.gone_to_house = False

    # Methode 1 : Discribes what is happening
    def describe_what_is_happening(self):

        print_pause(f"You see a very pretty girl in the {self.place}.")
        print_pause("She is setting next to the flowers.")
        print_pause("You really like her.")
        print()

    # Methode 2 : -Asks the player wether he wants to play again or quit
    def restart_or_quit(self):

        # Taking player's input
        self.input = valid_input("play again")

        # If player chooses to play again,
        # the game resets all the variables and calls the required methodes
        if self.input:

            # Printing the required message & separative line
            print_pause("Excellent! Restarting the game ...")
            print("--------------------------------------------------------")

            # Reseting the game variables
            self.input = None
            self.gone_to_house = False
            self.total_score = 5
            self.place = random.choice(["park", "garden", "farm"])
            self.clothes_color = random.choice(["blue", "black", "white"])

            # Calling the required methodes
            self.describe_what_is_happening()
            self.place_of_start()

        # If the player chooses to quit,
        # the game prints the required message and quits
        else:

            # Printing the required message and quiting
            print_pause("Thanks for playing! see you next time.")
            quit()

    # Methode 3 : -Shows the choices when the player is at the place
    #              (self.place -> park, garden or a farm)
    #             -Shows the total score of the player
    #             -Takes the input which is the choice that the player chooses
    #              (Moves on after a valid inputs only)
    #             -Calles the required methodes
    #              based on the player's choice to keep the game going
    def place_of_start(self):

        # The choices & score
        print_pause("Enter 1 to approach her.")
        print_pause("Enter 2 to just leave and go to your house.")
        print_pause("What would you like to do?")
        print(f"Your score is : {self.total_score}")

        # Taking input and validationg it
        self.input = valid_input("options")

        # Printing a line to separate these choices from others
        print()

        # Calling the "approach" methode if player choses "1"
        if self.input == "1":

            self.input = None
            self.approach()

        # Calling the "house" methode if player choses "2"
        else:

            self.input = None
            self.house()

    # Methode 4 : -Describes to the player what happened
    #              based on whether it's his 1st time going to the house or not
    #             -Increases player's score as he perfumed himself
    #              & shows choices (1st time in the house only)
    #             -Takes the input which is the choice that the player chooses
    #              (1st time in the house only)
    #             -Updates the score and shows messages
    #              based on the player's choices (1st time in the house only)
    #             -Sends the player back to the place
    def house(self):

        # if the player chose to go to the house for the first time
        if not self.gone_to_house:

            # Describtion of what happens
            print_pause("You can't stop thinking about her.")
            print_pause("So, you decide to go back to her but...")
            print_pause("First you perfume yourself"
                        " and then you go to a shop.")

            # Score updates because the player perfumed themselves
            self.total_score += 5
            print("Your score is :", self.total_score)

            # New choises & taking input and validating it
            print_pause(f"Should you buy (1) Flowers"
                        f" or (2) New {self.clothes_color} clothes for you?")
            self.input = valid_input("options")

            # Printing the message of choice "1" and updating the score
            if self.input == "1":

                self.input = None
                print()
                print_pause(f"You go back to the same {self.place}"
                            " with the flowers.")
                print_pause("While your going there you remember"
                            " that she was already surrounded by flowers.")
                print_pause("But it's too late to go back again so"
                            " you go and put your luck to the test!")

                # Score decreases because, flowers isn't the right choice
                # as the girl is already surrounded by flowers
                self.total_score -= 5

            # Printing the message of choice "2" and updating the score
            else:

                self.input = None
                print()
                print_pause(f"You go back to the same {self.place}"
                            f" with the new {self.clothes_color} clothes.")

                # Score increases because, new clothes is the right choice
                self.total_score += 5

            # Printing a separating line,
            # noting that the player has visited the house once
            # and sending the player to the place again
            print()
            self.gone_to_house = True
            self.place_of_start()

        # if the player chose to go to the house again
        else:

            # Printing the required message
            print_pause("You are too bored.")
            print_pause("And you can't stop thinking about her.")
            print_pause("So, you decide to go back to her.")

            # Printing a separating line
            # & sending the player to the place again
            print()
            self.place_of_start()

    # Methode 5 : -Describes to the player what happends
    #             -Shows the choices
    #             -Takes the input which is the choice that the player chooses
    #              (Moves on after a valid inputs only)
    #             -Updates the score if needed
    #             -Calles the required methodes based on the player's choice
    #              to keep the game going
    def approach(self):

        # Describes what is happening, shows choices
        # and shows the player's score
        print_pause("You walk towards her.")
        print_pause("You are getting closer and more nervous.")
        print_pause("Would you like to (1) Set next to her and talk to her"
                    " or (2) Pretend like nothing happend?")
        print("Your score is :", self.total_score)

        # Taking input
        self.input = valid_input("options")

        # Updating the score if needed
        # & calling the "talk" methode if the player chooses "1"
        if self.input == "1":

            self.input = None

            # Score decreases as the player went to talk to the girl
            #  with bad smell and old clothes
            if not self.gone_to_house:
                self.total_score -= 5

            # Separating line & and calling the "talk" methode
            print()
            self.talk()

        # Resending the player to the place if he chooses "2"
        else:

            self.input = None

            # Printing the required message between two separative lines
            # and resending the player to the place
            print()
            print_pause("You went back to your original spot."
                        " fortunately, she doesn't seem to have noticed you.")
            print()
            self.place_of_start()

    # Methode 6 : -Prints the required message based on the player's score
    #             -Updates the score based on the girl's likings
    #             -Shows the total score
    #              & asks the player wether to play again or quit
    def talk(self):

        # If the player scores 15 points which come from the new clothes
        # and the perfume from the house
        if self.total_score == 15:

            # Score increases because she likes the new clothes & your smell
            self.total_score += 5

            # The message of enough score to win the game
            print_pause("You talk to her.")
            print_pause(f"She likes your new {self.clothes_color}"
                        " clothes and your smell.")
            print_pause("She gives you her number and you go out together.")
            print_pause("You have made her like you. You are victorious!")

        # If the player scores the 5 points
        # which come from the perfume from the house
        elif self.total_score == 5:

            # Score decreases because she didn't like the flowers
            # as she is already surrounded by flowers
            self.total_score -= 5

            # Message of lose
            print_pause("You talk to her but...")
            print_pause("She gets mad.")
            print_pause("Because you got her flowers"
                        " while she is already surrounded by flowers.")
            print_pause("So sadly, she rejected you and you go back home sad.")

        # If the player's scores is 0
        else:

            # Message of lose
            print_pause("You talk to her but...")
            print_pause(f"She didn't like your old cloths and your smell.")
            print_pause("So sadly, she rejected you and you go back home sad.")

        # Showing the score of the player
        # & printing a separative line
        # & asking wether to play again or quit
        print("Your score is :", self.total_score)
        print()
        self.restart_or_quit()


# Class for the second option
# Coming soon

# Game starts
game = meeting_girl()
game.describe_what_is_happening()
game.place_of_start()
