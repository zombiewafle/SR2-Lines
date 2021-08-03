# Programa principal
from gl import Renderer, V2, color
from numpy import sin, cos, square
import random


width = 1920 
height = 1080

rend = Renderer(width, height)

#rend.glClearColor(0,0,0)
#rend.glColor(0,0,0)

#rend.glViewport(0, 0, width, height)

#Triangle
#rend.glLine(V2(100, 10), V2(100, 310), color(1,0,0))
#rend.glLine(V2(100, 10), V2(400, 10), color(1,0,0))
#rend.glLine(V2(100, 310), V2(400, 10), color(1,0,0))
#
##Rectangle
#rend.glLine(V2(1500, 10), V2(1500, 310), color(1,0,0))
#rend.glLine(V2(1600, 10), V2(1600, 310), color(1,0,0))
#rend.glLine(V2(1500, 310), V2(1600, 310), color(1,0,0))
#rend.glLine(V2(1500, 10), V2(1600, 10), color(1,0,0))
#
##David Star
#rend.glLine(V2(600, 310), V2(800, 620), color(1,0,0))
#rend.glLine(V2(600, 310), V2(1000, 310), color(1,0,0))
#rend.glLine(V2(1000, 310), V2(800, 620), color(1,0,0))
#
#rend.glLine(V2(600, 570), V2(800, 260), color(1,0,0))
#rend.glLine(V2(600, 570), V2(1000, 570), color(1,0,0))
#rend.glLine(V2(1000, 570), V2(800, 260), color(1,0,0))
#
#
#Square
#square=[(450,1000),(450,1300),(850,1000),(850,1300),(450,1300),(850,1300),(450,1000),(850,1000)]
Square = [(321, 335), (288, 286), (339, 251), (374, 302)]
Star = [(165, 380), (185, 360),  (180, 330) , (207, 345),  (233, 330) , (230, 360) , (250, 380) , (220, 385),  (205, 410),  (193, 383)]
Triangle = [(377, 249) ,(411, 197), (436, 249)]
tetera=[(413, 177) ,(448, 159) ,(502, 88) ,(553, 53), (535, 36) ,(676, 37) ,(660, 52),
(750, 145) ,(761, 179) ,(672, 192) ,(659, 214) ,(615, 214) ,(632, 230) ,(580, 230),
(597, 215) ,(552, 214) ,(517, 144) ,(466, 180)]
Tetera2= [(682, 175) ,(708, 120), (735, 148), (739, 170)]
#rend.glLoadModel("models/model.obj",V2(width/2, height/2), V2(500,500))
#rend.glLine(V2(450, 1000), V2(450, 1300), color(1,0,0))
#rend.glLine(V2(850, 1000), V2(850, 1300), color(1,0,0))
#rend.glLine(V2(450, 1300), V2(850, 1300), color(1,0,0))
#rend.glLine(V2(450, 1000), V2(850, 1000), color(1,0,0))
#
#
##Pentagon
#rend.glLine(V2(1000, 1600), V2(1300, 1900), color(1,0,0))
#rend.glLine(V2(1600, 1600), V2(1300, 1900), color(1,0,0))
#rend.glLine(V2(1000, 1250), V2(1000, 1600), color(1,0,0))
#rend.glLine(V2(1600, 1250), V2(1600, 1600), color(1,0,0))
#rend.glLine(V2(1000, 1250), V2(1600, 1250), color(1,0,0))

rend.glDrawPol(tetera)
rend.glDrawPol(Tetera2)
rend.glDrawPol(Star)
rend.glDrawPol(Triangle)
rend.glDrawPol(Square)

rend.glFillPol(Square, color(1,0,0))
rend.glFillPol(Triangle, color(1,0,0))
rend.glFillPol(tetera, color(1,0,0))
rend.glFillPol(Tetera2, color(0,0,0))
rend.glFillPol(Star, color(1,0,0))


#rend.glTriangle(V2(10, 70),  V2(50, 160), V2(70, 80), color(random.random(), random.random(),random.random()))
#for x in range (square):
 #  rend.glLine()

#for x in range(width):
 #   for y in range(height):
  #      if random.randint(0,2) > 0.5:
   #         rend.glPoint(x,y)


#rend.glVertex(1,1)
#rend.glVector(100,200)


rend.glFinish("output.bmp")


