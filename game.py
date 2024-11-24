import os
import pygame
import time
class Settings:
    Window = pygame.rect.Rect(0,0,450,450)
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH, "images")
    Timer = 0 
    FPS = 60
    global_speed = 1 # Global_speed value is a multiplyer that handels every speed variuble so you can make the game twice as fast

class Car(pygame.sprite.Sprite):
    def __init__(self,x,y,car_speed=1):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH,"TEMP_car.png"))
        self.image = pygame.transform.scale(self.image,(40,30))
        
        
        self.speed = Settings.global_speed*(2+car_speed)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def update(self):
        if self.speed>0:
            if self.rect.left >= Settings.Window.width:
                self.rect.right = 0
            else:
                self.rect = self.rect.move(self.speed,0)
        elif self.speed<0:
            if self.rect.right<= 0:
                self.rect.left = Settings.Window.width
            else:
                self.rect = self.rect.move(self.speed,0)


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "TEMP_player.png"))
        self.image = pygame.transform.scale(self.image,(20,20))
        
        self.speed = Settings.global_speed*5  
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.state = 0
        self.moving = False
        self.moving_down = False
        self.moving_up = False
        self.moving_right = False
        self.moving_left = False
        self.moving_distance = 0
    
    def spawn(self):
        self.rect.center =(225,425)
        self.nullefie()
        
    def nullefie(self):
        self.rect = self.rect.move(0,0)
        self.moving = False
        self.moving_down = False
        self.moving_up = False
        self.moving_right = False
        self.moving_left = False
        self.moving_distance = 0

    def update(self):
                    #Right
        if pygame.key.get_pressed()[pygame.K_RIGHT]and self.moving == False and Settings.Window.right !=self.rect.right: 
            self.moving = True 
            self.moving_right = True
        if self.moving_right == True and self.moving == True:
            self.rect = self.rect.move(self.speed,0)
            self.moving_distance +=self.speed
                    #Left
        if pygame.key.get_pressed()[pygame.K_LEFT]and self.moving == False and Settings.Window.left != self.rect.left: 
            self.moving = True 
            self.moving_left = True
        if self.moving_left == True and self.moving == True:
            self.rect = self.rect.move(-self.speed,0)
            self.moving_distance +=self.speed
                    #Up
        if pygame.key.get_pressed()[pygame.K_UP]and self.moving == False and Settings.Window.top != self.rect.top: 
            self.moving = True 
            self.moving_up = True
        if self.moving_up == True and self.moving == True:
            self.rect = self.rect.move(0,-self.speed)
            self.moving_distance +=self.speed
                    #Down
        if pygame.key.get_pressed()[pygame.K_DOWN]and self.moving == False and Settings.Window.bottom != self.rect.bottom:
            self.moving = True 
            self.moving_down = True
        if self.moving_down == True and self.moving == True:
            self.rect = self.rect.move(0,self.speed)
            self.moving_distance +=self.speed

        if self.moving_distance == 50:
            self.nullefie()

            if self.rect.top <=0:
                self.state +=1
                if self.state ==1:
                    self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "TEMP_player.png"))
                    self.image = pygame.transform.scale(self.image,(30,30))
                    self.spawn()
                elif self.state ==2:
                    self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "TEMP_player.png"))
                    self.image = pygame.transform.scale(self.image,(40,40))
                    self.spawn()
                    
                elif self.state ==3:
                    self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "TEMP_player.png"))
                    self.image = pygame.transform.scale(self.image,(50,50))
                    self.spawn()
            #elif self.state==4:
            #    Winn
            
    


                        


                

player = Player(225,425)

car1 = Car(5,360)
car2 = Car(205,360)
car3 = Car(405,360)
car4 = Car(5,260,2)
car5 = Car(205,260,2)
car6 = Car(405,260,2)
car7 = Car(5,160,-3)
car8 = Car(155,160,-3)
car9 = Car(305,160,-3)
car10 = Car(405,160,-3)
cars = pygame.sprite.Group()
cars.add(car1,car2,car3,car4,car5,car6,car7,car8,car9,car10)

def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
    pygame.init()

    screen = pygame.display.set_mode(Settings.Window.size) 
    pygame.display.set_caption("Froger Clone")
    clock = pygame.time.Clock()


    background_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH,"TEMP_Background.png"))
    background_image = pygame.transform.scale(background_image,Settings.Window.size)

    # game schleife
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        player.update() # Player direction up 

        for car in cars:
            car.update()
        if pygame.sprite.spritecollideany(player,cars):
            player.spawn()
            

        screen.blit(background_image,(0,0))
        screen.blit(player.image,player.rect.topleft)
        
        for car in cars:
            screen.blit(car.image,car.rect)
        
        #print(player.rect.topleft)

        #Flip of the blits
        pygame.display.flip()
        #FPS
        Settings.Timer +=1
        if Settings.Timer == 30:
            Settings.Timer = 0
        clock.tick(Settings.FPS)
    
    pygame.quit()






if __name__ =="__main__":
    main()