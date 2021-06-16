#Cube used for hints, not very developed at the moment

from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import basic_lighting_shader
from ursina.shaders import unlit_shader

class VisHints(Entity):
    anim = False
    cubes = []
    center = Entity(x=0, y=0, z=0)

    def __init__(self):
        super().__init__(
            scale=(1.1, 1.1, 1.1)
        )
        self.center.reparent_to(self)

        e1 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        e2 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        e3 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        e4 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        e5 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)
        e6 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        e7 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)
        e8 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        e9 = Entity(model='cube', color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)
        e10 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        e11 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        e12 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        e13 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        e14 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        e15 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        e16 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=0, z=0, world_scale=(1, 1, 1), parent=self)
        e17 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        e18 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=0, z=1, world_scale=(1, 1, 1), parent=self)
        e19 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=1, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        e20 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=0, z=0, world_scale=(1, 1, 1), parent=self)
        e21 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        e22 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=0, z=1, world_scale=(1, 1, 1), parent=self)
        e23 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=-1, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        e24 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        e25 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        e26 = Entity(model=load_model(name='cubetest'), color=color.rgba(200, 200, 0, 0), shader=unlit_shader, x=0, y=-0, z=1, world_scale=(1, 1, 1), parent=self)

        self.cubes.append(e1)
        self.cubes.append(e2)
        self.cubes.append(e3)
        self.cubes.append(e4)
        self.cubes.append(e5)
        self.cubes.append(e6)
        self.cubes.append(e7)
        self.cubes.append(e8)
        self.cubes.append(e9)
        self.cubes.append(e10)
        self.cubes.append(e11)
        self.cubes.append(e12)
        self.cubes.append(e13)
        self.cubes.append(e14)
        self.cubes.append(e15)
        self.cubes.append(e16)
        self.cubes.append(e17)
        self.cubes.append(e18)
        self.cubes.append(e19)
        self.cubes.append(e20)
        self.cubes.append(e21)
        self.cubes.append(e22)
        self.cubes.append(e23)
        self.cubes.append(e24)
        self.cubes.append(e25)
        self.cubes.append(e26)

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
