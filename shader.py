from OpenGL.GL import *

import OpenGL.GL.shaders as gls
from pyglm import glm

class Shader:
    def __init__(self, vertexPath, fragPath):
        self.shaderProgram = self.load_shaders(vertexPath, fragPath)

    def load_shaders(self, vertexPath, fragPath):
        with open(vertexPath, 'r') as file:
            vertexSource = file.read()
        with open(fragPath, 'r') as file:
            fragSource = file.read()
        
        vertexShader = gls.compileShader(vertexSource, GL_VERTEX_SHADER)
        fragShader = gls.compileShader(fragSource, GL_FRAGMENT_SHADER)
        program = gls.compileProgram(vertexShader, fragShader)

        glDeleteShader(vertexShader)
        glDeleteShader(fragShader)

        return program

    def use(self):
        glUseProgram(self.shaderProgram)
    
    def delete(self):
        glUseProgram(0)

    def get_program(self):
        return self.shaderProgram
    
    def set_matrix4_uniform(self, name, value):
        loc = glGetUniformLocation(self.shaderProgram, name)
        glUniformMatrix4fv(loc, 1, GL_FALSE, glm.value_ptr(value))
    
    def cleanup(self):
        if hasattr(self, 'shaderProgram') and self.shaderProgram:
            glDeleteProgram(self.shaderProgram)