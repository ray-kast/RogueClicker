from engine.entity import *
from engine.game import *
from engine.menu import *
from engine.player import *
from engine.world import *
from engine import levelloader

class TestGame(Game):
  def __init__(self):
    Game.__init__(self)

  def doBlocks(self, blocks, size):
    blocks = set(blocks)

    surf = pg.transform.scale(pg.image.load("assets\\sprites\\blocks\\metalBlock32x32.png"), (size, size))
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

    self.font = pg.font.Font("assets\\fonts\\FreePixel.ttf", 32)

    self.menu = Menu(self.win)

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
                lambda btn: None,
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

    self.world = World(self.win)

    surf = pg.Surface(self.scrRect.size)

    img = pg.image.load("assets\\sprites\\blocks\\metalSheet32x32.png")
    size = np.multiply(img.get_rect().size, 2)

    img = pg.transform.scale(img, size)

    for row in range(0, self.scrRect.height, size[1]):
      for col in range(0, self.scrRect.width, size[0]):
        surf.blit(img, (col, row))

    self.bkgd = Entity(self.world, (0, 0), (0, 0), surf, 1)

    self.world.bkgdSprites.add(self.bkgd, layer = 0)

    self.pic = pg.image.load("assets\\levels\\002\\003.png")

    level1 = levelloader.level(self.pic, self.world)
    self.blocks = level1.getblocks

    self.player = Player(self.world, self.world.dynSprites)

    self.currDrawing = self.menu

  def play(self, btn):
    self.win.fill(Colors.Green)

    self.currDrawing = self.world