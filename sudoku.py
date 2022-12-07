"""
Project 4 Group Assignment
Class: COP3502C
Semester: Fall 2022
Professor: Amanpreet Kapoor
Group Number: 9
Team Members: Daniel Kim, Carter Chavez, Alexis Cobb, and Kaleb Hoenisch
"""


from sudoku_generator import *

start_game = True
while start_game:
    game_on = True

    print("Welcome to Sudoku")
    menu_option_needed = True
    while menu_option_needed:
      # Loop executes while the program requires valid user input for the desired menu option
      try:
        print("\nSelect Game Mode:")
        game_mode = int(input("1. Easy | 2. Medium | 3. Hard\n"))
        print()
      except:
        print("Please select option 1, 2, or 3.")
        continue
      if game_mode != 1 and game_mode != 2 and game_mode != 3:
        print("Please select option 1, 2, or 3.")
      elif game_mode == 1 or game_mode == 2 or game_mode == 3:
        menu_option_needed = False

    solution = []
    if game_mode == 1:
        s = SudokuGenerator(9, 30)
        s.fill_values()
        solution = [num[:] for num in s.board]  # filled board solution
        s.remove_cells()

    elif game_mode == 2:
        s = SudokuGenerator(9, 40)
        s.fill_values()
        solution = [num[:] for num in s.board]  # filled board solution
        s.remove_cells()

    elif game_mode == 3:
        s = SudokuGenerator(9, 50)
        s.fill_values()
        solution = [num[:] for num in s.board]  # filled board solution
        s.remove_cells()

    og_board = [num[:] for num in s.board
                ]  # keeps track of the original board after removals

    while game_on:
        s.print_board()
        print("1. Fill in a box")
        print("2. Reset board")
        print("3. Restart")
        print("4. Quit")
        obtaining_input = True
        while obtaining_input:
          try:
            menu_input = int(input("\nChoose an option: "))
          except:
            print("\nPlease select a value between 1 and 4 (inclusive).")
            continue
          obtaining_input = False
        x_coor = None
        y_coor = None
        win = None
        if menu_input == 1:
            # Executes when the user enters "1" to fill in a box in the sudoku board
            obtaining_row_input = True
            obtaining_column_input = True
            while obtaining_column_input:
              # Loop executes while the program requires valid input for the board column
              try:
                column = int(input("Column: ")) - 1
              except:
                print("Please enter an integer between 1 and 9 (inclusive).")
                continue
              if column < 0 or column > 8:
                print("Please enter an integer between 1 and 9 (inclusive).")
                continue
              elif column >=0 and column <= 8:
                obtaining_column_input = False
            while obtaining_row_input:
              # Lopp executes whil the program requires valid input for the board row
              try:
                row = int(input("Row: ")) - 1
              except:
                print("Please enter an integer between 1 and 9 (inclusive).")
                continue
              if row < 0 or row > 8:
                print("Please enter an integer between 1 and 9 (inclusive)")
                continue
              elif row >=0 and row <= 8:
                obtaining_row_input = False
            while s.board[row][column] != 0 and s.board[row][column] == og_board[row][column]:
                print("Your selection is a generated number, please make another selection.")
                column = int(input("Column: ")) - 1
                row = int(input("Row: ")) - 1
            if s.board[row][column] == 0:
                # This code block automatically executes if the box is a "0," indicating it can be filled
                obtaining_choice = True
                while obtaining_choice:
                  try:
                    choice = int(input("Enter a number to fill in the box: "))
                  except:
                    print("Please enter a number between 1 and 9 (inclusive) to fill in the box.")
                    continue
                  if choice < 1 or choice > 9:
                      print(
                        "Please enter a number between 1 and 9 (inclusive) to fill in the box."
                      )
                  else:
                      s.board[row][column] = choice
                      print(f"\nBox at row {row + 1} and column {column + 1} is now {choice}.\n")
                      obtaining_choice = False
            elif s.board[row][column] != 0 and not(s.board[row][column] == og_board[row][column]):
                # Checks whether the selected box is filled in the original board, even if the current
                # box is not a "0."
                obtaining_choice = True
                while obtaining_choice:
                  try:
                    choice = int(input("Enter a number to fill in the box: "))
                  except:
                    print("Please enter a number between 1 and 9 (inclusive) to fill in the box.")
                    continue
                  if choice < 1 or choice > 9:
                      print(
                        "Please enter a number between 1 and 9 (inclusive) to fill in the box."
                      )
                  else:
                    s.board[row][column] = choice
                    print(f"\nBox at row {row + 1} and column {column + 1} is now {choice}.\n")
        elif menu_input == 2:
            # Option 2 allows the user to reset the game board to its original state.
            for i in range(len(s.board)):
                for j in range(len(s.board[i])):
                    s.board[i][j] = og_board[i][j]
            print("Board reset complete!\n")
        elif menu_input == 3:
            # Option 3 allows the user to restart the entire game, generating a new board.
            print("Restarting game...\n\n")
            game_on = False
        elif menu_input == 4:
            # Option 4 allows the user to exit the program entirely.
            game_on = False
            start_game = False
            print("\nExiting game. Thank you for playing!")
        elif menu_input != 1 and menu_input != 2 and menu_input != 3 and menu_input != 4:
            print(
                "\nInvalid selection: please select menu options 1, 2, 3, or 4.\n"
            )

        complete_board = True
        for i in range(9):
            # Checks for board completion - if there are any blank spaces, the board is incomplete
            for j in range(9):
                if s.board[i][j] == 0:
                    complete_board = False
        if complete_board:
            # Checks whether the board matches the true solution. If true, the player wins.
            # If false, the "Game Over" message will display and the game will resume.
            win = True
            for i in range(9):
              for j in range(9):
                if s.board[i][j] != solution[i][j]:
                  win = False
            game_on = False
          
            if win:
                s.print_board()
                print("You won!\n")
                print("Restarting game...\n\n")
    
            elif not win:
                s.print_board()
                print("GAME OVER :(")
                print("\nRestarting game...\n\n")

