from engine.entity import *
from engine.game import *
from engine.menu import *
from engine.player import *
from engine.world import *
from engine import levelloader

class RogueClickerGame(Game):
  def __init__(self):
    Game.__init__(self)
    pg.mixer.init()
    pg.mixer.music.load("assets/music/Fly.ogg")
    pg.mixer.music.play(loops = -1)

  def doBlocks(self, blocks, size):
    blocks = set(blocks)

    surf = pg.transform.scale(pg.image.load("assets/sprites/blocks/metalBlock32x32.png"), (size, size))
    shSurf = pg.Surface((size, size), pg.SRCALPHA)

    shSurf.fill((0, 0, 0, int(255 * .15)))
    
    ents = []
    shEnts = []
    
    for block in blocks:
      pos = np.multiply(block, size)
      ents.append(StaticEntity(self.world, pos, (0, 0), surf, 1, self.world.envSprites))
      shEnts.append(Entity(self.world, np.add(pos, (8, 8)), (0, 0), shSurf, 1))

    self.world.bkgdSprites.add(*shEnts, layer = 1)

  def init(self):
    Game.init(self)

    self.font = pg.font.Font("assets/fonts/FreePixel.ttf", 32)

    self.menu = Menu(self.win)
    self.n = 0

    norm = ((99, 98, 87), Colors.Black)
    hover = ((125, 122, 106), Colors.White)
    act = ((209, 55, 2), Colors.White)

    rect = pg.Rect(0, 8, 320, 48)

    xc = 1
    yc = 3

    x = self.scrRect.centerx - (rect.right * xc - rect.left) / 2
    y = self.scrRect.centery - (rect.bottom * yc - rect.top) / 2

    Menu.Button(self.menu,
                self.play,
                norm,
                hover,
                act,
                self.font,
                "Play",
                (x, y),
                rect.size)

    Menu.Button(self.menu,
                self.options,
                norm,
                hover,
                act,
                self.font,
                "Options",
                (x, y + rect.bottom),
                rect.size)

    Menu.Button(self.menu,
                lambda btn: self.postQuit(),
                norm,
                hover,
                act,
                self.font,
                "Quit",
                (x, y + rect.bottom * 2),
                rect.size)

    self.world = World(self.win, self.font)

    surf = pg.Surface(self.scrRect.size)

    #self.pic = pg.image.load("assets/levels/004/003.png")

    #level1 = levelloader.level(self.pic, self.world)
    #self.blocks = level1.getblocks

    self.player = Player(self.world, self.world.dynSprites)

    self.currDrawing = self.menu

  def play(self, btn):
    pg.mouse.set_visible(False)

    self.win.fill(Colors.Green)

    self.player.deathCount = 0

    self.world.lastDeathCount = 0

    self.world.begin(self)

    self.currDrawing = self.world

  def finish(self):
    self.win.fill(Colors.Green)

    self.currDrawing = self.menu

    pg.mouse.set_visible(True)

  def options(self, btn):
    if self.n == 0:
      self.win = pg.display.set_mode((1600, 900), pg.HWSURFACE | pg.DOUBLEBUF)
      self.n = 1
    elif self.n == 1: 
      self.win = pg.display.set_mode(self.scrRect.size, pg.HWSURFACE | pg.DOUBLEBUF | pg.FULLSCREEN)
      self.n = 0
