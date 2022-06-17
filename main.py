import pygame as game
import time

game.init()
window_width = 800
window_height = 600
window = game.display.set_mode((window_width, window_height))
game.display.update()
game.display.set_caption('Snake')

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)

x1 = 300
y1 = 300
x1_change = 0
y1_change = 0
clock = game.time.Clock()

game_over = False
font_style = game.font.SysFont(None, 50, bold=True, italic=True)
def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    window.blit(mesg, [window_width/2, window_height/2])

while not game_over:
    for event in game.event.get():
        if event.type==game.QUIT:
            game_over = True
        if event.type == game.KEYDOWN:
            if event.key == game.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == game.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == game.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == game.K_DOWN:
                x1_change = 0
                y1_change = 10
    if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
        game_over = True
        
    x1 += x1_change
    y1 += y1_change
    window.fill(white)
    game.draw.rect(window, black, [x1, y1, 10, 10])
    game.display.update()
    clock.tick(30)
message('You lost', red)
game.display.update()
time.sleep(3)
game.quit()
quit()
