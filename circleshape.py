import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def is_collide(self, other):
        return ( self.position.distance_to(other.position)
            <= (self.radius + other.radius) )
    
    def is_outside(self, screen):
        return (
            (self.position.x - self.radius) > screen.get_width()
            or (self.position.x + self.radius) < 0
            or (self.position.y - self.radius) > screen.get_height()
            or (self.position.y + self.radius) < 0
        )

    def is_inside(self, screen):
        return (
            (self.position.x + self.radius) <= screen.get_width()
            and (self.position.x - self.radius) >= 0
            and (self.position.y + self.radius) <= screen.get_height()
            and (self.position.y - self.radius) >= 0
        )
