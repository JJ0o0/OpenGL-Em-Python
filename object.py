from OpenGL.GL import *
from pyglm import glm
import ctypes as ct
import numpy as np

from texture import Texture

class Object:
    def __init__(self, name, vertices, indices):
        self.name = name
        self.vertices = vertices
        self.indices = indices
        self.vao = self.create_object(self.vertices, self.indices)

    def create_object(self, vertices, indices):
        vertices = np.array(vertices, np.dtype(np.float32)) # 4 Bytes ou 32 Bits
        indices = np.array(indices, np.dtype(np.int32))     # 4 Bytes ou 32 Bits

        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)
        
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 5 * ct.sizeof(ct.c_float), ct.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 5 * ct.sizeof(ct.c_float), ct.c_void_p(3 * ct.sizeof(ct.c_float)))
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        return vao
    
    def set_texture(self, texturePath, textureIndex):
        self.texture = Texture(texturePath)
        self.textureIndex = textureIndex

    def render(self):
        self.texture.bind(self.textureIndex)

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, len(self.indices) * 3, GL_UNSIGNED_INT, None)

        glBindVertexArray(0)
    
    def set_position(self, position=glm.vec3(0.0, 0.0, 0.0)):
        self.position = position
    
    def set_rotation(self, rotation=0.0):
        self.rotation = rotation
    
    def set_scale(self, scale=glm.vec3(1.0, 1.0, 1.0)):
        self.scale = scale

    def create_model_matrix(self, shader):
        self.model = glm.mat4(1.0)
        self.model = glm.translate(self.model, self.position) # vec3
        self.model = glm.rotate(self.model, glm.radians(self.rotation), glm.vec3(1.0, 0.3, 0.5)) # float
        self.model = glm.scale(self.model, self.scale) # vec3

        shader.set_matrix4_uniform('model', self.model)

    def cleanup(self):
        self.texture.unbind()

        glDeleteVertexArrays(1, [self.vao])