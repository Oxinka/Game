import pyglet
import player
import wall

window = pyglet.window.Window(width=640, height=360, resizable=True)
player = player.Player(window)
w1 = wall.Wall(64, 64)
w2 = wall.Wall(64, 128)
w3 = wall.Wall(128, 64)
w4 = wall.Wall(128, 128)
w5 = wall.Wall(256, 128)
w6 = wall.Wall(512, 128)
w7 = wall.Wall(1024, 128)

pyglet.gl.glClearColor(1, 1, 1, 1)


@window.event
def on_resize(x, y):
    player.resize(x, y)


@window.event
def on_draw():
    window.clear()
    w1.draw()
    w2.draw()
    w3.draw()
    w4.draw()
    w5.draw()
    w6.draw()
    w7.draw()
    player.draw()


def update(dt):
    player.update()


pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()


# TODO:
# - Create an entities list, iterate over it when drawing
# - Load a map from an XML file that we design
