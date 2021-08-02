
from os import curdir
from posixpath import normpath
import struct
from collections import namedtuple

from numpy.lib.polynomial import poly
from obj import Obj
import random
import numpy as np


V2 = namedtuple('Point2', ['x', 'y'])


def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

def color(r, g, b):
    # Acepta valores de 0 a 1
    # Se asegura que la información de color se guarda solamente en 3 bytes
    return bytes([ int(b * 255), int(g* 255), int(r* 255)])


BLACK = color(0,0,0)
WHITE = color(1,1,1)


class Renderer(object):
    def __init__(self, width, height):
        #Constructor
        self.curr_color = WHITE
        self.clear_color = BLACK
        self.glCreateWindow(width, height)


    def glClearColor(self, r, g, b):
        self.clear_color = color(r, g, b)

    def glClear(self):
        #Crea una lista 2D de pixeles y a cada valor le asigna 3 bytes de color
        self.pixels = [[ self.clear_color for y in range(self.height)] for x in range(self.width)]

    def glColor(self, r, g, b):
        self.curr_color = color(r,g,b)


    def glPoint(self, x, y, color = None):
        if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
            return

        if (0 < x < self.width) and (0 < y < self.height):
            self.pixels[int(x)][int(y)] = color or self.curr_color


    def glVertex(self, x, y):
        Xw = round((x + 1) * (self.vpWidth * 0.5) + self.vpX)
        Yw = round((y + 1) * (self.vpHeight * 0.5) + self.vpY)
        if (Xw == self.vpWidth):
            Xw -= 1
        if (Yw == self.vpHeight):
            Yw -= 1
        #print(Xw, Yw)
        self.pixels[int(Xw)][int(Yw)] = self.curr_color


    def glViewport(self, x, y, width, height):
        self.vpX = x
        self.vpY = y
        self.vpWidth = width
        self.vpHeight = height

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()
        self.glViewport(0, 0, width, height)

   
    def glLine(self, v0, v1, color = None):
        x0 = v0.x
        x1 = v1.x
        y0 = v0.y
        y1 = v1.y

        if x0 == x1 and y0 == y1:
            self.glPoint(x0,y1,color)
            return


        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        offset = 0
        limit = 0.5
        m = dy/dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                self.glPoint(y, x, color)
            else:
                self.glPoint(x, y, color)

            offset += m
            if offset >= limit:
                y += 1 if y0 < y1 else -1
                limit += 1

    def glDrawPol(self, polygon):
        
        for i in range(len(polygon)):
            x0 = polygon[i][0]
            y0 = polygon[i][1]
            x1 = polygon[(i + 1) % len(polygon)][0]
            y1 = polygon[(i + 1) % len(polygon)][1]

            self.glLine(V2(x0, y0), V2(x1, y1))

        #for y in range(y0, y1):
        #    for x in range(x0, x1):
        #        y += 1
        #        x += 1
        #        self.glLine(V2(x0,y0), V2(x,y))

    def glFillPol(self,polygon, paintColor=None):    
        xMin = 0
        xMax = 0
        yMin = 0
        yMax = 0
        lenPol = len(polygon)
        for i in range(lenPol):
            x0 = polygon[i][0]
            y0 = polygon[i][1]
            x1 = polygon[(i + 1) % lenPol][0]
            y1 = polygon[(i + 1) % lenPol][1]
            if xMin == 0 and yMin == 0:
                xMin, yMin = x0, y0
            if (x0 < xMin):
                xMin = x0
            if (x1 > xMax):
                xMax = x1
            if (y0 < yMin):
                yMin = y0
            if (y1 > yMax):
                yMax = y1
                
            #self.glLine(V2(x0, y0), V2(x1, y1))
        #print(xMin, xMax, yMin, yMax)

        for y in range(self.height):
            for x in range(self.width):
                if (self.pixels[x][y] == self.curr_color):
                    #self.glPoint(x,y, WHITE)
                    if (self.pixels[x-1][y-1] != self.curr_color):
                        #x0 =+ 1
                        #x0 = x0
                        #y0 =+ 1
                        #y0 = y0
                        #while x < int(min(polygon)):
                        self.glPoint(x,y, paintColor)
                        if(self.pixels[x+1][y+1] != self.curr_color):
                            x0 += 1
                            y0 += 1
                            self.glLine(V2(xMin,yMin), V2(x,y), paintColor)
                            #self.glLien
                            
                        else:
                            pass
                        #self.glLine(V2(x0,y0), V2(x,y), paintColor)
                        
                

                

    def glLoadModel(self, filename, translate = V2(0.0,0.0), scale = V2(1.0,1.0)):

        model = Obj(filename)

        for face in model.faces:
            vertCount = len(face)

            if vertCount == 3:
                index0 = face[0][0] - 1
                index1 = face[1][0] - 1
                index2 = face[2][0] - 1

                vert0 = model.vertices[index0]
                vert1 = model.vertices[index1]
                vert2 = model.vertices[index2]

                a = V2(int(vert0[0] * scale.x + translate.x), int(vert0[1] * scale.y + translate.y) )
                b = V2(int(vert1[0] * scale.x + translate.x), int(vert1[1] * scale.y + translate.y) )
                c = V2(int(vert2[0] * scale.x + translate.x), int(vert2[1] * scale.y + translate.y) )
                

                self.glTriangle(a, b, c, color(random.random(), random.random(), random.random()))


    def glTriangle(self, A, B, C, color = None):

        if A.y < B.y:
            A, B = B, A
        if A.y < C.y:
            A, C = C, A
        if B.y < C.y:
            B, C = C, B

        def flatBottomTriangle(v1, v2, v3):
            try:
                d_21 = (v2.x - v1.x) / (v2.y - v1.y)
                d_31 = (v3.x - v1.x) / (v3.y - v1.y)
            except:
                pass
            else:
                x1 = v2.x
                x2 = v3.x
                for y in range(v2.y, v1.y + 1):
                    self.glLine(V2(int(x1),y), V2(int(x2),y), color)
                    x1 += d_21
                    x2 += d_31

        def flatTopTriangle(v1, v2, v3):
            try:
                d_31 = (v3.x - v1.x) / (v3.y - v1.y)
                d_32 = (v3.x - v2.x) / (v3.y - v2.y)
            except:
                pass
            else:
                x1 = v3.x
                x2 = v3.x

                for y in range(v3.y, v1.y + 1):
                    self.glLine(V2(int(x1),y), V2(int(x2),y), color)
                    x1 += d_31
                    x2 += d_32

        if B.y == C.y:
            # triangulo con base inferior plana
            flatBottomTriangle(A, B, C)
        elif A.y == B.y:
            # triangulo con base superior plana
            flatTopTriangle(A, B, C)
        else:
            # dividir el triangulo en dos
            # dibujar ambos casos
            # Teorema de intercepto
            D = V2(A.x + ((B.y - A.y) / (C.y - A.y)) * (C.x - A.x)   , B.y)
            flatBottomTriangle(A, B, D)
            flatTopTriangle(B, D, C)

    def glFinish(self, filename):
        #Crea un archivo BMP y lo llena con la información dentro de self.pixels
        with open(filename, "wb") as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color Table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])









