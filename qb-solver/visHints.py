#Cube used for hints, not very developed at the moment

from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import basic_lighting_shader
from ursina.shaders import unlit_shader

class VisHints(Entity):
    anim = False
    cubes = []
    center = Entity(x=0, y=0, z=0)

    e1=Entity()
    e2=Entity()
    e3=Entity()
    e4=Entity()
    e5=Entity()
    e6=Entity()
    e7=Entity()
    e8=Entity()
    e9=Entity()
    e10=Entity()
    e11=Entity()
    e12=Entity()
    e13=Entity()
    e14=Entity()
    e15=Entity()
    e16=Entity()
    e17=Entity()
    e18=Entity()
    e19=Entity()
    e20=Entity()
    e21=Entity()
    e22=Entity()
    e23=Entity()
    e24=Entity()
    e25=Entity()
    e26=Entity()

    def __init__(self):
        super().__init__(
            scale=(1.1, 1.1, 1.1)
        )
        self.center.reparent_to(self)

        self.e1 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e2 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e3 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e4 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e5 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e6 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e7 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e8 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e9 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e10 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e11 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e12 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e13 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e14 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e15 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e16 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=0, z=0, world_scale=(1, 1, 1), parent=self)
        self.e17 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e18 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=0, z=1, world_scale=(1, 1, 1), parent=self)
        self.e19 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e20 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=0, z=0, world_scale=(1, 1, 1), parent=self)
        self.e21 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e22 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=0, z=1, world_scale=(1, 1, 1), parent=self)
        self.e23 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e24 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e25 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e26 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=-0, z=1, world_scale=(1, 1, 1), parent=self)
        #white cross e10-13 + 4
        self.cubes.append(self.e1)
        self.cubes.append(self.e2)
        self.cubes.append(self.e3)
        self.cubes.append(self.e4)
        self.cubes.append(self.e5)
        self.cubes.append(self.e6)
        self.cubes.append(self.e7)
        self.cubes.append(self.e8)
        self.cubes.append(self.e9)
        self.cubes.append(self.e10)
        self.cubes.append(self.e11)
        self.cubes.append(self.e12)
        self.cubes.append(self.e13)
        self.cubes.append(self.e14)
        self.cubes.append(self.e15)
        self.cubes.append(self.e16)
        self.cubes.append(self.e17)
        self.cubes.append(self.e18)
        self.cubes.append(self.e19)
        self.cubes.append(self.e20)
        self.cubes.append(self.e21)
        self.cubes.append(self.e22)
        self.cubes.append(self.e23)
        self.cubes.append(self.e24)
        self.cubes.append(self.e25)
        self.cubes.append(self.e26)

    def reparentCube(self):
        for e in self.cubes:
            e.reparent_to(self)
        self.center.rotation = (0, 0, 0)

    def recolorCube(self):
        for e in self.cubes:
            e.color=color.rgba(200, 200, 0, 0)
        self.center.rotation = (0, 0, 0)

    def rotateF(self):
        for e in self.cubes:
            if round(e.z) == -1:
                e.reparent_to(self.center)
                e.color=color.rgba(200, 200, 0, 100)
        self.center.animate('rotation_z', self.center.rotation_z + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)
        invoke(self.recolorCube, delay=.75)

    def showWhiteCross(self):
        self.e4.color=color.rgba(200, 200, 0, 100)
        self.e10.color = color.rgba(200, 200, 0, 100)
        self.e11.color = color.rgba(200, 200, 0, 100)
        self.e12.color = color.rgba(200, 200, 0, 100)
        self.e13.color = color.rgba(200, 200, 0, 100)

        #======================================================== unfinished below ==================================================

    def rotateFF(self):
        for e in self.cubes:
            if round(e.z) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateUU(self):
        for e in self.cubes:
            if round(e.y) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateU(self):
        for e in self.cubes:
            if round(e.y) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateE(self):
        for e in self.cubes:
            if round(e.y) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateEE(self):
        for e in self.cubes:
            if round(e.y) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateD(self):
        for e in self.cubes:
            if round(e.y) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateDD(self):
        for e in self.cubes:
            if round(e.y) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateS(self):
        for e in self.cubes:
            if round(e.z) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateSS(self):
        for e in self.cubes:
            if round(e.z) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateB(self):
        for e in self.cubes:
            if round(e.z) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateBB(self):
        for e in self.cubes:
            if round(e.z) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateL(self):
        for e in self.cubes:
            if round(e.x) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateLL(self):
        for e in self.cubes:
            if round(e.x) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateR(self):
        for e in self.cubes:
            if round(e.x) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateRR(self):
        for e in self.cubes:
            if round(e.x) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateM(self):
        for e in self.cubes:
            if round(e.x) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateMM(self):
        for e in self.cubes:
            if round(e.x) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)
