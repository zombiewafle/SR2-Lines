# Programa principal
from gl import Renderer, V2, color
from numpy import sin, cos

import random


width = 1920
height = 1080

rend = Renderer(width, height)

rend.glLoadModel("models/Mandalorian.obj",V2(width/2, 150), V2(20,20))


rend.glFinish("output.bmp")


