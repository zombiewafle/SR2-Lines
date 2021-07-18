# Programa principal
from gl import Renderer, V2, color
from numpy import sin, cos
import random


width = 3000
height = 4000

rend = Renderer(width, height)

rend.glClearColor(0.5,0.5,0.2)

#rend.glViewport(0, 0, width, height)

#Triangle
rend.glLine(V2(100, 10), V2(100, 310), color(1,0,0))
rend.glLine(V2(100, 10), V2(400, 10), color(1,0,0))
rend.glLine(V2(100, 310), V2(400, 10), color(1,0,0))

#Rectangle
rend.glLine(V2(1500, 10), V2(1500, 310), color(1,0,0))
rend.glLine(V2(1600, 10), V2(1600, 310), color(1,0,0))
rend.glLine(V2(1500, 310), V2(1600, 310), color(1,0,0))
rend.glLine(V2(1500, 10), V2(1600, 10), color(1,0,0))

#David Star
rend.glLine(V2(600, 310), V2(800, 620), color(1,0,0))
rend.glLine(V2(600, 310), V2(1000, 310), color(1,0,0))
rend.glLine(V2(1000, 310), V2(800, 620), color(1,0,0))

rend.glLine(V2(600, 570), V2(800, 260), color(1,0,0))
rend.glLine(V2(600, 570), V2(1000, 570), color(1,0,0))
rend.glLine(V2(1000, 570), V2(800, 260), color(1,0,0))


#Square
rend.glLine(V2(450, 1000), V2(450, 1300), color(1,0,0))
rend.glLine(V2(850, 1000), V2(850, 1300), color(1,0,0))
rend.glLine(V2(450, 1300), V2(850, 1300), color(1,0,0))
rend.glLine(V2(450, 1000), V2(850, 1000), color(1,0,0))

#Pentagon
rend.glLine(V2(1000, 1600), V2(1300, 1900), color(1,0,0))
rend.glLine(V2(1600, 1600), V2(1300, 1900), color(1,0,0))
rend.glLine(V2(1000, 1250), V2(1000, 1600), color(1,0,0))
rend.glLine(V2(1600, 1250), V2(1600, 1600), color(1,0,0))
rend.glLine(V2(1000, 1250), V2(1600, 1250), color(1,0,0))




#for x in range(width):
 #   for y in range(height):
  #      if random.randint(0,2) > 0.5:
   #         rend.glPoint(x,y)


#rend.glVertex(1,1)
#rend.glVector(100,200)


rend.glFinish("output.bmp")


