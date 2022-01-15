import os
clear = lambda: os.system('cls')
import random

def main():
    
    def multiplayer():
        
        tab = table()
        
        game_over = True
        while game_over:
            choice = player_choice(player=1)
            clear()
            change(tab, choice, player="❌")
            x = finish(tab, single=False)
            if x == True:
                break
            
            choice = player_choice(player=2)
            clear()
            change(tab, choice, player="⭕")
            x = finish(tab, single=False)
            if x == True:
                break

    def singleplayer():
        tab = table()
        
        game_over = True
        while game_over:
            choice = player_choice(player=1)
            clear()
            change(tab, choice, player="❌")
            x = finish(tab, single=True)
            if x == True:
                break
            
            computer = computer_choice()
            clear()
            change(tab, computer, player="⭕")
            x = finish(tab, single=True)
            if x == True:
                break
        

    clear()
    players = int(input("type 1 to play versus the computer\ntype 2 to play with another player\n"))    
    if players == 2:
        multiplayer()
    else:
        singleplayer()

    
        
def computer_choice():
    return random.randint(1,9)


def player_choice(player):
    choice = int(input(f"Player {player} choose: "))
    
    return choice

def table():
    tab = ['⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️','⬜️']
    print(f"""
  TIC TAC TOE

    {tab[0]}{tab[1]}{tab[2]}
    {tab[3]}{tab[4]}{tab[5]}
    {tab[6]}{tab[7]}{tab[8]}

    """)
    return tab

def change(table, choice, player):
    table[choice - 1] = player
    print(f"""

  TIC TAC TOE

    {table[0]}{table[1]}{table[2]}
    {table[3]}{table[4]}{table[5]}
    {table[6]}{table[7]}{table[8]}
    """)

def finish(table, single):
    if (table[0] == table[1] == table[2] == '⭕' or
        table[3] == table[4] == table[5] == '⭕' or
        table[6] == table[7] == table[8] == '⭕' or
        table[0] == table[3] == table[6] == '⭕' or
        table[1] == table[4] == table[7] == '⭕' or
        table[2] == table[5] == table[8] == '⭕' or
        table[0] == table[4] == table[8] == '⭕' or
        table[2] == table[4] == table[6] == '⭕'):
        if single:
            print("You lost")
        else:
            print("Player 2 is the winner")

        return True
        
    elif (table[0] == table[1] == table[2] == '❌' or
        table[3] == table[4] == table[5] == '❌' or
        table[6] == table[7] == table[8] == '❌' or
        table[0] == table[3] == table[6] == '❌' or
        table[1] == table[4] == table[7] == '❌' or
        table[2] == table[5] == table[8] == '❌' or
        table[0] == table[4] == table[8] == '❌' or
        table[2] == table[4] == table[6] == '❌'):
        if single:
            print("You win")
        else:
            print("Player 2 is the winner")

        return True
    
        
    elif table[0] != '⬜️' and table[1] != "⬜️" and table[2] != "⬜️" and table[3] != "⬜️" and table[4] != "⬜️" and table[5] !="⬜️" and table[6] != "⬜️" and table[7] != "⬜️" and table[8] != "⬜️":
        print("It's a draw")
        return True
    
        

if __name__ == "__main__":
    main()