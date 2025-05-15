import glfw

from OpenGL.GL import *
from pyglm import glm

from shader import Shader
from object_manager import ObjectManager
from camera import Camera

import numpy as np

window_instance = None

class Window:
    def __init__(self, title, width, height):
        global window_instance
        window_instance = self

        self.WIDTH = width
        self.HEIGHT = height
        self.TITLE = title

        self.delta_time = 0.0
        self.last_time = 0.0

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

        self.positions = [
            glm.vec3(0.0, 0.0, 0.0),
            glm.vec3(2.0, 5.0, -8.0),
            glm.vec3(-1.5, -2.2, -2.5),
            glm.vec3(-3.8, -2.0, -10.3)
        ]

        for i in range(4):
            self.objManager.create_cube(i, 'images/brick.jpg', GL_TEXTURE0)

        self.camera = Camera(self.WIDTH, self.HEIGHT)
    
    def render_window(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            self.render()

            glfw.swap_buffers(self.window)
        
        self.shader.cleanup()
        self.objManager.cleanup()
        
        glfw.terminate()

    def render(self):
        self.update_delta_time()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.process_input()

        self.shader.use()
        for i in range(self.objManager.get_object_list_length()):
            obj = self.objManager.get_object(i)
            obj.set_position(self.positions[i])
            obj.set_rotation(45 + (i * 20))
            obj.set_scale(glm.vec3(1.5, 1.5, 1.5))
            obj.create_model_matrix(self.shader)

            obj.render()

        self.camera.update(45, self.WIDTH, self.HEIGHT, 0.1, 100.0)
        self.camera.send_to_shader(self.shader)
    
    def update_delta_time(self):
        curr_frame = glfw.get_time()
        self.delta_time = curr_frame - self.last_time
        self.last_time = curr_frame

    def framebuffer_size_callback(window, width, height):
        glViewport(0, 0, width, height)

    @staticmethod
    def mouse_callback(window, xpos, ypos):
        window_instance.camera.camera_look(xpos, ypos)
        
    def process_input(self):
        if glfw.get_key(self.window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(self.window, True)

        camera_speed = 2.5 * self.delta_time

        if glfw.get_key(self.window, glfw.KEY_W) == glfw.PRESS:
            self.camera.position += camera_speed * self.camera.front
        if glfw.get_key(self.window, glfw.KEY_S) == glfw.PRESS:
            self.camera.position -= camera_speed * self.camera.front
        if glfw.get_key(self.window, glfw.KEY_D) == glfw.PRESS:
            self.camera.position += glm.normalize(glm.cross(self.camera.front, self.camera.up)) * camera_speed
        if glfw.get_key(self.window, glfw.KEY_A) == glfw.PRESS:
            self.camera.position -= glm.normalize(glm.cross(self.camera.front, self.camera.up)) * camera_speed
        
        if glfw.get_key(self.window, glfw.KEY_SPACE) == glfw.PRESS:
            self.camera.position += camera_speed * self.camera.up
        if glfw.get_key(self.window, glfw.KEY_LEFT_SHIFT) == glfw.PRESS:
            self.camera.position -= camera_speed * self.camera.up