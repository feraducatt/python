import pygame
import sys

class Box:
    def __init__(self, x, y, w, h, stroke = 0, color = (255,255,255), dim_num = 20):
        self.x, self.y, self.w, self.h, self.dim_num = x, y, w, h, dim_num
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.reg_color = (0,0,0)
        self.change_color = (250,000,000)
        self.white = (255,255,255)
        self.active = False
        self.width = stroke
        self.selected = True
        self.col = (x-x_start-1)/dim_num
        self.row = (y-y_start-1)/dim_num

    def handle_event(self, scr, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            if self.active:
                if self.color == self.white:
                    self.color = self.change_color
                    #self.width = 0
                    self.selected = True

                elif self.color == self.change_color:
                    self.color = self.white
                    self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
                    self.selected = False
                    #self.draw(scr)
                    #self.color = self.reg_color
                    #self.width = 1
                    #self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
                    #self.draw(scr)

                    #draw(scr)
                    #self.color = self.white
                    #self.width = 1
                    #self.color = self.reg_color


    def draw(self, screen):
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, self.width)

    #def update(self):
        # Resize the box if the text is too long.
     #   width = max(200, self.txt_surface.get_width()+10)
      #  self.rect.w = width


boxes = []
pygame.init()
scr = pygame.display.set_mode((500, 500))
scr.fill((255,255,255))
x_start = 0
y_start = 0
dim = 20
width = 1
for row in range(0, 250):

    pygame.draw.line(scr, (0, 0, 0), (x_start, (y_start + row * dim)), (x_start + 50 * dim, y_start + row * dim), width)

    for col in range(0, 250):
        boxes.append(Box(x_start+col*dim+1,y_start+row*dim+1,dim-1,dim-1, dim_num=dim))
        pygame.draw.line(scr, (0, 0, 0), (x_start + col * dim, y_start), (x_start + col * dim, y_start + 50 * dim), width)


while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for box in boxes:
            box.handle_event(scr, event)


    #for box in blankSpaces:
     #   box.update

    for box in boxes:
        box.draw(scr)

    pygame.display.update()
    num_selected = []
    for box in boxes:
        if box.selected:
            num_selected.append(box)
    if len(num_selected) == 2:
        num_selected[0]








#create box things with borders?
#set them up in grid
#let me click on grid and change the color of the box, saving it
#setting up origin as somewhere
#carry out algorythm:
    #for every box (x,y), check whether (x+1, y)(x-1, y), (x, y+1), (x, y-1)