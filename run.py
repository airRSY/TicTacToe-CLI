# --- MODULES ---
from game.game import GameClass
from cli.cli import CliClass


# -- INIT MODULES --
Game = GameClass()
CLI = CliClass(Game)
Game.set_cli_class(CLI)


# --- MAIN CODE ---
# -- MAIN FUNCTIONS --
def is_restart_game() -> bool:
    """ Ask the user and then restart the game if yes, then restart.

    When called, this functions will ask the user if they want to restart the game.
    If the user wants to restart the game. They have to write the words in the **accepted list**.
    This will resets the game by calling the **GameClass.reset()** function.

    If the user doesn't wants to restart the game. They have to write something that is not in
    the accepted list.

    **The accepted words are: "iya", "ya", "ulang", "kembali", "y", "mengulang", "yes"**

    :return: Is the user wants to restart
    """

    yes = ("iya", "ya", "ulang", "kembali", "y", "mengulang", "yes")

    print()
    print("Ingin mengulang permainan?")
    reset_input = str(input(">> "))

    if reset_input in yes:
        Game.reset()
        return True
    else:
        return False


# -- MAIN LOOP --
while True:
    CLI.display_cli()
    if not (Game.get_input_send_request()):
        continue
    Game.set_game_state()

    if not Game.is_game_running and not is_restart_game():
        break
