from ursina import *
app = Ursina()

skybox = load_texture('img/DaylightBox.png')

cenario = Entity(parent=camera.ui, model='quad', texture=skybox, scale_x=camera.aspect_ratio, z=1)

app.run()