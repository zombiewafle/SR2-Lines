import numpy as np
import mathLibraries as ml
import random

#Dependiendo de donde venga la luz, el color cambiara
#Donde el rojo es donde la luz pega directamente
#Amarillo la luz no golpea directamente
#Azul, la luz golpea muy poco o nada
def thermal(render, **kwargs):
    # Iluminacion por pixel

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = ml.dotProduct(normal, dirLight)


    #b*= intensity
    #g*= intensity
    #r*= intensity

    #glowAmount = 1 - ml.dotProduct(normal, camForward)
    heatColor = [1,0,0]
    coldColor = [0,0,1]

    colorIntensity = 1 - intensity

    if colorIntensity > 0.99:
        r += heatColor[0] * colorIntensity
        g += heatColor[1] * colorIntensity
        b += heatColor[2] * colorIntensity

        if r > 1:
            r =1.00

        if g > 1:
            g =0.00

        if b > 1:
            b =0

        return 1,0,0





    elif colorIntensity > 0.7 :
        r += heatColor[0] * colorIntensity
        g += heatColor[1] * colorIntensity
        b += heatColor[2] * colorIntensity

        if r > 1:
            r = 0.55

        if g > 1:
            g = 0.55

        if b > 1:
            b = 0

        return 0.55,0.55,0.00


    elif colorIntensity > 0.6 :
        r += heatColor[0] * colorIntensity
        g += heatColor[1] * colorIntensity
        b += heatColor[2] * colorIntensity

        if r > 1:
            r = 0.55

        if g > 1:
            g = 0.55

        if b > 1:
            b = 0.25

        return 0.00,0.00,1.00



    #elif colorIntensity < 0.5:
    #    r += heatColor[0] * colorIntensity
    #    g += heatColor[1] * colorIntensity
    #    b += heatColor[2] * colorIntensity

    #    if r > 1:
    #        r = 0

    #    if g > 1:
    #        g = 0

    #    if b > 1:
    #        b = 1

    #    return 0.00,0.00,1.00


    else:
        r += heatColor[0] * colorIntensity
        g += heatColor[1] * colorIntensity
        b += heatColor[2] * colorIntensity

        if r > 1:
            r = 0

        if g > 1:
            g = 0

        if b > 1:
            b = 1

        return 0.00,0.00,0.55




    #else:
    #    r += coldColor[0] * colorIntensity
    #    b += coldColor[2] * colorIntensity
    #    g += coldColor[1] * colorIntensity

    #    if r > 1:
    #        r =0

    #    if g > 1:
    #        g =0

    #    if b > 1:
    #        b =1

    #    return r,g,b





    #if colorIntensity >= 0.7:
    #    r += heatColor[0] * colorIntensity
    #    g += heatColor[1] * colorIntensity
    #    b += heatColor[2] * colorIntensity

    #    if r > 1:
    #        r =1

    #    if g > 1:
    #        g =0

    #    if b > 1:
    #        b =0

    #    return r,g,b

    #elif colorIntensity == 0.50:
    #    r += heatColor[0] * colorIntensity
    #    g += heatColor[1] * colorIntensity
    #    b += heatColor[2] * colorIntensity

    #    if r > 1:
    #        r =0.4

    #    if g > 1:
    #        g =0

    #    if b > 1:
    #        b =0.6

    #    return r,g,b

    #elif colorIntensity == 0.4:
    #    r += heatColor[0] * colorIntensity
    #    g += heatColor[1] * colorIntensity
    #    b += heatColor[2] * colorIntensity

    #    if r > 1:
    #        r =0.3

    #    if g > 1:
    #        g =0

    #    if b > 1:
    #        b =0.70


    #elif colorIntensity == 0.25:
    #    r += heatColor[0] * colorIntensity
    #    g += heatColor[1] * colorIntensity
    #    b += heatColor[2] * colorIntensity

    #    if r > 1:
    #        r =0.2

    #    if g > 1:
    #        g =0

    #    if b > 1:
    #        b =0.80

    #    return r,g,b


    #else:
    #    r += coldColor[0] * colorIntensity
    #    b += coldColor[2] * colorIntensity
    #    g += coldColor[1] * colorIntensity

    #    if r > 1:
    #        r =0

    #    if g > 1:
    #        g =0

    #    if b > 1:
    #        b =1

    #    return r,g,b



def static(render, **kwargs):
    #col = random.randint()
    r = random.random() *2
    g = random.random() *2
    b = random.random() *2


     # Iluminacion por pixel

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    #b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']


    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = ml.dotProduct(normal, dirLight)
    #intensity = np.dot(normal, dirLight)

    b*= intensity
    g*= intensity
    r*= intensity


    if intensity > 0:
        return r,g,b
    else:
        return 0,0,0

def glow (render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    triangleNormal = kwargs['triangleNormal']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)

        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]

    intensity = ml.dotProduct(triangleNormal, dirLight)
    #intensity = np.dot(triangleNormal, dirLight)
    if intensity <= 0:
        intensity = 0

    b *= intensity
    g *= intensity
    r *= intensity

    camForward = [ml.firstItemFunction(render.camMatrix), ml.secondItemFunction(render.camMatrix), ml.thirdItemFunction(render.camMatrix), ml.fourthItemFunction(render.camMatrix)]

    #camForward = [render.camMatrix(0,2),
    #              render.camMatrix(1,2),
    #              render.camMatrix(2,2)]

    glowAmount = 1 - ml.dotProduct(normal, camForward)
    glowColor = [0,0,1]

    r += glowColor[0] * glowAmount
    g += glowColor[1] * glowAmount
    b += glowColor[2] * glowAmount

    if r > 1:
        r =1

    if g > 1:
        g =1

    if b > 1:
        b =1

    return r, g, b

def flat(render, **kwargs):
    # Iluminacion se calcula por primitiva

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    triangleNormal = kwargs['triangleNormal']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = ml.dotProduct(triangleNormal, dirLight)
    #intensity = np.dot(triangleNormal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def gourad(render, **kwargs):
    # Iluminacion por vertice, se interpola
    # la iluminacion por cada pixel

    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensityA = ml.dotProduct(nA, dirLight)
    intensityB = ml.dotProduct(nB, dirLight)
    intensityC = ml.dotProduct(nC, dirLight)

    #intensityA = np.dot(nA, dirLight)
    #intensityB = np.dot(nB, dirLight)
    #intensityC = np.dot(nC, dirLight)

    intensity = intensityA *u + intensityB *v + intensityC *w
    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def phong(render, **kwargs):
    # Iluminacion por pixel

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = ml.dotProduct(normal, dirLight)
    #intensity = np.dot(normal, dirLight)

    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def unlit(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    return r, g, b


def toon(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = ml.dotProduct(normal, dirLight)
    #intensity = np.dot(normal, dirLight)

    if intensity > 0.85:
        intensity = 1
    elif intensity > 0.65:
        intensity = 0.5
    elif intensity > 0.45:
        intensity = 0.55
    elif intensity > 0.3:
        intensity = 0.4
    elif intensity > 0.15:
        intensity = 0.25
    else:
        intensity = 0.20


    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def textureBlend(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = ml.dotProduct(normal, dirLight)
    #intensity = np.dot(normal, dirLight)

    if intensity < 0:
        intensity = 0

    b*= intensity
    g*= intensity
    r*= intensity

    if render.active_texture2:
        texColor = render.active_texture2.getColor(tx, ty)
        b += (texColor[0] / 255) * (1 - intensity)
        g += (texColor[1] / 255) * (1 - intensity)
        r += (texColor[2] / 255) * (1 - intensity)


    return r, g, b


def normalMap(render, **kwargs):
    A, B, C = kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w
    normal = (nX, nY, nZ)

    dirLight = np.array(render.directional_light)


    if render.normal_map:
        texNormal = render.normal_map.getColor(tx, ty)
        texNormal = [(texNormal[2] / 255) * 2 - 1,
                     (texNormal[1] / 255) * 2 - 1,
                     (texNormal[0] / 255) * 2 - 1]

        texNormal = texNormal / np.linalg.norm(texNormal)

        edge1 = np.subtract(B, A)
        edge2 = np.subtract(C, A)
        deltaUV1 = np.subtract(tB, tA)
        deltaUV2 = np.subtract(tC, tA)

        f = 1 / (deltaUV1[0] * deltaUV2[1] - deltaUV2[0] * deltaUV1[1])

        tangent = [f * (deltaUV2[1] * edge1[0] - deltaUV1[1] * edge2[0]),
                   f * (deltaUV2[1] * edge1[1] - deltaUV1[1] * edge2[1]),
                   f * (deltaUV2[1] * edge1[2] - deltaUV1[1] * edge2[2])]
        tangent = tangent / np.linalg.norm(tangent)
        tangent = np.subtract(tangent, np.multiply(np.dot(tangent, normal), normal))
        tangent = tangent / np.linalg.norm(tangent)

        bitangent = np.cross(normal, tangent)
        bitangent = bitangent / np.linalg.norm(bitangent)

        tangentMatrix = np.matrix([[tangent[0],  bitangent[0],  normal[0]],
                                   [tangent[1],  bitangent[1],  normal[1]],
                                   [tangent[2],  bitangent[2],  normal[2]]])

        texNormal = tangentMatrix @ texNormal
        texNormal = texNormal.tolist()[0]
        texNormal = texNormal / np.linalg.norm(texNormal)
        intensity = np.dot(texNormal, -dirLight)
    else:
        intensity = np.dot(normal, -dirLight)

    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0
