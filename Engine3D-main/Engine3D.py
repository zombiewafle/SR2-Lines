# Programa principal
from gl import Renderer, V3, _color

from obj import Texture

import random

width = 1920
height = 1080

rend = Renderer(width, height)

modelTexture = Texture("models/model.bmp")


rend.glLoadModel("models/model.obj", modelTexture, V3(width/2, height/2, 0), V3(200,200,200))


rend.glFinish("output.bmp")
