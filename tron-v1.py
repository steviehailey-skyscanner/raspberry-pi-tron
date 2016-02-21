import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
done = False
is_blue = True
color = (0, 128, 255)
x = 30
y = 30
size = 60

while not done:
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      is_blue = not is_blue

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP]:
    y -= 1
  if pressed[pygame.K_DOWN]:
    y += 1
  if pressed[pygame.K_LEFT]:
    x -= 1
  if pressed[pygame.K_RIGHT]:
    x += 1

  if is_blue:
    color = (0, 128, 255)
  else: 
    color = (255, 100, 0)

  screen.fill((0,0,0))
  pygame.draw.rect(screen, color, pygame.Rect(x, y, size, size))
  pygame.display.flip()
  clock.tick(60)