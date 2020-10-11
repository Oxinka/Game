import pyglet
import player
import wall

window = pyglet.window.Window(width=640, height=360, resizable=True)
player = player.Player(window)
entityList = []
entityList.append(player)
entityList.append(wall.Wall(64, 64))
entityList.append(wall.Wall(64, 128))
entityList.append(wall.Wall(128, 64))
entityList.append(wall.Wall(128, 128))
entityList.append(wall.Wall(256, 128))
entityList.append(wall.Wall(512, 128))
entityList.append(wall.Wall(1024, 128))

pyglet.gl.glClearColor(1, 1, 1, 1)


@window.event
def on_resize(x, y):
    player.resize(x, y)


@window.event
def on_draw():
    window.clear()
    for entity in entityList:
        entity.draw()


def update(dt):
    for entity in entityList:
        entity.update()


pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()


# TODO:
# - Create an entities list, iterate over it when drawing
# - Load a map from an XML file that we design
