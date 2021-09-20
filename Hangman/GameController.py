from HangmanClass import HangmanGame


def run_game():
    game = HangmanGame()
    playing = True

    while playing:
        game.make_guess(game.get_guess_input())
        game.print_game_state()

        # Prompt user to restart if game is over
        if game.is_game_over():
            restart = input("\n\nWould you like to play again (Y/y to play again): ")
            if restart in ['Y', 'y']:
                game.reset_game()
            else:
                playing = False

    print("Thank you for playing")


