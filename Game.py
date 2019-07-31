from ASCIIDisplay import ASCIIDisplay
from GameController import Connect_four_Runner

debug_flag = False

if __name__ == "__main__":


    d = ASCIIDisplay(2) #display driver
    #d.printState(b)
    r = Connect_four_Runner(d)
    r.play_game()
