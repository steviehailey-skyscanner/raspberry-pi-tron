import pygame

# Classes and functions
class Player:
  def __init__(self, name, colour, x, y, direction):
    self.name = name
    self.colour = colour
    self.x = x
    self.y = y
    self.direction = direction
    self.isAlive = True
    self.updateDirection()
  def updateDirection(self):
    self.directionModifier = Directions.All[self.direction]
  def move(self):    
    self.x += self.directionModifier.modifyX
    self.y += self.directionModifier.modifyY
  def left(self):
    self.direction -= 1
    if self.direction < 0:
      self.direction = 3
    self.updateDirection()
  def right(self):
    self.direction += 1
    if self.direction > 3:
      self.direction = 0
    self.updateDirection()

class DirectionModifier:
  def __init__(self, modifyX, modifyY):
    self.modifyX = modifyX
    self.modifyY = modifyY

def init():
  pygame.init()  
  Graphics.font = pygame.font.SysFont("monospace", 15)
  Graphics.screen = pygame.display.set_mode((Settings.width, Settings.height))
  Graphics.clock = pygame.time.Clock()
  resetPlayers()

def resetPlayers():
  Game.p1 = Player("Player 1",
    Graphics.Blue,
    Settings.startOffset, Settings.startOffset,
    Directions.Right)
  Game.p2 = Player("Player 2",
    Graphics.Orange,
    Settings.width-Settings.startOffset,
    Settings.height-Settings.startOffset,
    Directions.Left)

def runGame():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      Game.over = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        Game.p1.left()
      elif event.key == pygame.K_DOWN:
        Game.p1.right()
      if event.key == pygame.K_z:
        Game.p2.left()
      elif event.key == pygame.K_x:
        Game.p2.right()

  Game.p1.move()
  Game.p2.move()

  if isDead(Game.p1):      
      kill(Game.p1)

  if isDead(Game.p2):
      kill(Game.p2)

  Graphics.screen.set_at((Game.p1.x, Game.p1.y), Game.p1.colour)
  Graphics.screen.set_at((Game.p2.x, Game.p2.y), Game.p2.colour)
  pygame.display.update()
  Graphics.clock.tick(Settings.fps)

def isDead(player):
  if player.x >= Settings.width:
    return True
  if player.x < 0:
    return True
  if player.y >= Settings.height:
    return True
  if player.y < 0:
    return True
  if Graphics.screen.get_at((player.x, player.y)) != Graphics.Black:
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

class Directions:
  Right=0
  Down=1
  Left=2
  Up=3
  RightModifier=DirectionModifier(1,0)
  DownModifier=DirectionModifier(0,1)
  LeftModifier=DirectionModifier(-1,0)
  UpModifier=DirectionModifier(0,-1)
  All=[RightModifier,DownModifier,LeftModifier,UpModifier]

# Start the game
init()
while not Game.over:
  runGame()
