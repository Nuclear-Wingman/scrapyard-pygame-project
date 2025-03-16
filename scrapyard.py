import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("scrapyard Game")
background = pygame.image.load("background.jpg")

# Animation variables
current_frame = 0
#player_images = [pygame.image.load(f"Larry{i}.png") for i in range(1, 2)]
larrydim = (30,20)
animation_speed = 0.1  # Adjust this value to change the animation speed
frame_timer = 0
# Load the player image + resting annimation
player = [pygame.image.load(f"Larry{i}.png") for i in range(1, 2)]
frame_count = len(player)
player_rect = player[0].get_rect()
player_rect.topleft = (400, 300)  # Initial position of the player

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            #basic key controls
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            #arrow key controls
            elif event.key == pygame.K_LEFT:
                print("Left arrow key pressed" + moveleft())
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed" + moveright())
            elif event.key == pygame.K_UP:
                print("Up arrow key pressed" + moveup())
            elif event.key == pygame.K_DOWN:
                print("Down arrow key pressed" + movedown())
            #wasd key controls
            elif event.key == pygame.K_w:
                print("W key pressed" + moveup())
            elif event.key == pygame.K_a:
                print("A key pressed" + moveleft())
            elif event.key == pygame.K_s:
                print("S key pressed" + movedown())
            elif event.key == pygame.K_d:
                print("D key pressed" + moveright())
    
    
    
    
    # Background stuff
    bg_x = 0
    bg_y = 0
    bg_speed = 1
    def moveup():
        bg_y += bg_speed
    def movedown():
        bg_y -= bg_speed
    def moveleft():
        bg_x += bg_speed
    def moveright():
        bg_x -= bg_speed

    # Reset the background position when it moves out of the screen
    if bg_y >= 600:  
        bg_y = 0
    elif bg_x >= 800:
        bg_x = 0        
    
    

    
    
    # Fill the screen with a color (RGB)
    screen.fill((100, 100, 100))
    screen.blit(background, (bg_x, bg_y))
    # Update the display
    pygame.display.flip()
    
    
    
    
                
    #player stuff                       
    #resting animation
    frame_timer += animation_speed
    if frame_timer == 1:
        frame_timer = 0
        current_frame = (current_frame + 1) % frame_count
        

    screen.blit(player[current_frame], player_rect.topleft)
