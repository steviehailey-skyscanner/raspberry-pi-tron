import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
done = False
fps = 120
color1 = (0, 128, 255)
color2 = (255, 100, 0)
x1 = 30
y1 = 30
x2 = 100
y2 = 100
size = 2
moveBy = 1

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP]:
    y1 -= moveBy
  if pressed[pygame.K_DOWN]:
    y1 += moveBy
  if pressed[pygame.K_LEFT]:
    x1 -= moveBy
  if pressed[pygame.K_RIGHT]:
    x1 += moveBy

  if pressed[pygame.K_s]:
    y2 -= moveBy
  if pressed[pygame.K_x]:
    y2 += moveBy
  if pressed[pygame.K_z]:
    x2 -= moveBy
  if pressed[pygame.K_c]:
    x2 += moveBy

  #screen.fill((0,0,0))
  #pygame.draw.rect(screen, color1, pygame.Rect(x1, y1, size, size))
  #pygame.draw.rect(screen, color2, pygame.Rect(x2, y2, size, size))
  #pygame.display.flip()
  screen.set_at((x1, y1), color1)
  screen.set_at((x2, y2), color2)
  pygame.display.update()
  clock.tick(fps)