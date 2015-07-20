from engine.entity import *
from engine.game import *
from engine.menu import *
from engine.player import *
from engine.world import *

class TestGame(Game):
  def __init__(self):
    Game.__init__(self)

  def doBlocks(self, blocks, size):
    surf = pg.transform.scale(pg.image.load("assets\\sprites\\blocks\\metalBlock32x32.png"), (size, size))
    shSurf = pg.Surface((size, size))

    shSurf.fill(Colors.Black)
    shSurf.set_alpha(int(255 * .15))
    
    ents = []
    shEnts = []
    
    for block in blocks:
      pos = np.multiply(block, size)
      ents.append(Entity(self.world, pos, (0, 0), surf, 1, self.world.envSprites))
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

    self.player = Player(self.world, (110, 110), (0, 0), self.world.dynSprites)

    surf = pg.Surface(self.scrRect.size)

    img = pg.image.load("assets\\sprites\\blocks\\metalSheet32x32.png")
    size = np.multiply(img.get_rect().size, 2)

    img = pg.transform.scale(img, size)

    for row in range(0, self.scrRect.height, size[1]):
      for col in range(0, self.scrRect.width, size[0]):
        surf.blit(img, (col, row))

    self.bkgd = Entity(self.world, (0, 0), (0, 0), surf, 1)

    self.world.bkgdSprites.add(self.bkgd, layer = 0)

    self.blocks = self.doBlocks([
      (1, 4),
      (2, 4),
      (3, 4),
      (4, 4),
      (5, 4),
      (6, 4),
      (7, 4),
      (8, 4),
      (1, 2),
      (2, 2),
      (3, 2),
      (4, 2),
      (5, 2),
      (6, 2),
    ],64 )

    self.currDrawing = self.menu

  def play(self, btn):
    self.win.fill(Colors.Green)

    self.currDrawing = self.world