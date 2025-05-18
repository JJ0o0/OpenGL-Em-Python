from pyglm import glm

class Camera:
    def __init__(self, width, height):
        self.position = glm.vec3(0.0, 0.0, 3.0)
        self.front = glm.vec3(0.0, 0.0, -1.0)
        self.up = glm.vec3(0.0, 1.0, 0.0)
        self.target = glm.vec3(0.0, 0.0, 0.0)

        self.yaw = -90.0
        self.pitch = 0.0

        self.first_mouse = True

        self.lastX = width / 2
        self.lastY = height / 2
    
    def update(self, fov, width, height, nearPlane, farPlane):
        self.create_view_matrix()
        self.create_projection_matrix(fov, width, height, nearPlane, farPlane)

    def camera_look(self, xpos, ypos, sensivity=0.1):
        if self.first_mouse:
            self.lastX = xpos
            self.lastY = ypos

            self.first_mouse = False
        
        xOffset = xpos - self.lastX
        yOffset = self.lastY - ypos
        self.lastX = xpos
        self.lastY = ypos

        xOffset *= sensivity
        yOffset *= sensivity

        self.yaw += xOffset
        self.pitch += yOffset

        self.pitch = max(-89.0, min(89.0, self.pitch))
        
        direction = glm.vec3(
            glm.cos(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch)), 
            glm.sin(glm.radians(self.pitch)),
            glm.sin(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch))
        )

        self.front = glm.normalize(direction)

    def set_camera_position(self, value):
        self.position = value

    def create_view_matrix(self):
        self.view = glm.mat4(1.0)
        self.view = glm.lookAt(self.position, self.position + self.front, self.up)
    
    def create_projection_matrix(self, fov, width, height, nearPlane, farPlane):
        self.projection = glm.mat4(1.0)
        self.projection = glm.perspective(glm.radians(fov), width / height, nearPlane, farPlane)

    def get_direction(self):
        return glm.normalize(self.position - self.target)

    def get_up(self):
        return glm.normalize(glm.cross(self.get_direction(), self.get_right()))

    def get_right(self):
        return glm.normalize(glm.cross(self.up, self.get_direction()))

    def send_to_shader(self, shader):
        shader.set_matrix4_uniform('view', self.view)
        shader.set_matrix4_uniform('projection', self.projection)