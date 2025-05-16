import glfw

from OpenGL.GL import *
from pyglm import glm

class Game: # Sistema pique Unity tlgd

    # Roda no primeiro frame da aplicação
    def start(self, window, shader, camera, objectManager):
        self.objectManager = objectManager
        self.camera = camera
        self.shader = shader
        self.window = window

        self.delta_time = 0.0
        self.last_time = 0.0

        self.positions = [
            glm.vec3(  0.0,  0.0, -5.0  )
        ]

        for i in range(len(self.positions)):
            self.objectManager.create_cube(i, 'assets/images/zam.jpg', GL_TEXTURE0)

    # Roda a cada frame da aplicação
    def update(self):
        self.update_delta_time()
        self.input_update()

        self.shader.use()

        for i in range(self.objectManager.get_object_list_length()):
            obj = self.objectManager.get_object(i)
            obj.set_position(self.positions[i])
            obj.set_rotation(glm.vec3(0.0, 0.0, 1.0), glfw.get_time() * 100)
            obj.create_model_matrix(self.shader)

            obj.render()

        self.camera.update(45, self.window.WIDTH, self.window.HEIGHT, 0.1, 100.0)
        self.camera.send_to_shader(self.shader)
    
    def input_update(self):
        wnd = self.window.window

        if glfw.get_key(wnd, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(wnd, True)
        
        speed = 2.5
    
        if glfw.get_key(wnd, glfw.KEY_LEFT_SHIFT) == glfw.PRESS:
            speed *= 1.5
        elif glfw.get_key(wnd, glfw.KEY_LEFT_SHIFT) == glfw.RELEASE:
            speed /= 1.5

        camera_speed = speed * self.delta_time

        if glfw.get_key(wnd, glfw.KEY_W) == glfw.PRESS:
            self.camera.position += camera_speed * self.camera.front
        if glfw.get_key(wnd, glfw.KEY_S) == glfw.PRESS:
            self.camera.position -= camera_speed * self.camera.front
        if glfw.get_key(wnd, glfw.KEY_D) == glfw.PRESS:
            self.camera.position += glm.normalize(glm.cross(self.camera.front, self.camera.up)) * camera_speed
        if glfw.get_key(wnd, glfw.KEY_A) == glfw.PRESS:
            self.camera.position -= glm.normalize(glm.cross(self.camera.front, self.camera.up)) * camera_speed
        
        if glfw.get_key(wnd, glfw.KEY_SPACE) == glfw.PRESS:
            self.camera.position += camera_speed * self.camera.up
        if glfw.get_key(wnd, glfw.KEY_LEFT_CONTROL) == glfw.PRESS:
            self.camera.position -= camera_speed * self.camera.up
    
    def update_delta_time(self):
        curr_frame = glfw.get_time()
        self.delta_time = curr_frame - self.last_time
        self.last_time = curr_frame
    
    def close(self):
        self.shader.cleanup()
        self.objectManager.cleanup()