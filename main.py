# Jemmy Seang
from TicTacToe import TicTacToe
version = "1.0"
wmsg = f"~ Tic Tac Toe {version} by JemButt ~"

def askName():
    p1 = input(f"--> Player X Name: ")
    p2 = input(f"--> Player O Name: ")
    pxo = input(f"--> Who goes first? X or O? ").lower()
    while True:
        if pxo == "x" or pxo == "o":
            break
        else:
            pxo = input(f"--> Invalid input! Enter X or O: ").lower()
    return [p1, p2, pxo, version]

def askInput(whois, xo):
    n = input(f"[{whois}({xo})] Enter a number from 1-9: ")
    while True:
        if n.isdigit():
            n = int(n)
            if n > 0 and n < 10:
                break
            else:
                n = input(f"[{whois}({xo})] Invalid range! Enter a number from 1-9: ")
        else:
            n = input(f"[{whois}({xo})] Invalid input! Enter a number from 1-9: ")
    return n

# Main Program
print(wmsg)
nl = askName()

jembutt = TicTacToe(nl[0], nl[1], nl[2], version)
print()
jembutt.welcome()

## Starting game!
jembutt.pBoard()

while jembutt.win is False:
    if jembutt.countinput < 8:
        while True:
            num = askInput(jembutt.pxo, jembutt.xo)
            valid = jembutt.isValid(num)
            if valid is True:
                jembutt.drawBoard(num)
                jembutt.checkWin()
                jembutt.pBoard()
                break
            else:
                print(f"[{jembutt.pxo}({jembutt.xo})] Location is Occupied! Try again!")
    else:
        jembutt.autoInput()
        print(f"[{jembutt.pxo}({jembutt.xo})] Bot auto input: {jembutt.autonum}")
        jembutt.pBoard()
        jembutt.checkWin()
        jembutt.countinput += 1

    if jembutt.win == True:
        print(f"[System] {jembutt.pxo}({jembutt.xo}) wins the game!")
        break
    else:
        if jembutt.countinput < 8:
            jembutt.countinput += 1
        jembutt.switchPlayer()
    
    if jembutt.countinput == 9:
        print(f"[System] No one wins! DRAW!")
        break
    

