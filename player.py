import pyglet


class Player:
    SCALE = 4
    SPEED = 10

    def __init__(self, window):
        image = pyglet.image.load("player.png")

        self.sprite = pyglet.sprite.Sprite(
            x=window.width / 2 - image.width * self.SCALE / 2,
            y=window.height / 2 - image.height * self.SCALE / 2,
            img=image
        )
        self.sprite.scale = self.SCALE
        self.keys = pyglet.window.key.KeyStateHandler()
        window.push_handlers(self.keys)

    def update(self):
        if self.keys[pyglet.window.key.A]:
            self.sprite.x -= self.SPEED
        if self.keys[pyglet.window.key.D]:
            self.sprite.x += self.SPEED
        if self.keys[pyglet.window.key.W]:
            self.sprite.y += self.SPEED
        if self.keys[pyglet.window.key.S]:
            self.sprite.y -= self.SPEED

    def resize(self, x, y):
        self.sprite.x = x / 2 - self.sprite.width / 2
        self.sprite.y = y / 2 - self.sprite.height / 2

    def draw(self):
        self.sprite.draw()
