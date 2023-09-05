import pygame
import time

pygame.init()
time.sleep(10)
pygame.display.set_mode((200, 200))
pygame.mixer.music.load("krik.mp3")
pygame.mixer.music.play()

while True:
    pygame.mixer.music.get_busy()
    pygame.time.Clock().tick(10)
    time.sleep(5)
    pygame.quit()


