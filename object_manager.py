import numpy as np

from object import Object

class ObjectManager:
    def __init__(self):
        self.objects = {}
        self.lightObjects = {}

    def add(self, index, obj):
        self.objects[index] = obj
    
    def add_light(self, index, obj):
        self.lightObjects[index] = obj
    
    def remove(self, index):
        self.objects.pop(index, None)
    
    def remove_light(self, index):
        self.lightObjects.pop(index, None)
    
    def create_object(self, name, index, vertices, indices, ambientTexturePath, specularTexturePath):
        obj = Object(name, vertices, indices)
        obj.set_ambient_texture(ambientTexturePath)
        obj.set_specular_texture(specularTexturePath)

        self.add(index, obj)
    
    def create_light_object(self, name, vertices, indices):
        obj = Object(name, vertices, indices, True)

        return obj
    
    def create_plane(self, index, ambientTexturePath, specularTexturePath):
        plane_vertices = [
            # posição          normal           UV
            [ -0.5, 0.0,  0.5,  0.0, 1.0, 0.0,  0.0, 1.0 ],  # v0
            [  0.5, 0.0,  0.5,  0.0, 1.0, 0.0,  1.0, 1.0 ],  # v1
            [  0.5, 0.0, -0.5,  0.0, 1.0, 0.0,  1.0, 0.0 ],  # v2
            [ -0.5, 0.0, -0.5,  0.0, 1.0, 0.0,  0.0, 0.0 ],  # v3
        ]

        plane_indices = [
            [0, 1, 2],
            [0, 2, 3]
        ]

        self.create_object('Plane', index, plane_vertices, plane_indices, ambientTexturePath, specularTexturePath)

    def create_cube(self, index, ambientTexturePath, specularTexturePath):
        cube_vertices = [
            # Frente (normal: 0,0,1)
            [ -0.5, -0.5,  0.5,   0.0, 0.0, 1.0,   0.0, 0.0 ],
            [  0.5, -0.5,  0.5,   0.0, 0.0, 1.0,   1.0, 0.0 ],
            [  0.5,  0.5,  0.5,   0.0, 0.0, 1.0,   1.0, 1.0 ],
            [ -0.5,  0.5,  0.5,   0.0, 0.0, 1.0,   0.0, 1.0 ],

            # Trás (normal: 0,0,-1)
            [  0.5, -0.5, -0.5,   0.0, 0.0, -1.0,  0.0, 0.0 ],
            [ -0.5, -0.5, -0.5,   0.0, 0.0, -1.0,  1.0, 0.0 ],
            [ -0.5,  0.5, -0.5,   0.0, 0.0, -1.0,  1.0, 1.0 ],
            [  0.5,  0.5, -0.5,   0.0, 0.0, -1.0,  0.0, 1.0 ],

            # Direita (normal: 1,0,0)
            [  0.5, -0.5,  0.5,   1.0, 0.0, 0.0,   0.0, 0.0 ],
            [  0.5, -0.5, -0.5,   1.0, 0.0, 0.0,   1.0, 0.0 ],
            [  0.5,  0.5, -0.5,   1.0, 0.0, 0.0,   1.0, 1.0 ],
            [  0.5,  0.5,  0.5,   1.0, 0.0, 0.0,   0.0, 1.0 ],

            # Esquerda (normal: -1,0,0)
            [ -0.5, -0.5, -0.5,  -1.0, 0.0, 0.0,   0.0, 0.0 ],
            [ -0.5, -0.5,  0.5,  -1.0, 0.0, 0.0,   1.0, 0.0 ],
            [ -0.5,  0.5,  0.5,  -1.0, 0.0, 0.0,   1.0, 1.0 ],
            [ -0.5,  0.5, -0.5,  -1.0, 0.0, 0.0,   0.0, 1.0 ],

            # Topo (normal: 0,1,0)
            [ -0.5,  0.5,  0.5,   0.0, 1.0, 0.0,   0.0, 0.0 ],
            [  0.5,  0.5,  0.5,   0.0, 1.0, 0.0,   1.0, 0.0 ],
            [  0.5,  0.5, -0.5,   0.0, 1.0, 0.0,   1.0, 1.0 ],
            [ -0.5,  0.5, -0.5,   0.0, 1.0, 0.0,   0.0, 1.0 ],

            # Base (normal: 0,-1,0)
            [ -0.5, -0.5, -0.5,   0.0, -1.0, 0.0,  0.0, 0.0 ],
            [  0.5, -0.5, -0.5,   0.0, -1.0, 0.0,  1.0, 0.0 ],
            [  0.5, -0.5,  0.5,   0.0, -1.0, 0.0,  1.0, 1.0 ],
            [ -0.5, -0.5,  0.5,   0.0, -1.0, 0.0,  0.0, 1.0 ],
        ]

        cube_indices = [
            # Frente
            [ 0, 1, 2 ], [ 0, 2, 3 ],
            # Trás
            [ 4, 5, 6 ], [ 4, 6, 7 ],
            # Direita
            [ 8, 9,10 ], [ 8,10,11 ],
            # Esquerda
            [12,13,14 ], [12,14,15 ],
            # Topo
            [16,17,18 ], [16,18,19 ],
            # Base
            [20,21,22 ], [20,22,23 ]
        ]

        self.create_object('Cube', index, cube_vertices, cube_indices, ambientTexturePath, specularTexturePath)

    def create_light_cube(self):
        cube_vertices = [
            # Frente
            [ -0.5, -0.5,  0.5 ],
            [  0.5, -0.5,  0.5 ],
            [  0.5,  0.5,  0.5 ],
            [ -0.5,  0.5,  0.5 ],

            # Trás
            [  0.5, -0.5, -0.5 ],
            [ -0.5, -0.5, -0.5 ],
            [ -0.5,  0.5, -0.5 ],
            [  0.5,  0.5, -0.5 ],

            # Direita
            [  0.5, -0.5,  0.5 ],
            [  0.5, -0.5, -0.5 ],
            [  0.5,  0.5, -0.5 ],
            [  0.5,  0.5,  0.5 ],

            # Esquerda
            [ -0.5, -0.5, -0.5 ],
            [ -0.5, -0.5,  0.5 ],
            [ -0.5,  0.5,  0.5 ],
            [ -0.5,  0.5, -0.5 ],

            # Topo
            [ -0.5,  0.5,  0.5 ],
            [  0.5,  0.5,  0.5 ],
            [  0.5,  0.5, -0.5 ],
            [ -0.5,  0.5, -0.5 ],

            # Base
            [ -0.5, -0.5, -0.5 ],
            [  0.5, -0.5, -0.5 ],
            [  0.5, -0.5,  0.5 ],
            [ -0.5, -0.5,  0.5 ],
        ]

        cube_indices = [
            # Frente
            [ 0, 1, 2 ], [ 0, 2, 3 ],
            # Trás
            [ 4, 5, 6 ], [ 4, 6, 7 ],
            # Direita
            [ 8, 9,10 ], [ 8,10,11 ],
            # Esquerda
            [12,13,14 ], [12,14,15 ],
            # Topo
            [16,17,18 ], [16,18,19 ],
            # Base
            [20,21,22 ], [20,22,23 ]
        ]

        return self.create_light_object('LightSource', cube_vertices, cube_indices)
    
    def get_object(self, index):
        if index not in self.objects:
            raise ValueError(f"Objeto '{index}' não encontrado.")

        return self.objects[index]

    def get_object_list_length(self):
        return len(self.objects)

    def get_light_object(self, index):
        if index not in self.lightObjects:
            raise ValueError(f"Luz '{index}' não encontrado.")

        return self.lightObjects[index]

    def get_light_object_list_length(self):
        return len(self.lightObjects)

    def render_all(self):
        for obj in self.objects.values():
            obj.render()
    
    def render_all_light(self):
        for obj in self.lightObjects.values():
            obj.render()
    
    def cleanup(self):
        for obj in self.objects.values():
            obj.cleanup()
        
        for obj in self.lightObjects.values():
            obj.cleanup()
