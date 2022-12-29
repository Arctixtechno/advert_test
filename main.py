import pygame
from pygame.locals import *
import math
import time

WIDTH, HEIGHT = 1000, 950
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('proof of concept')


imag1 = pygame.image.load('advert11.jpg').convert_alpha()
imag2 = pygame.image.load('advert21.jpg').convert_alpha()
imag3 = pygame.image.load('advert31.jpg').convert_alpha()

image_list = [imag1, imag2, imag3]
time_delay = 1

def draw_window():
    for image in image_list:
        WIN.blit(image, (0,0))
        time.sleep(time_delay)
        pygame.display.update()
        WIN.fill('white')

FPS = 60

clock = pygame.time.Clock()

def main():
    game_running = True
    while game_running:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False
        draw_window()

if __name__ == '__main__':
    main()
