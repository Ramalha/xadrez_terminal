import os
import colorama
from colorama import Fore
from colorama import init
import time
import sys
from time import sleep
init(autoreset=True)


peao2 = Fore.BLUE + '♙'
torre2 = Fore.BLUE + '♖'
cavalo2 = Fore.BLUE + '♘'
bispo2 = Fore.BLUE + '♗'
rei2 = Fore.BLUE + '♔'
rainha2 = Fore.BLUE + '♕'

peao1 = Fore.WHITE + '♙'
torre1 = Fore.WHITE + '♜'
cavalo1 = Fore.WHITE + '♞'
bispo1 = Fore.WHITE + '♝'
rei1 = Fore.WHITE + '♚'
rainha1 = Fore.WHITE + '♛'



def create_grid(rows, cols):
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    grid[0][0] = torre1  # Peça correspondente a 1,1
    grid[0][1] = cavalo1  # Peça correspondente a 1,2
    grid[0][2] = bispo1  # Peça correspondente a 1,3
    grid[0][3] = rei1  # Peça correspondente a 1,4
    grid[0][4] = rainha1  # Peça correspondente a 1,5
    grid[0][5] = bispo1  # Peça correspondente a 1,6
    grid[0][6] = cavalo1  # Peça correspondente a 1,7
    grid[0][7] = torre1  # Peça correspondente a 1,8
    
    grid[1] = [peao1 for _ in range(cols)]  # Peças correspondentes a segunda fileira
    
    grid[6] = [peao2 for _ in range(cols)]  # Peças correspondentes a sétima fileira
    
    grid[7][0] = torre2  # Peça correspondente a 8,1
    grid[7][1] = cavalo2  # Peça correspondente a 8,2
    grid[7][2] = bispo2  # Peça correspondente a 8,3
    grid[7][3] = rei2  # Peça correspondente a 8,4
    grid[7][4] = rainha2  # Peça correspondente a 8,5
    grid[7][5] = bispo2  # Peça correspondente a 8,6
    grid[7][6] = cavalo2  # Peça correspondente a 8,7
    grid[7][7] = torre2  # Peça correspondente a 8,8
    
    return grid

def print_grid(grid):
    print(Fore.GREEN + '#==========================================================================#')
    print(Fore.GREEN + r'''
           __   __                  __                            
          /\ \ /\ \                /\ \                           
          \ `\`\/'/'       __      \_\ \     _ __    __     ____  
           `\/ > <       /'__`\    /'_` \  /\`'__\ /'__`\  /',__\ 
              \/'/\`\   /\ \L\.\_ /\ \L\ \ \ \ \/ /\  __/ /\__, `\
              /\_\\ \_\ \ \__/.\_\\ \___,_\ \ \_\ \ \____\\/\____/
              \/_/ \/_/  \/__/\/_/ \/__,_ /  \/_/  \/____/ \/___/ 
                                                       
''')

    print(Fore.GREEN + '#==========================================================================#')
    print(Fore.WHITE + ' ')

    baarra1 = Fore.WHITE + ' │ '
                                                
    
    print("                     ┌───┐ ┌───┬───┬───┬───┬───┬───┬───┬───┐")
    for i, row in reversed(list(enumerate(grid))):
        formatted_row = baarra1.join(row)
        print(f"                     │ {i+1} │ │ {formatted_row} " + Fore.WHITE + "│")
        if i != len(grid) -8:
          print(f"                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤")
    print("                     └───┘ └───┴───┴───┴───┴───┴───┴───┴───┘")
    print("                           ┌───┬───┬───┬───┬───┬───┬───┬───┐")
    print("                           │ A │ B │ C │ D │ E │ F │ G │ H │")
    print("                           └───┴───┴───┴───┴───┴───┴───┴───┘")
    print(' ')
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_intro_menu():
    print(Fore.GREEN + r'''
 __   __                 __                                                    
/\ \ /\ \               /\ \                                                   
\ `\`\/'/'      __      \_\ \    _ __     __     ____       _____    __  __    
 `\/ > <      /'__`\    /'_` \  /\`'__\ /'__`\  /',__\     /\ '__`\ /\ \/\ \   
    \/'/\`\  /\ \L\.\_ /\ \L\ \ \ \ \/ /\  __/ /\__, `\ __ \ \ \L\ \\ \ \_\ \  
    /\_\\ \_\\ \__/.\_\\ \___,_\ \ \_\ \ \____\\/\____//\_\ \ \ ,__/ \/`____ \ 
    \/_/ \/_/ \/__/\/_/ \/__,_ /  \/_/  \/____/ \/___/ \/_/  \ \ \/   `/___/> \
                                                              \ \_\      /\___/
                                                               \/_/      \/__/
''')
    
    print(Fore.GREEN +'----------------------------------------------------------------------------------')
    print(Fore.BLUE + '\nBem-vindo ao jogo de xadrez em Python!\n')
    print(Fore.GREEN +'----------------------------------------------------------------------------------\n')
    
    while True:
        choice = input("Gostaria de iniciar o jogo? (sim/nao):").lower()
        print(' ')
        clear_screen()
        print(Fore.GREEN + '#==========================================================================#')
        if choice == "sim":
            lol = Fore.GREEN + '♙'
            print(Fore.GREEN + r'''
   ____                               
  / ___|   ___    _ __ ___     ___    
 | |      / _ \  | '_ ` _ \   / _ \   
 | |___  | (_) | | | | | | | | (_) |  
  \____|  \___/  |_| |_| |_|  \___/                
    ''')
            print(Fore.GREEN + r'''
                        _                                
                       | |   ___     __ _    __ _   _ __ 
                    _  | |  / _ \   / _` |  / _` | | '__|
                   | |_| | | (_) | | (_| | | (_| | | |   
                    \___/   \___/   \__, |  \__,_| |_|   
                                    |___/                 
    ''')
            print(Fore.GREEN + '#==========================================================================#')
            print("                                                     ┌────┐")
            print(Fore.BLUE + 'Primeiro selecione a peça que deseja mover, exemplo:' + Fore.WHITE +  f" │ {lol}" + Fore.WHITE + "  │")
            print("                                                     └────┘\n")
            print(Fore.GREEN +'----------------------------------------------------------------------------------\n')
            print(Fore.BLUE + "Vamos supor que você queira mover esse peão.\n")
            print(Fore.BLUE + "Digamos que ele esteja na posição 2,a do tabuleiro.\n")
            print(Fore.GREEN +'----------------------------------------------------------------------------------\n')
            print(Fore.RED + 'Você teria que digitar primeiro o eixo Y e depois o X\n')
            print(Fore.RED + 'Eixo Y seria '+ Fore.GREEN + '[ 2 ]' )
            print(Fore.RED + 'Eixo X seria '+ Fore.GREEN + '[ a ] ' + Fore.RED + 'em letra ' + Fore.GREEN + '[ minuscula ]\n')
            print(Fore.RED + 'Você teria de colocar uma '+ Fore.GREEN +'[ , ]' + Fore.RED + ' entre os eixos' + Fore.GREEN + ' [ 2,a ]\n')
            print(Fore.GREEN +'----------------------------------------------------------------------------------\n')
            print('                     ┌───┐ ┌───┬───┬───┬───┬───┬───┬───┬───┐')
            print('                     │ 8 │ │ ♖ │ ♘ │ ♗ │ ♔ │ ♕ │ ♗ │ ♘ │ ♖ │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 7 │ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 6 │ │   │   │   │   │   │   │   │   │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 5 │ │   │   │   │   │   │   │   │   │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 4 │ │   │   │   │   │   │   │   │   │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 3 │ │   │   │   │   │   │   │   │   │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 2 │' + Fore.WHITE +  f' │ {lol}' + Fore.WHITE + ' │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 1 │ │ ♜ │ ♞ │ ♝ │ ♚ │ ♛ │ ♝ │ ♞ │ ♜ │')
            print('                     └───┘ └───┴───┴───┴───┴───┴───┴───┴───┘')
            print('                           ┌───┬───┬───┬───┬───┬───┬───┬───┐')
            print('                           │ A │ B │ C │ D │ E │ F │ G │ H │')
            print('                           └───┴───┴───┴───┴───┴───┴───┴───┘ \n')
            print(Fore.GREEN +'----------------------------------------------------------------------------------\n')
            
            print(Fore.BLUE + 'Digamos que você queira mover o peão duas casas para frente.\n')
            print(Fore.BLUE + 'Você deve selecionar a nova "cordenada" do eixo X e Y\n') 
            print(Fore.GREEN +'----------------------------------------------------------------------------------\n')
            print(Fore.RED + 'Eixo Y seria '+ Fore.GREEN + '[ 4 ]' )
            print(Fore.RED + 'Eixo X seria '+ Fore.GREEN + '[ a ] ' + Fore.RED + 'em letra ' + Fore.GREEN + '[ minuscula ]\n')
            print(Fore.RED + 'Você teria de colocar uma '+ Fore.GREEN +'[ , ]' + Fore.RED + ' entre os eixos' + Fore.GREEN + ' [ 2,a ]\n')
            print(Fore.GREEN +'----------------------------------------------------------------------------------\n')
            print('                     ┌───┐ ┌───┬───┬───┬───┬───┬───┬───┬───┐')
            print('                     │ 8 │ │ ♖ │ ♘ │ ♗ │ ♔ │ ♕ │ ♗ │ ♘ │ ♖ │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 7 │ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 6 │ │   │   │   │   │   │   │   │   │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 5 │ │   │   │   │   │   │   │   │   │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 4 │ ' + Fore.WHITE +  f'│ {lol}' + Fore.WHITE + ' │   │   │   │   │   │   │   │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 3 │ │   │   │   │   │   │   │   │   │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 2 │ │   │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │')
            print('                     ├───┤ ├───┼───┼───┼───┼───┼───┼───┼───┤')
            print('                     │ 1 │ │ ♜ │ ♞ │ ♝ │ ♚ │ ♛ │ ♝ │ ♞ │ ♜ │')
            print('                     └───┘ └───┴───┴───┴───┴───┴───┴───┴───┘')
            print('                           ┌───┬───┬───┬───┬───┬───┬───┬───┐')
            print('                           │ A │ B │ C │ D │ E │ F │ G │ H │')
            print('                           └───┴───┴───┴───┴───┴───┴───┴───┘ \n')
            print(Fore.GREEN +'----------------------------------------------------------------------------------\n')
            pronto = input('Se entendeu tudo e deseja prosseguir para o jogo digite [ok]:\n'+ ' \n' + Fore.WHITE + ":").lower()
            if pronto == "ok":
              break 
      
        elif choice == "nao":
    # animação = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            print("Carregando:")
            animando = [Fore.GREEN +"■□□□□□□□□□",Fore.GREEN +"■■□□□□□□□□", Fore.GREEN +"■■■□□□□□□□", Fore.GREEN +"■■■■□□□□□□", Fore.GREEN +"■■■■■□□□□□", Fore.GREEN +"■■■■■■□□□□", Fore.GREEN +"■■■■■■■□□□", Fore.GREEN +"■■■■■■■■□□", Fore.GREEN +"■■■■■■■■■□", Fore.GREEN +"■■■■■■■■■■"]
            
            for i in range(len(animando)):
                time.sleep(0.2)
                sys.stdout.write("\r" + animando[i % len(animando)])
                sys.stdout.flush()
            
            print("\n")
            print(Fore.BLUE + '\nAté logo!\n')
            print(Fore.GREEN +  r'''
 ____                  __                                           
/\  _`\               /\ \                                          
\ \ \L\ \   __  __    \ \ \       __  __    ___      __       ____  
 \ \  _ <' /\ \/\ \    \ \ \  __ /\ \/\ \  /'___\  /'__`\    /',__\ 
  \ \ \L\ \\ \ \_\ \    \ \ \L\ \\ \ \_\ \/\ \__/ /\ \L\.\_ /\__, `\
   \ \____/ \/`____ \    \ \____/ \ \____/\ \____\\ \__/.\_\\/\____/
    \/___/   `/___/> \    \/___/   \/___/  \/____/ \/__/\/_/ \/___/ 
                /\___/                                              
                \/__/
''')
            print(Fore.GREEN +'----------------------------------------------------------------------------------')
            exit()
        else:
            print("Opção inválida. Por favor, escolha 'sim' ou 'nao'.")


def main():
    show_intro_menu()

    rows = 8
    cols = 8
    grid = create_grid(rows, cols)
    
    while True:
        try:
            clear_screen()
            print_grid(grid)
    
            print(Fore.GREEN + '#==========================================================================#\n')
    
            input_str = input(Fore.CYAN +"Digite as coordenadas da peça ou 'sair' para encerrar:\n" + ' \n' + Fore.WHITE + ":")
            print(Fore.GREEN +'----------------------------------------------------------------------------------')
    
            if input_str.lower() == 'sair':
                break
    
            x_str, y_str = input_str.split(',')
            x = int(x_str) - 1  # Ajuste para coordenadas internas de 0 a 7
            y = ord(y_str.lower()) - ord('a')  # Convertendo a coordenada alfanumérica para numérica
    
            if 0 <= x < rows and 0 <= y < cols:
                selected_piece = grid[x][y]
                sp = selected_piece
                print("                  ┌────┐")
                print(Fore.RED + "Peça selecionada:" + Fore.WHITE +  f" │ {sp}" + Fore.WHITE + "  │")
                print("                  └────┘")
                print(Fore.GREEN +'---------------------------------------------------------------------------\n')
    
                move_input = input(Fore.CYAN +"Digite as coordenadas para mover a peça ou 'cancelar' para cancelar:\n" + ' \n' + Fore.WHITE + ":")
                print(' ')
                print(Fore.GREEN + '#==========================================================================#')
                sleep(.8)
                
                if move_input.lower() == 'cancelar':
                    continue
    
                new_x_str, new_y_str = move_input.split(',')
                new_x = int(new_x_str) - 1  # Ajuste para coordenadas internas de 0 a 7
                new_y = ord(new_y_str.lower()) - ord('a')  # Convertendo a coordenada alfanumérica para numérica
                
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    new_grid = [row[:] for row in grid]
                    new_grid[new_x][new_y] = selected_piece
                    new_grid[x][y] = ' '
                    grid = new_grid
                else:
                    print("Coordenada de destino fora dos limites da grade.")
            else:
                print("Coordenada fora dos limites da grade.")
        
        except ValueError:
            print("Entrada inválida. Certifique-se de usar o formato x,y.")

    # animação = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    clear_screen()
    print("Carregando:")
    animando = [Fore.GREEN +"■□□□□□□□□□",Fore.GREEN +"■■□□□□□□□□", Fore.GREEN +"■■■□□□□□□□", Fore.GREEN +"■■■■□□□□□□", Fore.GREEN +"■■■■■□□□□□", Fore.GREEN +"■■■■■■□□□□", Fore.GREEN +"■■■■■■■□□□", Fore.GREEN +"■■■■■■■■□□", Fore.GREEN +"■■■■■■■■■□", Fore.GREEN +"■■■■■■■■■■"]
        
    for i in range(len(animando)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animando[i % len(animando)])
        sys.stdout.flush()
        
    print("\n")
    
    print(Fore.GREEN +  r'''
     ____                  __                                           
    /\  _`\               /\ \                                          
    \ \ \L\ \   __  __    \ \ \       __  __    ___      __       ____  
     \ \  _ <' /\ \/\ \    \ \ \  __ /\ \/\ \  /'___\  /'__`\    /',__\ 
      \ \ \L\ \\ \ \_\ \    \ \ \L\ \\ \ \_\ \/\ \__/ /\ \L\.\_ /\__, `\
       \ \____/ \/`____ \    \ \____/ \ \____/\ \____\\ \__/.\_\\/\____/
        \/___/   `/___/> \    \/___/   \/___/  \/____/ \/__/\/_/ \/___/ 
                    /\___/                                              
                    \/__/
    ''')
    print(' ')
    print(Fore.BLUE + '\nAté logo!\n')
    print(Fore.GREEN +'---------------------------------------------------------------------------\n')
    exit()




if __name__ == "__main__":
    main()