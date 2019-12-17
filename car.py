from pygame.math import Vector2

class car:
    def __init__(self, x=0, y=0, angle=0.0, length=5, width=2, max_steering=30.0, max_acceleration=5.0):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.width = width
        self.max_acceleration = max_acceleration
        self.max_steering_angle = max_steering
        self.acceleration = 0.0
        self.steering_angle = 0.0

    def update(self, secondsSinceLastFrame):
        self.velocity += (self.acceleration * secondsSinceLastFrame, 0)