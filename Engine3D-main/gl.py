import struct
from collections import namedtuple

from obj import Obj

import numpy as np

from numpy import pi, sin, cos, tan

import mathlibraries as ml

import random

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

def _color(r, g, b):
    # Acepta valores de 0 a 1
    # Se asegura que la información de color se guarda solamente en 3 bytes
    return bytes([ int(b * 255), int(g* 255), int(r* 255)])

def baryCoords(A, B, C, P):
    # u es para A, v es para B, w es para C
    try:
        #PCB/ABC
        u = (((B.y - C.y) * (P.x - C.x) + (C.x - B.x) * (P.y - C.y)) /
            ((B.y - C.y) * (A.x - C.x) + (C.x - B.x) * (A.y - C.y)))

        #PCA/ABC
        v = (((C.y - A.y) * (P.x - C.x) + (A.x - C.x) * (P.y - C.y)) /
            ((B.y - C.y) * (A.x - C.x) + (C.x - B.x) * (A.y - C.y)))

        w = 1 - u - v
    except:
        return -1, -1, -1

    return u, v, w


BLACK = _color(0,0,0)
WHITE = _color(1,1,1)


class Renderer(object):
    def __init__(self, width, height):
        #Constructor
        self.curr_color = WHITE
        self.clear_color = BLACK
        self.glViewMatrix()
        self.glCreateWindow(width, height)

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

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()
        self.glViewport(0,0, width, height)

    def glViewport(self, x, y, width, height):
        self.vpX = int(x)
        self.vpY = int(y)
        self.vpWidth = int(width)
        self.vpHeight = int(height)

        matrix = [(width/2),0,0, (x+(width/2)),0 , (height/2),0, (y+(height/2)),0,0,0.5,0.5,0,0,0,1]

        self.viewportMatrix = ml.createMatrix(4,4,matrix)
        #self.viewportMatrix = np.matrix([[width/2, 0, 0, x + width/2],
        #                                 [0, height/2, 0, y + height/2],
        #                                 [0, 0, 0.5, 0.5],
        #                                 [0, 0, 0, 1]])
        #print(self.viewportMatrix)

        self.glProjectionMatrix()

    def glClearColor(self, r, g, b):
        self.clear_color = color(r, g, b)

    def glClear(self):
        #Crea una lista 2D de pixeles y a cada valor le asigna 3 bytes de color
        self.pixels = [[ self.clear_color for y in range(self.height)]
                         for x in range(self.width)]

        self.zbuffer = [[ float('inf')for y in range(self.height)]
                          for x in range(self.width)]

    def glViewportClear(self, color = None):
        for x in range(self.vpX, self.vpX + self.vpWidth):
            for y in range(self.vpY, self.vpY + self.vpHeight):
                self.glPoint(x,y, color)

    def glColor(self, r, g, b):
        self.curr_color = color(r,g,b)

    def glPoint(self, x, y, color = None):
        if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
            return

        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[int(x)][int(y)] = color or self.curr_color

    def glPoint_NDC(self, x, y, color = None):
        x = int( (x + 1) * (self.vpWidth / 2) + self.vpX )
        y = int( (y + 1) * (self.vpHeight / 2) + self.vpY)


        if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
            return

        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[int(x)][int(y)] = color or self.curr_color

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

    def glLine_NDC(self, v0, v1, color = None):

        x0 = int( (v0.x + 1) * (self.vpWidth / 2) + self.vpX)
        x1 = int( (v1.x + 1) * (self.vpWidth / 2) + self.vpX)
        y0 = int( (v0.y + 1) * (self.vpHeight / 2) + self.vpY)
        y1 = int( (v1.y + 1) * (self.vpHeight / 2) + self.vpY)

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

    def glTriangle_standard(self, A, B, C, color = None):

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


    def glTriangle_bc(self, A, B, C, texCoords = (), texture = None, color = None, intensity = 1):
        #Bounding Box
        minX = round(min(A.x, B.x, C.x))
        minY = round(min(A.y, B.y, C.y))
        maxX = round(max(A.x, B.x, C.x))
        maxY = round(max(A.y, B.y, C.y))

        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                u, v, w = baryCoords(A, B, C, V2(x, y))

                if u >= 0 and v >= 0 and w >= 0:

                    z = A.z * u + B.z * v + C.z * w

                    if texture:
                        tA, tB, tC = texCoords
                        tx = tA[0] * u + tB[0] * v + tC[0] * w
                        ty = tA[1] * u + tB[1] * v + tC[1] * w
                        color = texture.getColor(tx, ty)

                    if 0<=x<self.width and 0<=y<self.height:
                        if z < self.zbuffer[x][y] and z<=1 and z >= -1:

                            self.glPoint(x,y, _color( color[2] * intensity / 255,
                                                      color[1] * intensity / 255,
                                                      color[0] * intensity / 255) )
                            self.zbuffer[x][y] = z




    def glTransform(self, vertex, vMatrix):
        augVertex = V4(vertex[0], vertex[1], vertex[2], 1)
        transVertex = ml.multiVecMatrix(augVertex, vMatrix)
        #transVertex = vMatrix @ augVertex
        #transVertex = transVertex.tolist()[0]

        transVertex = V3(transVertex[0] / transVertex[3],
                         transVertex[1] / transVertex[3],
                         transVertex[2] / transVertex[3])

        return transVertex

    def glCamTransform( self, vertex ):
        augVertex = V4(vertex[0], vertex[1], vertex[2], 1)
        transVertex1 = ml.dotProduct(self.viewportMatrix, self.projectionMatrix)
        transVertex2 = ml.dotProduct(transVertex1,self.viewportMatrix)
        transVertex3 = ml.dotProduct(transVertex2,augVertex)
        #transVertex = self.viewportMatrix @ self.projectionMatrix @ self.viewMatrix @ augVertex
        #transVertex = transVertex.tolist()[0]

        transVertex3 = V3(transVertex3[0] / transVertex3[3],
                         transVertex3[1] / transVertex3[3],
                         transVertex3[2] / transVertex3[3])

        return transVertex3


    def glCreateRotationMatrix(self, rotate=V3(0,0,0)):
        pitch = ml.deg2rads(rotate.x)
        yaw = ml.deg2rads(rotate.y)
        roll = ml.deg2rads(rotate.z)

        rotXMatrix = [1,0,0,0,0,cos(pitch),-sin(pitch),0,0,sin(pitch),cos(pitch),0,0,0,0,1]
        rotYMatrix = [cos(yaw),0,sin(yaw),0,0,1,0,0,-sin(yaw),0,cos(yaw),0,0,0,0,1]
        rotZMatrix = [cos(roll),-sin(roll),0,0,sin(roll),cos(roll),0,0,0,0,1,0,0,0,0,1]

        rotationX = ml.createMatrix(4,4,rotXMatrix)
        rotationY = ml.createMatrix(4,4,rotYMatrix)
        rotationZ = ml.createMatrix(4,4,rotZMatrix)
        #print(rotationX)
        #print()
        #print(rotationY)
        #print()
        #print(rotationZ)
        #rotationX = np.matrix([[1,0,0,0],
        #                       [0,cos(pitch),-sin(pitch),0],
        #                       [0,sin(pitch),cos(pitch),0],
        #                       [0,0,0,1]])

        #rotationY = np.matrix([[cos(yaw),0,sin(yaw),0],
        #                       [0,1,0,0],
        #                       [-sin(yaw),0,cos(yaw),0],
        #                       [0,0,0,1]])

        #rotationZ = np.matrix([[cos(roll),-sin(roll),0,0],
        #                       [sin(roll),cos(roll),0,0],
        #                       [0,0,1,0],
        #                       [0,0,0,1]])

        #print(rotationX)
        #print(rotationY)
        #print(rotationZ)

        multiplication1 = ml.multyMatrix(rotationX,rotationY)
        multiplication2 = ml.multyMatrix(multiplication1,rotationZ)

        return multiplication2#rotationX * rotationY * rotationZ


    def glCreateObjectMatrix(self, translate = V3(0,0,0), scale = V3(1,1,1), rotate = V3(0,0,0)):

        matrixTranslate = [1,0,0,translate.x,0,1,0, translate.y, 0,0,1, translate.z,0,0,0,1]
        matrixScale = [scale.x, 0, 0 ,0, 0, scale.y, 0, 0, 0, 0, scale.z, 0,0,0,0,1]
    
        translateMatrix = ml.createMatrix(4,4,matrixTranslate)
        scaleMatrix = ml.createMatrix(4,4,matrixScale)

        #translateMatrix = np.matrix([[1,0,0,translate.x],
        #                             [0,1,0,translate.y],
        #                             [0,0,1,translate.z],
        #                             [0,0,0,1]])
        #scaleMatrix = np.matrix([[scale.x,0,0,0],
        #                         [0,scale.y,0,0],
        #                         [0,0,scale.z,0],
        #                         [0,0,0,1]])

        rotationMatrix = self.glCreateRotationMatrix(rotate)

        multiplication1 = ml.multyMatrix(translateMatrix,rotationMatrix)
        multiplication2 = ml.multyMatrix(multiplication1 ,scaleMatrix)

        return multiplication2#translateMatrix * rotationMatrix * scaleMatrix

    def glViewMatrix(self, translate = V3(0,0,0), rotate = V3(0,0,0)):
        camMatrix = self.glCreateObjectMatrix(translate,V3(1,1,1),rotate)
        self.viewMatrix = np.linalg.inv(camMatrix)

    def glLookAt(self, eye, camPosition = V3(0,0,0)):
        forward = np.subtract(camPosition, eye)
        forward = forward / np.linalg.norm(forward)

        right = np.cross(V3(0,1,0), forward)
        right = right / np.linalg.norm(right)

        up = np.cross(forward, right)
        up = up / np.linalg.norm(up)

        camMatrix = np.matrix([[right[0],up[0],forward[0],camPosition.x],
                               [right[1],up[1],forward[1],camPosition.y],
                               [right[2],up[2],forward[2],camPosition.z],
                               [0,0,0,1]])

        self.viewMatrix = np.linalg.inv(camMatrix)



    def glProjectionMatrix(self, n = 0.1, f = 1000, fov = 60 ):
        t = tan((fov * np.pi / 180) / 2) * n
        r = t * self.vpWidth / self.vpHeight

        self.projectionMatrix = np.matrix([[n/r, 0, 0, 0],
                                           [0, n/t, 0, 0],
                                           [0, 0, -(f+n)/(f-n), -(2*f*n)/(f-n)],
                                           [0, 0, -1, 0]])


    def glLoadModel(self, filename, texture = None, translate = V3(0,0,0), scale = V3(1,1,1), rotate = V3(0,0,0)):

        model = Obj(filename)

        modelMatrix = self.glCreateObjectMatrix(translate,scale,rotate)

        light = V3(0,0,-1)
        light = light / np.linalg.norm(light)

        for face in model.faces:
            vertCount = len(face)

            vert0 = model.vertices[face[0][0] - 1]
            vert1 = model.vertices[face[1][0] - 1]
            vert2 = model.vertices[face[2][0] - 1]

            vt0 = model.texcoords[face[0][1] - 1]
            vt1 = model.texcoords[face[1][1] - 1]
            vt2 = model.texcoords[face[2][1] - 1]


            a = self.glTransform(vert0, modelMatrix)
            b = self.glTransform(vert1, modelMatrix)
            c = self.glTransform(vert2, modelMatrix)

            if vertCount == 4:
                vert3 = model.vertices[face[3][0] - 1]
                vt3 = model.texcoords[face[3][1] - 1]
                d = self.glTransform(vert3, modelMatrix)


            normal = ml.crossProduct(ml.subVectors(vert1,vert0), ml.subVectors(vert2,vert0))
            #b = ml.norm(normal)
            #print(b)
            normal = normal / np.linalg.norm(normal) # la normalizamos
            #normal = normal / ml.norm(np.float64(normal)) # la normalizamos
            intensity = ml.dotProduct(normal, -light)

            if intensity > 1:
                intensity = 1
            elif intensity < 0:
                intensity = 0

            a = self.glCamTransform(a)
            b = self.glCamTransform(b)
            c = self.glCamTransform(c)
            if vertCount == 4:
                d = self.glCamTransform(d)

            self.glTriangle_bc(a, b, c, texCoords = (vt0,vt1,vt2), texture = texture, intensity = intensity)
            if vertCount == 4:
                self.glTriangle_bc(a, c, d, texCoords = (vt0,vt2,vt3), texture = texture, intensity = intensity)


