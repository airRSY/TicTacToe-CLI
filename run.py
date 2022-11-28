# --- MODULES ---
from game.game import GameClass
from cli.cli import CliClass


# -- INIT MODULES --
Game = GameClass()
CLI = CliClass(Game)
Game.set_cli_class(CLI)


# --- MAIN CODE ---
# -- MAIN FUNCTIONS --
def restart_game() -> bool:
    yes = ("iya", "ya", "ulang", "kembali", "y", "mengulang", "yes")

    print()
    print("Ingin mengulang permainan?")
    reset_input = str(input(">> "))

    if reset_input in yes:
        Game.reset()
        Game.is_game_running = True
        return True
    else:
        return False


# -- MAIN LOOP --
while True:
    CLI.display_cli()
    if not (Game.get_input_send_request()):
        continue
    Game.set_game_state()

    if not Game.is_game_running and not restart_game():
        break
