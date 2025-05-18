from pyglm import glm

from object_manager import ObjectManager
from object import Object
from shader import Shader
from camera import Camera

class LightManager:
    def __init__(self, shader : Shader, objectManager: ObjectManager):
        self.objectManager = objectManager
        self.shader = shader
        self.lightShader = Shader('assets/shaders/light.vert', 'assets/shaders/light.frag')

        self.point_lights = {}
        self.spot_lights = {}
    
    def create_point_light(self, obj_index : int):
        obj = self.objectManager.create_light_cube()

        self.point_lights[obj_index] = obj
    
    def get_point_light(self, obj_index : int):
        return self.point_lights.get(obj_index)
    
    def set_directional_light_parameters(self, direction, 
                                         ambient=glm.vec3(0.05), diffuse=glm.vec3(0.8), specular=glm.vec3(1.0)):
        self.shader.set_vec3_uniform('directionalLight.direction', direction)
        self.shader.set_vec3_uniform('directionalLight.ambient', ambient)
        self.shader.set_vec3_uniform('directionalLight.diffuse', diffuse)
        self.shader.set_vec3_uniform('directionalLight.specular', specular)

    def set_point_light_obj_parameters(self, obj: Object,
                                       position=glm.vec3(0.0), 
                                       rotation=0.0, rotation_axis=glm.vec3(1.0, 0.0, 0.0), 
                                       scale=glm.vec3(0.1)):
        obj.set_position(position)
        obj.set_rotation(rotation_axis, rotation)
        obj.set_scale(scale)
        obj.create_model_matrix(self.lightShader)


    def set_point_light_parameters(self, name, position, 
                                   ambient=glm.vec3(0.05), diffuse=glm.vec3(0.8), specular=glm.vec3(1.0), 
                                   constant=1.0, linear=0.09, quadratic=0.032):
        self.shader.set_vec3_uniform(name + '.position', position)
        self.shader.set_vec3_uniform(name + '.ambient', ambient)
        self.shader.set_vec3_uniform(name + '.diffuse', diffuse)
        self.shader.set_vec3_uniform(name + '.specular', specular)
        
        self.shader.set_float_uniform(name + '.constant', constant)
        self.shader.set_float_uniform(name + '.linear', linear)
        self.shader.set_float_uniform(name + '.quadratic', quadratic)

    def render(self, camera: Camera, positions):
        self.lightShader.use()

        for i in range(len(self.point_lights)):
            point = self.point_lights[i]

            self.set_point_light_obj_parameters(point, positions[i])
            point.render()
        
        camera.send_to_shader(self.lightShader)