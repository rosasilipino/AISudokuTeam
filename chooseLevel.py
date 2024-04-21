#Group: Sudoku Team
#Class: CS 450-01
#Project: Final Project
#Date: 04/21/2024

import pygame
import sys

# Color pallet.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
L_GREEN = (150, 255, 150)
RED = (255, 0, 0)
L_RED = (255, 204, 203)
GRAY = (80, 80, 80)
YELLOW = (255, 255, 0)

# Initialize window for pygame.
pygame.init()
X = 700
Y = 700
size = (X, Y)
window = pygame.display.set_mode(size)
font = pygame.font.Font('freesansbold.ttf', 25)

# Function to draw buttons on the screen.
def drawButton(window, left, top, width, height, color, textInButton, font,  hover=False):
    rectSize = pygame.Rect(left, top, width, height)
    if hover:
        hover_color = (color[0] + 95 if color[0] <= 225 else 255, 
                       color[1] + 95 if color[1] <= 225 else 255, 
                       color[2] + 95 if color[2] <= 225 else 255)  # Lighten color for hover
        pygame.draw.rect(window, hover_color, rectSize)  # Draw with hover color
    else:
        pygame.draw.rect(window, color, rectSize)  # Normal color
    pygame.draw.rect(window, BLACK, rectSize, 3)  # Border color
    
    # Render the text
    fontButton = pygame.font.Font('freesansbold.ttf', 20)
    textButton = fontButton.render(textInButton, True, BLACK)
    
    textRectButton = textButton.get_rect()  # Get text rectangle
    textRectButton.center = rectSize.center  # Center text
    window.blit(textButton, textRectButton) # Draw text on button

# Function to choose the level of difficulty.
def chooseLevel(window):
    level = 0 # Initialize level to 0
    fontButton = pygame.font.Font('freesansbold.ttf', 20) # Font for buttons
    pygame.display.set_caption("CS 450 SUDOKU TEAM") # Set window title
    # Render the text
    text = font.render('DIFFICULTY LEVEL', True, BLACK, GRAY)
    textRect = text.get_rect() # Get text rectangle
    textRect.center = (window.get_width() // 2, 300) # Center text
    
    # Loop for event handling for program exiting and input based of user clicks. 
    done = True
    while done:
        window.fill(GRAY)
        window.blit(text, textRect)
        
        pos = pygame.mouse.get_pos()  # Get mouse position
        # Check hover and draw buttons
        drawButton(window, 215, 340, 70, 30, GREEN, "EASY", font, 215 <= pos[0] <= 285 and 340 <= pos[1] <= 370)
        drawButton(window, 315, 340, 70, 30, YELLOW, "MED", font, 315 <= pos[0] <= 385 and 340 <= pos[1] <= 370)
        drawButton(window, 415, 340, 70, 30, RED, "HARD", font, 415 <= pos[0] <= 485 and 340 <= pos[1] <= 370)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("EXITING PROGRAM, X WAS PRESSED.")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("EXITING PROGRAM ESC WAS PRESSED.")
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the click is within any button's rectangle
                if 225 <= pos[0] <= 285 and 340 <= pos[1] <= 370:
                    level = 1
                elif 325 <= pos[0] <= 385 and 340 <= pos[1] <= 370:
                    level = 2
                elif 425 <= pos[0] <= 485 and 340 <= pos[1] <= 370:
                    level = 3
                else:
                    print("INVALID LEVEL DEFAULT TO EASY")
                    level = 1
                return level  # Return level without quitting pygame
        pygame.display.update()
    



# chooseLevel()
