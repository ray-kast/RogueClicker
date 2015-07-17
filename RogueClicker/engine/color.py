def argb(val):
  """Get a tuple color from an 8-digit hexadecimal number"""
  return ((val >> 16) & 0xFF,
          (val >> 8) & 0xFF,
          val & 0xFF,
          (val >> 24) & 0xFF)

def rgb(val):
  """Get a tuple color from a 6-digit hexadecimal number"""
  return ((val >> 16) & 0xFF,
          (val >> 8) & 0xFF,
          val & 0xFF)

class Colors:
  """Provides constants for pygame colors"""

  Black           = argb(0xFF000000)
  CornflowerBlue  = argb(0xFF6495ED)
  Green           = argb(0xFF008000)
  White           = argb(0xFFFFFFFF)