import glfw

from OpenGL.GL import *
from pyglm import glm

import numpy as np

from light_manager import LightManager

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
            glm.vec3(  0.0,  -0.5,  0.0  )
        ]

        self.lightPositions = [
            glm.vec3(  0.0,  4.0,  0.0  ),
            glm.vec3(  2.0,  0.0,  0.0  )
        ]

        for i in range(len(self.positions)):
            self.objectManager.create_cube(i, 'assets/images/bricks_color.jpg', 'assets/images/bricks_specular.jpg')
        
        self.lightManager = LightManager(self.shader, self.objectManager)
        
        # for i in range(len(self.lightPositions)):
        #     self.lightManager.create_point_light(i)


    # Roda a cada frame da aplicação
    def update(self):
        self.update_delta_time()
        self.input_update()

        self.shader.use()
        
        self.shader.set_vec3_uniform('lightColor', glm.vec3(1.0))
        self.shader.set_float_uniform('material.shininess', 8.0)

        # for i in range(len(self.lightManager.point_lights)):
        #     self.lightManager.set_point_light_parameters('pointLight[' + str(i) + ']', self.lightPositions[i])
        
        self.lightManager.set_directional_light_parameters(glm.vec3(-0.2, -1.0, -0.3))

        for i in range(self.objectManager.get_object_list_length()):
            obj = self.objectManager.get_object(i)
            obj.set_position(self.positions[i])
            obj.set_rotation(glm.vec3(0.0, 0.0, 1.0), 0)
            obj.set_scale(glm.vec3(1.0, 1.0, 1.0))
            obj.create_object_material(self.shader, obj.ambientTextureIndex, obj.specularTextureIndex, 8.0)
            obj.create_model_matrix(self.shader)

            obj.render()

        self.camera.update(45, self.window.WIDTH, self.window.HEIGHT, 0.1, 100.0)
        self.camera.send_to_shader(self.shader)

        self.lightManager.render(self.camera, self.lightPositions)
    
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
        self.lightManager.lightShader.cleanup()
        self.objectManager.cleanup()