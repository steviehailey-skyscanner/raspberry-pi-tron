import random
import pygame

# Classes and functions
class Player:
  def __init__(self, name, colour, leftKey, rightKey):
    self.name = name
    self.colour = colour
    self.isAlive = True
    self.leftKey = leftKey
    self.rightKey = rightKey
  def setStartPosition(self, startPos):
    self.x = startPos.x
    self.y = startPos.y
    self.direction = startPos.direction
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

class StartingPosition:
  def __init__(self, x, y, direction):
    self.x = x
    self.y = y
    self.direction = direction

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
  Game.players = [];
  Game.players.append(Player("Player 1", Graphics.Blue, pygame.K_LEFT, pygame.K_DOWN));
  Game.players.append(Player("Player 2", Graphics.Orange, pygame.K_z, pygame.K_x));
  Game.players.append(Player("Player 3", Graphics.Green, pygame.K_n, pygame.K_m));
  Game.players.append(Player("Player 4", Graphics.Purple, pygame.K_1, pygame.K_2));
  
  Game.keyMap = {}
  for player in Game.players:
    Game.keyMap[player.leftKey] = player.left
    Game.keyMap[player.rightKey] = player.right

  random.shuffle(Game.players)
  random.shuffle(StartingPositions.All)
  for index,player in enumerate(Game.players):
    player.setStartPosition(StartingPositions.All[index])

def runGame():
  livingPlayers = len(Game.players)
  while livingPlayers > 1:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        Game.over = True
      elif event.type == pygame.KEYDOWN:
        if Game.keyMap.has_key(event.key):
          Game.keyMap[event.key]()

    for player in Game.players:
      if player.isAlive:
        player.move()
        if isDead(player):      
          player.isAlive = False
          livingPlayers-=1
        else:
          Graphics.screen.set_at((player.x, player.y), player.colour)

    pygame.display.update()
    Graphics.clock.tick(Settings.fps)

  endGame()

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

def endGame():   
  winningPlayer = Game.players[0]
  for player in Game.players:
    if player.isAlive:
      winningPlayer = player
  winnerText = winningPlayer.name + " Wins!"
  gameOverLabel = Graphics.font.render(winnerText, 1, Graphics.Yellow)
  Graphics.screen.blit(gameOverLabel, (Settings.width/2 - 30, Settings.height/2))
  pygame.display.update()

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
  fps=90

class Graphics:
  Blue=(0, 128, 255)
  Orange=(255, 100, 0)
  Yellow=(255,255,0)
  Purple=(150,50,255)
  Green=(50,205,50)
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

class StartingPositions:
  TopLeft=StartingPosition(Settings.startOffset, Settings.startOffset, Directions.Right)
  TopMiddle=StartingPosition(Settings.width/2, Settings.startOffset, Directions.Down)
  TopRight=StartingPosition(Settings.width-Settings.startOffset, Settings.startOffset, Directions.Left)
  MiddleLeft=StartingPosition(Settings.startOffset, Settings.height/2, Directions.Right)
  MiddleRight=StartingPosition(Settings.width-Settings.startOffset, Settings.height/2, Directions.Left)
  BottomLeft=StartingPosition(Settings.startOffset, Settings.height-Settings.startOffset, Directions.Right)
  BottomMiddle=StartingPosition(Settings.width/2, Settings.height-Settings.startOffset, Directions.Up)
  BottomRight=StartingPosition(Settings.width/2, Settings.height-Settings.startOffset, Directions.Left)
  Centre=StartingPosition(Settings.width/2, Settings.height/2, Directions.Right)
  All=[TopLeft,TopMiddle,TopRight,MiddleLeft,Centre,MiddleRight,BottomLeft,BottomMiddle,BottomRight]

# Start the game
init()
while not Game.over:
  runGame()
  promptPlayAgain()