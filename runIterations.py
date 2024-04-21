import pygame
import sys

def getNumOfRuns(window, message):
    pygame.display.set_caption("CS 450 SUDOKU TEAM") # Set window title
    font = pygame.font.Font('freesansbold.ttf', 25) # Font for buttons
    input = '' # Initialize input to empty string
    input_active = True # Flag for input box
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input = input[:-1]
                elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    input += event.unicode

        window.fill((80, 80, 80))
        prompt_text = font.render(message + input, True, (0, 0, 0))
        window.blit(prompt_text, (50, 50)) # Display prompt text at (50, 50)
        pygame.display.update()
        
    return input