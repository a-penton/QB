#Class for visual cube, includes clickable arrows
from ursina import *
from ursina.shaders import unlit_shader
from ursina.shaders import lit_with_shadows_shader
from ursina.curve import *
from rubik.cube import Cube
import os

#application.asset_folder=Path(os.path.join(application.package_folder.parent), 'qb_solver/')

class VisCube(Entity):
    cubes = [] #list of cublets
    arrows = [] #ui buttons
    notationText = []
    center = Entity(x=0, y=0, z=0) #central entity, used for rotations
    anim = False
    blinkSeq = Sequence()
    turnSpeed = .5
    W = Entity()
    WG = Entity()
    WB = Entity()
    WR = Entity()
    WO = Entity()
    WRG = Entity()
    WGO = Entity()
    WBR = Entity()
    WOB = Entity()
    R = Entity()
    GR = Entity()
    BR = Entity()
    YR = Entity()
    YGR = Entity()
    YRB = Entity()
    G = Entity()
    GO = Entity()
    YG = Entity()
    YOG = Entity()
    B = Entity()
    BO = Entity()
    YB = Entity()
    YBO = Entity()
    O = Entity()
    YO = Entity()
    Y = Entity()

    def __init__(self):
        super().__init__()
        self.virtualCube = Cube("RRRRRRRRRBBBWWWGGGYYYBBBWWWGGGYYYBBBWWWGGGYYYOOOOOOOOO")
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
        textE = Button(color=color.rgba(255,255,255,150), scale=.9, icon='E', rotation=(0,90,0), parent=arrowE, collider=None, enabled = False)
        self.notationText.append(textE)
        self.arrows.append(arrowE)

        arrowEi = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=-2.1, z=-1.6, rotation=(0, 90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateEi), scale=(.5, .5, .5))
        arrowEi.on_mouse_enter = Func(setattr, arrowEi, 'color', color.rgb(255, 255, 00, 225))
        arrowEi.on_mouse_exit = Func(setattr, arrowEi, 'color', color.rgb(255, 255, 00, 175))
        textEi = Button(color=color.rgba(255,255,255,150), scale=.9, icon='Ei', rotation=(0,-90,0), parent=arrowEi, collider=None, enabled = False)
        self.notationText.append(textEi)
        self.arrows.append(arrowEi)

        arrowU = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=-2.1, y=1, z=-1.6, rotation=(0, 90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateU), scale=(.5, .5, .5))
        arrowU.on_mouse_enter = Func(setattr, arrowU, 'color', color.rgb(255, 255, 00, 225))
        arrowU.on_mouse_exit = Func(setattr, arrowU, 'color', color.rgb(255, 255, 00, 175))
        textU = Button(color=color.rgba(255,255,255,150), scale=.9, icon='U', rotation=(0, -90, 0), parent=arrowU, collider=None, enabled = False)
        self.notationText.append(textU)
        self.arrows.append(arrowU)

        arrowUi = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=2.1, y=1, z=-1.6, rotation=(0, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateUi), scale=(.5, .5, .5))
        arrowUi.on_mouse_enter = Func(setattr, arrowUi, 'color', color.rgb(255, 255, 00, 225))
        arrowUi.on_mouse_exit = Func(setattr, arrowUi, 'color', color.rgb(255, 255, 00, 175))
        textUi = Button(color=color.rgba(255,255,255,150), scale=.9, icon='Ui', rotation=(0, 90, 0), parent=arrowUi, collider=None, enabled = False)
        self.notationText.append(textUi)
        self.arrows.append(arrowUi)

        arrowD = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=2.1,
                        y=-1, z=-1.6, rotation=(0, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateD), scale=(.5, .5, .5))
        arrowD.on_mouse_enter = Func(setattr, arrowD, 'color', color.rgb(255, 255, 00, 225))
        arrowD.on_mouse_exit = Func(setattr, arrowD, 'color', color.rgb(255, 255, 00, 175))
        textD = Button(color=color.rgba(255,255,255,150), scale=.9, icon='D', rotation=(0, 90, 0), parent=arrowD, collider=None, enabled = False)
        self.notationText.append(textD)
        self.arrows.append(arrowD)

        arrowDi = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=-2.1,
                         y=-1, z=-1.6, rotation=(0, 90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateDi), scale=(.5, .5, .5))
        arrowDi.on_mouse_enter = Func(setattr, arrowDi, 'color', color.rgb(255, 255, 00, 225))
        arrowDi.on_mouse_exit = Func(setattr, arrowDi, 'color', color.rgb(255, 255, 00, 175))
        textDi = Button(color=color.rgba(255,255,255,150), scale=.9, icon='Di', rotation=(0, -90, 0), parent=arrowDi, collider=None, enabled = False)
        self.notationText.append(textDi)
        self.arrows.append(arrowDi)

        arrowL = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=-1,
                        y=-2.1, z=-1.6, rotation=(-90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateL),
                        scale=(.5, .5, .5))
        arrowL.on_mouse_enter = Func(setattr, arrowL, 'color', color.rgb(255, 255, 00, 225))
        arrowL.on_mouse_exit = Func(setattr, arrowL, 'color', color.rgb(255, 255, 00, 175))
        textL = Button(color=color.rgba(255,255,255,150), scale=.9, icon='L', rotation=(0, 90, -90), parent=arrowL, collider=None, enabled = False)
        self.notationText.append(textL)
        self.arrows.append(arrowL)

        arrowLi = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=-1,
                        y=2.1, z=-1.6, rotation=(90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateLi),
                        scale=(.5, .5, .5))
        arrowLi.on_mouse_enter = Func(setattr, arrowLi, 'color', color.rgb(255, 255, 00, 225))
        arrowLi.on_mouse_exit = Func(setattr, arrowLi, 'color', color.rgb(255, 255, 00, 175))
        textLi = Button(color=color.rgba(255,255,255,150), scale=.9, icon='Li', rotation=(0, 90, 90), parent=arrowLi, collider=None, enabled = False)
        self.notationText.append(textLi)
        self.arrows.append(arrowLi)

        arrowM = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=0,
                         y=-2.1, z=-1.6, rotation=(-90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateM),
                         scale=(.5, .5, .5))
        arrowM.on_mouse_enter = Func(setattr, arrowM, 'color', color.rgb(255, 255, 00, 225))
        arrowM.on_mouse_exit = Func(setattr, arrowM, 'color', color.rgb(255, 255, 00, 175))
        textM = Button(color=color.rgba(255,255,255,150), scale=.9, icon='M', rotation=(0, 90, -90), parent=arrowM, collider=None, enabled = False)
        self.notationText.append(textM)
        self.arrows.append(arrowM)

        arrowMi = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=0,
                        y=2.1, z=-1.6, rotation=(90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateMi),
                        scale=(.5, .5, .5))
        arrowMi.on_mouse_enter = Func(setattr, arrowMi, 'color', color.rgb(255, 255, 00, 225))
        arrowMi.on_mouse_exit = Func(setattr, arrowMi, 'color', color.rgb(255, 255, 00, 175))
        textMi = Button(color=color.rgba(255,255,255,150), scale=.9, icon='Mi', rotation=(0, 90, 90), parent=arrowMi, collider=None, enabled = False)
        self.notationText.append(textMi)
        self.arrows.append(arrowMi)

        arrowR = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1,
                         y=2.1, z=-1.6, rotation=(90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateR),
                         scale=(.5, .5, .5))
        arrowR.on_mouse_enter = Func(setattr, arrowR, 'color', color.rgb(255, 255, 00, 225))
        arrowR.on_mouse_exit = Func(setattr, arrowR, 'color', color.rgb(255, 255, 00, 175))
        textR = Button(color=color.rgba(255,255,255,150), scale=.9, icon='R', rotation=(0, 90, 90), parent=arrowR, collider=None, enabled = False)
        self.notationText.append(textR)
        self.arrows.append(arrowR)

        arrowRi = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1,
                        y=-2.1, z=-1.6, rotation=(-90, -90, 0), parent=self, on_click=Func(self.arrowFunc, self.rotateRi),
                        scale=(.5, .5, .5))
        arrowRi.on_mouse_enter = Func(setattr, arrowRi, 'color', color.rgb(255, 255, 00, 225))
        arrowRi.on_mouse_exit = Func(setattr, arrowRi, 'color', color.rgb(255, 255, 00, 175))
        textRi = Button(color=color.rgba(255,255,255,150), scale=.9, icon='Ri', rotation=(0, 90, -90), parent=arrowRi, collider=None, enabled = False)
        self.notationText.append(textRi)
        self.arrows.append(arrowRi)

        arrowF = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                         y=-2.1, z=-1, rotation=(-90, -90, 90), parent=self, on_click=Func(self.arrowFunc, self.rotateF),
                         scale=(.5, .5, .5))
        arrowF.on_mouse_enter = Func(setattr, arrowF, 'color', color.rgb(255, 255, 00, 225))
        arrowF.on_mouse_exit = Func(setattr, arrowF, 'color', color.rgb(255, 255, 00, 175))
        textF = Button(color=color.rgba(255,255,255,150), scale=.9, icon='F', rotation=(180, -90, 90), parent=arrowF, collider=None, enabled = False)
        self.notationText.append(textF)
        self.arrows.append(arrowF)

        arrowFi = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                        y=2.1, z=-1, rotation=(90, -90, 90), parent=self,
                        on_click=Func(self.arrowFunc, self.rotateFi),
                        scale=(.5, .5, .5))
        arrowFi.on_mouse_enter = Func(setattr, arrowFi, 'color', color.rgb(255, 255, 00, 225))
        arrowFi.on_mouse_exit = Func(setattr, arrowFi, 'color', color.rgb(255, 255, 00, 175))
        textFi = Button(color=color.rgba(255,255,255,150), scale=.9, icon='Fi', rotation=(180, 90, 90), parent=arrowFi, collider=None, enabled = False)
        self.notationText.append(textFi)
        self.arrows.append(arrowFi)

        arrowS = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                         y=-2.1, z=0, rotation=(-90, -90, 90), parent=self,
                         on_click=Func(self.arrowFunc, self.rotateS),
                         scale=(.5, .5, .5))
        arrowS.on_mouse_enter = Func(setattr, arrowS, 'color', color.rgb(255, 255, 00, 225))
        arrowS.on_mouse_exit = Func(setattr, arrowS, 'color', color.rgb(255, 255, 00, 175))
        textS = Button(color=color.rgba(255,255,255,150), scale=.9, icon='S', rotation=(180, -90, 90), parent=arrowS, collider=None, enabled = False)
        self.notationText.append(textS)
        self.arrows.append(arrowS)

        arrowSi = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                        y=2.1, z=0, rotation=(90, -90, 90), parent=self,
                        on_click=Func(self.arrowFunc, self.rotateSi),
                        scale=(.5, .5, .5))
        arrowSi.on_mouse_enter = Func(setattr, arrowSi, 'color', color.rgb(255, 255, 00, 225))
        arrowSi.on_mouse_exit = Func(setattr, arrowSi, 'color', color.rgb(255, 255, 00, 175))
        textSi = Button(color=color.rgba(255,255,255,150), scale=.9, icon='Si', rotation=(180, 90, 90), parent=arrowSi, collider=None, enabled = False)
        self.notationText.append(textSi)
        self.arrows.append(arrowSi)

        arrowB = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                         y=2.1, z=1, rotation=(90, -90, 90), parent=self,
                         on_click=Func(self.arrowFunc, self.rotateB),
                         scale=(.5, .5, .5))
        arrowB.on_mouse_enter = Func(setattr, arrowB, 'color', color.rgb(255, 255, 00, 225))
        arrowB.on_mouse_exit = Func(setattr, arrowB, 'color', color.rgb(255, 255, 00, 175))
        textB = Button(color=color.rgba(255,255,255,150), scale=.9, icon='B', rotation=(180, 90, 90), parent=arrowB, collider=None, enabled = False)
        self.notationText.append(textB)
        self.arrows.append(arrowB)

        arrowBi = Entity(model='Arrow', color=color.rgb(255, 255, 00, 175), collider='box', shader=unlit_shader, x=1.6,
                        y=-2.1, z=1, rotation=(-90, -90, 90), parent=self,
                        on_click=Func(self.arrowFunc, self.rotateBi),
                        scale=(.5, .5, .5))
        arrowBi.on_mouse_enter = Func(setattr, arrowBi, 'color', color.rgb(255, 255, 00, 225))
        arrowBi.on_mouse_exit = Func(setattr, arrowBi, 'color', color.rgb(255, 255, 00, 175))
        textBi = Button(color=color.rgba(255,255,255,150), scale=.9, icon='Bi', rotation=(180, -90, 90), parent=arrowBi, collider=None, enabled = False)
        self.notationText.append(textBi)
        self.arrows.append(arrowBi)


        #=====================================creation of cublets=====================================

        self.W = Entity(model='W', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        self.WG = Entity(model='WG', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        self.WB = Entity(model='WB', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=0, z=-1, world_scale=(1, 1, 1), parent=self)
        self.WR = Entity(model='WR', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.WO = Entity(model='WO', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.WRG = Entity(model='WRG', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.WGO = Entity(model='WGO', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.WBR = Entity(model='WBR', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=1, z=-1, world_scale=(1, 1, 1), parent=self)
        self.WOB = Entity(model='WOB', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=-1, z=-1, world_scale=(1, 1, 1), parent=self)

        self.R = Entity(model='R', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        self.GR = Entity(model='GR', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        self.BR = Entity(model='BR', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=1, z=0, world_scale=(1, 1, 1), parent=self)
        self.YR = Entity(model='YR', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        self.YGR = Entity(model='YGR', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        self.YRB = Entity(model='YRB', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=1, z=1, world_scale=(1, 1, 1), parent=self)
        self.G = Entity(model='G', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=0, z=0, world_scale=(1, 1, 1), parent=self)
        self.GO = Entity(model='GO', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        self.YG = Entity(model='YG', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=0, z=1, world_scale=(1, 1, 1), parent=self)
        self.YOG = Entity(model='YOG', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=1, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        self.B = Entity(model='B', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=0, z=0, world_scale=(1, 1, 1), parent=self)
        self.BO = Entity(model='BO', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        self.YB = Entity(model='YB', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=0, z=1, world_scale=(1, 1, 1), parent=self)
        self.YBO = Entity(model='YBO', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=-1, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        self.O = Entity(model='O', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=-1, z=0, world_scale=(1, 1, 1), parent=self)
        self.YO = Entity(model='YO', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=-1, z=1, world_scale=(1, 1, 1), parent=self)
        self.Y = Entity(model='Y', color=color.rgb(200, 200, 200, 255), texture="RubiksTex", shader=lit_with_shadows_shader, x=0, y=0, z=1, world_scale=(1, 1, 1), parent=self)

        self.cubes.append(self.W)
        self.cubes.append(self.WG)
        self.cubes.append(self.WB)
        self.cubes.append(self.WR)
        self.cubes.append(self.WO)
        self.cubes.append(self.WRG)
        self.cubes.append(self.WGO)
        self.cubes.append(self.WBR)
        self.cubes.append(self.WOB)
        self.cubes.append(self.R)
        self.cubes.append(self.GR)
        self.cubes.append(self.BR)
        self.cubes.append(self.YR)
        self.cubes.append(self.YGR)
        self.cubes.append(self.YRB)
        self.cubes.append(self.G)
        self.cubes.append(self.GO)
        self.cubes.append(self.YG)
        self.cubes.append(self.YOG)
        self.cubes.append(self.B)
        self.cubes.append(self.BO)
        self.cubes.append(self.YB)
        self.cubes.append(self.YBO)
        self.cubes.append(self.O)
        self.cubes.append(self.YO)
        self.cubes.append(self.Y)

    def reparentCube(self): #reparent cublets from the center to the main cube
        for e in self.cubes:
            e.reparent_to(self)
        self.center.rotation = (0, 0, 0)

    #==============================================rotations===================================================
    #checks cublets by coordinates, reparents cublets to the center entity, rotates the center entity, reparents cublets to cube
    def rotateF(self):
        self.virtualCube.F()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z + 90, duration=self.turnSpeed, time_step=time.dt) #resolution=Func(self.reparentCube))

    def rotateFi(self):
        self.virtualCube.Fi()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z - 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateU(self):
        self.virtualCube.U()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y + 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateUi(self):
        self.virtualCube.Ui()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y - 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateE(self):
        self.virtualCube.E()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y - 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateEi(self):
        self.virtualCube.Ei()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y + 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateD(self):
        self.virtualCube.D()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y - 90, duration=self.turnSpeed, time_step=time.dt)
    def rotateDi(self):
        self.virtualCube.Di()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.y) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y + 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateS(self):
        self.virtualCube.S()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z + 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateSi(self):
        self.virtualCube.Si()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z - 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateB(self):
        self.virtualCube.B()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z - 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateBi(self):
        self.virtualCube.Bi()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.z) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z + 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateL(self):
        self.virtualCube.L()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x - 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateLi(self):
        self.virtualCube.Li()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == -1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x + 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateR(self):
        self.virtualCube.R()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x + 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateRi(self):
        self.virtualCube.Ri()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == 1:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x - 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateM(self):
        self.virtualCube.M()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x - 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateMi(self):
        self.virtualCube.Mi()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self)
            if round(e.x) == 0:
                e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x + 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateX(self):
        self.virtualCube.X()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x + 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateXi(self):
        self.virtualCube.Xi()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_x', self.center.rotation_x - 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateY(self):
        self.virtualCube.Y()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y + 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateYi(self):
        self.virtualCube.Yi()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_y', self.center.rotation_y - 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateZ(self):
        self.virtualCube.Z()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z + 90, duration=self.turnSpeed, time_step=time.dt)

    def rotateZi(self):
        self.virtualCube.Zi()
        self.reparentCube()
        for e in self.cubes:
            e.reparent_to(self.center)
        self.center.animate('rotation_z', self.center.rotation_z - 90, duration=self.turnSpeed, time_step=time.dt)

    def blink(self, current_piece):

        if current_piece == None:
            return
        #print(current_piece.colors) #for testing
        if "R" in current_piece.colors: # does top layer
            if "W" in current_piece.colors:
                if "B" in current_piece.colors:
                    self.startBlink(self.WBR)
                    return
                if "G" in current_piece.colors:
                    self.startBlink(self.WRG)
                    return
                self.startBlink(self.WR)
                return
            if "G" in current_piece.colors:
                if "Y" in current_piece.colors:
                    self.startBlink(self.YGR)
                    return
                self.startBlink(self.GR)
                return
            if "B" in current_piece.colors:
                if "Y" in current_piece.colors:
                    self.startBlink(self.YRB)
                    return
                self.startBlink(self.BR)
                return
            if "Y" in current_piece.colors:
                self.startBlink(self.YR)
                return
            self.startBlink(self.R)
            return
        if "O" in current_piece.colors: #does bottom layer
            if "W" in current_piece.colors:
                if "B" in current_piece.colors:
                    self.startBlink(self.WOB)
                    return
                if "G" in current_piece.colors:
                    self.startBlink(self.WGO)
                    return
                self.startBlink(self.WO)
                return
            if "G" in current_piece.colors:
                if "Y" in current_piece.colors:
                    self.startBlink(self.YOG)
                    return
                self.startBlink(self.GO)
                return
            if "B" in current_piece.colors:
                if "Y" in current_piece.colors:
                    self.startBlink(self.YBO)
                    return
                self.startBlink(self.BO)
                return
            if "Y" in current_piece.colors:
                self.startBlink(self.YO)
                return
            self.startBlink(self.O)
            return
        #middle front layer====
        if "W" in current_piece.colors:
            if "B" in current_piece.colors:
                self.startBlink(self.WB)
                return
            if "G" in current_piece.colors:
                self.startBlink(self.WG)
                return
            self.startBlink(self.W)
            return
        #middle back layer====
        if "Y" in current_piece.colors:
            if "B" in current_piece.colors:
                self.startBlink(self.YB)
                return
            if "G" in current_piece.colors:
                self.startBlink(self.YG)
                return
            self.startBlink(self.Y)
            return
        #remaining two centers====
        if "B" in current_piece.colors:
            self.startBlink(self.B)
            return
        if "G" in current_piece.colors:
            self.startBlink(self.G)
            return


    def startBlink(self, piece):
        self.blinkSeq.append(Func(piece.blink, value=color.black, duration=2))
        self.blinkSeq.loop = True
        self.blinkSeq.append(2.1)
        self.blinkSeq.start()

    def unblink(self):
        self.blinkSeq.loop = False
        self.blinkSeq.finish()
        self.blinkSeq.pause()
        self.blinkSeq.kill()
        self.blinkSeq = Sequence()
        for e in self.cubes:
            e.color = color.rgb(200, 200, 200, 255)

    def arrowFunc(self,func): #activates when an arrow is clicked, does the passed function, disables arrows during animation
        self.anim = True
        for arrow in self.arrows:
            arrow.enabled = False
        s = Sequence(
            Func(func),
            self.turnSpeed + .2,
            Func(self.reenableArrows),
            Func(self.assertVirtualCube),
            Loop = False
        )
        s.start()
        #invoke(self.reenableArrows, delay=self.turnSpeed+.2)
        #func()
        #invoke(self.assertVirtualCube, delay=self.turnSpeed+.15)

    def emptyArrowFunc(self):
        self.anim = True
        for arrow in self.arrows:
            arrow.enabled = False
        invoke(self.reenableArrows, delay=self.turnSpeed+.2)

    def reenableArrows(self):
        self.anim = False
        for arrow in self.arrows:
            arrow.enabled = True

    def disableArrows(self):
        for arrow in self.arrows:
            arrow.enabled = False

    def setTurnSpeed(self, t):
        self.turnSpeed = t

    def toggleNotation(self):
        if self.notationText[0].enabled:
            for e in self.notationText:
                e.enabled = False
        else:
            for e in self.notationText:
                e.enabled = True

    def assertVirtualCube(self):
        self.reparentCube()
        for i in range(26):
            current_piece = self.virtualCube.pieces[i]
            if "R" in current_piece.colors:  # does top layer
                if "W" in current_piece.colors:
                    if "B" in current_piece.colors:
                        self.WBR.x = current_piece.pos[0]
                        self.WBR.y = current_piece.pos[1]
                        self.WBR.z = current_piece.pos[2] * -1
                        if current_piece.pos[2] == 1:
                            if current_piece.colors[2] == 'W':
                                self.WBR.rotation_x = 0
                                self.WBR.rotation_y = 0
                                if current_piece.colors[0] == 'B':
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_z = 0
                                    else:
                                        self.WBR.rotation_z = 180
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_z = 90
                                    else:
                                        self.WBR.rotation_z = -90
                            elif current_piece.colors[2] == 'R':
                                self.WBR.rotation_x = 0
                                self.WBR.rotation_y = 90
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_y = 90
                                        self.WBR.rotation_z = 90
                                    else:
                                        self.WBR.rotation_y = -90
                                        self.WBR.rotation_z = -90
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_x = 90
                                        self.WBR.rotation_y = 0
                                        self.WBR.rotation_z = 180
                                    else:
                                        self.WBR.rotation_x = -90
                                        self.WBR.rotation_y = 0
                                        self.WBR.rotation_z = 0
                            elif current_piece.colors[2] == 'B':
                                self.WBR.rotation_y = -90
                                self.WBR.rotation_z = 0
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_x = 0
                                    else:
                                        self.WBR.rotation_x = 180
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_x = 90
                                    else:
                                        self.WBR.rotation_x = -90
                        elif current_piece.pos[2] == -1:
                            if current_piece.colors[2] == 'W':
                                self.WBR.rotation_x = 0
                                self.WBR.rotation_y = 180
                                if current_piece.colors[0] == 'B':
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_z = 0
                                    else:
                                        self.WBR.rotation_z = 180
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_z = 90
                                    else:
                                        self.WBR.rotation_z = -90
                            elif current_piece.colors[2] == 'R':
                                self.WBR.rotation_x = 0
                                self.WBR.rotation_y = -90
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_y = -90
                                        self.WBR.rotation_z = 90
                                    else:
                                        self.WBR.rotation_y = 90
                                        self.WBR.rotation_z = -90
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_x = 90
                                        self.WBR.rotation_y = 180
                                        self.WBR.rotation_z = 180
                                    else:
                                        self.WBR.rotation_x = -90
                                        self.WBR.rotation_y = 180
                                        self.WBR.rotation_z = 0
                            elif current_piece.colors[2] == 'B':
                                self.WBR.rotation_y = 90
                                self.WBR.rotation_z = 0
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_x = 0
                                    else:
                                        self.WBR.rotation_x = 180
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WBR.rotation_x = 90
                                    else:
                                        self.WBR.rotation_x = -90
                        continue
                    if "G" in current_piece.colors:
                        self.WRG.x = current_piece.pos[0]
                        self.WRG.y = current_piece.pos[1]
                        self.WRG.z = current_piece.pos[2] * -1

                        if current_piece.pos[2] == 1:
                            if current_piece.colors[2] == 'W':
                                self.WRG.rotation_x = 0
                                self.WRG.rotation_y = 0
                                if current_piece.colors[0] == 'G':
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_z = 0
                                    else:
                                        self.WRG.rotation_z = 180
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_z = -90
                                    else:
                                        self.WRG.rotation_z = 90
                            elif current_piece.colors[2] == 'R':

                                self.WRG.rotation_x = 0
                                self.WRG.rotation_y = 90
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_y = -90
                                        self.WRG.rotation_z = -90
                                    else:
                                        self.WRG.rotation_z = 90
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_x = 90
                                        self.WRG.rotation_y = 0
                                        self.WRG.rotation_z = 180
                                    else:
                                        self.WRG.rotation_x = -90
                                        self.WRG.rotation_y = 0
                                        self.WRG.rotation_z = 0

                            elif current_piece.colors[2] == 'G':
                                self.WRG.rotation_y = 90
                                self.WRG.rotation_z = 0
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_x = 0
                                    else:
                                        self.WRG.rotation_x = 180
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_x = 90
                                    else:
                                        self.WRG.rotation_x = -90
                        elif current_piece.pos[2] == -1:
                            if current_piece.colors[2] == 'W':
                                self.WRG.rotation_x = 0
                                self.WRG.rotation_y = 180
                                if current_piece.colors[0] == 'G':
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_z = 0
                                    else:
                                        self.WRG.rotation_z = 180
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_z = -90
                                    else:
                                        self.WRG.rotation_z = 90
                            elif current_piece.colors[2] == 'R':
                                self.WRG.rotation_x = 0
                                self.WRG.rotation_y = -90
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_y = 90
                                        self.WRG.rotation_z = -90
                                    else:
                                        self.WRG.rotation_z = 90
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_x = 90
                                        self.WRG.rotation_y = 180
                                        self.WRG.rotation_z = 180
                                    else:
                                        self.WRG.rotation_x = -90
                                        self.WRG.rotation_y = 180
                                        self.WRG.rotation_z = 0
                            elif current_piece.colors[2] == 'G':
                                self.WRG.rotation_y = -90
                                self.WRG.rotation_z = 0
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_x = 0
                                    else:
                                        self.WRG.rotation_x = 180
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WRG.rotation_x = 90
                                    else:
                                        self.WRG.rotation_x = -90
                        continue
                    self.WR.x = current_piece.pos[0]
                    self.WR.y = current_piece.pos[1]
                    self.WR.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == 1:
                        if current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'R':
                                self.WR.rotation_x = 90
                                self.WR.rotation_y = 0
                                self.WR.rotation_z = 180
                            else:
                                self.WR.rotation_x = 0
                                self.WR.rotation_y = 0
                                self.WR.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'R':
                                self.WR.rotation_x = -90
                                self.WR.rotation_y = 0
                                self.WR.rotation_z = 0
                            else:
                                self.WR.rotation_x = 0
                                self.WR.rotation_y = 0
                                self.WR.rotation_z = 180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'R':
                                self.WR.rotation_x = 0
                                self.WR.rotation_y = 0
                                self.WR.rotation_z = -90
                            else:
                                self.WR.rotation_x = 180
                                self.WR.rotation_y = -90
                                self.WR.rotation_z = -90
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'R':
                                self.WR.rotation_x = 0
                                self.WR.rotation_y = 0
                                self.WR.rotation_z = 90
                            else:
                                self.WR.rotation_x = 180
                                self.WR.rotation_y = 90
                                self.WR.rotation_z = 90
                    elif current_piece.pos[2] == -1:
                        if current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'R':
                                self.WR.rotation_x = 90
                                self.WR.rotation_y = 0
                                self.WR.rotation_z = 0
                            else:
                                self.WR.rotation_x = 0
                                self.WR.rotation_y = 180
                                self.WR.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'R':
                                self.WR.rotation_x = -90
                                self.WR.rotation_y = 0
                                self.WR.rotation_z = 180
                            else:
                                self.WR.rotation_x = 0
                                self.WR.rotation_y = 180
                                self.WR.rotation_z = 180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'R':
                                self.WR.rotation_x = 0
                                self.WR.rotation_y = 180
                                self.WR.rotation_z = 90
                            else:
                                self.WR.rotation_x = 180
                                self.WR.rotation_y = -90
                                self.WR.rotation_z = 90
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'R':
                                self.WR.rotation_x = 0
                                self.WR.rotation_y = 180
                                self.WR.rotation_z = -90
                            else:
                                self.WR.rotation_x = 180
                                self.WR.rotation_y = 90
                                self.WR.rotation_z = -90
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == 1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'R':
                                    self.WR.rotation_x = 0
                                    self.WR.rotation_y = -90
                                    self.WR.rotation_z = 0
                                else:
                                    self.WR.rotation_x = 90
                                    self.WR.rotation_y = 90
                                    self.WR.rotation_z = 0
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'R':
                                    self.WR.rotation_x = 0
                                    self.WR.rotation_y = 90
                                    self.WR.rotation_z = 0
                                else:
                                    self.WR.rotation_x = 90
                                    self.WR.rotation_y = 90
                                    self.WR.rotation_z = 180
                        elif current_piece.pos[1] == -1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'R':
                                    self.WR.rotation_x = 0
                                    self.WR.rotation_y = -90
                                    self.WR.rotation_z = 180
                                else:
                                    self.WR.rotation_x = -90
                                    self.WR.rotation_y = -90
                                    self.WR.rotation_z = 0
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'R':
                                    self.WR.rotation_x = 0
                                    self.WR.rotation_y = 90
                                    self.WR.rotation_z = 180
                                else:
                                    self.WR.rotation_x = -90
                                    self.WR.rotation_y = 90
                                    self.WR.rotation_z = 0
                    continue
                if "G" in current_piece.colors:
                    if "Y" in current_piece.colors:
                        self.YGR.x = current_piece.pos[0]
                        self.YGR.y = current_piece.pos[1]
                        self.YGR.z = current_piece.pos[2] * -1
                        if current_piece.pos[2] == -1:
                            if current_piece.colors[2] == 'Y':
                                self.YGR.rotation_x = 0
                                self.YGR.rotation_y = 0
                                if current_piece.colors[0] == 'G':
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_z = 180
                                    else:
                                        self.YGR.rotation_z = 0
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_z = 90
                                    else:
                                        self.YGR.rotation_z = -90
                            elif current_piece.colors[2] == 'R':
                                self.YGR.rotation_x = 0
                                self.YGR.rotation_y = 90
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_y = -90
                                        self.YGR.rotation_z = 90
                                    else:
                                        self.YGR.rotation_y = 90
                                        self.YGR.rotation_z = -90
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_x = 90
                                        self.YGR.rotation_y = 0
                                        self.YGR.rotation_z = 0
                                    else:
                                        self.YGR.rotation_x = -90
                                        self.YGR.rotation_y = 0
                                        self.YGR.rotation_z = 180
                            elif current_piece.colors[2] == 'G':
                                self.YGR.rotation_y = -90
                                self.YGR.rotation_z = 0
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_x = 180
                                    else:
                                        self.YGR.rotation_x = 0
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_x = 90
                                    else:
                                        self.YGR.rotation_x = -90
                        elif current_piece.pos[2] == 1:
                            if current_piece.colors[2] == 'Y':
                                self.YGR.rotation_x = 0
                                self.YGR.rotation_y = 180
                                if current_piece.colors[0] == 'G':
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_z = 180
                                    else:
                                        self.YGR.rotation_z = 0
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_z = 90
                                    else:
                                        self.YGR.rotation_z = -90
                            elif current_piece.colors[2] == 'R':
                                self.YGR.rotation_x = 0
                                self.YGR.rotation_y = -90
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_y = 90
                                        self.YGR.rotation_z = 90
                                    else:
                                        self.YGR.rotation_y = -90
                                        self.YGR.rotation_z = -90
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_x = 90
                                        self.YGR.rotation_y = 180
                                        self.YGR.rotation_z = 0
                                    else:
                                        self.YGR.rotation_x = -90
                                        self.YGR.rotation_y = 180
                                        self.YGR.rotation_z = 180
                            elif current_piece.colors[2] == 'G':
                                self.YGR.rotation_y = 90
                                self.YGR.rotation_z = 0
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_x = 180
                                    else:
                                        self.YGR.rotation_x = 0
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YGR.rotation_x = 90
                                    else:
                                        self.YGR.rotation_x = -90
                        continue
                    self.GR.x = current_piece.pos[0]
                    self.GR.y = current_piece.pos[1]
                    self.GR.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == 1:
                        if current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'R':
                                self.GR.rotation_x = 0
                                self.GR.rotation_y = 90+180
                                self.GR.rotation_z = 0-90
                            else:
                                self.GR.rotation_x = 0
                                self.GR.rotation_y = 90
                                self.GR.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'R':
                                self.GR.rotation_x = 0
                                self.GR.rotation_y = 0 - 90 + 180
                                self.GR.rotation_z = 180 - 90
                            else:
                                self.GR.rotation_x = 0
                                self.GR.rotation_y = 0-90
                                self.GR.rotation_z = 180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'R':
                                self.GR.rotation_x = -90
                                self.GR.rotation_y = 0+90
                                self.GR.rotation_z = 0
                            else:
                                self.GR.rotation_x = 90
                                self.GR.rotation_y = 0 + 90 - 180
                                self.GR.rotation_z = 0 - 90
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'R':
                                self.GR.rotation_x = 90
                                self.GR.rotation_y = 0+90
                                self.GR.rotation_z = 0
                            else:
                                self.GR.rotation_x = -90
                                self.GR.rotation_y = 0 + 90 - 180
                                self.GR.rotation_z = 0 - 90
                    elif current_piece.pos[2] == -1:
                        if current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'R':
                                self.GR.rotation_x = 0 +180
                                self.GR.rotation_y = -90
                                self.GR.rotation_z = 0 +90
                            else:
                                self.GR.rotation_x = 0
                                self.GR.rotation_y = -90
                                self.GR.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'R':
                                self.GR.rotation_x = 0 + 180
                                self.GR.rotation_y = 90
                                self.GR.rotation_z = 180 + 90
                            else:
                                self.GR.rotation_x = 0
                                self.GR.rotation_y = 90
                                self.GR.rotation_z = 180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'R':
                                self.GR.rotation_x = 90
                                self.GR.rotation_y = -90
                                self.GR.rotation_z = 0
                            else:
                                self.GR.rotation_x = 90 +180
                                self.GR.rotation_y = -90
                                self.GR.rotation_z = 0 + 90
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'R':
                                self.GR.rotation_x = -90
                                self.GR.rotation_y = -90
                                self.GR.rotation_z = 0
                            else:
                                self.GR.rotation_x = -90 + 180
                                self.GR.rotation_y = -90
                                self.GR.rotation_z = 0 + 90
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == 1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'R':
                                    self.GR.rotation_x = 0
                                    self.GR.rotation_y = 0
                                    self.GR.rotation_z = 0
                                else:
                                    self.GR.rotation_x = 180
                                    self.GR.rotation_y = 0
                                    self.GR.rotation_z = 90
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'R':
                                    self.GR.rotation_x = 0
                                    self.GR.rotation_y = 90+90
                                    self.GR.rotation_z = 0
                                else:
                                    self.GR.rotation_x = 0
                                    self.GR.rotation_y = 0
                                    self.GR.rotation_z = -90
                        elif current_piece.pos[1] == -1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'R':
                                    self.GR.rotation_x = 0
                                    self.GR.rotation_y = -90-90
                                    self.GR.rotation_z = 180
                                else:
                                    self.GR.rotation_x = 0
                                    self.GR.rotation_y = 0
                                    self.GR.rotation_z = 90
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'R':
                                    self.GR.rotation_x = 0
                                    self.GR.rotation_y = 90-90
                                    self.GR.rotation_z = 180
                                else:
                                    self.GR.rotation_x = 0
                                    self.GR.rotation_y = 180
                                    self.GR.rotation_z = 90
                    continue
                if "B" in current_piece.colors:
                    if "Y" in current_piece.colors:
                        self.YRB.x = current_piece.pos[0]
                        self.YRB.y = current_piece.pos[1]
                        self.YRB.z = current_piece.pos[2] * -1
                        if current_piece.pos[2] == -1:
                            if current_piece.colors[2] == 'Y':
                                self.YRB.rotation_x = 0
                                self.YRB.rotation_y = 0
                                if current_piece.colors[0] == 'B':
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_z = 180
                                    else:
                                        self.YRB.rotation_z = 0
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_z = -90
                                    else:
                                        self.YRB.rotation_z = 90
                            elif current_piece.colors[2] == 'R':
                                self.YRB.rotation_x = 0
                                self.YRB.rotation_y = 90
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_y = 90
                                        self.YRB.rotation_z = -90
                                    else:
                                        self.YRB.rotation_y = -90
                                        self.YRB.rotation_z = 90
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_x = 90
                                        self.YRB.rotation_y = 0
                                        self.YRB.rotation_z = 0
                                    else:
                                        self.YRB.rotation_x = -90
                                        self.YRB.rotation_y = 0
                                        self.YRB.rotation_z = 180
                            elif current_piece.colors[2] == 'B':
                                self.YRB.rotation_y = 90
                                self.YRB.rotation_z = 0
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_x = 180
                                    else:
                                        self.YRB.rotation_x = 0
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_x = 90
                                    else:
                                        self.YRB.rotation_x = -90
                        elif current_piece.pos[2] == 1:
                            if current_piece.colors[2] == 'Y':
                                self.YRB.rotation_x = 0
                                self.YRB.rotation_y = 180
                                if current_piece.colors[0] == 'B':
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_z = 180
                                    else:
                                        self.YRB.rotation_z = 0
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_z = -90
                                    else:
                                        self.YRB.rotation_z = 90
                            elif current_piece.colors[2] == 'R':
                                self.YRB.rotation_x = 0
                                self.YRB.rotation_y = -90
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_y = -90
                                        self.YRB.rotation_z = -90
                                    else:
                                        self.YRB.rotation_y = 90
                                        self.YRB.rotation_z = 90
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_x = 90
                                        self.YRB.rotation_y = 0
                                        self.YRB.rotation_z = 180
                                    else:
                                        self.YRB.rotation_x = -90
                                        self.YRB.rotation_y = 180
                                        self.YRB.rotation_z = 180
                            elif current_piece.colors[2] == 'B':
                                self.YRB.rotation_y = -90
                                self.YRB.rotation_z = 0
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_x = 180
                                    else:
                                        self.YRB.rotation_x = 0
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YRB.rotation_x = 90
                                    else:
                                        self.YRB.rotation_x = -90
                        continue
                    self.BR.x = current_piece.pos[0]
                    self.BR.y = current_piece.pos[1]
                    self.BR.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == -1:
                        if current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'R':
                                self.BR.rotation_x = 0
                                self.BR.rotation_y = 90+180
                                self.BR.rotation_z = 0-90+180
                            else:
                                self.BR.rotation_x = 0
                                self.BR.rotation_y = 90
                                self.BR.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'R':
                                self.BR.rotation_x = 0
                                self.BR.rotation_y = 0 - 90 + 180
                                self.BR.rotation_z = 180 - 90+180
                            else:
                                self.BR.rotation_x = 0
                                self.BR.rotation_y = 0-90
                                self.BR.rotation_z = 180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'R':
                                self.BR.rotation_x = -90
                                self.BR.rotation_y = 0+90
                                self.BR.rotation_z = 0
                            else:
                                self.BR.rotation_x = 90
                                self.BR.rotation_y = 0 + 90 - 180
                                self.BR.rotation_z = 0 - 90+180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'R':
                                self.BR.rotation_x = 90
                                self.BR.rotation_y = 0+90
                                self.BR.rotation_z = 0
                            else:
                                self.BR.rotation_x = -90
                                self.BR.rotation_y = 0 + 90 - 180
                                self.BR.rotation_z = 0 - 90+180
                    elif current_piece.pos[2] == 1:
                        if current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'R':
                                self.BR.rotation_x = 0 +180
                                self.BR.rotation_y = -90
                                self.BR.rotation_z = 0 +90 +180
                            else:
                                self.BR.rotation_x = 0
                                self.BR.rotation_y = -90
                                self.BR.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'R':
                                self.BR.rotation_x = 0 + 180
                                self.BR.rotation_y = 90
                                self.BR.rotation_z = 180 + 90 +180
                            else:
                                self.BR.rotation_x = 0
                                self.BR.rotation_y = 90
                                self.BR.rotation_z = 180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'R':
                                self.BR.rotation_x = 90
                                self.BR.rotation_y = -90
                                self.BR.rotation_z = 0
                            else:
                                self.BR.rotation_x = 90 +180
                                self.BR.rotation_y = -90
                                self.BR.rotation_z = 0 + 90 +180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'R':
                                self.BR.rotation_x = -90
                                self.BR.rotation_y = -90
                                self.BR.rotation_z = 0
                            else:
                                self.BR.rotation_x = -90 + 180
                                self.BR.rotation_y = -90
                                self.BR.rotation_z = 0 + 90 +180
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == 1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'R':
                                    self.BR.rotation_x = 0
                                    self.BR.rotation_y = 0
                                    self.BR.rotation_z = 0
                                else:
                                    self.BR.rotation_x = 0
                                    self.BR.rotation_y = 180
                                    self.BR.rotation_z = 90
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'R':
                                    self.BR.rotation_x = 0
                                    self.BR.rotation_y = 90+90
                                    self.BR.rotation_z = 0
                                else:
                                    self.BR.rotation_x = 0
                                    self.BR.rotation_y = 0
                                    self.BR.rotation_z = 90
                        elif current_piece.pos[1] == -1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'R':
                                    self.BR.rotation_x = 0
                                    self.BR.rotation_y = -90-90
                                    self.BR.rotation_z = 180
                                else:
                                    self.BR.rotation_x = 0
                                    self.BR.rotation_y = 0
                                    self.BR.rotation_z = -90
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'R':
                                    self.BR.rotation_x = 0
                                    self.BR.rotation_y = 90-90
                                    self.BR.rotation_z = 180
                                else:
                                    self.BR.rotation_x = 180
                                    self.BR.rotation_y = 0
                                    self.BR.rotation_z = 90
                    continue
                if "Y" in current_piece.colors:
                    self.YR.x = current_piece.pos[0]
                    self.YR.y = current_piece.pos[1]
                    self.YR.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == -1:
                        if current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'R':
                                self.YR.rotation_x = 90
                                self.YR.rotation_y = 0
                                self.YR.rotation_z = 0
                            else:
                                self.YR.rotation_x = 0
                                self.YR.rotation_y = 0
                                self.YR.rotation_z = 180
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'R':
                                self.YR.rotation_x = -90
                                self.YR.rotation_y = 0
                                self.YR.rotation_z = 180
                            else:
                                self.YR.rotation_x = 0
                                self.YR.rotation_y = 0
                                self.YR.rotation_z = 0
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'R':
                                self.YR.rotation_x = 0
                                self.YR.rotation_y = 0
                                self.YR.rotation_z = 90
                            else:
                                self.YR.rotation_x = 180
                                self.YR.rotation_y = -90
                                self.YR.rotation_z = 90
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'R':
                                self.YR.rotation_x = 0
                                self.YR.rotation_y = 0
                                self.YR.rotation_z = -90
                            else:
                                self.YR.rotation_x = 180
                                self.YR.rotation_y = 90
                                self.YR.rotation_z = -90
                    elif current_piece.pos[2] == 1:
                        if current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'R':
                                self.YR.rotation_x = 90
                                self.YR.rotation_y = 0
                                self.YR.rotation_z = 180
                            else:
                                self.YR.rotation_x = 0
                                self.YR.rotation_y = 180
                                self.YR.rotation_z = 180
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'R':
                                self.YR.rotation_x = -90
                                self.YR.rotation_y = 0
                                self.YR.rotation_z = 0
                            else:
                                self.YR.rotation_x = 0
                                self.YR.rotation_y = 180
                                self.YR.rotation_z = 0
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'R':
                                self.YR.rotation_x = 0
                                self.YR.rotation_y = 180
                                self.YR.rotation_z = -90
                            else:
                                self.YR.rotation_x = 180
                                self.YR.rotation_y = -90
                                self.YR.rotation_z = -90
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'R':
                                self.YR.rotation_x = 0
                                self.YR.rotation_y = 180
                                self.YR.rotation_z = 90
                            else:
                                self.YR.rotation_x = 180
                                self.YR.rotation_y = 90
                                self.YR.rotation_z = 90
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == -1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'R':
                                    self.YR.rotation_x = 0
                                    self.YR.rotation_y = -90
                                    self.YR.rotation_z = 180
                                else:
                                    self.YR.rotation_x = 90
                                    self.YR.rotation_y = 90
                                    self.YR.rotation_z = 180
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'R':
                                    self.YR.rotation_x = 0
                                    self.YR.rotation_y = 90
                                    self.YR.rotation_z = 180
                                else:
                                    self.YR.rotation_x = 90
                                    self.YR.rotation_y = 90
                                    self.YR.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'R':
                                    self.YR.rotation_x = 0
                                    self.YR.rotation_y = -90
                                    self.YR.rotation_z = 0
                                else:
                                    self.YR.rotation_x = -90
                                    self.YR.rotation_y = -90
                                    self.YR.rotation_z = 180
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'R':
                                    self.YR.rotation_x = 0
                                    self.YR.rotation_y = 90
                                    self.YR.rotation_z = 0
                                else:
                                    self.YR.rotation_x = -90
                                    self.YR.rotation_y = 90
                                    self.YR.rotation_z = 180
                    continue
                self.R.x = current_piece.pos[0]
                self.R.y = current_piece.pos[1]
                self.R.z = current_piece.pos[2] * -1
                if current_piece.pos[1] == 1:
                    self.R.rotation_x = 0
                    self.R.rotation_y = 0
                    self.R.rotation_z = 0
                elif current_piece.pos[1] == -1:
                    self.R.rotation_x = 0
                    self.R.rotation_y = 0
                    self.R.rotation_z = 180
                if current_piece.pos[0] == 1:
                    self.R.rotation_x = 0
                    self.R.rotation_y = 0
                    self.R.rotation_z = 90
                elif current_piece.pos[0] == -1:
                    self.R.rotation_x = 0
                    self.R.rotation_y = 0
                    self.R.rotation_z = -90
                if current_piece.pos[2] == 1:
                    self.R.rotation_x = -90
                    self.R.rotation_y = 0
                    self.R.rotation_z = 0
                elif current_piece.pos[2] == -1:
                    self.R.rotation_x = 90
                    self.R.rotation_y = 0
                    self.R.rotation_z = 0
                continue
            if "O" in current_piece.colors:  # does bottom layer
                if "W" in current_piece.colors:
                    if "B" in current_piece.colors:
                        self.WOB.x = current_piece.pos[0]
                        self.WOB.y = current_piece.pos[1]
                        self.WOB.z = current_piece.pos[2] * -1
                        if current_piece.pos[2] == 1:
                            if current_piece.colors[2] == 'W':
                                self.WOB.rotation_x = 0
                                self.WOB.rotation_y = 0
                                if current_piece.colors[0] == 'B':
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_z = 180
                                    else:
                                        self.WOB.rotation_z = 0
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_z = 90
                                    else:
                                        self.WOB.rotation_z = -90
                            elif current_piece.colors[2] == 'O':
                                self.WOB.rotation_x = 0
                                self.WOB.rotation_y = 90
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_y = -90
                                        self.WOB.rotation_z = 90
                                    else:
                                        self.WOB.rotation_y = 90
                                        self.WOB.rotation_z = -90
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_x = 90
                                        self.WOB.rotation_y = 0
                                        self.WOB.rotation_z = 0
                                    else:
                                        self.WOB.rotation_x = -90
                                        self.WOB.rotation_y = 0
                                        self.WOB.rotation_z = 180
                            elif current_piece.colors[2] == 'B':
                                self.WOB.rotation_y = -90
                                self.WOB.rotation_z = 0
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_x = 180
                                    else:
                                        self.WOB.rotation_x = 0
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_x = 90
                                    else:
                                        self.WOB.rotation_x = -90
                        elif current_piece.pos[2] == -1:
                            if current_piece.colors[2] == 'W':
                                self.WOB.rotation_x = 0
                                self.WOB.rotation_y = 180
                                if current_piece.colors[0] == 'B':
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_z = 180
                                    else:
                                        self.WOB.rotation_z = 0
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_z = 90
                                    else:
                                        self.WOB.rotation_z = -90
                            elif current_piece.colors[2] == 'O':
                                self.WOB.rotation_x = 0
                                self.WOB.rotation_y = -90
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_y = 90
                                        self.WOB.rotation_z = 90
                                    else:
                                        self.WOB.rotation_y = -90
                                        self.WOB.rotation_z = -90
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_x = 90
                                        self.WOB.rotation_y = 180
                                        self.WOB.rotation_z = 0
                                    else:
                                        self.WOB.rotation_x = -90
                                        self.WOB.rotation_y = 180
                                        self.WOB.rotation_z = 180
                            elif current_piece.colors[2] == 'B':
                                self.WOB.rotation_y = 90
                                self.WOB.rotation_z = 0
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_x = 180
                                    else:
                                        self.WOB.rotation_x = 0
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WOB.rotation_x = 90
                                    else:
                                        self.WOB.rotation_x = -90
                        continue
                    if "G" in current_piece.colors:
                        self.WGO.x = current_piece.pos[0]
                        self.WGO.y = current_piece.pos[1]
                        self.WGO.z = current_piece.pos[2] * -1
                        if current_piece.pos[2] == 1:
                            if current_piece.colors[2] == 'W':
                                self.WGO.rotation_x = 0
                                self.WGO.rotation_y = 0
                                if current_piece.colors[0] == 'G':
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_z = 180
                                    else:
                                        self.WGO.rotation_z = 0
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_z = -90
                                    else:
                                        self.WGO.rotation_z = 90
                            elif current_piece.colors[2] == 'O':
                                self.WGO.rotation_x = 0
                                self.WGO.rotation_y = 90
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_y = 90
                                        self.WGO.rotation_z = -90
                                    else:
                                        self.WGO.rotation_y = -90
                                        self.WGO.rotation_z = 90
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_x = 90
                                        self.WGO.rotation_y = 0
                                        self.WGO.rotation_z = 0
                                    else:
                                        self.WGO.rotation_x = -90
                                        self.WGO.rotation_y = 0
                                        self.WGO.rotation_z = 180
                            elif current_piece.colors[2] == 'G':
                                self.WGO.rotation_y = 90
                                self.WGO.rotation_z = 0
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_x = 180
                                    else:
                                        self.WGO.rotation_x = 0
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_x = 90
                                    else:
                                        self.WGO.rotation_x = -90
                        elif current_piece.pos[2] == -1:
                            if current_piece.colors[2] == 'W':
                                self.WGO.rotation_x = 0
                                self.WGO.rotation_y = 180
                                if current_piece.colors[0] == 'G':
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_z = 180
                                    else:
                                        self.WGO.rotation_z = 0
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_z = -90
                                    else:
                                        self.WGO.rotation_z = 90
                            elif current_piece.colors[2] == 'O':
                                self.WGO.rotation_x = 0
                                self.WGO.rotation_y = -90
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_y = -90
                                        self.WGO.rotation_z = -90
                                    else:
                                        self.WGO.rotation_y = 90
                                        self.WGO.rotation_z = 90
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_x = 90
                                        self.WGO.rotation_y = 0
                                        self.WGO.rotation_z = 180
                                    else:
                                        self.WGO.rotation_x = -90
                                        self.WGO.rotation_y = 180
                                        self.WGO.rotation_z = 180
                            elif current_piece.colors[2] == 'G':
                                self.WGO.rotation_y = -90
                                self.WGO.rotation_z = 0
                                if current_piece.colors[0] == 'W':
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_x = 180
                                    else:
                                        self.WGO.rotation_x = 0
                                else:
                                    if current_piece.pos[1] == 1:
                                        self.WGO.rotation_x = 90
                                    else:
                                        self.WGO.rotation_x = -90
                        continue
                    self.WO.x = current_piece.pos[0]
                    self.WO.y = current_piece.pos[1]
                    self.WO.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == 1:
                        if current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'O':
                                self.WO.rotation_x = 90
                                self.WO.rotation_y = 0
                                self.WO.rotation_z = 0
                            else:
                                self.WO.rotation_x = 0
                                self.WO.rotation_y = 0
                                self.WO.rotation_z = 180
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'O':
                                self.WO.rotation_x = -90
                                self.WO.rotation_y = 0
                                self.WO.rotation_z = 180
                            else:
                                self.WO.rotation_x = 0
                                self.WO.rotation_y = 0
                                self.WO.rotation_z = 0
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'O':
                                self.WO.rotation_x = 0
                                self.WO.rotation_y = 0
                                self.WO.rotation_z = 90
                            else:
                                self.WO.rotation_x = 180
                                self.WO.rotation_y = -90
                                self.WO.rotation_z = 90
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'O':
                                self.WO.rotation_x = 0
                                self.WO.rotation_y = 0
                                self.WO.rotation_z = -90
                            else:
                                self.WO.rotation_x = 180
                                self.WO.rotation_y = 90
                                self.WO.rotation_z = -90
                    elif current_piece.pos[2] == -1:
                        if current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'O':
                                self.WO.rotation_x = 90
                                self.WO.rotation_y = 0
                                self.WO.rotation_z = 180
                            else:
                                self.WO.rotation_x = 0
                                self.WO.rotation_y = 180
                                self.WO.rotation_z = 180
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'O':
                                self.WO.rotation_x = -90
                                self.WO.rotation_y = 0
                                self.WO.rotation_z = 0
                            else:
                                self.WO.rotation_x = 0
                                self.WO.rotation_y = 180
                                self.WO.rotation_z = 0
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'O':
                                self.WO.rotation_x = 0
                                self.WO.rotation_y = 180
                                self.WO.rotation_z = -90
                            else:
                                self.WO.rotation_x = 180
                                self.WO.rotation_y = -90
                                self.WO.rotation_z = -90
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'O':
                                self.WO.rotation_x = 0
                                self.WO.rotation_y = 180
                                self.WO.rotation_z = 90
                            else:
                                self.WO.rotation_x = 180
                                self.WO.rotation_y = 90
                                self.WO.rotation_z = 90
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == 1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'O':
                                    self.WO.rotation_x = 0
                                    self.WO.rotation_y = -90
                                    self.WO.rotation_z = 180
                                else:
                                    self.WO.rotation_x = 90
                                    self.WO.rotation_y = 90
                                    self.WO.rotation_z = 180
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'O':
                                    self.WO.rotation_x = 0
                                    self.WO.rotation_y = 90
                                    self.WO.rotation_z = 180
                                else:
                                    self.WO.rotation_x = 90
                                    self.WO.rotation_y = 90
                                    self.WO.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'O':
                                    self.WO.rotation_x = 0
                                    self.WO.rotation_y = -90
                                    self.WO.rotation_z = 0
                                else:
                                    self.WO.rotation_x = -90
                                    self.WO.rotation_y = -90
                                    self.WO.rotation_z = 180
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'O':
                                    self.WO.rotation_x = 0
                                    self.WO.rotation_y = 90
                                    self.WO.rotation_z = 0
                                else:
                                    self.WO.rotation_x = -90
                                    self.WO.rotation_y = 90
                                    self.WO.rotation_z = 180
                    continue
                if "G" in current_piece.colors:
                    if "Y" in current_piece.colors:
                        self.YOG.x = current_piece.pos[0]
                        self.YOG.y = current_piece.pos[1]
                        self.YOG.z = current_piece.pos[2] * -1
                        if current_piece.pos[2] == -1:
                            if current_piece.colors[2] == 'Y':
                                self.YOG.rotation_x = 0
                                self.YOG.rotation_y = 0
                                if current_piece.colors[0] == 'G':
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_z = 0
                                    else:
                                        self.YOG.rotation_z = 180
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_z = 90
                                    else:
                                        self.YOG.rotation_z = -90
                            elif current_piece.colors[2] == 'O':
                                self.YOG.rotation_x = 0
                                self.YOG.rotation_y = 90
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_y = 90
                                        self.YOG.rotation_z = 90
                                    else:
                                        self.YOG.rotation_y = -90
                                        self.YOG.rotation_z = -90
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_x = 90
                                        self.YOG.rotation_y = 0
                                        self.YOG.rotation_z = 180
                                    else:
                                        self.YOG.rotation_x = -90
                                        self.YOG.rotation_y = 0
                                        self.YOG.rotation_z = 0
                            elif current_piece.colors[2] == 'G':
                                self.YOG.rotation_y = -90
                                self.YOG.rotation_z = 0
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_x = 0
                                    else:
                                        self.YOG.rotation_x = 180
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_x = 90
                                    else:
                                        self.YOG.rotation_x = -90
                        elif current_piece.pos[2] == 1:
                            if current_piece.colors[2] == 'Y':
                                self.YOG.rotation_x = 0
                                self.YOG.rotation_y = 180
                                if current_piece.colors[0] == 'G':
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_z = 0
                                    else:
                                        self.YOG.rotation_z = 180
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_z = 90
                                    else:
                                        self.YOG.rotation_z = -90
                            elif current_piece.colors[2] == 'O':
                                self.YOG.rotation_x = 0
                                self.YOG.rotation_y = -90
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_y = -90
                                        self.YOG.rotation_z = 90
                                    else:
                                        self.YOG.rotation_y = 90
                                        self.YOG.rotation_z = -90
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_x = 90
                                        self.YOG.rotation_y = 180
                                        self.YOG.rotation_z = 180
                                    else:
                                        self.YOG.rotation_x = -90
                                        self.YOG.rotation_y = 180
                                        self.YOG.rotation_z = 0
                            elif current_piece.colors[2] == 'G':
                                self.YOG.rotation_y = 90
                                self.YOG.rotation_z = 0
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_x = 0
                                    else:
                                        self.YOG.rotation_x = 180
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YOG.rotation_x = 90
                                    else:
                                        self.YOG.rotation_x = -90
                        continue
                    self.GO.x = current_piece.pos[0]
                    self.GO.y = current_piece.pos[1]
                    self.GO.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == 1:
                        if current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'O':
                                self.GO.rotation_x = 0
                                self.GO.rotation_y = 90+180
                                self.GO.rotation_z = 0-90+180
                            else:
                                self.GO.rotation_x = 0
                                self.GO.rotation_y = 90
                                self.GO.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'O':
                                self.GO.rotation_x = 0
                                self.GO.rotation_y = 0 - 90 + 180
                                self.GO.rotation_z = 180 - 90+180
                            else:
                                self.GO.rotation_x = 0
                                self.GO.rotation_y = 0-90
                                self.GO.rotation_z = 180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'O':
                                self.GO.rotation_x = -90
                                self.GO.rotation_y = 0+90
                                self.GO.rotation_z = 0
                            else:
                                self.GO.rotation_x = 90
                                self.GO.rotation_y = 0 + 90 - 180
                                self.GO.rotation_z = 0 - 90+180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'O':
                                self.GO.rotation_x = 90
                                self.GO.rotation_y = 0+90
                                self.GO.rotation_z = 0
                            else:
                                self.GO.rotation_x = -90
                                self.GO.rotation_y = 0 + 90 - 180
                                self.GO.rotation_z = 0 - 90+180
                    elif current_piece.pos[2] == -1:
                        if current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'O':
                                self.GO.rotation_x = 0 +180
                                self.GO.rotation_y = -90
                                self.GO.rotation_z = 0 +90 +180
                            else:
                                self.GO.rotation_x = 0
                                self.GO.rotation_y = -90
                                self.GO.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'O':
                                self.GO.rotation_x = 0 + 180
                                self.GO.rotation_y = 90
                                self.GO.rotation_z = 180 + 90 +180
                            else:
                                self.GO.rotation_x = 0
                                self.GO.rotation_y = 90
                                self.GO.rotation_z = 180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'O':
                                self.GO.rotation_x = 90
                                self.GO.rotation_y = -90
                                self.GO.rotation_z = 0
                            else:
                                self.GO.rotation_x = 90 +180
                                self.GO.rotation_y = -90
                                self.GO.rotation_z = 0 + 90 +180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'O':
                                self.GO.rotation_x = -90
                                self.GO.rotation_y = -90
                                self.GO.rotation_z = 0
                            else:
                                self.GO.rotation_x = -90 + 180
                                self.GO.rotation_y = -90
                                self.GO.rotation_z = 0 + 90 +180
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == -1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'O':
                                    self.GO.rotation_x = 0
                                    self.GO.rotation_y = 0
                                    self.GO.rotation_z = 0
                                else:
                                    self.GO.rotation_x = 0
                                    self.GO.rotation_y = 180
                                    self.GO.rotation_z = 90
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'O':
                                    self.GO.rotation_x = 0
                                    self.GO.rotation_y = 90+90
                                    self.GO.rotation_z = 0
                                else:
                                    self.GO.rotation_x = 0
                                    self.GO.rotation_y = 0
                                    self.GO.rotation_z = 90
                        elif current_piece.pos[1] == 1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'O':
                                    self.GO.rotation_x = 0
                                    self.GO.rotation_y = -90-90
                                    self.GO.rotation_z = 180
                                else:
                                    self.GO.rotation_x = 0
                                    self.GO.rotation_y = 0
                                    self.GO.rotation_z = -90
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'O':
                                    self.GO.rotation_x = 0
                                    self.GO.rotation_y = 90-90
                                    self.GO.rotation_z = 180
                                else:
                                    self.GO.rotation_x = 180
                                    self.GO.rotation_y = 0
                                    self.GO.rotation_z = 90
                    continue
                if "B" in current_piece.colors:
                    if "Y" in current_piece.colors:
                        self.YBO.x = current_piece.pos[0]
                        self.YBO.y = current_piece.pos[1]
                        self.YBO.z = current_piece.pos[2] * -1
                        if current_piece.pos[2] == -1:
                            if current_piece.colors[2] == 'Y':
                                self.YBO.rotation_x = 0
                                self.YBO.rotation_y = 0
                                if current_piece.colors[0] == 'B':
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_z = 0
                                    else:
                                        self.YBO.rotation_z = 180
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_z = -90
                                    else:
                                        self.YBO.rotation_z = 90
                            elif current_piece.colors[2] == 'O':

                                self.YBO.rotation_x = 0
                                self.YBO.rotation_y = 90
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_y = -90
                                        self.YBO.rotation_z = -90
                                    else:
                                        self.YBO.rotation_z = 90
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_x = 90
                                        self.YBO.rotation_y = 0
                                        self.YBO.rotation_z = 180
                                    else:
                                        self.YBO.rotation_x = -90
                                        self.YBO.rotation_y = 0
                                        self.YBO.rotation_z = 0

                            elif current_piece.colors[2] == 'B':
                                self.YBO.rotation_y = 90
                                self.YBO.rotation_z = 0
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_x = 0
                                    else:
                                        self.YBO.rotation_x = 180
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_x = 90
                                    else:
                                        self.YBO.rotation_x = -90
                        elif current_piece.pos[2] == 1:
                            if current_piece.colors[2] == 'Y':
                                self.YBO.rotation_x = 0
                                self.YBO.rotation_y = 180
                                if current_piece.colors[0] == 'B':
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_z = 0
                                    else:
                                        self.YBO.rotation_z = 180
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_z = -90
                                    else:
                                        self.YBO.rotation_z = 90
                            elif current_piece.colors[2] == 'O':
                                self.YBO.rotation_x = 0
                                self.YBO.rotation_y = -90
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_y = 90
                                        self.YBO.rotation_z = -90
                                    else:
                                        self.YBO.rotation_z = 90
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_x = 90
                                        self.YBO.rotation_y = 180
                                        self.YBO.rotation_z = 180
                                    else:
                                        self.YBO.rotation_x = -90
                                        self.YBO.rotation_y = 180
                                        self.YBO.rotation_z = 0
                            elif current_piece.colors[2] == 'B':
                                self.YBO.rotation_y = -90
                                self.YBO.rotation_z = 0
                                if current_piece.colors[0] == 'Y':
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_x = 0
                                    else:
                                        self.YBO.rotation_x = 180
                                else:
                                    if current_piece.pos[1] == -1:
                                        self.YBO.rotation_x = 90
                                    else:
                                        self.YBO.rotation_x = -90
                        continue
                    self.BO.x = current_piece.pos[0]
                    self.BO.y = current_piece.pos[1]
                    self.BO.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == -1:
                        if current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'O':
                                self.BO.rotation_x = 0
                                self.BO.rotation_y = 90+180
                                self.BO.rotation_z = 0-90
                            else:
                                self.BO.rotation_x = 0
                                self.BO.rotation_y = 90
                                self.BO.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'O':
                                self.BO.rotation_x = 0
                                self.BO.rotation_y = 0 - 90 + 180
                                self.BO.rotation_z = 180 - 90
                            else:
                                self.BO.rotation_x = 0
                                self.BO.rotation_y = 0-90
                                self.BO.rotation_z = 180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'O':
                                self.BO.rotation_x = -90
                                self.BO.rotation_y = 0+90
                                self.BO.rotation_z = 0
                            else:
                                self.BO.rotation_x = 90
                                self.BO.rotation_y = 0 + 90 - 180
                                self.BO.rotation_z = 0 - 90
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'O':
                                self.BO.rotation_x = 90
                                self.BO.rotation_y = 0+90
                                self.BO.rotation_z = 0
                            else:
                                self.BO.rotation_x = -90
                                self.BO.rotation_y = 0 + 90 - 180
                                self.BO.rotation_z = 0 - 90
                    elif current_piece.pos[2] == 1:
                        if current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'O':
                                self.BO.rotation_x = 0 +180
                                self.BO.rotation_y = -90
                                self.BO.rotation_z = 0 +90
                            else:
                                self.BO.rotation_x = 0
                                self.BO.rotation_y = -90
                                self.BO.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'O':
                                self.BO.rotation_x = 0 + 180
                                self.BO.rotation_y = 90
                                self.BO.rotation_z = 180 + 90
                            else:
                                self.BO.rotation_x = 0
                                self.BO.rotation_y = 90
                                self.BO.rotation_z = 180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'O':
                                self.BO.rotation_x = 90
                                self.BO.rotation_y = -90
                                self.BO.rotation_z = 0
                            else:
                                self.BO.rotation_x = 90 +180
                                self.BO.rotation_y = -90
                                self.BO.rotation_z = 0 + 90
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'O':
                                self.BO.rotation_x = -90
                                self.BO.rotation_y = -90
                                self.BO.rotation_z = 0
                            else:
                                self.BO.rotation_x = -90 + 180
                                self.BO.rotation_y = -90
                                self.BO.rotation_z = 0 + 90
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == -1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'O':
                                    self.BO.rotation_x = 0
                                    self.BO.rotation_y = 0
                                    self.BO.rotation_z = 0
                                else:
                                    self.BO.rotation_x = 180
                                    self.BO.rotation_y = 0
                                    self.BO.rotation_z = 90
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'O':
                                    self.BO.rotation_x = 0
                                    self.BO.rotation_y = 90+90
                                    self.BO.rotation_z = 0
                                else:
                                    self.BO.rotation_x = 0
                                    self.BO.rotation_y = 0
                                    self.BO.rotation_z = -90
                        elif current_piece.pos[1] == 1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'O':
                                    self.BO.rotation_x = 0
                                    self.BO.rotation_y = -90-90
                                    self.BO.rotation_z = 180
                                else:
                                    self.BO.rotation_x = 0
                                    self.BO.rotation_y = 0
                                    self.BO.rotation_z = 90
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'O':
                                    self.BO.rotation_x = 0
                                    self.BO.rotation_y = 90-90
                                    self.BO.rotation_z = 180
                                else:
                                    self.BO.rotation_x = 0
                                    self.BO.rotation_y = 180
                                    self.BO.rotation_z = 90
                    continue
                if "Y" in current_piece.colors:
                    self.YO.x = current_piece.pos[0]
                    self.YO.y = current_piece.pos[1]
                    self.YO.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == -1:
                        if current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'O':
                                self.YO.rotation_x = 90
                                self.YO.rotation_y = 0
                                self.YO.rotation_z = 180
                            else:
                                self.YO.rotation_x = 0
                                self.YO.rotation_y = 0
                                self.YO.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'O':
                                self.YO.rotation_x = -90
                                self.YO.rotation_y = 0
                                self.YO.rotation_z = 0
                            else:
                                self.YO.rotation_x = 0
                                self.YO.rotation_y = 0
                                self.YO.rotation_z = 180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'O':
                                self.YO.rotation_x = 0
                                self.YO.rotation_y = 0
                                self.YO.rotation_z = -90
                            else:
                                self.YO.rotation_x = 180
                                self.YO.rotation_y = -90
                                self.YO.rotation_z = -90
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'O':
                                self.YO.rotation_x = 0
                                self.YO.rotation_y = 0
                                self.YO.rotation_z = 90
                            else:
                                self.YO.rotation_x = 180
                                self.YO.rotation_y = 90
                                self.YO.rotation_z = 90
                    elif current_piece.pos[2] == 1:
                        if current_piece.pos[1] == -1:
                            if current_piece.colors[2] == 'O':
                                self.YO.rotation_x = 90
                                self.YO.rotation_y = 0
                                self.YO.rotation_z = 0
                            else:
                                self.YO.rotation_x = 0
                                self.YO.rotation_y = 180
                                self.YO.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[2] == 'O':
                                self.YO.rotation_x = -90
                                self.YO.rotation_y = 0
                                self.YO.rotation_z = 180
                            else:
                                self.YO.rotation_x = 0
                                self.YO.rotation_y = 180
                                self.YO.rotation_z = 180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'O':
                                self.YO.rotation_x = 0
                                self.YO.rotation_y = 180
                                self.YO.rotation_z = 90
                            else:
                                self.YO.rotation_x = 180
                                self.YO.rotation_y = -90
                                self.YO.rotation_z = 90
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'O':
                                self.YO.rotation_x = 0
                                self.YO.rotation_y = 180
                                self.YO.rotation_z = -90
                            else:
                                self.YO.rotation_x = 180
                                self.YO.rotation_y = 90
                                self.YO.rotation_z = -90
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == -1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'O':
                                    self.YO.rotation_x = 0
                                    self.YO.rotation_y = -90
                                    self.YO.rotation_z = 0
                                else:
                                    self.YO.rotation_x = 90
                                    self.YO.rotation_y = 90
                                    self.YO.rotation_z = 0
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'O':
                                    self.YO.rotation_x = 0
                                    self.YO.rotation_y = 90
                                    self.YO.rotation_z = 0
                                else:
                                    self.YO.rotation_x = 90
                                    self.YO.rotation_y = 90
                                    self.YO.rotation_z = 180
                        elif current_piece.pos[1] == 1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'O':
                                    self.YO.rotation_x = 0
                                    self.YO.rotation_y = -90
                                    self.YO.rotation_z = 180
                                else:
                                    self.YO.rotation_x = -90
                                    self.YO.rotation_y = -90
                                    self.YO.rotation_z = 0
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'O':
                                    self.YO.rotation_x = 0
                                    self.YO.rotation_y = 90
                                    self.YO.rotation_z = 180
                                else:
                                    self.YO.rotation_x = -90
                                    self.YO.rotation_y = 90
                                    self.YO.rotation_z = 0
                    continue
                self.O.x = current_piece.pos[0]
                self.O.y = current_piece.pos[1]
                self.O.z = current_piece.pos[2] * -1
                if current_piece.pos[1] == -1:
                    self.O.rotation_x = 0
                    self.O.rotation_y = 0
                    self.O.rotation_z = 0
                elif current_piece.pos[1] == 1:
                    self.O.rotation_x = 0
                    self.O.rotation_y = 0
                    self.O.rotation_z = 180
                if current_piece.pos[0] == -1:
                    self.O.rotation_x = 0
                    self.O.rotation_y = 0
                    self.O.rotation_z = 90
                elif current_piece.pos[0] == 1:
                    self.O.rotation_x = 0
                    self.O.rotation_y = 0
                    self.O.rotation_z = -90
                if current_piece.pos[2] == -1:
                    self.O.rotation_x = -90
                    self.O.rotation_y = 0
                    self.O.rotation_z = 0
                elif current_piece.pos[2] == 1:
                    self.O.rotation_x = 90
                    self.O.rotation_y = 0
                    self.O.rotation_z = 0
                continue
            # middle front layer====
            if "W" in current_piece.colors:
                if "B" in current_piece.colors:
                    self.WB.x = current_piece.pos[0]
                    self.WB.y = current_piece.pos[1]
                    self.WB.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == 1:
                        if current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'W':
                                self.WB.rotation_x = 180
                                self.WB.rotation_y = 90
                                self.WB.rotation_z = 180
                            else:
                                self.WB.rotation_x = 0
                                self.WB.rotation_y = 0
                                self.WB.rotation_z = 180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'W':
                                self.WB.rotation_x = 0
                                self.WB.rotation_y = 90
                                self.WB.rotation_z = 180
                            else:
                                self.WB.rotation_x = 0
                                self.WB.rotation_y = 0
                                self.WB.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[1] == 'B':
                                self.WB.rotation_x = 0
                                self.WB.rotation_y = 0
                                self.WB.rotation_z = 90
                            else:
                                self.WB.rotation_x = 90
                                self.WB.rotation_y = -90
                                self.WB.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[1] == 'B':
                                self.WB.rotation_x = 0
                                self.WB.rotation_y = 0
                                self.WB.rotation_z = -90
                            else:
                                self.WB.rotation_x = -90
                                self.WB.rotation_y = -90
                                self.WB.rotation_z = 0
                    elif current_piece.pos[2] == -1:
                        if current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'W':
                                self.WB.rotation_x = 180
                                self.WB.rotation_y = 90
                                self.WB.rotation_z = 0
                            else:
                                self.WB.rotation_x = 180
                                self.WB.rotation_y = 0
                                self.WB.rotation_z = 180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'W':
                                self.WB.rotation_x = 0
                                self.WB.rotation_y = 90
                                self.WB.rotation_z = 0
                            else:
                                self.WB.rotation_x = 180
                                self.WB.rotation_y = 0
                                self.WB.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[1] == 'B':
                                self.WB.rotation_x = 180
                                self.WB.rotation_y = 0
                                self.WB.rotation_z = -90
                            else:
                                self.WB.rotation_x = 90
                                self.WB.rotation_y = -90
                                self.WB.rotation_z = 180
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[1] == 'B':
                                self.WB.rotation_x = 180
                                self.WB.rotation_y = 0
                                self.WB.rotation_z = 90
                            else:
                                self.WB.rotation_x = -90
                                self.WB.rotation_y = -90
                                self.WB.rotation_z = 180
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == -1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'W':
                                    self.WB.rotation_x = -90
                                    self.WB.rotation_y = 0
                                    self.WB.rotation_z = 180
                                else:
                                    self.WB.rotation_x = 180
                                    self.WB.rotation_y = 90
                                    self.WB.rotation_z = 90
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'W':
                                    self.WB.rotation_x = -90
                                    self.WB.rotation_y = 0
                                    self.WB.rotation_z = 0
                                else:
                                    self.WB.rotation_x = 180
                                    self.WB.rotation_y = -90
                                    self.WB.rotation_z = 90
                        elif current_piece.pos[1] == 1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'W':
                                    self.WB.rotation_x = 90
                                    self.WB.rotation_y = 0
                                    self.WB.rotation_z = 180
                                else:
                                    self.WB.rotation_x = 180
                                    self.WB.rotation_y = 90
                                    self.WB.rotation_z = -90
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'W':
                                    self.WB.rotation_x = 90
                                    self.WB.rotation_y = 0
                                    self.WB.rotation_z = 0
                                else:
                                    self.WB.rotation_x = 0
                                    self.WB.rotation_y = 90
                                    self.WB.rotation_z = 90
                    continue
                if "G" in current_piece.colors:
                    self.WG.x = current_piece.pos[0]
                    self.WG.y = current_piece.pos[1]
                    self.WG.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == 1:
                        if current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'W':
                                self.WG.rotation_x = 180
                                self.WG.rotation_y = -90
                                self.WG.rotation_z = 180
                            else:
                                self.WG.rotation_x = 0
                                self.WG.rotation_y = 0
                                self.WG.rotation_z = 180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'W':
                                self.WG.rotation_x = 0
                                self.WG.rotation_y = -90
                                self.WG.rotation_z = 180
                            else:
                                self.WG.rotation_x = 0
                                self.WG.rotation_y = 0
                                self.WG.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[1] == 'G':
                                self.WG.rotation_x = 0
                                self.WG.rotation_y = 0
                                self.WG.rotation_z = 90
                            else:
                                self.WG.rotation_x = -90
                                self.WG.rotation_y = 90
                                self.WG.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[1] == 'G':
                                self.WG.rotation_x = 0
                                self.WG.rotation_y = 0
                                self.WG.rotation_z = -90
                            else:
                                self.WG.rotation_x = 90
                                self.WG.rotation_y = 90
                                self.WG.rotation_z = 0
                    elif current_piece.pos[2] == -1:
                        if current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'W':
                                self.WG.rotation_x = 180
                                self.WG.rotation_y = -90
                                self.WG.rotation_z = 0
                            else:
                                self.WG.rotation_x = 180
                                self.WG.rotation_y = 0
                                self.WG.rotation_z = 180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'W':
                                self.WG.rotation_x = 0
                                self.WG.rotation_y = -90
                                self.WG.rotation_z = 0
                            else:
                                self.WG.rotation_x = 180
                                self.WG.rotation_y = 0
                                self.WG.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[1] == 'G':
                                self.WG.rotation_x = 180
                                self.WG.rotation_y = 0
                                self.WG.rotation_z = -90
                            else:
                                self.WG.rotation_x = -90
                                self.WG.rotation_y = 90
                                self.WG.rotation_z = 180
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[1] == 'G':
                                self.WG.rotation_x = 180
                                self.WG.rotation_y = 0
                                self.WG.rotation_z = 90
                            else:
                                self.WG.rotation_x = 90
                                self.WG.rotation_y = 90
                                self.WG.rotation_z = 180
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == 1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'W':
                                    self.WG.rotation_x = 90
                                    self.WG.rotation_y = 0
                                    self.WG.rotation_z = 0
                                else:
                                    self.WG.rotation_x = 180
                                    self.WG.rotation_y = 90
                                    self.WG.rotation_z = 90
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'W':
                                    self.WG.rotation_x = 90
                                    self.WG.rotation_y = 0
                                    self.WG.rotation_z = 180
                                else:
                                    self.WG.rotation_x = 180
                                    self.WG.rotation_y = -90
                                    self.WG.rotation_z = 90
                        elif current_piece.pos[1] == -1:
                            if current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'W':
                                    self.WG.rotation_x = -90
                                    self.WG.rotation_y = 0
                                    self.WG.rotation_z = 0
                                else:
                                    self.WG.rotation_x = 180
                                    self.WG.rotation_y = 90
                                    self.WG.rotation_z = -90
                            elif current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'W':
                                    self.WG.rotation_x = -90
                                    self.WG.rotation_y = 0
                                    self.WG.rotation_z = 180
                                else:
                                    self.WG.rotation_x = 0
                                    self.WG.rotation_y = 90
                                    self.WG.rotation_z = 90
                    continue
                self.W.x = current_piece.pos[0]
                self.W.y = current_piece.pos[1]
                self.W.z = current_piece.pos[2] * -1
                if current_piece.pos[2] == 1:
                    self.W.rotation_x = 0
                    self.W.rotation_y = 0
                    self.W.rotation_z = 0
                elif current_piece.pos[2] == -1:
                    self.W.rotation_x = 0
                    self.W.rotation_y = 180
                    self.W.rotation_z = 0
                if current_piece.pos[0] == 1:
                    self.W.rotation_x = 0
                    self.W.rotation_y = -90
                    self.W.rotation_z = 0
                elif current_piece.pos[0] == -1:
                    self.W.rotation_x = 0
                    self.W.rotation_y = 90
                    self.W.rotation_z = 0
                if current_piece.pos[1] == 1:
                    self.W.rotation_x = 90
                    self.W.rotation_y = 0
                    self.W.rotation_z = 0
                elif current_piece.pos[1] == -1:
                    self.W.rotation_x = -90
                    self.W.rotation_y = 0
                    self.W.rotation_z = 0
                continue
            # middle back layer====
            if "Y" in current_piece.colors:
                if "B" in current_piece.colors:
                    self.YB.x = current_piece.pos[0]
                    self.YB.y = current_piece.pos[1]
                    self.YB.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == -1:
                        if current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'Y':
                                self.YB.rotation_x = 180
                                self.YB.rotation_y = -90
                                self.YB.rotation_z = 180
                            else:
                                self.YB.rotation_x = 0
                                self.YB.rotation_y = 0
                                self.YB.rotation_z = 180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'Y':
                                self.YB.rotation_x = 0
                                self.YB.rotation_y = -90
                                self.YB.rotation_z = 180
                            else:
                                self.YB.rotation_x = 0
                                self.YB.rotation_y = 0
                                self.YB.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[1] == 'B':
                                self.YB.rotation_x = 0
                                self.YB.rotation_y = 0
                                self.YB.rotation_z = 90
                            else:
                                self.YB.rotation_x = -90
                                self.YB.rotation_y = 90
                                self.YB.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[1] == 'B':
                                self.YB.rotation_x = 0
                                self.YB.rotation_y = 0
                                self.YB.rotation_z = -90
                            else:
                                self.YB.rotation_x = 90
                                self.YB.rotation_y = 90
                                self.YB.rotation_z = 0
                    elif current_piece.pos[2] == 1:
                        if current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'Y':
                                self.YB.rotation_x = 180
                                self.YB.rotation_y = -90
                                self.YB.rotation_z = 0
                            else:
                                self.YB.rotation_x = 180
                                self.YB.rotation_y = 0
                                self.YB.rotation_z = 180
                        elif current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'Y':
                                self.YB.rotation_x = 0
                                self.YB.rotation_y = -90
                                self.YB.rotation_z = 0
                            else:
                                self.YB.rotation_x = 180
                                self.YB.rotation_y = 0
                                self.YB.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[1] == 'B':
                                self.YB.rotation_x = 180
                                self.YB.rotation_y = 0
                                self.YB.rotation_z = -90
                            else:
                                self.YB.rotation_x = -90
                                self.YB.rotation_y = 90
                                self.YB.rotation_z = 180
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[1] == 'B':
                                self.YB.rotation_x = 180
                                self.YB.rotation_y = 0
                                self.YB.rotation_z = 90
                            else:
                                self.YB.rotation_x = 90
                                self.YB.rotation_y = 90
                                self.YB.rotation_z = 180
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == -1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'Y':
                                    self.YB.rotation_x = 90
                                    self.YB.rotation_y = 0
                                    self.YB.rotation_z = 0
                                else:
                                    self.YB.rotation_x = 180
                                    self.YB.rotation_y = 90
                                    self.YB.rotation_z = 90
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'Y':
                                    self.YB.rotation_x = 90
                                    self.YB.rotation_y = 0
                                    self.YB.rotation_z = 180
                                else:
                                    self.YB.rotation_x = 180
                                    self.YB.rotation_y = -90
                                    self.YB.rotation_z = 90
                        elif current_piece.pos[1] == 1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'Y':
                                    self.YB.rotation_x = -90
                                    self.YB.rotation_y = 0
                                    self.YB.rotation_z = 0
                                else:
                                    self.YB.rotation_x = 180
                                    self.YB.rotation_y = 90
                                    self.YB.rotation_z = -90
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'Y':
                                    self.YB.rotation_x = -90
                                    self.YB.rotation_y = 0
                                    self.YB.rotation_z = 180
                                else:
                                    self.YB.rotation_x = 0
                                    self.YB.rotation_y = 90
                                    self.YB.rotation_z = 90
                    continue
                if "G" in current_piece.colors:
                    self.YG.x = current_piece.pos[0]
                    self.YG.y = current_piece.pos[1]
                    self.YG.z = current_piece.pos[2] * -1
                    if current_piece.pos[2] == -1:
                        if current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'Y':
                                self.YG.rotation_x = 180
                                self.YG.rotation_y = 90
                                self.YG.rotation_z = 180
                            else:
                                self.YG.rotation_x = 0
                                self.YG.rotation_y = 0
                                self.YG.rotation_z = 180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'Y':
                                self.YG.rotation_x = 0
                                self.YG.rotation_y = 90
                                self.YG.rotation_z = 180
                            else:
                                self.YG.rotation_x = 0
                                self.YG.rotation_y = 0
                                self.YG.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[1] == 'G':
                                self.YG.rotation_x = 0
                                self.YG.rotation_y = 0
                                self.YG.rotation_z = 90
                            else:
                                self.YG.rotation_x = 90
                                self.YG.rotation_y = -90
                                self.YG.rotation_z = 0
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[1] == 'G':
                                self.YG.rotation_x = 0
                                self.YG.rotation_y = 0
                                self.YG.rotation_z = -90
                            else:
                                self.YG.rotation_x = -90
                                self.YG.rotation_y = -90
                                self.YG.rotation_z = 0
                    elif current_piece.pos[2] == 1:
                        if current_piece.pos[0] == -1:
                            if current_piece.colors[0] == 'Y':
                                self.YG.rotation_x = 180
                                self.YG.rotation_y = 90
                                self.YG.rotation_z = 0
                            else:
                                self.YG.rotation_x = 180
                                self.YG.rotation_y = 0
                                self.YG.rotation_z = 180
                        elif current_piece.pos[0] == 1:
                            if current_piece.colors[0] == 'Y':
                                self.YG.rotation_x = 0
                                self.YG.rotation_y = 90
                                self.YG.rotation_z = 0
                            else:
                                self.YG.rotation_x = 180
                                self.YG.rotation_y = 0
                                self.YG.rotation_z = 0
                        elif current_piece.pos[1] == -1:
                            if current_piece.colors[1] == 'G':
                                self.YG.rotation_x = 180
                                self.YG.rotation_y = 0
                                self.YG.rotation_z = -90
                            else:
                                self.YG.rotation_x = 90
                                self.YG.rotation_y = -90
                                self.YG.rotation_z = 180
                        elif current_piece.pos[1] == 1:
                            if current_piece.colors[1] == 'G':
                                self.YG.rotation_x = 180
                                self.YG.rotation_y = 0
                                self.YG.rotation_z = 90
                            else:
                                self.YG.rotation_x = -90
                                self.YG.rotation_y = -90
                                self.YG.rotation_z = 180
                    elif current_piece.pos[2] == 0:
                        if current_piece.pos[1] == 1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'Y':
                                    self.YG.rotation_x = -90
                                    self.YG.rotation_y = 0
                                    self.YG.rotation_z = 180
                                else:
                                    self.YG.rotation_x = 180
                                    self.YG.rotation_y = 90
                                    self.YG.rotation_z = 90
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'Y':
                                    self.YG.rotation_x = -90
                                    self.YG.rotation_y = 0
                                    self.YG.rotation_z = 0
                                else:
                                    self.YG.rotation_x = 180
                                    self.YG.rotation_y = -90
                                    self.YG.rotation_z = 90
                        elif current_piece.pos[1] == -1:
                            if current_piece.pos[0] == -1:
                                if current_piece.colors[1] == 'Y':
                                    self.YG.rotation_x = 90
                                    self.YG.rotation_y = 0
                                    self.YG.rotation_z = 180
                                else:
                                    self.YG.rotation_x = 180
                                    self.YG.rotation_y = 90
                                    self.YG.rotation_z = -90
                            elif current_piece.pos[0] == 1:
                                if current_piece.colors[1] == 'Y':
                                    self.YG.rotation_x = 90
                                    self.YG.rotation_y = 0
                                    self.YG.rotation_z = 0
                                else:
                                    self.YG.rotation_x = 0
                                    self.YG.rotation_y = 90
                                    self.YG.rotation_z = 90
                    continue
                self.Y.x = current_piece.pos[0]
                self.Y.y = current_piece.pos[1]
                self.Y.z = current_piece.pos[2] * -1
                if current_piece.pos[2] == -1:
                    self.Y.rotation_x = 0
                    self.Y.rotation_y = 0
                    self.Y.rotation_z = 0
                elif current_piece.pos[2] == 1:
                    self.Y.rotation_x = 0
                    self.Y.rotation_y = 180
                    self.Y.rotation_z = 0
                if current_piece.pos[0] == -1:
                    self.Y.rotation_x = 0
                    self.Y.rotation_y = -90
                    self.Y.rotation_z = 0
                elif current_piece.pos[0] == 1:
                    self.Y.rotation_x = 0
                    self.Y.rotation_y = 90
                    self.Y.rotation_z = 0
                if current_piece.pos[1] == -1:
                    self.Y.rotation_x = 90
                    self.Y.rotation_y = 0
                    self.Y.rotation_z = 0
                elif current_piece.pos[1] == 1:
                    self.Y.rotation_x = -90
                    self.Y.rotation_y = 0
                    self.Y.rotation_z = 0
                continue
            # remaining two centers====
            if "B" in current_piece.colors:
                self.B.x = current_piece.pos[0]
                self.B.y = current_piece.pos[1]
                self.B.z = current_piece.pos[2] * -1
                if current_piece.pos[0] == -1:
                    self.B.rotation_x = 0
                    self.B.rotation_y = 0
                    self.B.rotation_z = 0
                elif current_piece.pos[0] == 1:
                    self.B.rotation_x = 0
                    self.B.rotation_y = 0
                    self.B.rotation_z = 180
                if current_piece.pos[2] == -1:
                    self.B.rotation_x = 0
                    self.B.rotation_y = 90
                    self.B.rotation_z = 0
                elif current_piece.pos[2] == 1:
                    self.B.rotation_x = 0
                    self.B.rotation_y = -90
                    self.B.rotation_z = 0
                if current_piece.pos[1] == -1:
                    self.B.rotation_x = 0
                    self.B.rotation_y = 0
                    self.B.rotation_z = -90
                elif current_piece.pos[1] == 1:
                    self.B.rotation_x = 0
                    self.B.rotation_y = 0
                    self.B.rotation_z = 90
                continue
            if "G" in current_piece.colors:
                self.G.x = current_piece.pos[0]
                self.G.y = current_piece.pos[1]
                self.G.z = current_piece.pos[2] * -1
                if current_piece.pos[0] == 1:
                    self.G.rotation_x = 0
                    self.G.rotation_y = 0
                    self.G.rotation_z = 0
                elif current_piece.pos[0] == -1:
                    self.G.rotation_x = 0
                    self.G.rotation_y = 0
                    self.G.rotation_z = 180
                if current_piece.pos[2] == 1:
                    self.G.rotation_x = 0
                    self.G.rotation_y = 90
                    self.G.rotation_z = 0
                elif current_piece.pos[2] == -1:
                    self.G.rotation_x = 0
                    self.G.rotation_y = -90
                    self.G.rotation_z = 0
                if current_piece.pos[1] == 1:
                    self.G.rotation_x = 0
                    self.G.rotation_y = 0
                    self.G.rotation_z = -90
                elif current_piece.pos[1] == -1:
                    self.G.rotation_x = 0
                    self.G.rotation_y = 0
                    self.G.rotation_z = 90
                continue

    def arrowsHovered(self):
        for e in self.arrows:
            if e.hovered:
                return True
        return False

    def print(self):
        print('-------------------------')
        print(self.virtualCube)

    def delete(self): #deletes all cubes and arrows, the old coordinates were still lingering and messing with stuff temp fix was moving, should look into later
        self.reparentCube()
        for e in self.cubes:
            e.position=(100, 100, 100)
            destroy(e)
        for e in self.arrows:
            e.position=(100, 100, 100)
            destroy(e)
        self.cubes.clear()
        self.arrows.clear()
        self.notationText.clear()
        self.rotation = (0, 0, 0)
        self.anim = False
        self.center.rotation = (0, 0, 0)
