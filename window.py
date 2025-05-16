import glfw

from OpenGL.GL import *
from pyglm import glm

from game import Game
from shader import Shader
from object_manager import ObjectManager
from camera import Camera

import numpy as np

window_instance = None

class Window:
    def __init__(self, title, width, height):
        global window_instance
        window_instance = self

        self.game = Game()

        self.WIDTH = width
        self.HEIGHT = height
        self.TITLE = title

        glfw.init()

        self.window = glfw.create_window(self.WIDTH, self.HEIGHT, self.TITLE, None, None)
        glfw.make_context_current(self.window)
        glfw.set_framebuffer_size_callback(self.window, self.framebuffer_size_callback)

        glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED)
        glfw.set_cursor_pos_callback(self.window, self.mouse_callback)

        self.init_gl()

    def init_gl(self):
        glEnable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);  
        glClearColor(0.18, 0.03, 0.26, 1.0)

        self.shader = Shader('shaders/default.vert', 'shaders/default.frag')

        self.objManager = ObjectManager()
        self.camera = Camera(self.WIDTH, self.HEIGHT)

        self.game.start(self, self.shader, self.camera, self.objManager)
    
    def render_window(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            self.render()

            glfw.swap_buffers(self.window)
        
        self.game.close()
        
        glfw.terminate()

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.game.update()

    def framebuffer_size_callback(window, width, height):
        glViewport(0, 0, width, height)

    @staticmethod
    def mouse_callback(window, xpos, ypos):
        window_instance.camera.camera_look(xpos, ypos)