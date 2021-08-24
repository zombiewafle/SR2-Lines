import numpy as np
import mathLibraries as ml

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






