import pygame
import threading
from time import sleep

import board
import pathfind

pygame.init()

window = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Pathfinding")

threading.Thread(target=pathfind.findpath).start()

blkdia = 640 // board.size()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()

    pygame.draw.rect(window, (0,0,0), (0, 0, 640, 640))

    for y, row in enumerate(board.get()):
        for x, tile in enumerate(row):
            if tile == "#":
                pygame.draw.rect(window, (20,20,20), (x * blkdia, y * blkdia, blkdia, blkdia))
            elif tile == "-":
                if x == pathfind.goalState.x and y == pathfind.goalState.y:
                    pygame.draw.rect(window, (0,255,0), (x * blkdia, y * blkdia, blkdia, blkdia))
                elif pathfind.isGoalRoute(pathfind.State(x, y)):
                    pygame.draw.rect(window, (89, 255, 89), (x * blkdia, y * blkdia, blkdia, blkdia))
                elif pathfind.isExplored(pathfind.State(x, y)):
                    pygame.draw.rect(window, (255,245,64), (x * blkdia, y * blkdia, blkdia, blkdia))
                else:
                    pygame.draw.rect(window, (235,235,235), (x * blkdia, y * blkdia, blkdia, blkdia))

    pygame.display.update()
    sleep(0.01)