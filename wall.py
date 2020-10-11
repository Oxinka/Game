import pyglet


class Wall:

    def __init__(self, x, y):
        wimage = pyglet.image.load("wall.png")
        wimage.anchor_x = wimage.width // 2
        wimage.anchor_y = wimage.height // 2
        self.sprite = pyglet.sprite.Sprite(x=x, y=y, img=wimage)
        self.sprite.scale = 4

        rotateBy = 0
        if (x / 64) % 2:
            rotateBy += 180
        if (y / 64) % 2:
            rotateBy += 90

        self.sprite.rotation = rotateBy

    def update(self):
        pass

    def draw(self):
        self.sprite.draw()
