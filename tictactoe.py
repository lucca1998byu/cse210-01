import os
clear = lambda: os.system('cls')


def main():
    clear()
    tab = table()
    game_over =True
    
    while game_over:
        choice = player_choice(player=1)
        
        change(tab, choice, player="❌")
        x = finish(tab)
        if x == True:
            break
       
        choice = player_choice(player=2)
        change(tab, choice, player="⭕")
        x = finish(tab)
        if x == True:
            break
      
       


    
   
    
        

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
    {table[0]}{table[1]}{table[2]}
    {table[3]}{table[4]}{table[5]}
    {table[6]}{table[7]}{table[8]}
    """)


def finish(table):
    if (table[0] == table[1] == table[2] == '⭕' or
        table[3] == table[4] == table[5] == '⭕' or
        table[6] == table[7] == table[8] == '⭕' or
        table[0] == table[3] == table[6] == '⭕' or
        table[1] == table[4] == table[7] == '⭕' or
        table[2] == table[5] == table[8] == '⭕' or
        table[0] == table[4] == table[8] == '⭕' or
        table[2] == table[4] == table[6] == '⭕'):
        print("2 is the winner")
        return True
        
    elif (table[0] == table[1] == table[2] == '❌' or
        table[3] == table[4] == table[5] == '❌' or
        table[6] == table[7] == table[8] == '❌' or
        table[0] == table[3] == table[6] == '❌' or
        table[1] == table[4] == table[7] == '❌' or
        table[2] == table[5] == table[8] == '❌' or
        table[0] == table[4] == table[8] == '❌' or
        table[2] == table[4] == table[6] == '❌'):
        print("1 is the winner")
        return True
    elif table[0] != '⬜️' and table[1] != "⬜️" and table[2] != "⬜️" and table[3] != "⬜️" and table[4] != "⬜️" and table[5] !="⬜️" and table[6] != "⬜️" and table[7] != "⬜️" and table[8] != "⬜️":
        print("It's a draw")
        return True
    
        
        


if __name__ == "__main__":
    main()