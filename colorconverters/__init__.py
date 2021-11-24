from .colorutilities import *

version = ""
with open("../VERSION.txt") as f:
    version = f.read()

__title__ = "colorconverters"
__summary__ = "A useful package which handles the utilities of converting colors to different forms."
__author__ = "GenZ Gamer"
__version__ = version
__license__ = "MIT"

def get_version():
    return __version__
