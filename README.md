# Sudoku App
'''To generate empty sudoku puzzles and let the user fill in until the grid is complete'''

'''It's a GUI-based application using Pygame'''

'''It generates a 9x9 grid and then makes a few blanks for the user to fill[for now it is set to easy mode]'''

'''The difficulty level is managed by hiding a few boxes'''

'''The valid and invalid inputs are color-coded, easy for users'''

'''It detects the win state by checking after every input if the grid is equivalent to the originally generated grid'''

"""File Structure"""

'''game.py- main game loop and pygame application logic'''
'''grid.py-contains grid generation, logic, rendering and input handling'''
'''selection.py-renders number buttons(1-9) for selection'''

"""Dependencies using pip"""
'''pip install pygame'''

"""Code Overview"""

'''SelectNumber-(selection.py)'''
#draw()-to render buttons with hover and selected state
#button_clicked()-to update the currently selected number
#on_button() and button_hover() to detect mouse interaction

'''Grid-(grid.py)'''
#Grid cretions shuffling and cell hiding for gameplay
#Drawing grid lines and numbers
#Mouse input detection and interaction logic
#Validity check against original solution













