def argb(val):
  return ((val >> 16) & 0xFF,
          (val >> 8) & 0xFF,
          val & 0xFF,
          (val >> 24) & 0xFF)

def rgb(val):
  return ((val >> 16) & 0xFF,
          (val >> 8) & 0xFF,
          val & 0xFF)

class Colors:
  Black           = argb(0xFF000000)
  CornflowerBlue  = argb(0xFF6495ED)
  Green           = argb(0xFF008000)
  White           = argb(0xFFFFFFFF)