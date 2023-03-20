from ursina import *
import random
import time

app=Ursina(borderless=False)
camera.orthographic=True
camera.fov=20
me = Entity(
    model='quad',
    texture='assets\pl',
    scale=(3,2),
)

skybox_image = load_texture("assets\sky.png")
Sky(texture=skybox_image) 

fly=Entity(
    model='cube',
    texture='assets\\mon',
    collider='box',
    scale=4,
    x=20,
    y=-10
)
flies=[]
def newFly():
    new=duplicate(
        fly,
        y=-5+(5124*time.dt)%15
    )
    flies.append(new)
    invoke(newFly,delay=1)
newFly()

def update():
    me.x -=held_keys['a']*6*time.dt 
    me.x +=held_keys['d']*6*time.dt 
    me.y -=held_keys['s']*6*time.dt 
    me.y +=held_keys['w']*6*time.dt
    b=held_keys['s']*20
    a=held_keys['w']*-20
    if(a!=0):
        me.rotation_z=a
    else:
        me.rotation_z=b
    for fly in flies:
        fly.x-=4*time.dt
        touch=fly.intersects()
        if touch.hit:
            flies.remove(fly)
            destroy(fly)
        #t=me.intersects(fly)
        if me.intersects().hit==True:
            quit()

def input(key):
    if(key=='space'):
        e=Entity(
            y=me.y,
            x=me.x+2,
            model='cube',
            texture='assets\Bul',
            collider='cube'
        )
        e.animate_x(
            30,
            duration=2,
            curve=curve.linear
        )
        invoke(destroy,e,delay=2)

app.run()