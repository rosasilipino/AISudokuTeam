#Group: Sudoku Team
#Class: CS 450-01
#Project: Final Project
#Date: 04/21/2024
import pygame 
import sys

# GUI for the user to input the number of runs
def getNumOfRuns(window, message):
    pygame.display.set_caption("CS 450 SUDOKU TEAM")  # Set window title
    font = pygame.font.Font('freesansbold.ttf', 25)  # Font for text
    input = ''  # Initialize input to empty string
    input_active = True  # Flag for input box
    cursor_visibility = True  # Cursor visibility toggle
    last_cursor_toggle_time = pygame.time.get_ticks()
    cursor_blink_interval = 500  # Cursor blink time in milliseconds

    # Calculate positions based on the message size
    message_surface = font.render(message, True, (255, 255, 255))
    message_rect = message_surface.get_rect(center=(window.get_width() // 2, 100))

    # Create input box rect centered below the message
    input_box_width = 70  # Wider input box for better centering
    input_box_height = 50  # Define the height of the input box
    input_box_x = (window.get_width() - input_box_width) // 2  # Center horizontally
    input_box_y = message_rect.bottom + 20  # Position below the message
    input_box_rect = pygame.Rect(input_box_x, input_box_y, input_box_width, input_box_height)

    # While input is active event handing.
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("EXITING PROGRAM, X WAS PRESSED.")
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("EXITING PROGRAM ESC WAS PRESSED.")
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN and input.strip():
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input = input[:-1]
                elif event.unicode.isdigit():
                    input += event.unicode

        window.fill((80, 80, 80))  # Background color

        # Render message
        window.blit(message_surface, message_rect.topleft)

        # Toggle cursor visibility for blinking effect
        current_time = pygame.time.get_ticks()
        if current_time - last_cursor_toggle_time > cursor_blink_interval:
            cursor_visibility = not cursor_visibility
            last_cursor_toggle_time = current_time

        # Draw input box
        pygame.draw.rect(window, (200, 200, 200), input_box_rect)  # Draw background for input
        pygame.draw.rect(window, (255, 255, 255), input_box_rect, 2)  # Draw border

        # Calculate the x position to center the text
        input_text_surface = font.render(input, True, (0, 0, 0))
        input_text_width = input_text_surface.get_width()
        text_x = input_box_x + (input_box_width - input_text_width) // 2
        
        # Render input text
        window.blit(input_text_surface, (text_x, input_box_y + 10))  # Vertically centering the text in the box
        
        # Render cursor if visible
        if cursor_visibility:
            cursor_surface = font.render('|', True, (0, 0, 0))
            cursor_x = text_x + input_text_width  # Position cursor right after the text
            window.blit(cursor_surface, (cursor_x, input_box_y + 10))
        pygame.display.update()

    return input
