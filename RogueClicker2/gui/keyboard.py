import pygame as pg

class KeyCommand:
  def __init__(self, func, key, **kwargs):
    self.func = func
    self.key = key

    self.mods = 0
    ignoreMsk = 0

    mods = kwargs.get("mods")
    ignores = kwargs.get("ignores")

    if mods != None:
      for mod in mods:
        self.mods |= mod
      
    if ignores != None:
      for ignore in kwargs["ignores"]:
        ignoreMsk |= ignore

    ignoreMsk ^= pg.KMOD_CAPS | pg.KMOD_MODE | pg.KMOD_NUM

    self.filter = ~ignoreMsk

    self.mods &= self.filter

  def handle(self, key, mods):
    if key == self.key \
      and (mods & self.filter) == self.mods:
      self.func()
      return True

    return False

class KeyCommandList:
  def __init__(self):
    self._cmds = []

  def add(self, cmd):
    self._cmds.append(cmd)

  def remove(self, cmd):
    self._cmds.remove(cmd)

  def handle(self, key, mods):
    for cmd in self._cmds:
      if cmd.handle(key, mods): return True

    return False

