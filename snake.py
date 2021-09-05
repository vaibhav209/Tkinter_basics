import pygame                                                                                                            # Import a pygame module
import random                                                                                                            # Import random module for random number generation
import os


pygame.mixer.init()                                                                                                      # Mixer module helps control the music used in pygame programs

pygame.mixer.music.load("start.mp3")
pygame.mixer.music.play()

pygame.init()                                                                                                            # Initialize imported pygame modules

screen_width = 700                                                                                                       # Defined a screen width
screen_height = 500                                                                                                      # Defined a screen height


screen = pygame.display.set_mode((screen_width, screen_height))                                                          # Create Window Screen for game


pygame.display.set_caption("The_Simple_Snake_Game")                                                                      # Game Title
pygame.display.update()                                                                                                  # This function is mandatory to use because it's update the window screen 



clock = pygame.time.Clock()                                                                                              # Define Clock
font = pygame.font.SysFont(None,30)



def text_screen(text,color,x,y):                                                                                         # Defined text Function "Your Score"    
    screen_score = font.render(text, True, color)
    screen.blit(screen_score, [x,y])


def plot_snake(screen, color, snk_list , snake_length, snake_width):                                                     # Defined function for updated snake length
    for x,y in snk_list: 
        pygame.draw.rect(screen,color,[x, y, snake_length, snake_width])


def welcome_page():                                                                                                      # Defined a welcome function for user's welcome
    exit_game = False
    while not exit_game:
        screen.fill((22, 23, 22))
        text_screen("Welcome To Python Based Snake Game!", (255, 36, 36), 150, 200)
        text_screen("Press Enter to Play", (89, 255, 225), 250, 250)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("back.mp3")
                        pygame.mixer.music.play(-1,0.0)                                                                  # Play when Game loop start
                        gameloop()                                                                                       # Here code will jump to next function that is "gameloop()"
        
        
        pygame.display.update()
        clock.tick(60)



def gameloop():                                                                                                         # Defined a Game Loop function

    
                                                                        
    exit_game = False                                                                                                   # Specified a Variable here that used in function
    game_over = False
    snake_x = 60
    snake_y = 45
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20,screen_width / 2)                                                                       # Defined a area of randomly generated place of food  
    food_y = random.randint(20,screen_height / 2)
    snake_length = 20
    snake_width = 20
    food_length = 16
    food_width = 16
    score = 0
    fps = 60                                                                                                           # It is use to refresh the frame of window per seconds

    
    snk_list = []                                                                                                      # When snake eat food as soon as snake length will increase
    snk_length = 1

    while not exit_game:
        if game_over:
            screen.fill((22, 23, 22))                                                                                 # Here we used a rgb color code values for colour settings
            text_screen("Game Over ! Press Space Bar To Continue...", (180, 143, 255), 150, 200)
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:                                                                      # Determines if a key has been released (not pressed)
                    if event.key == pygame.K_SPACE:
                        welcome_page()


        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = + 2
                        velocity_y = 0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = - 2
                        velocity_y = 0


                    if event.key == pygame.K_UP:
                        velocity_y = + 2
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = - 2
                        velocity_x = 0
                

                    

            snake_x += velocity_x
            snake_y -= velocity_y

            if abs(snake_x - food_x) < 6  and abs(snake_y - food_y) < 6:                                            # Define on how many distance as snake eat a food
                score = score + 1

                food_x = random.randint(20,screen_width/2)
                food_y = random.randint(20,screen_height/2)
                snk_length += 2


            screen.fill((22, 23, 22))
            text_screen("Your Score: "+ str(score * 5),(255, 255, 0), 15,15)
            pygame.draw.rect(screen,(255, 0, 0),[food_x, food_y, food_length, food_width])
            
            
            head = []                                                                                              # Stored a empty list in head only for initialised a game 
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:                                                                         # When snake eat a food snake length will increases But we have to decrease their first index
                del snk_list[0]
            
            if head in snk_list[:-1]:                                                                              # create condition that is snake hits itself
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()                                                                        
            

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:                    # Create condition that is snake hits the wall
                game_over = True
                pygame.mixer.music.load("gameover.mp3") 
                pygame.mixer.music.play()                                                                          # Music play on Game Over condition


            
            plot_snake(screen,(0, 255, 0), snk_list, snake_length, snake_width)
        pygame.display.update()
        clock.tick(fps)

    
    

    pygame.quit()
    quit()
welcome_page()



