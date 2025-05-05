import pygame
import os
from grid import Grid


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400,100)

surface = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Sudoku')

pygame.font.init()
game_font = pygame.font.SysFont('Comic Sans MS', 50)
game_font2=pygame.font.SysFont('Comic Sans MS', 25)

grid=Grid(pygame, game_font)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.win:
            if pygame.mouse.get_pressed()[0]:#check only for left mouse button
                pos= pygame.mouse.get_pos()
                grid.get_mouse_click(pos[0],pos[1])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.win:
                grid.restart()


    surface.fill((0,0,0))

    #draw te grid here
    grid.draw_all(pygame,surface)

    if grid.win:
        won_surface = game_font.render("You Won!", False, (0, 255, 0))
        surface.blit(won_surface, (950, 650))

        press_space_surf = game_font2.render("Press Space to restart!", False, (0, 255, 200))
        surface.blit(press_space_surf, (920, 750))
    pygame.display.flip()
