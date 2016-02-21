import pygame

# Global settings
class Settings:
  width=600
  height=600
  startOffset=50
  fps=120
class Graphics:
  Blue=(0, 128, 255)
  Orange=(255, 100, 0)
  Yellow=(255,255,0)
  Black=(0,0,0)
class Game:
  over=False


# Classes and functions
class Player:
  def __init__(self, name, colour, x, y):
    self.name = name
    self.colour = colour
    self.x = x
    self.y = y
    self.isAlive = True 

def init():
  pygame.init()
  Graphics.font = pygame.font.SysFont("monospace", 15)
  Graphics.screen = pygame.display.set_mode((Settings.width, Settings.height))
  Graphics.clock = pygame.time.Clock()
  resetPlayers()

def resetPlayers():
  Game.p1 = Player("Player 1", Graphics.Blue, Settings.startOffset, Settings.startOffset)
  Game.p2 = Player("Player 2", Graphics.Orange, Settings.width-Settings.startOffset, Settings.height-Settings.startOffset)

def runGame():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      Game.over = True

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP]:
    Game.p1.y -= 1
  if pressed[pygame.K_DOWN]:
    Game.p1.y += 1
  if pressed[pygame.K_LEFT]:
    Game.p1.x -= 1
  if pressed[pygame.K_RIGHT]:
    Game.p1.x += 1

  if pressed[pygame.K_s]:
    Game.p2.y -= 1
  if pressed[pygame.K_x]:
    Game.p2.y += 1
  if pressed[pygame.K_z]:
    Game.p2.x -= 1
  if pressed[pygame.K_c]:
    Game.p2.x += 1

  if isDead(Game.p1):      
      kill(Game.p1)

  if isDead(Game.p2):
      kill(Game.p2)

  Graphics.screen.set_at((Game.p1.x, Game.p1.y), Game.p1.colour)
  Graphics.screen.set_at((Game.p2.x, Game.p2.y), Game.p2.colour)
  pygame.display.update()
  Graphics.clock.tick(Settings.fps)

def isDead(player):
  if player.x > Settings.width:
    return True
  if player.x < 0:
    return True
  if player.y > Settings.height:
    return True
  if player.y < 0:
    return True
  return False

def kill(player):
  player.isAlive = False
  endGame();

def endGame():
  winnerText = " Wins!"
  if(Game.p1.isAlive):
      winnerText = Game.p1.name + winnerText
  elif(Game.p2.isAlive):
      winnerText = Game.p2.name + winnerText  
  gameOverLabel = Graphics.font.render(winnerText, 1, Graphics.Yellow)
  Graphics.screen.blit(gameOverLabel, (Settings.width/2 - 30, Settings.height/2))
  pygame.display.update()
  promptPlayAgain()

def promptPlayAgain():
  isChoosingPlayAgain = True;
  while isChoosingPlayAgain:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        Game.over = True
        isChoosingPlayAgain = False;
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        Graphics.screen.fill(Graphics.Black)
        pygame.display.update()
        Graphics.clock.tick(60)
        resetPlayers()
        isChoosingPlayAgain = False;

# Main game loop
init()
while not Game.over:
  runGame()
