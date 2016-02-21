import pygame

done = False
width = 600
height = 600
fps = 120
color1 = (0, 128, 255)
color2 = (255, 100, 0)
x1 = 30
y1 = 30
x2 = 100
y2 = 100
moveBy = 1
gameOver = False


pygame.init()
myfont = pygame.font.SysFont("monospace", 15)
p1WinsLabel = myfont.render("Player 1 Wins!", 1, (255,255,0))
p2WinsLabel = myfont.render("Player 2 Wins!", 1, (255,255,0))
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

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

  if x1 > width or x1 < 0 or y1 > height or y1 < 0:
      done = True
      screen.blit(p2WinsLabel, (width/2, height/2))

  if x2 > width or x2 < 0 or y2 > height or 21 < 0:
      done = True
      screen.blit(p1WinsLabel, (width/2, height/2))

  screen.set_at((x1, y1), color1)
  screen.set_at((x2, y2), color2)
  pygame.display.update()
  clock.tick(fps)

clock.tick(100)