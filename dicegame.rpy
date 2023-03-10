# Ren'Py automatically loads all script files ending with .rpy. To use this
# fildealer,define a label and jump to it from another file.

define dealer = Character("Dealer")

label minigame:

default player_funds = 1000

init python:
    import random

python:

    #Dice version of 21/blackjack

    dice = list(range(1,21))
	
	#Flag to check if the player wants to keep playing
    player_continue = True

    renpy.say(dealer,"Your funds are [player_funds]")

	#Main loop
    while (player_continue):
        def get_dice():
            return random.choice(dice)

        d1 = get_dice()
        d2 = get_dice()
        d3 = get_dice()
        d4 = get_dice()
        player_sum = d1 + d2
        dealer_sum = d3 + d4

        renpy.say(dealer,"Your rolls are [d1] and [d2], you have [player_sum]. \nDealer's dice is [d3].")
        
		#Checks all possible conditions
        if (player_sum == 21):
                renpy.say(dealer,"Winner winner! You win!")
                player_funds += 2000
                renpy.say(dealer,"Your funds are [player_funds].")

        if (player_sum > 21):
            if (d1 == 20 and d2 == 20):
                renpy.say(dealer,"Jackpot, you win!")
                player_funds += 5000
                renpy.say(dealer,"Your funds are [player_funds].")

            else:
                renpy.say(dealer,"Bust. You Lose...")
                player_funds -= 100
                renpy.say(dealer,"Your funds are [player_funds].")

        else:
            if (d1 == 1 and d2 == 1):
                renpy.say(dealer,"Jackpot, you win!")
                player_funds += 5000
                renpy.say(dealer,"Your funds are [player_funds].")

            else:
                if (d3 > player_sum):
                    renpy.say(dealer,"Dealer stands.\nYou lose...")
                    player_funds -= 100
                    renpy.say(dealer,"Your funds are [player_funds].")

                else:
                    renpy.say(dealer,"Dealer's new dice is [d4]")

                    if (dealer_sum > 21):
                        renpy.say(dealer,"Dealer busts ([dealer_sum]). You win!")
                        player_funds += 200
                        renpy.say(dealer,"Your funds are [player_funds].")

                    elif (player_funds == dealer_sum):
                        renpy.say(dealer,"Dealer has [dealer_sum].")
                        renpy.say(dealer,"It's a tie.")
                        renpy.say(dealer,"Your funds are [player_funds].")

                    else:
                        if (player_sum > dealer_sum):
                            renpy.say(dealer,"Dealer has [dealer_sum].")
                            renpy.say(dealer,"You win!")
                            player_funds += 200
                            renpy.say(dealer,"Your funds are [player_funds].")

                        elif ([player_sum] < [dealer_sum]):
                            renpy.say(dealer,"Dealer has [dealer_sum].")
                            renpy.say(dealer,"You lose...")
                            player_funds -= 100
                            renpy.say(dealer,"Your funds are [player_funds].")


		#Asks if the player wants to keep playing, you should add a "jump" function to go back to your main game if "no" is selected in line 100
        while True:
            keep_playing = renpy.input("Do you wish to play again? y/n")
            if (keep_playing == "y"):
                break
            elif (keep_playing == "n"):
                player_continue = False
                break
            else:
                renpy.say(dealer,"Invalid Choice")
