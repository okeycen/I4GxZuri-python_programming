import random


class Game:
    error_msg="Invalid input, try again"
    start_msg= "Please type in one of the options to play game: "
    message="There is no winner. The result is tie"

    def run(output):
        user = str(input(f'''{output.start_msg}
        R for Rock
        P for Paper
        S for Scissors

        '''))
        list=["R","P","S"]
        output.cpu= random.choice(list)
        output.player=user.upper()

        if (output.player in list):
            if(output.cpu==output.player):
                output.result()
                print(output.message)
                output.run()
            else:
                output.result()
                output.winner()
        else:
            print(output.error_msg)
            output.run()

    def result(res):
        mydict= {"R":"Rock", "P":"Paper", "S":"Scissors"  }
        print(f"Player ({mydict[res.player]})  :  CPU ({mydict[res.cpu]})")

    def winner(win):
        # Rock beats Scissors
        # Paper beats Rock
        # Scissors beats Paper
        if (win.cpu=="R" and win.player=="S"):
            print("The winner is CPU")
        elif(win.cpu=="P" and win.player=="R"):
            print("The winner is CPU")
        elif(win.cpu=="S" and win.player=="P"):
            print("The winner is CPU")
        else:
            print("The winner is Player")


game=Game()

game.run()