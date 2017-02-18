import pygame
import math
import time
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
KEY_ENTER = 13
KEY_SPACE = 32
KEY_LeftCLICK = 1


KEY_Q = 113
KEY_W = 119
KEY_E = 101
KEY_A = 97
KEY_S = 115
KEY_D = 100

#initiate background
background_width = 1024
background_height = 960
background_line_thickness = 6
blue_color = (97, 159, 182)
screen = pygame.display.set_mode((background_width, background_height))
screen.fill(blue_color)
pygame.draw.lines(screen, (000,000,000), False, [(background_width/2,0),(background_width/2,background_height)],background_line_thickness)
pygame.draw.lines(screen, (000,000,000), False, [(0,background_height/2),(background_width, background_height/2)],background_line_thickness)


#initiate end condition
stop_game = False



class Square_jump_game(object):
    def __init__(self):

        #rectangle info
        self.x = background_width / 10
        self.y = background_height / 3
        self.rectangle_height = 60
        self.rectangle_width = 60
        self.rectangle_speed = 0

        #wall info
        self.wall_x = (background_width / 10) + ((background_width/2 - background_width/10) * .8)
        self.wall_y = (background_height / 3) - 30
        self.wall_speed = 6

        #ground
        self.ground_height = (background_height/2)-(self.y+self.rectangle_height+background_line_thickness/2)
        self.ground_width = background_width/2-(background_line_thickness/2)
        self.ground_x = 0
        self.ground_y = self.y + self.rectangle_height



        pygame.draw.rect(screen, (0,0,255), (self.x,self.y,self.rectangle_width,self.rectangle_height), 0)
        pygame.draw.rect(screen, (139,69,19),(self.ground_x,self.ground_y,self.ground_width, self.ground_height),0)
        pygame.draw.rect(screen, (255,0,0), (self.wall_x, self.wall_y, 60,90), 0)
        print "in the square"

    def jump(self):
        self.rectangle_speed = 10


    def render(self):
        pygame.draw.rect(screen, (0,0,255), (self.x,self.y,self.rectangle_width,self.rectangle_height), 0)
        pygame.draw.rect(screen, (139,69,19),(self.ground_x,self.ground_y,self.ground_width, self.ground_height),0)
        pygame.draw.rect(screen, (255,0,0), (self.wall_x, self.wall_y, 60,90), 0)

    def jumping(self):
        self.y -= self.rectangle_speed
        if self.rectangle_speed >0 and self.y < ((background_height/3) - 250):
            self.rectangle_speed = -10
        if self.rectangle_speed <0 and self.y >= (background_height / 3):
            self.rectangle_speed = 0

    def wall_movement(self):
        self.wall_x -= self.wall_speed

        if self.wall_x <= 0 - 60:
            self.wall_x = (background_width / 10) + ((background_width/2 - background_width/10) * .8)

    def collision(self):
            if self.x+30 > self.wall_x-30 and self.x-30 < self.wall_x+30 and self.y-30 > self.wall_y-40:
                print "Box Collision"

            if self.x+30 > self.wall_x-30 and self.x-30 < self.wall_x+30 and self.y+30 > self.wall_y-40:
                print "Box Collision"
            pass

class Defuse_bomb(object):
    def __init__(self):

        #edges
        #x - 512 > 800
        #y - 50 > 280
        #self.x = (background_width / 2)
        #self.y = (background_height / 2)

        #self.x = random.randint(512,800)
        #self.y = random.randint(50,280)
        self.x = random.randint(512,800)
        self.y = random.randint(50,280)
        self.curr_time = time.time()

        self.size = 150
        self.explosion = 5
        self.explosion_text = ""
        self.bomb_pic = pygame.image.load("Zeeky_H_Bomb.png").convert_alpha()
        self.bomb_pic = pygame.transform.scale(self.bomb_pic, (self.size,self.size))

        print self.x
        print self.y

    def render(self):
        if time.time() - self.curr_time > 1:
            self.explosion -= 1
            self.curr_time = time.time()
        self.explosion_text = str(self.explosion)
        font = pygame.font.Font(None, 100)
        text = font.render(self.explosion_text, True, (255, 0, 0))
        screen.blit(text, (self.x + 70, self.y - 40))

        screen.blit((self.bomb_pic),(self.x, self.y))
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.size,self.size), 1)



    def collision(self,x,y):
        if x < self.x+ self.size and x > self.x and y < self.y+self.size and y > self.y:
            print "collision on bomb"
            return True

    def reposition(self):
        self.x = random.randint(512,800)
        self.y = random.randint(50,280)
        self.size = 150

        self.explosion = 5

class Drive(object):
    def __init__(self):
        #1024 960
        self.size_x = 100
        self.size_y = 150
        self.x = 50
        self.y = 800
        self.curr_time = time.time()
        self.car_position = 2

        self.rabbit_x = 80
        self.rabbit_y = 483
        self.rabbit_position = random.randint(1,4)

        self.rabbit = pygame.image.load("rabbit.png").convert_alpha()
        self.rabbit = pygame.transform.scale(self.rabbit, (50,100))

        self.background = pygame.image.load("green-background.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, (512-3, 480-3))
        self.race_car = pygame.image.load("Pink_car.png").convert_alpha()
        self.race_car = pygame.transform.scale(self.race_car, (self.size_x,self.size_y))
    def render(self):
        screen.blit((self.background),(0, 483))
        screen.blit((self.race_car),(self.x, self.y))
        screen.blit((self.rabbit),(self.rabbit_x,self.rabbit_y))

    def turn_left(self):
        if self.car_position <= 1:
            self.car_position = 1
        else:
            self.car_position -= 1

    def turn_right(self):
        if self.car_position >= 4:
            self.car_position = 4
        else:
            self.car_position += 1

    def check_car_position(self):
        if self.car_position == 1:
            self.x = 50
        elif self.car_position == 2:
            self.x = 150
        elif self.car_position == 3:
            self.x = 250
        elif self.car_position == 4:
            self.x = 350

        if self.car_position == self.rabbit_position and self.y - 200  < self.rabbit_y - 100:
            print "Rabbit Hitted"
    def obstacle_move(self):
        if self.rabbit_position == 1:
            self.rabbit_x = 80
        if self.rabbit_position == 2:
            self.rabbit_x = 180
        if self.rabbit_position == 3:
            self.rabbit_x = 280
        if self.rabbit_position == 4:
            self.rabbit_x = 380

        if time.time() - self.curr_time >= 1:
            self.rabbit_y += 100
            self.curr_time = time.time()

    def new_rabbit(self):
        if self.rabbit_y > 900:
            self.rabbit_position = random.randint(1,4)
            self.rabbit_y = 483

#1024
#512
# class Mole(object, position):
#     def __init__(self):
#         self.mole_pic = pygame.image.load("mole.png").convert_alpha()
#         self.mole_background = pygame.transform.scale(self.mole_pic, (509, 477))
#         if position == 1:
#             print "hello 1"
#
#
#         elif position == 2:
#             print "hello 2"
#
#         else:
#             print "hello 3"
#         pass

class Whack_a_mole(object):
    def __init__(self):
        self.background_x = background_width/2+ 6
        self.background_y = 483

        self.mole1_x = 535
        self.mole1_y = 485

        self.mole2_x = 700
        self.mole2_y = 485

        self.mole3_x = 865
        self.mole3_y = 485

        self.mole4_x = 535
        self.mole4_y = 695

        self.mole5_x = 700
        self.mole5_y = 695

        self.mole6_x = 864
        self.mole6_y = 695

        self.mole_pic = pygame.image.load("mole.png").convert_alpha()
        self.mole_pic = pygame.transform.scale(self.mole_pic, (150, 150))
        self.mole_background = pygame.image.load("whack_a_mole.png").convert_alpha()
        self.mole_background = pygame.transform.scale(self.mole_background, (512-3, 480-3))

        # self.mole [[Display Condition, Reset Spawn Timer Condition, Stored Time, Spawn Time]]
        self.mole = [[True, True, time.time(),5],[True, True, time.time(),5],[True, True, time.time(),5],[True, True, time.time(),5],[True, True, time.time(),5],[True, True, time.time(),5]]





    def spawn_mole(self):

        for i in range(len(self.mole)):

            if self.mole[i][0] == False:
                if self.mole[i][1] == True:
                    self.mole[i][2] = time.time()
                    self.mole[i][1] = False
                else:
                    if time.time() - self.mole[i][2] > 3:
                        self.mole[i][0] = True
                        self.mole[i][3] = 5

    def check_mole(self, input):
            if self.mole[input][0] == True:
                self.mole[input][0] = False
                self.mole[input][1] = True

    def render(self):
        screen.blit((self.mole_background),(self.background_x, self.background_y))
        if self.mole[0][0] == True:
            screen.blit((self.mole_pic),(self.mole1_x, self.mole1_y))
        if self.mole[1][0] == True:
            screen.blit((self.mole_pic),(self.mole2_x, self.mole2_y))
        if self.mole[2][0] == True:
            screen.blit((self.mole_pic),(self.mole3_x, self.mole3_y))
        if self.mole[3][0] == True:
            screen.blit((self.mole_pic),(self.mole4_x, self.mole4_y))
        if self.mole[4][0] == True:
            screen.blit((self.mole_pic),(self.mole5_x, self.mole5_y))
        if self.mole[5][0] == True:
            screen.blit((self.mole_pic),(self.mole6_x, self.mole6_y))


def main():
    pygame.init()

    #initiate the games
    screen_1 = Square_jump_game()
    screen_2 = Defuse_bomb()
    screen_3 = Drive()
    screen_4 = Whack_a_mole()


    while not stop_game:
        screen_1.jumping()
        screen_1.wall_movement()
        screen_4.spawn_mole()
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.KEYDOWN:
                print event.key
                if event.key == KEY_SPACE:
                    if screen_1.y > (background_height / 3) - 50 :
                        screen_1.jump()
                if event.key == KEY_LEFT:
                    screen_3.turn_left()
                    print "to the left"
                if event.key == KEY_RIGHT:
                    screen_3.turn_right()

                if event.key == KEY_Q:
                    screen_4.check_mole(0)
                if event.key == KEY_W:
                    screen_4.check_mole(1)
                if event.key == KEY_E:
                    screen_4.check_mole(2)
                if event.key == KEY_A:
                    screen_4.check_mole(3)
                if event.key == KEY_S:
                    screen_4.check_mole(4)
                if event.key == KEY_D:
                    screen_4.check_mole(5)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    x, y = event.pos
                    if screen_2.collision(x,y):
                        screen_2.reposition()

                    print "Hello"
                if event.button == 3:
                    print "right click"
        screen.fill(blue_color)
        pygame.draw.lines(screen, (255,255,255), True, [(background_width/2,0),(background_width/2,background_height)],background_line_thickness)
        pygame.draw.lines(screen, (255,255,255), False, [(0,background_height/2),(background_width, background_height/2)],background_line_thickness)
        screen_1.render()
        screen_2.render()
        screen_3.render()
        screen_4.render()

        if screen_2.explosion <= 0:
            print "boom!"
            screen_2.reposition()
        pygame.display.update()
        screen_1.collision()
        screen_3.obstacle_move()
        screen_3.check_car_position()
        screen_3.new_rabbit()
    pygame.quit()

if __name__ == '__main__':
    main()
