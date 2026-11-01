import utils


class Entities:
    def __init__(self, name, x, y, frames, tilemap, direction="left"):
        self.name = name
        self.x = x                  
        self.y = y
        self.frames = frames        
        self.tilemap = tilemap      
        self.direction = direction
        self.frame_index = 0        
        self.timer = 0              
        self.frame_duration = 100   

    def update(self, dt):
        
        self.timer += dt
        if self.timer >= self.frame_duration:
            self.timer -= self.frame_duration
            self.frame_index += 1   # image suivante

    def get_image(self):
        frames = self.frames[self.direction]
        local_id = frames[self.frame_index % len(frames)]   
        return self.tilemap.tiles[self.tilemap.sprite_firstgid + local_id]

    def draw(self, surface):
        image = self.get_image()
        rect = image.get_rect(center=(self.x * utils.ZOOM, self.y * utils.ZOOM))
        surface.blit(image, rect)