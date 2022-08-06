from game import *

from game_display import GameDisplay

def main_loop(gd: GameDisplay) -> None:
    game = Game()
    state = KEEP_PLAYING
    
    init_game(gd, game)

    while state != LOSE:
        key_clicked = gd.get_key_clicked()

        state = game.single_turn(key_clicked)
        game.draw(gd)
        gd.show_score(int(game.get_score()))
        
        gd.end_round()
    
    if state == WIN:
        print("You've won!")
    elif state == LOSE:
        print("You've lost the game :(")
    else:
        print("How'd you even do that weirdo")
    
def init_game(gd, game):
    gd.show_score(game.get_score())
    game.draw(gd)
    gd.end_round()