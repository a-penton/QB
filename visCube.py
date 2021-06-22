#Class for visual cube, includes clickable arrows
from ursina import *
from ursina.shaders import unlit_shader
from ursina.shaders import lit_with_shadows_shader
from ursina.curve import *

class VisCube(Entity):
    cubes = [] #list of cublets
    arrows = [] #ui buttons
    center = Entity(x=0, y=0, z=0) #central entity, used for rotations
    anim = False
    blinkSeq = Sequence()
    e1 = Entity()
    e2 = Entity()
    e3 = Entity()
    e4 = Entity()
    e5 = Entity()
    e6 = Entity()
    e7 = Entity()
    e8 = Entity()
    e9 = Entity()
    e10 = Entity()
    e11 = Entity()
    e12 = Entity()
    e13 = Entity()
    e14 = Entity()
    e15 = Entity()
    e16 = Entity()
    e17 = Entity()
    e18 = Entity()
    e19 = Entity()
    e20 = Entity()
    e21 = Entity()
    e22 = Entity()
    e23 = Entity()
    e24 = Entity()
    e25 = Entity()
    e26 = Entity()

    def __init__(self):
        super().__init__(
        )
        self.center.reparent_to(self)
        #can delete these, just visual axis
        #xAxis = Entity(model='cube', scale=(6, .1, .1), color=color.red, parent=self)
        #yAxis = Entity(model='cube', scale=(.1, 6, .1), color=color.green, parent=self)
        #zAxis = Entity(model='cube', scale=(.1, .1, 6), color=color.blue, parent=self)
        #frontHead = Entity(model='sphere', position=(0,0,-.5), scale=(2, 2, 0.03333), color=color.blue, parent=zAxis)

        collider = Entity(collider='box', scale=(3, 3, 3), parent=self)

        #=====================================ui arrows=====================================
        arrowE = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=2.1, z=-1.6, rotation=(0,-90,0), parent=self, on_click=Func(self.arrowFunc, self.rotateE), scale=(.5,.5,.5))
        arrowE.on_mouse_enter = Func(setattr, arrowE, 'color', color.rgb(255, 255, 00, 225))
        arrowE.on_mouse_exit = Func(setattr, arrowE, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowE)

        arrowEE = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=-2.1, z=-1.6, rotation=(0, 90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateEE), scale=(.5, .5, .5))
        arrowEE.on_mouse_enter = Func(setattr, arrowEE, 'color', color.rgb(255, 255, 00, 225))
        arrowEE.on_mouse_exit = Func(setattr, arrowEE, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowEE)

        arrowU = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=-2.1, y=1, z=-1.6, rotation=(0, 90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateU), scale=(.5, .5, .5))
        arrowU.on_mouse_enter = Func(setattr, arrowU, 'color', color.rgb(255, 255, 00, 225))
        arrowU.on_mouse_exit = Func(setattr, arrowU, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowU)

        arrowUU = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=2.1, y=1, z=-1.6, rotation=(0, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateUU), scale=(.5, .5, .5))
        arrowUU.on_mouse_enter = Func(setattr, arrowUU, 'color', color.rgb(255, 255, 00, 225))
        arrowUU.on_mouse_exit = Func(setattr, arrowUU, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowUU)

        arrowD = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=2.1,
                        y=-1, z=-1.6, rotation=(0, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateD), scale=(.5, .5, .5))
        arrowD.on_mouse_enter = Func(setattr, arrowD, 'color', color.rgb(255, 255, 00, 225))
        arrowD.on_mouse_exit = Func(setattr, arrowD, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowD)

        arrowDD = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=-2.1,
                         y=-1, z=-1.6, rotation=(0, 90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateDD), scale=(.5, .5, .5))
        arrowDD.on_mouse_enter = Func(setattr, arrowDD, 'color', color.rgb(255, 255, 00, 225))
        arrowDD.on_mouse_exit = Func(setattr, arrowDD, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowDD)

        arrowL = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=-1,
                        y=-2.1, z=-1.6, rotation=(-90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateL),
                        scale=(.5, .5, .5))
        arrowL.on_mouse_enter = Func(setattr, arrowL, 'color', color.rgb(255, 255, 00, 225))
        arrowL.on_mouse_exit = Func(setattr, arrowL, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowL)

        arrowLL = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=-1,
                        y=2.1, z=-1.6, rotation=(90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateLL),
                        scale=(.5, .5, .5))
        arrowLL.on_mouse_enter = Func(setattr, arrowLL, 'color', color.rgb(255, 255, 00, 225))
        arrowLL.on_mouse_exit = Func(setattr, arrowLL, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowLL)

        arrowM = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=0,
                         y=-2.1, z=-1.6, rotation=(-90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateM),
                         scale=(.5, .5, .5))
        arrowM.on_mouse_enter = Func(setattr, arrowM, 'color', color.rgb(255, 255, 00, 225))
        arrowM.on_mouse_exit = Func(setattr, arrowM, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowM)

        arrowMM = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=0,
                        y=2.1, z=-1.6, rotation=(90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateMM),
                        scale=(.5, .5, .5))
        arrowMM.on_mouse_enter = Func(setattr, arrowMM, 'color', color.rgb(255, 255, 00, 225))
        arrowMM.on_mouse_exit = Func(setattr, arrowMM, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowMM)

        arrowR = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1,
                         y=2.1, z=-1.6, rotation=(90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateR),
                         scale=(.5, .5, .5))
        arrowR.on_mouse_enter = Func(setattr, arrowR, 'color', color.rgb(255, 255, 00, 225))
        arrowR.on_mouse_exit = Func(setattr, arrowR, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowR)

        arrowRR = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1,
                        y=-2.1, z=-1.6, rotation=(-90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateRR),
                        scale=(.5, .5, .5))
        arrowRR.on_mouse_enter = Func(setattr, arrowRR, 'color', color.rgb(255, 255, 00, 225))
        arrowRR.on_mouse_exit = Func(setattr, arrowRR, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowRR)

        arrowF = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                         y=-2.1, z=-1, rotation=(-90, -90, 90), parent=self, on_click=Func(self.arrowFunc, self.rotateF),
                         scale=(.5, .5, .5))
        arrowF.on_mouse_enter = Func(setattr, arrowF, 'color', color.rgb(255, 255, 00, 225))
        arrowF.on_mouse_exit = Func(setattr, arrowF, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowF)

        arrowFF = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                        y=2.1, z=-1, rotation=(90, -90, 90), parent=self,
                        on_click=Func(self.arrowFunc, self.rotateFF),
                        scale=(.5, .5, .5))
        arrowFF.on_mouse_enter = Func(setattr, arrowFF, 'color', color.rgb(255, 255, 00, 225))
        arrowFF.on_mouse_exit = Func(setattr, arrowFF, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowFF)

        arrowS = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                         y=-2.1, z=0, rotation=(-90, -90, 90), parent=self,
                         on_click=Func(self.arrowFunc, self.rotateS),
                         scale=(.5, .5, .5))
        arrowS.on_mouse_enter = Func(setattr, arrowS, 'color', color.rgb(255, 255, 00, 225))
        arrowS.on_mouse_exit = Func(setattr, arrowS, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowS)

        arrowSS = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                        y=2.1, z=0, rotation=(90, -90, 90), parent=self,
                        on_click=Func(self.arrowFunc, self.rotateSS),
                        scale=(.5, .5, .5))
        arrowSS.on_mouse_enter = Func(setattr, arrowSS, 'color', color.rgb(255, 255, 00, 225))
        arrowSS.on_mouse_exit = Func(setattr, arrowSS, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowSS)

        arrowB = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                         y=2.1, z=1, rotation=(90, -90, 90), parent=self,
                         on_click=Func(self.arrowFunc, self.rotateB),
                         scale=(.5, .5, .5))
        arrowB.on_mouse_enter = Func(setattr, arrowB, 'color', color.rgb(255, 255, 00, 225))
        arrowB.on_mouse_exit = Func(setattr, arrowB, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowB)

        arrowBB = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                        y=-2.1, z=1, rotation=(-90, -90, 90), parent=self,
                        on_click=Func(self.arrowFunc, self.rotateBB),
                        scale=(.5, .5, .5))
        arrowBB.on_mouse_enter = Func(setattr, arrowBB, 'color', color.rgb(255, 255, 00, 225))
        arrowBB.on_mouse_exit = Func(setattr, arrowBB, 'color', color.rgb(255, 255, 00, 175))
        self.arrows.append(arrowBB)


        #=====================================creation of cublets=====================================

        self.e1 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e2 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e3 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e4 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e5 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e6 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e7 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e8 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.e9 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)

        self.e10 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e11 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e12 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e13 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e14 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e15 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e16 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=0, z=0, world_scale=(1, 1, 1), parent=self)
        self.e17 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e18 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=0, z=1, world_scale=(1, 1, 1), parent=self)
        self.e19 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e20 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=0, z=0, world_scale=(1, 1, 1), parent=self)
        self.e21 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e22 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=0, z=1, world_scale=(1, 1, 1), parent=self)
        self.e23 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e24 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        self.e25 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        self.e26 = Entity(model=load_model(name='cubetest'), color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=-0, z=1, world_scale=(1, 1, 1), parent=self)

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

    def reparentCube(self): #reparent cublets from the center to the main cube
        for e in self.cubes:
            e.reparent_to(self)
        self.center.rotation = (0, 0, 0)

    #==============================================rotations===================================================
    #checks cublets by coordinates, reparents cublets to the center entity, rotates the center entity, reparents cublets to cube
    def rotateF(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateFF(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateUU(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateU(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateE(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateEE(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateD(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateDD(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateS(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateSS(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateB(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateBB(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateL(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateLL(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateR(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateRR(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateM(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateMM(self):
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateX(self):
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateXX(self):
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateY(self):
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateYY(self):
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateZ(self):
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z - 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def rotateZZ(self):
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z + 90, duration=.5)
        invoke(self.reparentCube, delay=.55)

    def blink(self):
        self.blinkSeq.append(Func(self.e1.blink, value=color.black,duration=2))
        self.blinkSeq.append(Func(self.e2.blink, value=color.black, duration=2))
        self.blinkSeq.append(Func(self.e3.blink, value=color.black, duration=2))
        self.blinkSeq.append(Func(self.e4.blink, value=color.black, duration=2))
        self.blinkSeq.append(Func(self.e5.blink, value=color.black, duration=2))

        self.blinkSeq.loop = True
        self.blinkSeq.append(2)
        self.blinkSeq.start()

    def unblink(self):
        self.blinkSeq.kill()
        self.blinkSeq.loop = False
        self.blinkSeq = Sequence()

    def arrowFunc(self,func): #activates when an arrow is clicked, does the passed function, disables arrows during animation
        self.anim = True
        for arrow in self.arrows:
            arrow.enabled = False
        invoke(self.reenableArrows, delay=.6)
        func()

    def reenableArrows(self):
        self.anim = False
        for arrow in self.arrows:
            arrow.enabled = True

    def disableArrows(self):
        for arrow in self.arrows:
            arrow.enabled = False

    def delete(self): #deletes all cubes and arrows, the old coordinates were still lingering and messing with stuff temp fix was moving, should look into later
        for e in self.cubes:
            e.position=(100, 100, 100)
            destroy(e)
        for e in self.arrows:
            e.position=(100, 100, 100)
            destroy(e)
        self.cubes.clear()
        self.arrows.clear()
        self.rotation = (0, 0, 0)
        self.anim = False
        self.center.rotation = (0, 0, 0)
