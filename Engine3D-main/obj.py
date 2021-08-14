# Carga un archivo OBJ
import struct

def _color(r, g, b):
    return bytes([ int(b * 255), int(g* 255), int(r* 255)])

class Obj(object):
    def __init__(self, filename):
        
        with open(filename, "r") as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.texcoords = []
        self.normals = []
        self.faces = []

        self.read()


    def read(self):
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)

                if prefix == 'v': # Vertices
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'vt': #Texture Coordinates
                    self.texcoords.append(list(map(float, value.split(' '))))
                elif prefix == 'vn': #Normales
                    self.normals.append(list(map(float, value.split(' '))))
                elif prefix == 'f': #Caras
                    self.faces.append( [ list(map(int, vert.split('/'))) for vert in value.split(' ')] )


class Texture(object):
    def __init__(self, filename):
        self.filename = filename
        self.read()

    def read(self):
        with open(self.filename, "rb") as image:
            image.seek(10)
            headerSize = struct.unpack('=l', image.read(4))[0]

            image.seek(14 + 4)
            self.width = struct.unpack('=l', image.read(4))[0]
            self.height = struct.unpack('=l', image.read(4))[0]

            image.seek(headerSize)

            self.pixels = []

            for x in range(self.width):
                self.pixels.append([])
                for y in range(self.height):
                    b = ord(image.read(1)) / 255
                    g = ord(image.read(1)) / 255
                    r = ord(image.read(1)) / 255

                    self.pixels[x].append( _color(r,g,b) )

    def getColor(self, tx, ty):
        if 0<=tx<1 and 0<=ty<1:
            x = round(tx * self.width)
            y = round(ty * self.height)
            return self.pixels[y][x]
        else:
            return _color(0,0,0)










