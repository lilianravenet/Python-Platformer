import pygame

width, height = 800, 600
win = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    win.fill((255, 255, 255))

    pygame.draw.rect(win, (0, 255, 0), pygame.Rect(30, 30, 150, 20), border_radius=10)

    pygame.display.update()

"""if 200:
    rgb = (0, 255, 0)
elif 0:
    rgb = (255, 0, 0)"""