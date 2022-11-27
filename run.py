# --- MODULES ---
from game.game import GameClass
from cli.cli import CliClass
# -- INIT MODULES --
Game = GameClass()
CLI = CliClass(Game)
Game.set_cli_class(CLI)

# --- MAIN CODE ---
# -- MAIN FUNCTIONS --
def restartGame() -> bool:
    yes = ("iya", "ya", "ulang", "kembali", "y", "mengulang", "yes")
    
    CLI.new_line()
    print("Ingin mengulang permainan?")
    resetInput = str(input(">> "))
    
    if (resetInput in yes):
        Game.reset()
        Game.is_game_running = True
        return True
    else:
        return False

# -- MAIN LOOP --
while (True):
    CLI.display_cli()
    if not (Game.get_input_send_request()):
        continue
    Game.set_game_state()
    
    if not (Game.is_game_running) and not (restartGame()):
        break