import pygame
import time

pygame.init()
time.sleep(1)
sc = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Downloading...")
sc.fill((255,255,255))
f = pygame.font.Font(None, 35)
text = f.render("Загрузка, не закрывайте окно...", True, (0, 0, 0))
sc.blit(text, (50, 75))
pygame.display.update()
time.sleep(1800)
pygame.mixer.music.load("krik.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
    time.sleep(5)
    pygame.quit()
    