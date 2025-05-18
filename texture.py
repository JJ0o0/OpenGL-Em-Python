from PIL import Image
from OpenGL.GL import *

import os

class Texture:
    def __init__(self, filepath):
        here = os.path.dirname(os.path.abspath(__file__))
        fp = os.path.join(here, filepath)

        img = Image.open(fp)
        img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        
        imgData = img.convert("RGBA").tobytes()

        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, imgData)
    
    def bind(self, index=0):
        glActiveTexture(GL_TEXTURE0 + index)
        glBindTexture(GL_TEXTURE_2D, self.texture)
    
    def unbind(self):
        glBindTexture(GL_TEXTURE_2D, 0)