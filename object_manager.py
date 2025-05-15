import numpy as np

from object import Object

class ObjectManager:
    def __init__(self):
        self.objects = {}

    def add(self, index, obj):
        self.objects[index] = obj
    
    def remove(self, index):
        self.objects.pop(index, None)
    
    def create_object(self, name, index, vertices, indices, texturePath, textureIndex):
        obj = Object(name, vertices, indices)
        obj.set_texture(texturePath, textureIndex)

        self.add(index, obj)
    
    def create_cube(self, index, texturePath, textureIndex):
        cube_vertices = [
            # Frente
            [ -0.5, -0.5,  0.5,   0.0, 0.0 ],
            [  0.5, -0.5,  0.5,   1.0, 0.0 ],
            [  0.5,  0.5,  0.5,   1.0, 1.0 ],
            [ -0.5,  0.5,  0.5,   0.0, 1.0 ],

            # Trás
            [  0.5, -0.5, -0.5,   0.0, 0.0 ],
            [ -0.5, -0.5, -0.5,   1.0, 0.0 ],
            [ -0.5,  0.5, -0.5,   1.0, 1.0 ],
            [  0.5,  0.5, -0.5,   0.0, 1.0 ],

            # Direita
            [  0.5, -0.5,  0.5,   0.0, 0.0 ],
            [  0.5, -0.5, -0.5,   1.0, 0.0 ],
            [  0.5,  0.5, -0.5,   1.0, 1.0 ],
            [  0.5,  0.5,  0.5,   0.0, 1.0 ],

            # Esquerda
            [ -0.5, -0.5, -0.5,   0.0, 0.0 ],
            [ -0.5, -0.5,  0.5,   1.0, 0.0 ],
            [ -0.5,  0.5,  0.5,   1.0, 1.0 ],
            [ -0.5,  0.5, -0.5,   0.0, 1.0 ],

            # Topo
            [ -0.5,  0.5,  0.5,   0.0, 0.0 ],
            [  0.5,  0.5,  0.5,   1.0, 0.0 ],
            [  0.5,  0.5, -0.5,   1.0, 1.0 ],
            [ -0.5,  0.5, -0.5,   0.0, 1.0 ],

            # Base
            [ -0.5, -0.5, -0.5,   0.0, 0.0 ],
            [  0.5, -0.5, -0.5,   1.0, 0.0 ],
            [  0.5, -0.5,  0.5,   1.0, 1.0 ],
            [ -0.5, -0.5,  0.5,   0.0, 1.0 ],
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

        self.create_object('Cube', index, cube_vertices, cube_indices, texturePath, textureIndex)
    
    def get_object(self, index):
        if index not in self.objects:
            raise ValueError(f"Objeto '{index}' não encontrado.")

        return self.objects[index]

    def get_object_list_length(self):
        return len(self.objects)

    def render_all(self):
        for obj in self.objects.values():
            obj.render()
    
    def cleanup(self):
        for obj in self.objects.values():
            obj.cleanup()
