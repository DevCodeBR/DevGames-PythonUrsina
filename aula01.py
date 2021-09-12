from ursina import *
app = Ursina()

Quadrado = Entity(model='quad', color=color.orange, texture='brick', scale=(2, 2, 2))
#Quadrado.rotation_x = 45

app.run()